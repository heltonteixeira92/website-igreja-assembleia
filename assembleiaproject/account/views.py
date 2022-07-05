from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages
# from django.conf import

# Create your views here.
def register(request):
    if request.method == "POST":
        context = {'has_error': False}
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Senha deve ser maior que 6 caracteres')
            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'A senha de confirmação deve ser igual')
            context['has_error'] = True

        # if User.objects.filter(username)

    return render(request, '')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['email'],
                                password=cd['password'])
            if user.email_verified:
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('admin:index')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})
