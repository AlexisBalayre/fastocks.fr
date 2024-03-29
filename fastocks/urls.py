"""fastocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from api import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/register', views.register),
    url(r'^api/login', views.login),
    url(r'^api/profiles/$', views.profiles_list),
    url(r'^api/profiles/(?P<pk>[0-999999999999999999999]+)$', views.profile_detail),  
    url(r'^api/user-account/$', views.user_account),  
    url(r'^api/user-account/settings', views.user_account_settings),  
    url(r'^api/user-account/password', views.user_account_password),  
    url(r'^api/user-account/delete', views.user_account_delete),  
    url(r'^api/user-monitoring/$', views.user_account_monitoring),  
    url(r'^api/user-monitoring/(?P<pk>[0-999999999999999999999]+)$', views.user_account_monitoring_detail),  
    url(r'^api/user-new-product-step-1', views.user_new_product_step_1),
    url(r'^api/user-new-product-step-2', views.user_new_product_step_2),
    url(r'^api/monitoring/$', views.monitoring_list), 
    url(r'^api/monitoring/(?P<pk>[0-999999999999999999999]+)$', views.monitoring_detail),  
    url(r'^api/products/$', views.products_list),   
    url(r'^api/products/(?P<pk>[0-999999999999999999999]+)$', views.product_detail),  
    url(r'^api/search-products/$', views.search_products), 
]
