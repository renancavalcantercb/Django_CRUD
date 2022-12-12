"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from app.views import home, form, create_car, view_car, edit_car, update_car, delete_car, create_user, login_user, \
    login_user_without_auth, logout_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("form/", form, name="form"),
    path("create/", create_car, name="create"),
    path("view/<int:id>/", view_car, name="view"),
    path("edit/<int:id>/", edit_car, name="edit"),
    path("update/<int:id>/", update_car, name="update"),
    path("delete/<int:id>/", delete_car, name="delete"),
    path("register/", create_user, name="register"),
    path("login/", login_user, name="login"),
    path("login_auth/", login_user_without_auth, name="login_without_auth"),
    path("logout/", logout_user, name="logout"),

]
