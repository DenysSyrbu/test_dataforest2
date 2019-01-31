from .forms import ClientForm
from .models import Client
from django.views.generic import DetailView, UpdateView, CreateView
from django.shortcuts import render, HttpResponse


class ClientView(CreateView):
    template_name = 'client/create_new_client.html'
    form_class = ClientForm
    success_url = 'success'


def succes_created(request):
    return render(request, 'client/success.html')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['client_name', 'client_email', 'phone_number']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        return super().form_valid(form)


class ClientDetailView(DetailView):
    """
    Display the details of the selected book.
    """
    model = Client
