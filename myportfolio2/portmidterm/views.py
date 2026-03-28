from django.shortcuts import render
from .models import Skills

def portmidterm(request):
  skills = Skills.objects.all()
  context = {'skills':skills}

  return render(request, 'portfolio.html', context)