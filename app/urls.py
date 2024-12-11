from django.urls import path
from app.views.user_view import RegisterView, LoginView, UserListView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # remove `api/`
    path('login/', LoginView.as_view(), name='login'),           # remove `api/`
    path('users/', UserListView.as_view(), name='user-list'),    # remove `api/`
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),  # remove `api/`
    path('user/', UserDetailView.as_view(), name='user-detail-self'),             # remove `api/`
]
