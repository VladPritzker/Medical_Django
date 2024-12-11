# user_serializer.py
from rest_framework import serializers
from app.models.users import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)  # Password field is write-only and must have at least 8 characters

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'full_name', 'date_of_birth', 'gender']  # Fields that will be included in the serialization

    def create(self, validated_data):
        # Create a new user with the provided data
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data.get('full_name', ''),  # Optional full name
            date_of_birth=validated_data.get('date_of_birth', None),  # Optional date of birth
            gender=validated_data.get('gender', ''),  # Optional gender
        )
        return user

    def update(self, instance, validated_data):
        # Update user details, handle password hashing if needed
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  # Update password with proper hashing
        
        instance.save()  # Save the updated instance to the database
        return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Email field for user login
    password = serializers.CharField(write_only=True)  # Password field is write-only
