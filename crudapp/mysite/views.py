from django.shortcuts import render

def home(request):
    """
    Rendert de homepage.
    """
    return render(request, 'index.html', {})

def contact(request):
    """
    Rendert de contactpagina.
    """
    return render(request, 'contact.html', {})

def about(request):
    """
    Rendert de over ons-pagina.
    """
    return render(request, 'about.html', {})