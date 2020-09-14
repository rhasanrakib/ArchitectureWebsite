from django.urls import path
from . import views
urlpatterns = [

    path('', views.home_view, name='home'),
    path('details/<str:section>/<int:pk>/',
         views.details_view, name='details'),
]
