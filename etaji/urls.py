from django.urls import path
from .views import (
    ApartmentListView, ApartmentDetailView, ApartmentCreateView, ApartmentUpdateView, ApartmentDeleteView,
    PersonListView, PersonDetailView, PersonCreateView, PersonUpdateView, PersonDeleteView,
    TransactionListView, TransactionDetailView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView,
    AgencyListView, AgencyDetailView, AgencyCreateView, AgencyUpdateView, AgencyDeleteView,
    AgentListView, AgentDetailView, AgentCreateView, AgentUpdateView, AgentDeleteView
)

urlpatterns = [
    path('apartments/', ApartmentListView.as_view(), name='apartment-list'),
    path('apartments/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
    path('apartments/new/', ApartmentCreateView.as_view(), name='apartment-create'),
    path('apartments/<int:pk>/edit/', ApartmentUpdateView.as_view(), name='apartment-update'),
    path('apartments/<int:pk>/delete/', ApartmentDeleteView.as_view(), name='apartment-delete'),

    path('persons/', PersonListView.as_view(), name='person-list'),
    path('persons/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('persons/new/', PersonCreateView.as_view(), name='person-create'),
    path('persons/<int:pk>/edit/', PersonUpdateView.as_view(), name='person-update'),
    path('persons/<int:pk>/delete/', PersonDeleteView.as_view(), name='person-delete'),

    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/new/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),

    path('agencies/', AgencyListView.as_view(), name='agency-list'),
    path('agencies/<int:pk>/', AgencyDetailView.as_view(), name='agency-detail'),
    path('agencies/new/', AgencyCreateView.as_view(), name='agency-create'),
    path('agencies/<int:pk>/edit/', AgencyUpdateView.as_view(), name='agency-update'),
    path('agencies/<int:pk>/delete/', AgencyDeleteView.as_view(), name='agency-delete'),

    path('agents/', AgentListView.as_view(), name='agent-list'),
    path('agents/<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('agents/new/', AgentCreateView.as_view(), name='agent-create'),
    path('agents/<int:pk>/edit/', AgentUpdateView.as_view(), name='agent-update'),
    path('agents/<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),
]
