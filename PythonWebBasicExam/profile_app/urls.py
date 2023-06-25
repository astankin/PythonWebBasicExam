from django.urls import path, include

from PythonWebBasicExam.profile_app import views
from PythonWebBasicExam.profile_app.views import ProfileCreateView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create-profile'),
    path('details/', views.details_profile, name='details-profile'),
    path('edit/', views.edit_profile, name='edit-profile'),
    path('delete/', views.delete_profile, name='delete-profile'),
]

