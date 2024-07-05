from django.shortcuts import render

from .models import Category,Navbar,Header,Company,Amenity
from .serializers import CategorySerializer,NavbarSerializer,HeaderSerializer,CompanySerializer,AmenitySerializer
from .permissions import OnlyAdminPermission

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class CategoryCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [OnlyAdminPermission]



class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [OnlyAdminPermission]



class NavbarCreateApiView(ListCreateAPIView):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer
    permission_classes = [OnlyAdminPermission]


class NavbarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer
    permission_classes = [OnlyAdminPermission]


class HeaderCreateApiView(ListCreateAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
    permission_classes = [OnlyAdminPermission]


class HeaderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
    permission_classes = [OnlyAdminPermission]


class CompanyCreateApiView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [OnlyAdminPermission]


class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [OnlyAdminPermission]


class AmenityCreateApiView(ListCreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [OnlyAdminPermission]


class AmenityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [OnlyAdminPermission]

