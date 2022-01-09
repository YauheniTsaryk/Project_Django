from django.shortcuts import render, get_object_or_404, redirect
from .models import Catalogue, Category
from .forms import BookForm

# Create your views here.
def index(request):
    catalogue = Catalogue.objects.all()
    context = {
        'catalogue': catalogue,
        'title': 'Blog Catalogue',
    }
    return render(request, template_name='catalogue/index.html', context=context)


def get_category(request, category_id):
    catalogue = Catalogue.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'catalogue/category.html',
                  {'catalogue': catalogue, 'category': category})


def view_catalogue (request, catalogue_id):
    catalogue_item = get_object_or_404(Catalogue, pk=catalogue_id)
    #catalogue_item = Catalogue.object.get(pk= catalogue_id)
    return render(request, 'catalogue/view_catalogue.html', {"catalogue_item": catalogue_item})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Catalogue.objects.create(**form.cleaned_data)
            #присваивание поля и очистка поля
            #print(form.cleaned_data)
            return redirect('main')
    else:
        form = BookForm()
    return render(request, 'catalogue/add_book.html', {'form':form})