from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalogs(request) :
    items = CatalogItem.objects.all()
    context = {
        "items": items,
        "student_name": "Shafa Najwa Nathania",
        "student_id": 2106634414,
    }
    return render(request, "katalog.html", context)
