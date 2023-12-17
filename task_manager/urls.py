from django.contrib import admin
from django.urls import path, include

import task_manager.authorization.views
from task_manager import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('login/', task_manager.authorization.views.LoginUserView.as_view(), name='login'),
    path('logout/', task_manager.authorization.views.LogoutUserView.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('admin/', admin.site.urls),
]
