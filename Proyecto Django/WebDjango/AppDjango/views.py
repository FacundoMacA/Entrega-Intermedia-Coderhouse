# IMPORTS
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from AppDjango.models import Torneos, Equipos, Jugadores
from AppDjango.forms import TorneosForm, EquiposForms, JugadoresForms, BuscarTorneosForm, BuscarEquiposForm, BuscarJugadoresForms



#-----------------------------------------------------------------
# VISTA INICIO
def inicio(request):
    template = loader.get_template('AppDjango/landing_page.html')
    context = {}
    return HttpResponse(template.render(context, request))




# TORNEOS:
#-----------------------------------------------------------------
# LISTAR
def torneos_index(request):
    torneo = Torneos.objects.all()
    template = loader.get_template('AppDjango/list_torneo.html')
    context = {
        'torneos': torneo,
    }
    return HttpResponse(template.render(context, request))
#-----------------------------------------------------------------
# AGREGAR
def agregar_torneo(request):
    if request.method == "POST":
        form = TorneosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            año = form.cleaned_data['año']
            pais = form.cleaned_data['pais']
            duracion = form.cleaned_data['duracion']
            campeon = form.cleaned_data['campeon']

            Torneos(nombre=nombre, año=año, pais=pais, duracion=duracion, campeon=campeon).save()
            return HttpResponseRedirect("/torneos/")
    elif request.method == "GET":
        form = TorneosForm()
    else:
        return HttpResponseBadRequest("ERROR --> No conozco el método para esta request.")
    
    return render(request, 'AppDjango/load_torneo.html', {'form':form})
#-----------------------------------------------------------------
# BORRAR
def borrar_torneo(request, identificador):
    if request.method == "GET":
        torneo = Torneos.objects.filter(id=int(identificador)).first()
        if torneo:
            torneo.delete()
        return HttpResponseRedirect("/torneos/")
    else:
        return HttpResponseBadRequest("ERROR --> No conozco este método para esta request")
#-----------------------------------------------------------------
# BUSCAR
def buscar_torneo(request):
    if request.method == "GET":
        form_busqueda = BuscarTorneosForm()
        return render(request, 'AppDjango/search_torneo.html', {"form_busqueda": form_busqueda})
    elif request.method == "POST":
        form_busqueda = BuscarTorneosForm(request.POST)
        if form_busqueda.is_valid():
            torneo_a_buscar = form_busqueda.cleaned_data['torneo_a_buscar']
            torneos = Torneos.objects.filter(nombre__icontains=torneo_a_buscar)
        return  render(request, 'AppDjango/list_torneo.html', {"torneos": torneos})




# EQUIPOS:
#-----------------------------------------------------------------
# LISTAR
def equipos_index(request):
    equipo = Equipos.objects.all()
    template = loader.get_template('AppDjango/list_equipo.html')
    context = {
        'equipos':equipo,
    }
    return HttpResponse(template.render(context,request))
#-----------------------------------------------------------------
# AGREGAR
def agregar_equipo(request):
    form = EquiposForms(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        pais = form.cleaned_data['pais']
        fecha_fundacion = form.cleaned_data['fecha_fundacion']
        estadio = form.cleaned_data['estadio']
        provincia = form.cleaned_data['provincia']

        Equipos(nombre=nombre, pais=pais, fecha_fundacion=fecha_fundacion, estadio=estadio, provincia=provincia).save()
        return HttpResponseRedirect("/equipos/")
    elif request.method == "GET":
        form = EquiposForms()
    else:
        return HttpResponseBadRequest("ERROR --> No conozco el método para esta request.")
    
    return render(request, 'AppDjango/load_equipo.html', {'form':form})
#-----------------------------------------------------------------
# BORRAR
def borrar_equipo(request, identificador):
    if request.method == "GET":
        equipo = Equipos.objects.filter(id=int(identificador)).first()
        if equipo:
            equipo.delete()
        return HttpResponseRedirect("/equipos/")
    else:
        return HttpResponseBadRequest("ERROR --> No conozco este método para esta request")
#-----------------------------------------------------------------
# BUSCAR
def buscar_equipo(request):
    if request.method == "GET":
        form_busqueda = BuscarEquiposForm()
        return render(request, 'AppDjango/search_equipo.html', {"form_busqueda":form_busqueda})
    elif request.method == "POST":
        form_busqueda = BuscarEquiposForm(request.POST)
        if form_busqueda.is_valid():
            equipo_a_buscar = form_busqueda.cleaned_data['equipo_a_buscar']
            equipos = Equipos.objects.filter(nombre__icontains=equipo_a_buscar)
        return render(request, 'AppDjango/list_equipo.html', {"equipos":equipos})



    
# JUGADORES:
#-----------------------------------------------------------------
# LISTAR
def jugadores_index(request):
    jugador = Jugadores.objects.all()
    template = loader.get_template('AppDjango/list_jugador.html')
    context = {
        'jugadores':jugador,
    }
    return HttpResponse(template.render(context,request))
#-----------------------------------------------------------------
# AGREGAR
def agregar_jugador(request):
    form = JugadoresForms(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        nacionalidad = form.cleaned_data['nacionalidad']
        equipo = form.cleaned_data['equipo']
        posicion = form.cleaned_data['posicion']
        valor = form.cleaned_data['valor']

        Jugadores(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, nacionalidad=nacionalidad, equipo=equipo, posicion=posicion, valor=valor).save()
        return HttpResponseRedirect('/jugadores/')
    elif request.method == "GET":
        form = JugadoresForms()
    else:
        return HttpResponseBadRequest("ERROR --> No conozco el método para esta request.")
    
    return render(request, 'AppDjango/load_jugador.html', {'form':form})
#-----------------------------------------------------------------
# BORRAR
def borrar_jugador(request, identificador):
    if request.method == "GET":
        jugador = Jugadores.objects.filter(id=int(identificador)).first()
        if jugador:
            jugador.delete()
        return HttpResponseRedirect('/jugadores/')
    else:
        return HttpResponseBadRequest("ERROR --> No conozco este método para esta request")
#-----------------------------------------------------------------
# BUSCAR
def buscar_jugador(request):
    if request.method == "GET":
        form_busqueda = BuscarJugadoresForms()
        return render(request, 'AppDjango/search_jugador.html', {"form_busqueda":form_busqueda})
    elif request.method == "POST":
        form_busqueda = BuscarJugadoresForms(request.POST)
        if form_busqueda.is_valid():
            jugador_a_buscar = form_busqueda.cleaned_data['jugador_a_buscar']
            jugadores = Jugadores.objects.filter(apellido__icontains=jugador_a_buscar)
        return render(request, 'AppDjango/list_jugador.html', {'jugadores':jugadores})