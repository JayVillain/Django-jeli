from django.shortcuts import render, redirect
from .models import (
    Pendaftar, Negara, Provinsi,
    Kabupaten, Kecamatan, Desa
)

def daftar(request):
    selected_negara = request.POST.get('negara')
    selected_provinsi = request.POST.get('provinsi')
    selected_kabupaten = request.POST.get('kabupaten')
    selected_kecamatan = request.POST.get('kecamatan')

    negara_list = Negara.objects.all()
    provinsi_list = Provinsi.objects.filter(
        negara_id=selected_negara
    ) if selected_negara else Provinsi.objects.none()

    kabupaten_list = Kabupaten.objects.filter(
        provinsi_id=selected_provinsi
    ) if selected_provinsi else Kabupaten.objects.none()

    kecamatan_list = Kecamatan.objects.filter(
        kabupaten_id=selected_kabupaten
    ) if selected_kabupaten else Kecamatan.objects.none()

    desa_list = Desa.objects.filter(
        kecamatan_id=selected_kecamatan
    ) if selected_kecamatan else Desa.objects.none()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'save':
            nama = request.POST.get('nama')
            email = request.POST.get('email')

            if not nama:
                return render(request, 'daftar.html', {
                    'error': 'Nama wajib diisi',
                    'negara_list': negara_list,
                    'provinsi_list': provinsi_list,
                    'kabupaten_list': kabupaten_list,
                    'kecamatan_list': kecamatan_list,
                    'desa_list': desa_list,
                })

            Pendaftar.objects.create(
                nama=nama,
                email=email,
                negara_id=selected_negara,
                provinsi_id=selected_provinsi,
                kabupaten_id=selected_kabupaten,
                kecamatan_id=selected_kecamatan,
                desa_id=request.POST.get('desa')
            )

            return redirect('sri:sukses')

        return render(request, 'daftar.html', {
            'negara_list': negara_list,
            'provinsi_list': provinsi_list,
            'kabupaten_list': kabupaten_list,
            'kecamatan_list': kecamatan_list,
            'desa_list': desa_list,
        })

    return render(request, 'daftar.html', {
        'negara_list': negara_list,
        'provinsi_list': provinsi_list,
        'kabupaten_list': kabupaten_list,
        'kecamatan_list': kecamatan_list,
        'desa_list': desa_list,
    })


def sukses(request):
    return render(request, 'sukses.html')
