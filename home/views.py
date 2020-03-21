from django.shortcuts import render

def home(request):
    return render(request, "home_page.html")

def about(request):
    return render(request, "about.html")

def contact_and_resume(request):
    return render(request, "contact.html")