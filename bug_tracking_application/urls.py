"""
URL configuration for bug_tracking_application project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, admin_views, staff_views, user_views

# from bug_tracking_application.bug_tracking_application import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('base/', views.BASE, name='base'),
    
    # Home page
    path('', views.INDEX, name='index'),
    
    # Login page path
    path('login', views.LOGIN, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('doLogout/', views.doLogout, name='doLogout'), 
    path("otp/", views.otpLogin, name="otp"),
      
     
    
    # Profile page path
    path('profile', views.profile, name='profile'),
    path('profile/update', views.update_profile, name='update_profile'),
    
    # admin panel path
    path('administrator/admin_home', admin_views.admin_home, name='admin_home'),
    path('administrator/customer/admin_user', admin_views.admin_user, name='admin_user'),
    path('administrator/customer/admin_add_user', admin_views.admin_add_user, name='admin_add_user'),
    path('administrator/customer/edit_user/<str:id>', admin_views.admin_add_user, name='edit_user'),
    path('administrator/staff/admin_staff', admin_views.admin_staff, name='admin_staff'),
    path('administrator/staff/add_staff', admin_views.add_staff, name='add_staff'),
    path('administrator/staff/delete_staff', admin_views.delete_staff, name='delete_staff'),
    path('administrator/bug/view_bug', admin_views.view_bug, name="view_bug"),
    
    
    # staff panel path
    path('staff/staff_home', staff_views.staff_home, name='staff_home'),
    path('staff/staff_bug_details', staff_views.staff_bug_details, name='staff_bug_details'),
    path('staff/update_bug_status', staff_views.update_bug_status, name='update_bug_status'),
    path('staff/assign_bug', staff_views.assign_bug, name='assign_bug'),
    
    
    # user panel path
    path('register', user_views.register_user, name='register_user'),
    path('user/user_home', user_views.user_home, name='user_home'),
    path('user/userbugreports', user_views.user_bug_reports, name='userbugreports'),
    path('user/bug_update', user_views.bug_update, name='bug_update' )
    
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
 