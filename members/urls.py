
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register,name='register'),
    path('test/',views.test,name='test'),

]
