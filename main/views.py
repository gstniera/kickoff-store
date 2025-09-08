from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'KickOff Store',
        'name': 'Gusti Niera',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)