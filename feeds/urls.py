from django.urls import path
from feeds import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    path('award',views.award,name="award"),
    path('about',views.about,name="about"),
    path('service',views.service,name="service"),
    path('bi_tri',views.bi_tri,name="bi_tri"),
    path('back',views.back,name="back"),
    path('shoulders',views.shoulders,name="shoulders"),
    path('chest',views.chest,name="chest"),
    path('legs',views.legs,name="legs"),
    path('policy',views.policy,name="policy"),
]