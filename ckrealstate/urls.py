"""
URL configuration for ckrealstate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path
from django.views.static import serve
from django.conf import settings
from .views import home,propertyDetail,addEditPropertyDetail,storeUpdateListing,deletelistings,contactUs


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), #serve static files when deployed
    path('accounts/', include('accounts.urls')),
    path('property-detail/<int:id>/',propertyDetail, name = 'property-detail'),
    path('add-property-detail/<str:id>/',addEditPropertyDetail,name="add-edit-property-detail"),
    path('add-property-detail',addEditPropertyDetail,name="add-edit-property-detail"),
    path('store-update-listing',storeUpdateListing,name="store-update-listing"),
    path('delete-listing/<int:id>', deletelistings, name='deletelistings'),
    path("contact-us",contactUs,name="contact-us"),
    path('',home)
 
]
