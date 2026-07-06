from django.urls import path
from . import views

urlpatterns = [
    # Authentication routes
    path("", views.reference_code, name="reference_code"),
    path('login/', views.login_view, name='login'),
    path("register/<str:code>/", views.register, name="register"),
    path('logout/', views.logout_view, name='logout_page'),
    
]