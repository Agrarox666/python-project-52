from django.urls import path

import users.views

urlpatterns = [
    path('', users.views.UsersIndexView.as_view(), name='users_index'),
    path('create/', users.views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', users.views.UserUpdateView.as_view(), name='user_update'),  # noqa: E501
    path('<int:pk>/delete/', users.views.UserDeleteView.as_view(), name='user_delete'),  # noqa: E501
]
