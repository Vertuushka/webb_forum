from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def error(request):
    return render(request, 'error.html')
