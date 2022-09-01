from django.shortcuts import render, redirect

# import our model
from .models import Festival, Ticket

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def festivals_index(request):
    # use our model to find all the Festivals from our festivals table (all of the rows on the table)
    festivals = Festival.objects.all()
    return render(request, 'festivals/index.html', {'festivals': festivals})

def festivals_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)
    tickets_festival_doesnt_have = Ticket.objects.exclude(id__in = festival.tickets.all().values_list('id'))

    return render(request, 'festivals/detail.html', {'festival': festival, 'tickets': tickets_festival_doesnt_have})

def assoc_ticket(request, festival_id, ticket_id):
    festival = Festival.objects.get(id=festival_id)
    festival.tickets.add(ticket_id)
    return redirect('detail', festival_id=festival_id)

class FestivalCreate(CreateView):
    model = Festival
    fields = ['name', 'description', 'date', 'location', 'website', 'genre', 'attendance'] #<- telling django what keys on the model we want to generate the form the with
    # redirect is the get_absolute_url defined in the model

class FestivalUpdate(UpdateView):
    model = Festival
    # exclude the name from update
    fields = ['date', 'location', 'website', 'description', 'genre', 'attendance']

class FestivalDelete(DeleteView):
    model = Festival
    success_url = '/festivals/'

class TicketList(ListView):
    model = Ticket


class TicketDetail(DetailView):
    model = Ticket

class TicketCreate(CreateView):
    model = Ticket
    fields = '__all__'

class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['name', 'price', 'type']

class TicketDelete(DeleteView):
    model = Ticket
    success_url = '/tickets/' # define this, because the get_absolute_url is going to the detail page, which wouldn't exist anymore




