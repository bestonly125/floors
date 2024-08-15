from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Apartment, Person, Transaction, Agency, Agent
from django.http import HttpResponse
from django.template import loader



# def apartament(request,pk):
#     template = loader.get_template("apartment_detail.html")
#     # context = 'apartments'
#     return render(request,"etaji/apartment_detail.html")

# Views for Apartments
class ApartmentListView(ListView):
    model = Apartment
    template_name = 'etaji/apartment_list.html'
    context_object_name = 'apartments'

class ApartmentDetailView(DetailView):
    model = Apartment
    context_object_name = 'apartment'
    template_name = 'etaji/apartament_detail.html'


class ApartmentCreateView(CreateView):
    model = Apartment
    template_name = 'template/apartment_form.html'
    fields = ['address', 'city', 'state', 'zip_code', 'square_footage', 'number_of_rooms', 'price']
    success_url = reverse_lazy('apartment-list')

class ApartmentUpdateView(UpdateView):
    model = Apartment
    template_name = 'template/apartment_form.html'
    fields = ['address', 'city', 'state', 'zip_code', 'square_footage', 'number_of_rooms', 'price']
    success_url = reverse_lazy('apartment-list')

class ApartmentDeleteView(DeleteView):
    model = Apartment
    template_name = 'template/apartment_confirm_delete.html'
    success_url = reverse_lazy('apartment-list')

# Views for Persons
class PersonListView(ListView):
    model = Person
    template_name = 'template/person_list.html'
    context_object_name = 'persons'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'template/person_detail.html'
    context_object_name = 'person'

class PersonCreateView(CreateView):
    model = Person
    template_name = 'template/person_form.html'
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']
    success_url = reverse_lazy('person-list')

class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'template/person_form.html'
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']
    success_url = reverse_lazy('person-list')

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'template/person_confirm_delete.html'
    success_url = reverse_lazy('person-list')

# Views for Transactions
class TransactionListView(ListView):
    model = Transaction
    template_name = 'template/transaction_list.html'
    context_object_name = 'transactions'

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'template/transaction_detail.html'
    context_object_name = 'transaction'

class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'template/transaction_form.html'
    fields = ['apartment', 'seller', 'buyer', 'transaction_date', 'sale_price']
    success_url = reverse_lazy('transaction-list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = 'template/transaction_form.html'
    fields = ['apartment', 'seller', 'buyer', 'transaction_date', 'sale_price']
    success_url = reverse_lazy('transaction-list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'template/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction-list')

# Views for Agencies
class AgencyListView(ListView):
    model = Agency
    template_name = 'template/agency_list.html'
    context_object_name = 'agencies'

class AgencyDetailView(DetailView):
    model = Agency
    template_name = 'template/agency_detail.html'
    context_object_name = 'agency'

class AgencyCreateView(CreateView):
    model = Agency
    template_name = 'template/agency_form.html'
    fields = ['agency_name', 'address', 'phone_number']
    success_url = reverse_lazy('agency-list')

class AgencyUpdateView(UpdateView):
    model = Agency
    template_name = 'template/agency_form.html'
    fields = ['agency_name', 'address', 'phone_number']
    success_url = reverse_lazy('agency-list')

class AgencyDeleteView(DeleteView):
    model = Agency
    template_name = 'template/agency_confirm_delete.html'
    success_url = reverse_lazy('agency-list')

# Views for Agents
class AgentListView(ListView):
    model = Agent
    template_name = 'template/agent_list.html'
    context_object_name = 'agents'

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'template/agent_detail.html'
    context_object_name = 'agent'

class AgentCreateView(CreateView):
    model = Agent
    template_name = 'template/agent_form.html'
    fields = ['person', 'agency', 'license_number']
    success_url = reverse_lazy('agent-list')

class AgentUpdateView(UpdateView):
    model = Agent
    template_name = 'template/agent_form.html'
    fields = ['person', 'agency', 'license_number']
    success_url = reverse_lazy('agent-list')

class AgentDeleteView(DeleteView):
    model = Agent
    template_name = 'template/agent_confirm_delete.html'
    success_url = reverse_lazy('agent-list')
