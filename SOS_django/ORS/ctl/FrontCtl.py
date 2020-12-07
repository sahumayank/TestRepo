from django.http import HttpResponse
from django.shortcuts import render,redirect
from ORS.ctl.WelcomeCtl import WelcomeCtl
from ORS.ctl.LoginCtl import LoginCtl

class FrontCtl(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    '''def process_view(self,request,view_func,*view_args,**view_kargs):
        if request.session.get('name')!=None:
            pass
        else:
            return redirect("/ORS/Login")'''
    