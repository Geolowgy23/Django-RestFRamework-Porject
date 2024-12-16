from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.HomeAPIView.as_view(), name='home'),
    path('api/about', views.AboutAPIView.as_view(), name='about'),
    path('api/delete/<int:item_id>', views.DeleteAPIView.as_view(), name='delete'),
    path('api/crossoff/<int:item_id>', views.CrossOffAPIView.as_view(), name='cross_off'),
    path('api/uncross/<int:item_id>', views.UncrossAPIView.as_view(), name='uncross'),
    path('api/edit/<int:item_id>', views.EditAPIView.as_view(), name='edit'),
    path('api/signup/', views.SignupAPIView.as_view(), name='signup'),
    path('api/login/', views.LoginAPIView.as_view(), name='login'),
]
