from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app.forms import CarForm, UserForm, UpdateUserForm
from app.models import Car


# Create your views here.
@login_required(login_url='login_without_auth')
def home(request):
    cars = Car.objects.all()
    user = User.objects.get(id=request.user.id)
    search = request.GET.get('search')
    if search:
        cars = cars.filter(model__icontains=search) | cars.filter(brand__icontains=search) | cars.filter(
            year__icontains=search)
    else:
        cars = Car.objects.all()
    paginator = Paginator(cars, 5)
    page = request.GET.get('page')
    cars = paginator.get_page(page)
    return render(request, "index.html", {'cars': cars, 'user': user})


@login_required(login_url='login_without_auth')
def form(request):
    data = {'form': CarForm()}
    return render(request, "form.html", data)


@login_required(login_url='login_without_auth')
def create_car(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


@login_required(login_url='login_without_auth')
def view_car(request, id):
    if request.user.is_authenticated:
        data = {'car': Car.objects.get(id=id)}
        return render(request, "view.html", data)


@login_required(login_url='login_without_auth')
def edit_car(request, id):
    data = {}
    car = Car.objects.get(id=id)
    data['car'] = car
    data['form'] = CarForm(instance=car)
    return render(request, "form.html", data)


@login_required(login_url='login_without_auth')
def update_car(request, id):
    data = {'car': Car.objects.get(id=id)}
    form = CarForm(request.POST or None, instance=data['car'])
    if form.is_valid():
        form.save()
        return redirect('home')


@login_required(login_url='login_without_auth')
def delete_car(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('home')


def create_user(request):
    data = {'form': UserForm()}
    form = UserForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        if User.objects.filter(username=username).exists():
            message = f'The user "{username}" is already in use'
            div_class = 'alert alert-danger'
            messages.warning(request, message, extra_tags=div_class)
        elif User.objects.filter(email=email).exists():
            message = f'The email "{email}" is already in use'
            div_class = 'alert alert-danger'
            messages.warning(request, message, extra_tags=div_class)
        else:
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                     password=password)
            user.save()
            messages.warning(request, 'User created successfully', extra_tags='alert alert-success')
            return redirect('register')
    return render(request, "register.html", data)


def login_user(request):
    data = {'form': UserForm().LoginForm()}
    form = UserForm().LoginForm(request.POST or None)
    if form.is_valid():
        email = User.objects.get(email=form.cleaned_data['email'])
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect('home')
        else:
            message = 'Invalid login or password'
            div_class = 'alert alert-danger'
            messages.warning(request, message, extra_tags=div_class)
    return render(request, "login.html", data)


def login_user_without_auth(request):
    message = 'You must be logged in to access this page'
    div_class = 'alert alert-danger'
    messages.warning(request, message, extra_tags=div_class)
    return login_user(request)


def logout_user(request):
    logout(request)
    message = 'You have been logged out'
    div_class = 'alert alert-success'
    messages.warning(request, message, extra_tags=div_class)
    return redirect('login')


@login_required(login_url='login_without_auth')
def view_profile_user(request):
    data = {}
    user = User.objects.get(id=request.user.id)
    data['user'] = user
    return render(request, "profile.html", data)


@login_required(login_url='login_without_auth')
def edit_profile_user(request, id):
    data = {}
    user = User.objects.get(id=id)
    data['user'] = user
    data['form'] = UserForm(instance=user)
    return render(request, "edit_profile.html", data)


def update_profile_user(request, id):
    data = {'user': User.objects.get(id=id)}
    form = UpdateUserForm(request.POST or None, instance=data['user'])
    if form.is_valid():
        form.save()
        message = 'Profile updated successfully'
        div_class = 'alert alert-success'
        messages.warning(request, message, extra_tags=div_class)
        return redirect('profile')
    return render(request, "edit_profile.html", data)


def error_404(request, exception):
    return render(request, '404.html')
