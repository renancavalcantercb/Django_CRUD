from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app.forms import CarForm
from app.models import Car


# Create your views here.
def home(request):
    data = {'cars': Car.objects.all()}
    all = Car.objects.all()
    paginator = Paginator(all, 2)
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


def create(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, id):
    data = {'car': Car.objects.get(id=id)}
    return render(request, "view.html", data)


def edit(request, id):
    data = {}
    car = Car.objects.get(id=id)
    data['car'] = car
    data['form'] = CarForm(instance=car)
    return render(request, "form.html", data)


def update(request, id):
    data = {'car': Car.objects.get(id=id)}
    form = CarForm(request.POST or None, instance=data['car'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('home')
