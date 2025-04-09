from django.urls import path

from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('toggle_complete/<str:task_id>', toggle_complete, name='toggle_complete'),
    path('task_delete/<str:task_id>', task_delete, name='task_delete'),
    path('insert/', insert_task,name='insert_task'),
     path('update_task/<int:task_id>', update_task, name='update_task'),  # New URL for editing tasks
]