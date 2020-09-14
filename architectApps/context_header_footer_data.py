from .models import Company_details


def context_data(request):
    query = Company_details.objects.all()
    return {'context_data': query, }
