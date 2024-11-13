from django.shortcuts import render, redirect
from .forms import EncuestaForm

# Vistas para las páginas 
def index(request):
    return render(request, 'Paises/index.html')

def arabe(request):
    return render(request, 'Paises/arabe.html')

def china(request):
    return render(request, 'Paises/china.html')

def corea(request):
    return render(request, 'Paises/corea.html')

def hungria(request):
    return render(request, 'Paises/hungaria.html')

def japon(request):
    return render(request, 'Paises/japon.html')

def encuesta_view(request):
    return render(request, 'Paises/encuesta.html', {'form': form})

# Vista para el formulario de encuesta
def encuesta_view(request):
    if request.method == 'POST':
        form = EncuestaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('gracias')  # Redirige a la página de gracias
    else:
        form = EncuestaForm()  # Si es GET o el formulario está vacío

    return render(request, 'Paises/encuesta.html', {'form': form})  # Pasa el formulario a la plantilla

# Vista para la página de agradecimiento
def gracias_view(request):
    return render(request, 'Paises/gracias.html')  # Mostrar la página de agradecimiento