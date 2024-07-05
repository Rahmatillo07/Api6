from rest_framework import serializers

from .models import Category, Navbar, Header, Company, Amenity, About, Social, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

