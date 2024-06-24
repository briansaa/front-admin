from rest_framework import generics, response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Horario,
    Laboratorio,
    Pabellon,
    Polideportivo,
    ReservaLaboratorio,
    ReservaPolideportivo,
    Usuario,
    PabellonLaboratorio,
)
from .serializers import (
    HorarioSerializer,
    LaboratorioSerializer,
    PabellonSerializer,
    PolideportivoSerializer,
    ReservaLaboratorioSerializer,
    ReservaPolideportivoSerializer,
    UsuarioSerializer,
)


class UsuarioListView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Usuario.objects.all()
        serializer_class = UsuarioSerializer(queryset, many=True)
        return response.Response(serializer_class.data)

    def post(self, request, *args, **kwargs):

        serializer_class = UsuarioSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return response.Response(serializer_class.data)
        return response.Response("Error", status=status.HTTP_400_BAD_REQUEST)


class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PolideportivoListView(generics.ListCreateAPIView):

    def get(self, request, *args, **kwargs):
        queryset = (
            Laboratorio.objects.all()
            .filter(tipo__nombre="Polideportivo")
            .prefetch_related("pabellones")
        )
        serializer_class = LaboratorioSerializer(queryset, many=True)
        return response.Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        serializer_class = LaboratorioSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return response.Response(serializer_class.data)
        return response.Response("Error", status=status.HTTP_400_BAD_REQUEST)


class PolideportivoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polideportivo.objects.all()
    serializer_class = PolideportivoSerializer


class PabellonListView(generics.ListCreateAPIView):
    queryset = Pabellon.objects.all()
    serializer_class = PabellonSerializer


class PabellonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pabellon.objects.all()
    serializer_class = PabellonSerializer


class LaboratorioListView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = (
            Laboratorio.objects.all()
            .filter(tipo__nombre="Laboratorio")
            .prefetch_related("pabellones")
        )
        serializer_class = LaboratorioSerializer(queryset, many=True)
        return response.Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        serializer_class = LaboratorioSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return response.Response(serializer_class.data)
        return response.Response("Error", status=status.HTTP_400_BAD_REQUEST)


class LaboratorioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


class HorarioListView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Horario.objects.all().order_by("hora_inicio")
        serializer_class = HorarioSerializer(queryset, many=True)
        return response.Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        serializer_class = LaboratorioSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return response.Response(serializer_class.data)
        return response.Response("Error", status=status.HTTP_400_BAD_REQUEST)


class HorarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class ReservaPolideportivoListView(generics.ListCreateAPIView):
    queryset = ReservaLaboratorio.objects.all().filter(
        laboratorio__tipo__nombre="Polideportivo"
    )
    serializer_class = ReservaLaboratorioSerializer


class ReservaPolideportivoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReservaPolideportivo.objects.all()
    serializer_class = ReservaPolideportivoSerializer


class ReservaLaboratorioListView(generics.ListCreateAPIView):
    queryset = ReservaLaboratorio.objects.all().filter(laboratorio__tipo__nombre="Laboratorio")
    serializer_class = ReservaLaboratorioSerializer


class ReservaLaboratorioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReservaLaboratorio.objects.all()
    serializer_class = ReservaLaboratorioSerializer
