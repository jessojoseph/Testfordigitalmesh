from . import views
from django.urls import path


urlpatterns = [
    path('', views.tour, name="tour"),
    path('add/<int:key>/',views.add,name='add'),
]