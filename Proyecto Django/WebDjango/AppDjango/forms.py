from django import forms
# TORNEOS
class TorneosForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Torneo", max_length=50)
    año = forms.IntegerField(label="Año del Torneo", widget=forms.NumberInput(attrs={'placeholder':"2022"}))
    pais = forms.CharField(label="País del Torneo", max_length=50)
    duracion = forms.IntegerField(label="Duración del Torneo", widget=forms.NumberInput(attrs={'placeholder':'6 meses'}))
    campeon = forms.CharField(label="Equipo Campeón", max_length=100)

class BuscarTorneosForm(forms.Form):
    torneo_a_buscar = forms.CharField(label="Buscar Torneo")


# EQUIPOS
class EquiposForms(forms.Form):
    nombre = forms.CharField(label="Nombre del Equipo", max_length=100)
    pais = forms.CharField(label="País del Equipo", max_length=100)
    fecha_fundacion = forms.DateField(label="Fecha de Fundación", input_formats=["%d/%m/%Y"], widget=forms.TextInput(attrs={'placeholder': '25/05/1901'}))
    estadio = forms.CharField(label="Nombre del Estadio", max_length=100)
    provincia = forms.CharField(label="Provincia del Equipo", max_length=50)

class BuscarEquiposForm(forms.Form):
    equipo_a_buscar = forms.CharField(label="Buscar Equipo")


# JUGADORES
class JugadoresForms(forms.Form):
    nombre = forms.CharField(label="Nombre del Jugador", max_length=50)
    apellido = forms.CharField(label="Apellido del Jugador", max_length=50)
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", input_formats=["%d/%m/%Y"], widget=forms.TextInput(attrs={'placeholder': '13/12/1990'}))
    nacionalidad = forms.CharField(label="Nacionalidad", max_length=100)
    equipo = forms.CharField(label="Equipo Actual", max_length=100)
    posicion = forms.CharField(label="Posición", max_length=20)
    valor = forms.CharField(label="Valor del Pase", widget=forms.TextInput(attrs={'placeholder':"100M U$D"}))

class BuscarJugadoresForms(forms.Form):
    jugador_a_buscar = forms.CharField(label="Buscar Jugador")