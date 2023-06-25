from django.shortcuts import render, redirect
from django.views.generic import DetailView

from PythonWebBasicExam.fruit.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm

from PythonWebBasicExam.fruit.models import FruitModel

from PythonWebBasicExam.profile_app.models import ProfileModel


# Create your views here.
def index(request):
    profile = ProfileModel.objects.first()
    fruits = FruitModel.objects.all()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'index.html', context)


def dashboard(request):
    profile = ProfileModel.objects.first()
    fruits = FruitModel.objects.all()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'dashboard.html', context)


def create_fruit(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitCreateForm()
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-fruit.html', context)


# def details_fruit(request, id):
#     profile = ProfileModel.objects.first()
#     fruit = FruitModel.objects.get(id=id)
#     context = {
#         'profile': profile,
#         'fruit': fruit,
#     }
#     return render(request, 'details-fruit.html', context)


class FruitDetailsView(DetailView):
    context_object_name = 'fruit'
    template_name = 'details-fruit.html'
    model = FruitModel


def edit_fruit(request, id):
    profile = ProfileModel.objects.first()
    fruit = FruitModel.objects.get(id=id)
    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitEditForm(instance=fruit)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'edit-fruit.html', context)


def delete_fruit(request, id):
    profile = ProfileModel.objects.first()
    fruit = FruitModel.objects.get(id=id)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')
    form = FruitDeleteForm(instance=fruit)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'delete-fruit.html', context)
