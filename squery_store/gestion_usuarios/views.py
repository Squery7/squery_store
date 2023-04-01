from django.shortcuts import render, redirect
from gestion_usuarios.models import Pokemon, Usuario
from gestion_usuarios.forms import PokemonForm, RegistroForm, LoginForm
from django.contrib import messages

# Create your views here.

def index(request):
    
        
    return render(request, 'index.html')

def login(request):
    
    # if request.method == "POST":
       
    #     mi_formulario = LoginForm(request.POST)
    #     info = {}
    #     if mi_formulario.is_valid():
    #         info = mi_formulario.cleaned_data
            
    #         try:
    #             objeto = Usuario.objects.get(email=info['email'])
    #         except Usuario.DoesNotExist:
    #             print("el usuario no existe")
    #             pass

    #         if objeto.password == info['password']:
                
    #             return render(request, 'index.html')
    #         print("Contraseña incorrecta")
    # else:
    #     mi_formulario = LoginForm()   

    #print(mi_formulario)
    return render(request, 'login.html') #, {"form":mi_formulario}

def registro(request):
    storage = messages.get_messages(request)
    storage.used = True
    bandera = True
    if request.POST:
        e = request.POST['email']
        objeto = ''
        try:
            objeto = Usuario.objects.get(email=e)
            if objeto.email == e:
                messages.success(request, "Error, el email ya está registrado.")
                bandera = False
                
        except Usuario.DoesNotExist:
            pass
        
    if request.method == 'POST' and bandera == True:
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    
    return render(request, 'registro.html')

def biblioteca(request):
    pokemones = Pokemon.objects.all()
    return render(request, 'biblioteca.html', {"pokemones": pokemones})

def perfil(request):
    return render(request, 'perfil.html')

def subir_producto(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'cargar_imagen.html')
    else:
        form = PokemonForm()
    return render(request, 'cargar_imagen.html', {'form': form})