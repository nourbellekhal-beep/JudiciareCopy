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
    orders = Order.objects.filter(user=request.user)
    return render(request, 'base/dashboard.html', {'orders': orders})
