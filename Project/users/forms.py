from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User

# ユーザーログインフォームを定義
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']  # フォームに表示するフィールド

# ユーザー登録フォームを定義
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']  # フォームに表示するフィールド

    first_name = forms.CharField()  # 名前入力フィールド
    last_name = forms.CharField()  # 苗字入力フィールド
    username = forms.CharField()  # ユーザー名入力フィールド
    email = forms.CharField()  # メールアドレス入力フィールド
    password1 = forms.CharField()  # パスワード入力フィールド
    password2 = forms.CharField()  # パスワード確認フィールド

# ユーザープロファイルフォームを定義
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['image', 'first_name', 'last_name', 'username', 'email']  # フォームに表示するフィールド

    image = forms.ImageField(required=False)  # プロファイル画像フィールド（任意）
    first_name = forms.CharField()  # 名前入力フィールド
    last_name = forms.CharField()  # 苗字入力フィールド
    username = forms.CharField()  # ユーザー名入力フィールド
    email = forms.CharField()  # メールアドレス入力フィールド