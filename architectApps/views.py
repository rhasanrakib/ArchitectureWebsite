from django.shortcuts import render
from .models import Company_details, Academic
# Create your views here.


def home_view(request):
    query_academic = Academic.objects.all()
    # print(query_academic)
    return render(request, 'home.html', {'academic': query_academic})


def details_view(request, section, pk):
    query = ''
    if(section == 'academic'):
        query = query_academic = Academic.objects.get(pk=pk)
    return render(request, 'details.html', {'data': query})
