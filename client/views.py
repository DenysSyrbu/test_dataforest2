from .forms import ClientForm
from django.views.generic.edit import CreateView


class ContactView(CreateView):
    template_name = 'client/create_new_client.html'
    form_class = ClientForm

