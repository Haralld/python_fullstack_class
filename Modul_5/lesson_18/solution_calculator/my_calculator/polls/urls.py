from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:num1>/<str:operation>/<int:num2>/', views.calculator, name='calculator'),
]