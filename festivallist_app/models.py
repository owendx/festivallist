from django.db import models
from django.urls import reverse


class Ticket(models.Model):

    name = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=6, decimal_places=2, default=999.99)
    type = models.CharField(max_length=20, choices=(('GA', 'General Admission'), ('VIP', 'VIP')), default='GA')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tickets_detail', kwargs={'pk': self.id})

class Festival(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, default='')
    date = models.DateField()
    genre = models.CharField(max_length=20, default='EDM')
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    attendance = models.IntegerField(default=0)
    tickets = models.ManyToManyField(Ticket)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'festival_id': self.id})
