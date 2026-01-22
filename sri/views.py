from django.shortcuts import render, redirect
from .models import Pendaftar, Negara, Provinsi, Kabupaten

def daftar(request):
    selected_negara = request.POST.get('negara')
    selected_provinsi = request.POST.get('provinsi')

    negara_list = Negara.objects.all()
    provinsi_list = Provinsi.objects.filter(negara_id=selected_negara) if selected_negara else Provinsi.objects.none()
    kabupaten_list = Kabupaten.objects.filter(provinsi_id=selected_provinsi) if selected_provinsi else Kabupaten.objects.none()

    if request.method == 'POST' and request.POST.get('action') == 'save':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        negara_id = request.POST.get('negara')
        provinsi_id = request.POST.get('provinsi')
        kabupaten_id = request.POST.get('kabupaten')

        if not nama:
            return render(request, 'daftar.html', {
                'error': 'Nama wajib diisi',
                'negara_list': negara_list,
                'provinsi_list': provinsi_list,
                'kabupaten_list': kabupaten_list,
            })

        Pendaftar.objects.create(
            nama=nama,
            email=email,
            negara_id=negara_id,
            provinsi_id=provinsi_id,
            kabupaten_id=kabupaten_id
        )

        return redirect('sri:sukses')

    return render(request, 'daftar.html', {
        'negara_list': negara_list,
        'provinsi_list': provinsi_list,
        'kabupaten_list': kabupaten_list,
    })


def sukses(request):
    return render(request, 'sukses.html')
