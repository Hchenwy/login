from django.shortcuts import render,HttpResponseRedirect, HttpResponse, render_to_response
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from user.permission import require_role


@require_role(role='user')
def index(request):
    return render(request, 'index.html')

def Login(request):
    msg = ''
    if request.method == 'GET':
        try:
            username = request.GET.get('username')
            password = request.GET.get('password')
        except:
            pass
        print(dir(request.session))
        print(request.session.session_key)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.role == 'SU':
                    request.session['role_id'] = 2
                elif user.role == 'GA':
                    request.session['role_id'] = 1
                else:
                    request.session['role_id'] = 0
                return JsonResponse({'result': 'ok', 'msg': msg})
            else:
                msg = '用户未激活'
        else:
            msg = '用户名或密码错误.'

    return JsonResponse({'result': 'fail', 'msg': msg})