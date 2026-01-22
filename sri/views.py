from django.shortcuts import render, redirect

def daftar(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')

        if not nama:
            return render(request, 'daftar.html', {
                'error': 'Nama wajib diisi'
            })

        return redirect('sri:sukses')

    return render(request, 'daftar.html')
def sukses(request):
    return render(request, 'sukses.html')
