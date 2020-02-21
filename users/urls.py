from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.ELoginView.as_view(), name='login'),
    path('logout/', views.ELogoutView.as_view(), name='logout'),
]
