from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import ProfileForm, UserLoginForm, UserRegisterForm

# ログイン機能を提供するビュー
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}様、ログイン成功")

                # ログイン後にリダイレクト
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'ログイン',
        'form': form
    }
    return render(request, 'users/login.html', context)

# ユーザー登録機能を提供するビュー
def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}様、新規登録成功")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'ユーザー登録',
        'form': form
    }
    return render(request, 'users/registration.html', context)

# プロファイル管理機能を提供するビュー（ログインが必要）
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "保存成功")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    
    context = {
        'title': 'プロファイル',
        'form': form
    }
    return render(request, 'users/profile.html', context)

# ユーザーのカートページを表示するビュー
def users_cart(request):
    return render(request, 'users/users_cart.html')

# ログアウト機能を提供するビュー（ログインが必要）
@login_required
def logout(request):
    messages.success(request, "ログアウト成功")
    auth.logout(request)
    return redirect(reverse('main:index'))