from django.shortcuts import render, redirect
from .models import PetrolEntry

def create_petrol_entry(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        bike = request.POST.get('bike')
        amount = request.POST.get('amount')

        PetrolEntry.objects.create(date=date, bike=bike, amount=amount)
        return redirect('dashboard')  # Replace with your actual success URL/view

    return render(request, 'create_entry.html')

def dashboard(request):
    a = PetrolEntry.objects.all().order_by('-id')
    return render(request,'show_data.html',{'data':a})

def delete(request,id):
    d = PetrolEntry.objects.get(id=id)
    d.delete()
    return redirect('dashboard')
