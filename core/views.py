from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

async def main(request):
    return render(request, 'main.html')
