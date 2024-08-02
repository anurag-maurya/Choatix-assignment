
from django.urls import path, include
from home.views import index, generate_images, get_task_status,image_count



urlpatterns = [
    path('', index, name="home"),
    path('generate/', generate_images, name='generate_images'),
    path('get_task_status/', get_task_status, name='generate_images'),
    path('image_count/', image_count, name='image_count'),
]
