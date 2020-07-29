from django.shortcuts import render, get_object_or_404
from .models import Hack

def all_hacks(request):
    hacks = Hack.objects.all()
    return render(request, 'hacks/all_hacks.html',{'hacks':hacks})

def detail(request,hack_id):
    
    hack = get_object_or_404(Hack,pk = hack_id)
    return render(request, 'hacks/hack_details.html',{'hack':hack})

