"""Main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mainapp_2 import views
from django.conf.urls import url

urlpatterns = [
        path('admin/', admin.site.urls),   
        path('form/', views.Login_page),            #1 It will redirects to the login page
        path('form_check/', views.signin_page),     #1 It will sends the user to signinpage
        path('signin/',views.signin_page),          #2 It also sends the user to the signin page
        path('signin_check/', views.user_signin),   #3 It will checks whether the users credentials correct or not
        path('start_test/',views.strt_test),        #4 It will starts the test,
        path('index/', views.index),                # 5 It will checks the user answer is correct or not
        path('last_answer/', views.last_answer),    # 6 It will sends the user Right answers
        path(r'index/', views.index),
]