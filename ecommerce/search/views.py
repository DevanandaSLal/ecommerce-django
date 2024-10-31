from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

# Create your views here.
def search_products(request):
    query = ""
    p = None  # Initialize `p` as None to avoid UnboundLocalError

    if request.method == "POST":
        query = request.POST.get('q', '')  # Use get to safely retrieve 'q'
        if query:
            p = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
        else:
            p = []  # Set p to an empty list if the query is empty

    return render(request, 'search.html', {'product': p, 'q': query})
