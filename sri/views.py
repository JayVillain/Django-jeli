from django.shortcuts import render, redirect
from .models import (
    Pendaftar, Negara, Provinsi,
    Kabupaten, Kecamatan, Desa
)

def daftar(request):
    data = request.POST

    selected_negara = data.get('negara')
    selected_provinsi = data.get('provinsi')
    selected_kabupaten = data.get('kabupaten')
    selected_kecamatan = data.get('kecamatan')

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
        action = data.get('action')

        if action == 'save':
            nama = data.get('nama')
            email = data.get('email')

            if not nama:
                return render(request, 'daftar.html', {
                    'error': 'Nama wajib diisi',
                    'negara_list': negara_list,
                    'provinsi_list': provinsi_list,
                    'kabupaten_list': kabupaten_list,
                    'kecamatan_list': kecamatan_list,
                    'desa_list': desa_list,
                    'data': data,
                })

            Pendaftar.objects.create(
                nama=nama,
                email=email,
                negara_id=selected_negara,
                provinsi_id=selected_provinsi,
                kabupaten_id=selected_kabupaten,
                kecamatan_id=selected_kecamatan,
                desa_id=data.get('desa')
            )

            return redirect('sri:sukses')

    return render(request, 'daftar.html', {
        'negara_list': negara_list,
        'provinsi_list': provinsi_list,
        'kabupaten_list': kabupaten_list,
        'kecamatan_list': kecamatan_list,
        'desa_list': desa_list,
        'data': data,
    })


def sukses(request):
    return render(request, 'sukses.html')
