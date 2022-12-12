from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app.forms import CarForm, UserForm
from app.models import Car


# Create your views here.
def home(request):
    data = {'cars': Car.objects.all()}
    all = Car.objects.all()
    paginator = Paginator(all, 2, orphans=1)
    page = request.GET.get('page')
    data['cars'] = paginator.get_page(page)
    search = request.GET.get('search')
    if search:
        data['cars'] = Car.objects.filter(modelo__icontains=search)
    else:
        data['cars'] = Car.objects.all()
    return render(request, "index.html", data)


def form(request):
    data = {'form': CarForm()}
    return render(request, "form.html", data)


def create_car(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view_car(request, id):
    data = {'car': Car.objects.get(id=id)}
    return render(request, "view.html", data)


def edit_car(request, id):
    data = {}
    car = Car.objects.get(id=id)
    data['car'] = car
    data['form'] = CarForm(instance=car)
    return render(request, "form.html", data)


def update_car(request, id):
    data = {'car': Car.objects.get(id=id)}
    form = CarForm(request.POST or None, instance=data['car'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete_car(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('home')


def create_user(request):
    data = {'form': UserForm()}
    form = UserForm(request.POST or None)
    if form.is_valid():
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
            User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.warning(request, 'User created successfully', extra_tags='alert alert-success')
            return redirect('register')
    return render(request, "register.html", data)
