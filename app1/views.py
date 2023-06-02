from django.shortcuts import render

# Create your views here.
def tom(request):
    return render(request,'tom.html')
def jerry(request):
    return render(request,'jerry.html')
