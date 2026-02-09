from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from django.contrib.auth.hashers import make_password, check_password

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'role',
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')

        if not email and not phone:
            raise serializers.ValidationError("Please provide either email or phone number.")

        try:
            if email:
                user = User.objects.get(email=email)
            else:
                user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials.")

        if not user.is_active:
            raise serializers.ValidationError("User account is inactive.")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid credentials.")

        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'phone',
            'email',
            'first_name',
            'last_name',
            'role',
            'is_active',
            'created_at'
        ]

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'email',
            'first_name',
            'last_name',
            'password',
            'role'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.password = make_password(password)
        # user.set_password(password)
        user.save()
        return user

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['id']

class BrokerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Broker
        fields = '__all__'

class BrokerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        exclude = [
            'verified',
            'verified_at',
            'verified_by',
            'rating',
            'active_listings',
            'total_listings',
            'total_sales'
        ]

class OwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Owner
        fields = '__all__'

class OwnerCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Owner
        fields = [
            'owner_type',
            'user',
            'relationship_status'
        ]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'user',
            'registration_number',
            'address',
            'property_types',
            'website',
            'profile_description',
            'profile_picture'
        ]


class PartnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Partner
        fields = '__all__'

class PartnerCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Partner
        fields = [
            'user',
            'partner_type',
            'company_name',
            'contact_person',
            'contact_email',
            'contact_phone',
            'address',
            'services_offered'
        ]


class ReferralAgentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ReferralAgent
        fields = '__all__'

class ReferralAgentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ReferralAgent
        fields = [
            'user',
            'agency_name',
            'contact_person',
            'contact_email',
            'contact_phone',
            'address'
        ]


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = '__all__'

class AdminCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Admin
        fields = [
            'user',
            'role_description'
        ]


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = '__all__'

class StaffCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Staff
        fields = [
            'user',
            'position',
            'department'
        ]
