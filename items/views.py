from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import NewItemForm, EditItemForm
from core.views import get_cities
from django.db import connection
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# Create your views here.


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:10]
    auth_items = Item.objects.filter(created_by=item.created_by, is_sold=False).exclude(pk=pk)[:5]

    return render(request, 'items/detail.html', {
        'item': item,
        'related_items': related_items,
        'auth_items': auth_items,
    })


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.phone_number = request.user.phone_number
            item.save()

            connection.close()
            connection.connect()
            return redirect('core:dashboard', item.created_by)
    else:
        form = NewItemForm()
    some_items = True
    return render(request, 'items/form.html', {
        'form': form,
        'title': 'New Item',
        'some_items': some_items,

    })


def browse(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, "items/index.html", {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    some_items = False
    return render(request, 'items/form.html', {
        'form': form,
        'title': 'Edit Item',
        'some_items': some_items,
    })


def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('core:dashboard', {'user': request.user})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer