from .forms import ClientForm, SearchClientForm
from .models import Client
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.shortcuts import render, HttpResponse
import operator
from django.db.models import Q


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

    model = Client


# class ClientListView(ListView):
#     model = Client
#     form_class = SearchClientForm
#     template_name = 'client/clients_view.html'
#     context_object_name = 'clients'
#     paginate_by = 10
#
#     def get_queryset(self):
#         try:
#             name = self.kwargs['client_name']
#         except:
#             name = ''
#         if name != '':
#             object_list = self.model.objects.filter(client_name__icontains=name)
#         else:
#             object_list = self.model.objects.all()
#         return object_list


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

