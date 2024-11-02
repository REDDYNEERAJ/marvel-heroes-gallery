from django.urls import path
from . import views


urlpatterns = [
    path('avengers/ironman/',views.ironman),
    path('avengers/',views.avengers),
    path('avengers/captainamerica/',views.captainamerica),
    path('avengers/thor/',views.thor),
    path('avengers/hulk/',views.hulk),
    path('avengers/blackpanther/',views.blackpanther),
    path('avengers/doctorstrange/',views.doctorstrange),
    path('avengers/spiderman/',views.spiderman)
]