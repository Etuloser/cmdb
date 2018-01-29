from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from ldap3 import Server, Connection, ALL, NTLM


def login(request):
    return render(request, 'login\login.html')


@csrf_exempt
def login_post(request):
    if request.is_ajax():
        server = Server('luxshare.com.cn', get_info=ALL)
        username = request.POST.get('username')
        password = request.POST.get('password')
        conn = Connection(server, user='luxshare\\' + username, password=password, authentication=NTLM,
                          auto_bind=True)
        if conn:
            return HttpResponseRedirect('/')
        else:
            print('error')
