from urllib.parse import urlparse

from django.shortcuts import redirect, render_to_response
from django.contrib import auth
from django.template.context_processors import csrf
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import TemporaryBanIp
from django.utils import timezone

class ELogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class ELoginView(View):

    def get(self, request):
        # если пользователь авторизован, то делаем редирект на главную страницу
        if auth.get_user(request).is_authenticated:
            return redirect('/')
        else:
            # Иначе формируем контекст с формой авторизации и отдаём страницу
            # с этим контекстом.
            # работает, как для url - /admin/login/ так и для /accounts/login/
            context = create_context_username_csrf(request)
            return render_to_response('registration/login.html', context=context)

    def post(self, request):
        # забираем данные формы авторизации из запроса
        form = AuthenticationForm(request, data=request.POST)

        # забираем IP адрес из запроса
        ip = get_client_ip(request)
        # получаем или создаём новую запись об IP, с которого вводится пароль, на предмет блокировки
        obj, created = TemporaryBanIp.objects.get_or_create(
            defaults={
                'ip_address': ip,
                'time_unblock': timezone.now()
            },
            ip_address=ip
        )

        # если IP заблокирован и время разблокировки не настало
        if obj.status is True and obj.time_unblock > timezone.now():
            context = create_context_username_csrf(request)
            if obj.attempts == 3:
                # то открываем страницу с сообщением о блокировки на 15 минут при 3 и 6 неудачных попытках входа
                return render_to_response('registration/block_1_minute.html', context=context)
        elif obj.status is True and obj.time_unblock < timezone.now():
            # если IP заблокирован, но время разблокировки настало, то разблокируем IP
            obj.status = False
            obj.save()

        # если пользователь ввёл верные данные, то авторизуем его и удаляем запись о блокировке IP
        if form.is_valid():
            auth.login(request, form.get_user())
            obj.delete()

            return HttpResponseRedirect('/')
        else:
            # иначе считаем попытки и устанавливаем время разблокировки и статус блокировки
            obj.attempts += 1
            if obj.attempts >= 3: # TODO ME
                obj.time_unblock = timezone.now() #+ timezone.timedelta(minutes=1)
                obj.status = True
                obj.attempts = 0
            obj.save()
            return HttpResponseRedirect('/users/login')

        context = create_context_username_csrf(request)
        context['login_form'] = form

        return render_to_response('registration/login.html', context=context)


# вспомогательный метод для формирования контекста с csrf_token
# и добавлением формы авторизации в этом контексте
def create_context_username_csrf(request):
    context = {}
    context.update(csrf(request))
    context['login_form'] = AuthenticationForm
    return context


# для получения айпи пользователя
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
