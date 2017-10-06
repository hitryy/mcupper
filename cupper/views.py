from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from cupper.forms import SignupForm
from cupper.token_registration import token_registration


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            print(user.pk)

            our_site = get_current_site(request)
            activation_token = token_registration.make_token(user)

            message_to_send = render_to_string('cupper/signup_message.html', {
                'user': user,
                'domain': our_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': activation_token
            })

            message_subject = 'Активация аккаунта'
            email_address = form.cleaned_data.get('email')

            email = EmailMessage(message_subject, message_to_send, to=[email_address])
            email.send()

            return HttpResponseRedirect('/signup_success')

    else:
        form = SignupForm()

    return render(request, 'cupper/signup.html', {'form': form})


def signup_success(request):
    return render(request, 'cupper/signup_success.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_registration.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('/activation_success')
    else:
        return render(request, 'cupper/activation_bad_token.html')