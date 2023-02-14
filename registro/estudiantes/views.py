from django.shortcuts import render,redirect
from .models import estudiantes
from .forms import estudiantesForm
from django.contrib import messages
from asyncio.windows_events import NULL



def index(request,letter=NULL):
    if letter != NULL:
        estudiante=estudiantes.objects.filter(name__startswith=letter)
    else:
        estudiante=estudiantes.objects.filter(name__contains=request.GET.get('search',''))
    context={
        'estudiantes':estudiante
    }
    return render(request,'estudiantes/index.html',context)

def view(request,id):
    estudiante=estudiantes.objects.get(id=id)
    context={
        'estudiante':estudiante
    }
    return render(request,'estudiantes/detail.html',context)
def create(request):
    if request.method=="GET":
        form=estudiantesForm()
        context={
            'form':form
        }
        return render(request,'estudiantes/create.html',context)
    if request.method == "POST":
        form=estudiantesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ("estudiante")
def delete(request,id):
    if request.method =="GET":

       estudiante=estudiantes.objects.get(id=id)
       estudiante.delete()
       
       mensaje=messages.success(request, 'Estudiante eliminado.')
       context={
        'mensaje':mensaje
       }
       return render(request,'estudiantes/alertsucces.html',context)
def edit(request,id):
    estudiante=estudiantes.objects.get(id=id)
    if (request.method) == "GET":
        
        form=estudiantesForm(instance=estudiante)

        context={
            'form':form,
            'id':id
        }
        return render(request,'estudiantes/editar.html',context)
    if (request.method == "POST"):
        estudiante=estudiantesForm(request.POST,instance=estudiante)
        if estudiante.is_valid():
            estudiante.save()

      
        mensaje=messages.success(request, 'Los cambios se guardaron exitosamente.')
        context={
        'mensaje':mensaje,
        'estudiante':estudiante,
        'id':id
       }
        return render(request,'estudiantes/alertsucces.html',context)

        
    
            


    
    
   


