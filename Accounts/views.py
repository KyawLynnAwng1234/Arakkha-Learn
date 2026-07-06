from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

#custome model
from django.utils import timezone
from .models import InviteCode
User = get_user_model()

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")  # your input is still "username"
        password = request.POST.get("password")
        user = authenticate(
            request,
            email=email,   # THIS is actually email because of USERNAME_FIELD
            password=password
        )
        if user:
            login(request, user)
            if user.gender == "M" and user.role == "TEACHER":
                messages.success(request, f"သာလီစွပါ ဆရာ, {user.username}!")
            elif user.gender == "F" and user.role == "TEACHER":
                messages.success(request, f"သာလီစွပါ ဆရာမ, {user.username}!")
            elif user.role == "ADMIN":
                messages.success(request, f"သာလီစွပါ Admin, {user.username}!")
            else:
                messages.success(request, f"သာလီစွပါ {user.username}!")
            return redirect("dashboard_page")
        messages.error(request, "Invalid email or password.")
    return render(request, "login/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

def reference_code(request):
    if request.method == "POST":
        code = request.POST.get("code")
        try:
            invite = InviteCode.objects.get(code=code)
        except InviteCode.DoesNotExist:
            return render(request, "code/enter_code.html", {
                "error": "Invalid code"
            })
        if invite.is_used:
            return render(request, "code/enter_code.html", {
                "error": "Code already used"
            })
        if invite.expires_at < timezone.now():
            return render(request, "code/enter_code.html", {
                "error": "Code expired"
            })
        # redirect to registration step
        return redirect("register", code=invite.code)
    return render(request, "code/enter_code.html")

def register(request, code):
    try:
        invite = InviteCode.objects.get(code=code)
    except InviteCode.DoesNotExist:
        return redirect("enter_code")
    if invite.is_used:
        return redirect("enter_code")
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password= request.POST.get("confirm_password")
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register", code=code)

        #CHECK USERNAME
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register", code=code)

        #CHECK EMAIL
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("register",code=code)

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
            role=invite.role,
        )
        invite.is_used = True
        invite.used_by = user  # optional if you added FK
        invite.save()
        return redirect("login")
    return render(request, "register/register.html", {"code": code})
