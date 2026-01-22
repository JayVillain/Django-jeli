from django.shortcuts import render, redirect
from .models import Pendaftar

def daftar(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')

        if not nama:
            return render(request, 'daftar.html', {
                'error': 'Nama wajib diisi'
            })

        Pendaftar.objects.create(
            nama=nama,
            email=email
        )

        return redirect('sri:sukses')

    return render(request, 'daftar.html')


def sukses(request):
    return render(request, 'sukses.html')
