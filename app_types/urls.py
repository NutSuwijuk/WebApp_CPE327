from django.urls import path
from. import views

urlpatterns = [
    path('', views.types, name='types'),
    path('<int:type_id>', views.type, name='type')
]