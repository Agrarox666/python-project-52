from django.contrib import admin
from django.urls import path, include

import authorization.views
from task_manager import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('login/', authorization.views.LoginUserView.as_view(), name='login'),
    path('logout/', authorization.views.LogoutUserView.as_view(), name='logout'),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')),
    path('admin/', admin.site.urls),
]
