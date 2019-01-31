from django.urls import path

from . import views


urlpatterns = [
    path('create_new_client/', views.ContactView.as_view(), name='create_new_client'),

]