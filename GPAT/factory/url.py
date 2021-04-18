from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/',views.dash,name='dash'),
    path('signup/',views.signup,name='signup'),
    path('adminn/',views.adminn,name='adminn'),
    path('home/',views.logout,name='logout'),
    path('home1/',views.postsignup,name='postsignup'),
    path('approve/',views.approve,name='approve'),
    path('denied/',views.denied,name='denied'),
    path('pending/',views.pending,name='pending'),
    path('form/',views.form,name='form'),
    path('renew/',views.renew,name='renew'),
    path('adminhome/',views.postadmin,name='postadmin'),
    path('formdata/',views.formdata,name='formdata'),
    path('adminrequest/',views.adminrequest,name='adminrequest'),
    path('factoryprofile/',views.factoryprofile,name='factoryprofile'),
]