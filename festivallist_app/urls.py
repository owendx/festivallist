from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('festivals/', views.festivals_index, name='index'),
    path('festivals/<int:festival_id>/', views.festivals_detail, name="detail"),
    path('festivals/create/', views.FestivalCreate.as_view(), name='festivals_create'),
    path('festivals/<int:pk>/update/', views.FestivalUpdate.as_view(), name='festivals_update'),
    path('festivals/<int:pk>/delete/', views.FestivalDelete.as_view(), name='festivals_delete'),
    path('festivals/<int:festival_id>/assoc_ticket/<int:ticket_id>/', views.assoc_ticket, name='assoc_ticket'),
    path('tickets/', views.TicketList.as_view(), name='tickets_index'),
    path('tickets/<int:pk>/', views.TicketDetail.as_view(), name='tickets_detail'),
    path('tickets/create/', views.TicketCreate.as_view(), name='tickets_create'),
    path('tickets/<int:pk>/update/', views.TicketUpdate.as_view(), name='tickets_update'),
    path('tickets/<int:pk>/delete/', views.TicketDelete.as_view(), name='tickets_delete'),
]
