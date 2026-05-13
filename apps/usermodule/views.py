from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registerUser(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered")
            return redirect("/users/login/")
        else:
            messages.error(request, "Registration error. Please check the form.")

    return render(request, "usermodule/register.html", {"form": form})


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect("/books/lab11/liststudents/")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "usermodule/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("/users/login/")