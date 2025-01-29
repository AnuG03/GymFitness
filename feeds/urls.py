from django.urls import path
from feeds import views

urlpatterns = [
    path('',views.Home,name="Home")
]