from django.urls import path
from app.views.user_view import RegisterView, LoginView, UserListView, UserDetailView
from app.views.client_view import ClientRegisterView, ClientListView, ClientDetailView

urlpatterns = [
    # Specialist URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
    path('user/', UserDetailView.as_view(), name='user-detail-self'),
    
    # Client URLs
    path('client/register/', ClientRegisterView.as_view(), name='client-register'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:client_id>/', ClientDetailView.as_view(), name='client-detail'),
]
