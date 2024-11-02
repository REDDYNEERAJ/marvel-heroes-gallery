from django.shortcuts import render



def ironman(request):
    return render(request ,'site1/ironman.html')

def avengers(request):
    return render(request ,'site1/avengers.html')

def captainamerica(request):
    return render(request ,'site1/captainamerica.html')

def thor(request):
    return render(request ,'site1/thor.html')

def hulk(request):
    return render(request ,'site1/hulk.html')

def blackpanther(request):
    return render(request ,'site1/blackpanther.html')

def doctorstrange(request):
    return render(request ,'site1/doctorstrange.html')

def spiderman(request):
    return render(request ,'site1/spiderman.html')        