from django.shortcuts import render
from .models import Company_details, Academic, Professional
# Create your views here.


def home_view(request):
    query_academic = Academic.objects.all()
    query_professional = Professional.objects.all()
    # print(query_academic)
    return render(request, 'home.html', {'academic': query_academic, 'professional': query_professional})


def details_view(request, section, pk):
    query = ''
    if(section == 'academic'):
        query = Academic.objects.get(pk=pk)
    elif(section == 'professional'):
        query = Professional.objects.get(pk=pk)
    return render(request, 'details.html', {'data': query})
