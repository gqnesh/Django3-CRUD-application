from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_signin/', views.user_signin, name='user_signin'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('addpost/', views.addpost, name='addpost'),
    path('editpost/<int:id>/', views.editpost, name='editpost'),
    path('deletepost/<int:id>/', views.deletepost, name='deletepost'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
]