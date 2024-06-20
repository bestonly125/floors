from django.contrib import admin
from .models import Apartment, Person, Transaction, Agency, Agent

admin.site.register(Apartment)
admin.site.register(Person)
admin.site.register(Transaction)
admin.site.register(Agency)
admin.site.register(Agent)
