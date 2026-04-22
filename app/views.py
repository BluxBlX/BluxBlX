from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # sau này xử lý login thật
        return redirect("/")

    return render(request, "index.html")


def register_view(request):
    if request.method == "POST":
        # sau này xử lý đăng ký thật
        return redirect("/")

    return render(request, "register.html")
