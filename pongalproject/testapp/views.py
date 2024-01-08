from django.shortcuts import render
# Create your views here.
def form_views(request):
    return render(request,'testapp/index.html')

def poo_views(request):
    return render(request,'testapp/pongal.html')
