
from django.contrib import admin
from django.urls import path
from .views import adminloginview,authenticateadmin,adminhomepageview,logoutadmin,homepageview,signupuser,userloginview,customerwelcomeview,userauthenticate,userlogout
urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('adminlogout/',logoutadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('',homepageview,name='homepage'),
    path('signupuser/', signupuser),
    path('loginuser/',userloginview,name='userloginpage'),
    path('customer/welcome/',customerwelcomeview, name='customerpage' ),
    path('customer/authenticate/',userauthenticate),
    path('userlogout/',userlogout),
]
