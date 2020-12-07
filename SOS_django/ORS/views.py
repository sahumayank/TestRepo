from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session

#Import controller classes
from ORS.ctl.UserCtl import UserCtl
from ORS.ctl.AccountCtl import AccountCtl
from ORS.ctl.CollegeCtl import CollegeCtl
from ORS.ctl.LoginCtl import LoginCtl
from ORS.ctl.WelcomeCtl import WelcomeCtl
from ORS.ctl.RoleCtl import RoleCtl
from ORS.ctl.RoleListCtl import RoleListCtl
from ORS.ctl.FacultyCtl import FacultyCtl
from ORS.ctl.CourseCtl import CourseCtl
from ORS.ctl.StudentCtl import StudentCtl
from ORS.ctl.MarksheetCtl import MarksheetCtl
from ORS.ctl.SubjectCtl import SubjectCtl
from ORS.ctl.TimetableCtl import TimetableCtl
from ORS.ctl.UserListCtl import UserListCtl
from ORS.ctl.UserCtl import UserCtl
from ORS.ctl.CollegeListCtl import CollegeListCtl
from ORS.ctl.CourseListCtl import CourseListCtl
from ORS.ctl.MarksheetListCtl import MarksheetListCtl
from ORS.ctl.StudentListCtl import StudentListCtl
from ORS.ctl.RegistrationCtl import RegistrationCtl
from ORS.ctl.ForgetPasswordCtl import ForgetPasswordCtl
from ORS.ctl.ChangePasswordCtl import ChangePasswordCtl
from ORS.ctl.LogoutCtl import LogoutCtl
def info(request,page,action ):
    print("REQ Method: ", request.method )
    print("Page: ", page)
    print("Action: ", action)
    print("Base Path: ", __file__)    

@csrf_exempt
def actionId(request,page="", id = 0):
    if request.session.get('user') != None and page!="":
        ctlName =  page + "Ctl()"
        ctlObj = eval(ctlName)
        res=ctlObj.execute(request,{"id":id})
    elif(page=="Registration"):
        ctlName =  "Registration" + "Ctl()"
        ctlObj = eval(ctlName)
        res=ctlObj.execute(request,{"id":id})
    else:
        ctlName =  "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        res=ctlObj.execute(request,{"id":id})
    return res

@csrf_exempt
def auth(request,page="",operation="" ,id = 0 ):
    if(page=="Logout"):
        Session.objects.all().delete()
        ctlName =  page + "Ctl()"
        ctlObj = eval(ctlName)
        res=ctlObj.execute(request,{"id":id})
    elif(page=="ForgetPassword"):
        ctlName =  "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res=ctlObj.execute(request,{"id":id})
    else:
        ctlName =  "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        res=ctlObj.execute(request,{"id":id})
    return res




