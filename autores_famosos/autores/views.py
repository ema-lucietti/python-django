from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from .models import Autor


def home(request):
    """Vista para la página principal"""
    return render(request, 'home.html')

class AutorListView(ListView):
    model = Autor
    template_name = 'autor_list.html'
    context_object_name = 'autores'
    
    def get_queryset(self):
        return Autor.objects.filter(activo=True)

class AutorInactivoListView(ListView):
    model = Autor
    template_name = 'autor_inactivo.html'
    context_object_name = 'autores'
    
    def get_queryset(self):
        return Autor.objects.filter(activo=False)


def autor_json_list(request):
    """Vista para mostrar todos los autores en formato JSON"""
    autores = list(Autor.objects.all().values())
    return JsonResponse(autores, safe=False)

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autor_detail.html'
    context_object_name = 'autor'

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

def toggle_autor_status(request, pk):
    """Vista para cambiar el estado de un autor (activo/inactivo)"""
    autor = get_object_or_404(Autor, pk=pk)
    autor.activo = not autor.activo
    autor.save()
    return redirect('autor_detail', pk=pk)