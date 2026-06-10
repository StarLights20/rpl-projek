from django.shortcuts import render
from .models import Mahasiswa
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)

@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()

    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})
