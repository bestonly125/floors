from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Apartment, Person, Transaction, Agency, Agent

# Views for Apartments
class ApartmentListView(ListView):
    model = Apartment
    template_name = 'apartments/apartment_list.html'
    context_object_name = 'apartments'

class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'apartments/apartment_detail.html'
    context_object_name = 'apartment'

class ApartmentCreateView(CreateView):
    model = Apartment
    template_name = 'apartments/apartment_form.html'
    fields = ['address', 'city', 'state', 'zip_code', 'square_footage', 'number_of_rooms', 'price']
    success_url = reverse_lazy('apartment-list')

class ApartmentUpdateView(UpdateView):
    model = Apartment
    template_name = 'apartments/apartment_form.html'
    fields = ['address', 'city', 'state', 'zip_code', 'square_footage', 'number_of_rooms', 'price']
    success_url = reverse_lazy('apartment-list')

class ApartmentDeleteView(DeleteView):
    model = Apartment
    template_name = 'apartments/apartment_confirm_delete.html'
    success_url = reverse_lazy('apartment-list')

# Views for Persons
class PersonListView(ListView):
    model = Person
    template_name = 'persons/person_list.html'
    context_object_name = 'persons'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'persons/person_detail.html'
    context_object_name = 'person'

class PersonCreateView(CreateView):
    model = Person
    template_name = 'persons/person_form.html'
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']
    success_url = reverse_lazy('person-list')

class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'persons/person_form.html'
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']
    success_url = reverse_lazy('person-list')

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'persons/person_confirm_delete.html'
    success_url = reverse_lazy('person-list')

# Views for Transactions
class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transactions/transaction_detail.html'
    context_object_name = 'transaction'

class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'transactions/transaction_form.html'
    fields = ['apartment', 'seller', 'buyer', 'transaction_date', 'sale_price']
    success_url = reverse_lazy('transaction-list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = 'transactions/transaction_form.html'
    fields = ['apartment', 'seller', 'buyer', 'transaction_date', 'sale_price']
    success_url = reverse_lazy('transaction-list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction-list')

# Views for Agencies
class AgencyListView(ListView):
    model = Agency
    template_name = 'agencies/agency_list.html'
    context_object_name = 'agencies'

class AgencyDetailView(DetailView):
    model = Agency
    template_name = 'agencies/agency_detail.html'
    context_object_name = 'agency'

class AgencyCreateView(CreateView):
    model = Agency
    template_name = 'agencies/agency_form.html'
    fields = ['agency_name', 'address', 'phone_number']
    success_url = reverse_lazy('agency-list')

class AgencyUpdateView(UpdateView):
    model = Agency
    template_name = 'agencies/agency_form.html'
    fields = ['agency_name', 'address', 'phone_number']
    success_url = reverse_lazy('agency-list')

class AgencyDeleteView(DeleteView):
    model = Agency
    template_name = 'agencies/agency_confirm_delete.html'
    success_url = reverse_lazy('agency-list')

# Views for Agents
class AgentListView(ListView):
    model = Agent
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

class AgentCreateView(CreateView):
    model = Agent
    template_name = 'agents/agent_form.html'
    fields = ['person', 'agency', 'license_number']
    success_url = reverse_lazy('agent-list')

class AgentUpdateView(UpdateView):
    model = Agent
    template_name = 'agents/agent_form.html'
    fields = ['person', 'agency', 'license_number']
    success_url = reverse_lazy('agent-list')

class AgentDeleteView(DeleteView):
    model = Agent
    template_name = 'agents/agent_confirm_delete.html'
    success_url = reverse_lazy('agent-list')
