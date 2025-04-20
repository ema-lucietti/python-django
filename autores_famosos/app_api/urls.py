from django.urls import path
from .views import(
    AutorListAPIview,
    AutorRetrieveAPIview
)

app_name = 'app_api'

urlpatterns = [
    path('', AutorListAPIview.as_view(), name='listar_api'),
    path('<int:pk>/', AutorRetrieveAPIview.as_view(), name='retrieve_api')
]
