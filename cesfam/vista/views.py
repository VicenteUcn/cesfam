from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .form import *



# Create your views here.



def programas(request):
    return render(request, 'programas.html')


def inicio(request):
    """
    form_class = citaForm
    formulario = form_class(request.POST)

    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        pass


    citas = cita.objects.all()
    context = {
        'form': formulario,

        'lista': cita.objects.all(),

    }
"""
    return render(request, 'modulos/inicio.html', )





def pacientes(request):

    form_class=PacienteForm
    formulario=form_class(request.POST or None)

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return redirect('pacientes')
    else:
       pass

    context= {
        'form':formulario,
        'lista':Pacientes.objects.all()
        
    }

    return render(request, 'modulos/usuarios.html',context )


def programas(request):

    return render(request, 'modulos/programas.html',)


def calendario(request):
    return render(request, 'modulos/calendario.html',)




def citas(request):
    """
    form_class = citaForm
    formulario = form_class(request.POST)

    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return redirect('persona')
    else:
        pass

    citas=cita.objects.all()
    context={
        'form':formulario,
        'lista':cita.objects.all()
    }
"""
    return render(request, 'modulos/citas.html',)


def buscar(request):
   
    return render(request,'buscar.html')

def modificar_paciente(request, rut):

    form_class =PacienteForm
    rutPaciente = get_object_or_404(Pacientes, rut_paciente=rut)
    formulario = form_class(data=request.POST, instance=rutPaciente)

    data = {
        'form': PacienteForm(instance=rutPaciente)
    }
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()

            return redirect(to='pacientes')
    else:
        pass

    return render(request, 'modulos/modificar.html', data )

