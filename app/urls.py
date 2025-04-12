from django.urls import path

from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('toggle_complete/<str:task_id>', toggle_complete, name='toggle_complete'),
    path('task_delete/<str:task_id>', task_delete, name='task_delete'),
    path('insert/', insert_task,name='insert_task'),
    path('update_task/<int:task_id>', update_task, name='update_task'),  
     #api-calls
    path('api/tasks/', api_get_tasks, name='api_get_tasks'),
    path('api/tasks/create/', api_create_task, name='api_create_task'),
    path('api/tasks/update/<int:task_id>/', api_update_task, name='api_update_task'),
    path('api/tasks/delete/<int:task_id>', api_delete_task, name='api_delete_task')

]