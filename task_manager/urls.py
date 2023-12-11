from django.contrib import admin
from django.urls import path, include

from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='main'),
    path('users/', views.UsersIndexView.as_view(), name='users_index'),
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),  # noqa: E501
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),  # noqa: E501
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')),
]
