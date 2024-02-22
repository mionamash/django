from django.shortcuts import render

def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def contacts(request):
    return render(request,'contacts.html')
def gallery(request):
    return render(request,'gallery.html')