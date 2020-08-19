from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')


def apropos(request):
    return render(request, 'pages/apropos.html')

def contact(request):
    return render(request, 'pages/contact.html')


def handler400(request, exception):
    return render(request, 'erreurs/400.html')


def handler403(request, exception):
    return render(request, 'erreurs/403.html')


def handler404(request, exception):
    return render(request, 'erreurs/404.html')


def handler500(request):
    return render(request, 'erreurs/500.html')