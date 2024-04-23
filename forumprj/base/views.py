from django.shortcuts import render

# Create your views here.
def index(request):

    print(request.META.get('HTTP_USER_AGENT'))
    
    return render(request, 'base.html')

def error(request):
    return render(request, 'error.html')
