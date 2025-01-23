from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from transactions.models import Wallet_FIAT as wlt
from .models import User
from .forms import NicknameLoginForm, AccnameLoginForm


class Registration(View):
    def get(self, request):
        return render(request, 'usermanage/registration.html')
    
    def post(self, request):
        nickname = request.POST.get('nickname')
        password = make_password(request.POST.get('password'))
        favorite_word = request.POST.get('favorite_word')

        if User.objects.filter(nickname=nickname).exists():
            return render(request, 'usermanage/registration.html', {'error': 'username already exists'})

        User.objects.create(nickname=nickname, password=password, favorite_word=favorite_word)

        return redirect('/mywallets/auth0/')


class Authbynick(View):
    def get(self, request):
        form = NicknameLoginForm()
        return render(request, 'usermanage/auth_nickname.html', {'form': form})
    
    def post(self, request):
        nickname = request.POST.get('username')
        password = request.POST.get('password')

        try:
            if user := authenticate(nickname=nickname, password=password):
                login(request, user)
                return redirect(f'/mywallets/profile/{user.token}')
            else:
                return redirect('/mywallets/auth0/')
        except User.DoesNotExist:
            return render(request, 'usermanage/auth_nickname.html', {'error': 'User does not exist'})


class Authbyacc(View):
    def get(self, request):
        form = AccnameLoginForm()
        return render(request, 'usermanage/auth_account_num.html', {'form': form})

    def post(self, request):
        token = request.POST.get('token')
        password = request.POST.get('password')
        
        try:
            if user := authenticate(token=token, password=password):
                login(request, user)
                return redirect(f'/mywallets/profile/{user.token}')
            else:
                return redirect('/mywallets/auth1')
        except User.DoesNotExist:
            return render(request, 'usermanage/auth_account_num.html', {'error': 'account number or password is incorrect'})

class PersonalPage(View):
    def get(self, request, token):
        user = get_object_or_404(User, token=token)
        wallets = wlt.objects.filter(user=request.user)
        
        data = {
            "user": user,
            "wallets": wallets,
        }

        return render(request, 'usermanage/profile.html', data)
    
class Llogout(View):
    def post(self, request):
        logout(request)
        return redirect('/')
     
class Setting(View):
    def get(self, request, token):

        user = get_object_or_404(User, token=token)
        wallets = wlt.objects.filter(user=request.user)
        
        data = {
            "user": user,
            "wallets": wallets,
        }
        return render(request, 'usermanage/setting.html', data)