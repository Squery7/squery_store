from django.shortcuts import render, redirect
from gestion_usuarios.models import Pokemon
from squery_store.forms import PokemonForm

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def biblioteca(request):
    # hacer un select a la base de datos y pasarle los datos a la plantilla
    pokemones = Pokemon.objects.all()

    return render(request, 'biblioteca.html', {"pokemones": pokemones})

def perfil(request):

    return render(request, 'perfil.html')

def subir_producto(request):
    # print(vars(request))
    if request.POST:
        print("Nombre: ",request.POST['nombre'])
        print("Tipo: ",request.POST['tipo'])
        print("Nivel: ",request.POST['nivel'])
        print("Imagen: ",request.FILES['imagen'])
        print("Descripcion: ",request.POST['descripcion'])

    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = PokemonForm()
    return render(request, 'cargar_imagen.html', {'form': form})