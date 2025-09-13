from django.shortcuts import render,redirect
from django.http import HttpResponse

def login_view(request):
    error = None
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        if usuario == "inacap" and password == "clinica2025":
            request.session['autenticado'] = True
            return redirect('/recepcion/registrar/')
        else:
            error = "Usuario o clave incorrectos intentelo otra vez."
            
            
    return render(request, 'Clinica_PC/login.html', {'error': error})

# Create your views here.
