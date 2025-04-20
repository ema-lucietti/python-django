from django.urls import path
from .views import(
   # AutorListAPIview,
    #AutorRetrieveAPIview,
    #AutorDestroyAPIview,
    #AutorCreateAPIview,
    AutorListCreateAPIView,
    AutorRetrieveUpdateDestroyAPIview
)

app_name = 'app_api'

urlpatterns = [
    #path('', AutorListAPIview.as_view(), name='listar_api'),
    #path('<int:pk>/', AutorRetrieveAPIview.as_view(), name='retrieve_api'),
    #path('borrar/<int:pk>/', AutorDestroyAPIview.as_view(), name='borrar_api'),
    #path('crear/', AutorCreateAPIview.as_view(), name='crear_api'),
    path('', AutorListCreateAPIView.as_view(), name='listar_crear_api'),            
    path('<int:pk>/', AutorRetrieveUpdateDestroyAPIview.as_view(),name='todo_lo_Demas') 
]
