from django.urls import path

from . import views

urlpatterns = [
    path('', views.request, name='request'),
    path('delete/<int:expense_id>', views.delete_exp, name='delete'),
]