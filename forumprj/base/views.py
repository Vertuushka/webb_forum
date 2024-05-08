from django.shortcuts import render


# Create your views here.
def index(request):

    print(request.META.get('HTTP_USER_AGENT'))
    
    return render(request, 'base.html')

def error_page(request):
    return render(request, 'error.html')

# Kiril delete it in correct way!
def custom_404_page(request, exception):
    return render(request, 'error.html')

