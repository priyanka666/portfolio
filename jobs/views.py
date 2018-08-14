from django.shortcuts import render, get_object_or_404
from .models import Jobs
def Home(request):
    jobs = Jobs.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
