from django.shortcuts import reverse
from django.http import HttpResponseRedirect


def require_role(role='user'):
    def _deco(func):
        def __dec(request, *args, **kwargs):
            if not request.user.is_authenticated():
                return HttpResponseRedirect('/login')
            return func(request, *args, **kwargs)
        return __dec
    return _deco