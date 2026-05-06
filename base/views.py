from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from services.models import Service
from orders.models import Order

def home(request):
    featured_services = Service.objects.all()[:3]
    return render(request, 'base/home.html', {'featured_services': featured_services})

def contact(request):
    return render(request, 'base/contact.html')

def about(request):
    return render(request, 'base/about.html')

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    active_dossiers_count = orders.count()
    upcoming_consultations_count = active_dossiers_count
    unread_messages_count = 0 
    next_order = orders.first()
    
    context = {
        'orders': orders[:5],  # Only show last 5 in dashboard
        'active_dossiers_count': active_dossiers_count,
        'upcoming_consultations_count': upcoming_consultations_count,
        'unread_messages_count': unread_messages_count,
        'next_order': next_order,
    }
    return render(request, 'base/dashboard.html', context)

@login_required
def mes_dossiers(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'base/mes_dossiers.html', {'orders': orders})

@login_required
def mes_consultations(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'base/mes_consultations.html', {'orders': orders})
