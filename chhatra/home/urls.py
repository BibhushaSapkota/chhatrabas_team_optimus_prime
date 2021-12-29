from django.contrib import admin
from django.urls import path
from home import views

app_name="home"
urlpatterns=[
    path("",views.index,name='index'),
    # path("",views.registration, name='registrationhostel'),
    path("Login1",views.login,name='Login1'),
    path("registrationhostel",views.registration, name='registrationhostel'),
    path('registration1',views.registration1,name='registration1')
]