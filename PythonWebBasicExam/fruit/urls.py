from django.urls import path, include

from PythonWebBasicExam.fruit import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create-fruit'),
    path('<int:id>/', include([
        path('details/', views.details_fruit, name='details-fruit'),
        path('edit/', views.edit_fruit, name='edit-fruit'),
        path('delete/', views.delete_fruit, name='delete-fruit'),
    ]))

]