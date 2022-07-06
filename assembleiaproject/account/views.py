from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import LoginForm
from django.contrib import messages
from ..base.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading


# Create your views here.
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('account/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email])

    # if not settings.DEBUG:
    #     EmailThread(email).start()
    EmailThread(email).start()


def register(request):
    if request.method == "POST":
        context = {'has_error': False}

        first_name = request.POST.get('first_name')
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

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Já existe usuário cadastrado com esse e-mail')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'account/register.html', context)

        user = User.objects.create_user(email=email, first_name=first_name)
        user.set_password(password)
        user.save()

        send_activation_email(user, request)

        messages.add_message(request, messages.SUCCESS,
                             'Conta criada, você recebera um link de confirmação no seu e-mail')
        return redirect('login')

    return render(request, 'account/register.html')


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
                        if user.is_superuser:
                            return redirect('admin:index')
                        else:
                            return redirect('base:home')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        print(e)
        user = None

    if user and generate_token.check_token(user, token):
        user.email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS, 'Email verificado, agora você pode logar')
        return redirect(reverse('login'))

    return render(request, 'account/activate-failed.html', {'user': user})
