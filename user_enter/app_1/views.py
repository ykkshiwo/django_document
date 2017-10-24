#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms
from .models import User
# Create your views here.


def index(request):
    HttpResponse("hello")


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')


def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']

            User.objects.create(username=username, password=password, email=email)
            User.save()

            return HttpResponse('regist success!!!')
    else:
        userform = UserForm()
    return render_to_response('regist.html', {'userform': userform})


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(username__exact=username,password__exact=password)

            if user:
                return render_to_response('index.html', {'userform': userform})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')
    else:
        userform = UserForm()
    return render_to_response('login.html', {'userform': userform})