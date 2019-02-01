from .forms import ClientForm, SearchClientForm
from .models import Client
from django.views.generic import DetailView, UpdateView, CreateView
from django.shortcuts import render


class ClientView(CreateView):
    template_name = 'client/create_new_client.html'
    form_class = ClientForm
    success_url = 'success'


def succes_created(request):
    return render(request, 'client/success.html')

def succes_updated(request, pk):
    return render(request, 'client/success.html')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['client_name', 'client_email', 'phone_number', 'contact_name', 'state', 'street_name', 'suburb', 'postcode']
    template_name_suffix = '_update_form'
    success_url = 'update_success'

    def form_valid(self, form):
        return super().form_valid(form)


class ClientDetailView(DetailView):

    model = Client



def client_list_with_searh(request):
    if request.method == 'POST':
        form = SearchClientForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['client_name']
            # phone_number = form.cleaned_data['phone_number']
            # client_email = form.cleaned_data['client_email']
            # suburb = form.cleaned_data['suburb']
            your_values = {'name': form.cleaned_data['client_name'], 'phone_number': form.cleaned_data['phone_number'], 'client_email': form.cleaned_data['client_email'],
                           'suburb': form.cleaned_data['suburb']}
            arguments = {}
            for k, v in your_values.items():
                if v:
                    arguments[k] = v

            object_list = Client.objects.filter(**arguments)


            context = {
                'clients': object_list,
                'form': form
            }
            return render(request, 'client/clients_view.html', context)

    else:
        object_list = Client.objects.all()
        form = SearchClientForm()
        context = {
            'clients': object_list,
            'form': form
        }
        return render(request, 'client/clients_view.html', context)

