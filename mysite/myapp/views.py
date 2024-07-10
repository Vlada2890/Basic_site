from django.shortcuts import render
from .models import ExampleModel

def index(request):
    examples = ExampleModel.objects.all()
    return render(request, 'index.html', {'examples': examples})
