from django.shortcuts import render
#from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AutorSerializer
from autores.models import Autor

# Create your views here.

#class AutorListAPIview(ListAPIView):
#    queryset = Autor.objects.all()
#    serializer_class = AutorSerializer


#class AutorRetrieveAPIview(RetrieveAPIView):
#   queryset = Autor.objects.all()
#    serializer_class = AutorSerializer


#class AutorDestroyAPIview(DestroyAPIView):
#    queryset = Autor.objects.all()
#    serializer_class = AutorSerializer


#class AutorCreateAPIview(CreateAPIView):
#    queryset = Autor.objects.all()
#    serializer_class = AutorSerializer
   

class AutorListCreateAPIView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class=AutorSerializer
    

class AutorRetrieveUpdateDestroyAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class=AutorSerializer
          