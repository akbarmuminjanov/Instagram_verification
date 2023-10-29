from django.shortcuts import render
from django.contrib import messages
from .models import Accaunt


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        acc = Accaunt.objects.create(username=username, password=password)
        acc.save()
        if acc:
            messages.success(request, "Вы успешно зарегистрированы проверьте свой аккаунт после 24 час")
        else:
            return render(request, "index.html")
    return render(request, "index.html")