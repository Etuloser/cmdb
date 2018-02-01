from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from ldap3 import Server, Connection, ALL, NTLM
from django.contrib.auth.models import User
import sys


class ActiveDirectoryBackend:
    def authenticate(self, username=None, password=None):
        if len(password) == 0:
            return None
        server = Server('luxshare.com.cn', get_info=ALL)
        conn = Connection(server, user='luxshare\\' + username, password=password, authentication=NTLM, auto_bind=True)
        if conn:
            return self.get_or_create_user(username,password)

    def get_or_create_user(self, username, password):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            mail = username + '@example.com'
            user = User(username=username, email=mail)
            user.is_staff=True
            user.is_superuser = False
            user.set_password(password)
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def login(request):
    return render(request, 'login\login.html')

# @csrf_exempt
# def login_post(request):
#     if request.is_ajax():
#         server = Server('luxshare.com.cn', get_info=ALL)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         conn = Connection(server, user='luxshare\\' + username, password=password, authentication=NTLM,
#                           auto_bind=True)
#         if conn:
#             return HttpResponseRedirect('/')
#         else:
#             print('error')
