from django.shortcuts import render , redirect , get_object_or_404
from .models import Category 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")  # ya email agar use karna hai
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")  # aapka SB Admin login template

# Logout View
def logout_view(request):
    logout(request)
    return redirect("login")

# Home Page (protected)
@login_required(login_url="login")
def home(request):
    return render(request, "index.html")  # apka dashboard page
def home(request):
    return render(request, 'index.html')

def category_list(request):
    categories = Category.objects.all()  # fetch all categories
    return render(request, 'category_list.html', {'categories': categories})


def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Category.objects.create(name=name, description=description)
        return redirect("category_list")
    return render(request, "add_category.html")

def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.name = request.POST.get("name")
        category.description = request.POST.get("description")
        category.save()
        return redirect("category_list")
    return render(request, "edit_category.html", {"category": category})

# Delete
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect("category_list")