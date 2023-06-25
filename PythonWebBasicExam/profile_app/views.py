from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from PythonWebBasicExam.fruit.models import FruitModel
from PythonWebBasicExam.profile_app.forms import ProfileCreateForm, ProfileEditForm
from PythonWebBasicExam.profile_app.models import ProfileModel


# Create your views here.
# def create_profile(request):
#     profile = ProfileModel.objects.first()
#     if request.method == 'POST':
#         form = ProfileCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = ProfileCreateForm()
#     context = {
#         'profile': profile,
#         'form': form,
#     }
#     return render(request, 'create-profile.html', context)

class ProfileCreateView(CreateView):
    model = ProfileModel
    template_name = 'create-profile.html'
    form_class = ProfileCreateForm
    # success_url = '/' # Return to home

    def get_success_url(self):
        created_object = self.get_object
        return reverse('dashboard')
        # return reverse('dashboard', kwargs={'pk': created_object.pk}) # if we want to redirect to page with pk


def details_profile(request):
    profile = ProfileModel.objects.first()
    posts_count = len(FruitModel.objects.all())
    context = {
        'profile': profile,
        'posts_count': posts_count,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')
    else:
        form = ProfileEditForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)



def delete_profile(request):
    profile = ProfileModel.objects.first()
    fruits = FruitModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')
    context = {
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)
