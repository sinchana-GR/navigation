from django.shortcuts import render

# Create your views here.
def candy(request):
    return render(request,'candy.html')