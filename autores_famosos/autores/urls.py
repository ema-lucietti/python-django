from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/inactivos/', views.AutorInactivoListView.as_view(), name='autor_inactivos_list'),
    path('autores/json/', views.autor_json_list, name='autor_json_list'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor_detail'),
    path('autores/<int:pk>/delete/', views.AutorDeleteView.as_view(), name='autor_delete'),
    path('autores/<int:pk>/toggle/', views.toggle_autor_status, name='toggle_autor_status'),
]