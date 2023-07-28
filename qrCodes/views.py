from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import QRCode
from .forms import QRCodeForm


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def qr_home(request):
    context = {}
    return render(request, 'home.html', context)


def qr_create_page(request):
    context = {}
    return render(request, "apps/qr-codes/create.html", context)


def qr_create_request(request):
    # print(request.POST.get('url'))
    form = QRCodeForm(request.POST or None)
    if is_ajax(request=request):
        if form.is_valid:
            new_qr = form.save(commit=False)
            new_qr.save()
            return JsonResponse({'qr':new_qr.qr_code.url})
    return redirect('qr-codes:create')