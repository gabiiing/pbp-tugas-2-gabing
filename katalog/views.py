from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_barang':data_catalog,
        'nama': 'Gabriel Zebaoth Krisopras Putra',
        'student_id' : '2106751480',
    }

    return render(request, "katalog.html", context)