from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Paciente
from .serializers import PacienteSerializer

@api_view(['GET'])
def api_lista_pacientes(request):
    Pacientes = Paciente.objects.all()
    serializer = PacienteSerializer(Pacientes, many=True)
    return Response(serializer.data)
    


@api_view(['POST'])
def api_agregar_pacientes(request):
    serializer = PacienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_modificar_pacientes(request, pk):
    try:
        Pacientes = Paciente.objects.get(pk=pk)
    except Paciente.DoesNotExist:
        return Response({'error':'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PacienteSerializer(Pacientes, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def api_eliminar_pacientes(request, pk):
    try:
        Pacientes = Paciente.objects.get(pk=pk)
    except Paciente.DoesNotExist:
        return Response({'error':'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    Pacientes.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)