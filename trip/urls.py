from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import (CategoryCreateApiView, CategoryDetailView, NavbarCreateApiView, NavbarDetailView,
                    HeaderCreateApiView,
                    HeaderDetailView, CompanyCreateApiView, CompanyDetailView, AmenityCreateApiView, AmenityDetailView)

urlpatterns = [
    path('api/v1/categories/', CategoryCreateApiView.as_view()),
    path('api/v1/category/<int:pk>/', CategoryDetailView.as_view()),

    path('api/v1/navbar/', NavbarCreateApiView.as_view()),
    path('api/v1/navbar/<int:pk>/', NavbarDetailView.as_view()),

    path('api/v1/header/', HeaderCreateApiView.as_view()),
    path('api/v1/header/<int:pk>/', HeaderDetailView.as_view()),

    path('api/v1/company/', CompanyCreateApiView.as_view()),
    path('api/v1/company/<int:pk>/', CompanyDetailView.as_view()),

    path('api/v1/amenities/', AmenityCreateApiView.as_view()),
    path('api/v1/amenity/<int:pk>/', AmenityDetailView.as_view()),


    path('api-auth/', include('rest_framework.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
