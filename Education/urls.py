from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home, name='home_page'),
    path('detail/<int:lesson_id>/', views.detail, name='detail_page'),
    path('dashboard/', views.dashboard, name='dashboard_page'),
    path('lesson/', views.lesson, name='lesson_page'),

    # Authentication routes
    path('', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout_page'),
    
]