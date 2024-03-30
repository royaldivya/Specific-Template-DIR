from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')


def msd(request):
    return HttpResponse('MR.Captin Cool')