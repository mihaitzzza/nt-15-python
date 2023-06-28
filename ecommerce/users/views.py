from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "users/register.html", {
        "form": form
    })
