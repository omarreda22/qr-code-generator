from django.shortcuts import render


def qr_home(request):
    context = {}
    return render(request, 'home.html', context)


def qr_create(request):
    context = {}
    return render(request, "apps/qr-codes/create.html", context)