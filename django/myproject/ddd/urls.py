from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('ddd/', views.ddd, name='ddd'), 
] 