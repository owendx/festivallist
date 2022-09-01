from django.contrib import admin

# Register your models here.
from .models import Festival, Ticket

admin.site.register(Festival)
admin.site.register(Ticket)
