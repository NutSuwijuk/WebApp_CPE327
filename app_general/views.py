from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Nut</h1>')
    return render(request, 'app_general/home.html')

def about(request):
    return HttpResponse('Suwijuk')