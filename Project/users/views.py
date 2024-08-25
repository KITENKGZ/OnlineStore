from django.shortcuts import render

def login(request):
    context = {
        'title': 'ログイン'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'ユーザー登録'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'プロファイル'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    pass