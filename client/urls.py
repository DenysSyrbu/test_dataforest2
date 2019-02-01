from django.urls import path

from . import views


urlpatterns = [
    path('create_new_client/', views.ClientView.as_view(), name='create_new_client'),
    path('create_new_client/success', views.succes_created, name='success'),
    path('detail/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('detail/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_apdate'),
    path('detail/<int:pk>/update/update_success', views.succes_updated, name='update_success'),
    path('', views.client_list_with_searh, name='clients_home'),

]