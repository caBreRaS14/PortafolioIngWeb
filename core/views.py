from django.shortcuts import render, redirect, get_object_or_404
from .models import Series, Contact, FAQ
from django.views.decorators.csrf import csrf_protect

def home(request):
    banners = Series.objects.all()[:2]
    latest_series = Series.objects.order_by('-created_at')[:6]
    context = {'banners': banners, 'latest_series': latest_series}
    return render(request, 'home.html', context)

@csrf_protect
def contactame(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre','').strip()
        correo = request.POST.get('correo','').strip()
        telefono = request.POST.get('telefono','').strip()
        mensaje = request.POST.get('mensaje','').strip()
        # Validación mínima del lado servidor
        if not nombre or not correo or not mensaje:
            return render(request, 'contactame.html', {'error': 'Por favor completa los campos obligatorios.'})
        Contact.objects.create(nombre=nombre, correo=correo, telefono=telefono, mensaje=mensaje)
        return redirect('home')
    return render(request, 'contactame.html')


def fyq(request):
    faqs = FAQ.objects.all()
    return render(request, 'fyq.html', {'faqs': faqs})

def open_list(request):
    items = Series.objects.order_by('-created_at')
    return render(request, 'open.html', {'items': items})

def open_detail(request, pk):
    item = get_object_or_404(Series, pk=pk)
    return render(request, 'open_detail.html', {'item': item})