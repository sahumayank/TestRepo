from django.shortcuts import render,redirect
from service.utility.DataValidator import DataValidator
from django.http import HttpResponse
from .BaseCtl import BaseCtl
from service.models import User
from service.service.UserService import UserService
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class UserListCtl(BaseCtl):

    def request_to_form(self,requestForm):
        self.form["firstName"] = requestForm.get( "firstName", None)
        self.form["lastName"] =  requestForm.get( "lastName", None) 
        self.form["login"] =  requestForm.get( "login", None) 
        self.form["next"] =  requestForm.get( "next", None) 
        self.form["pageNo"] =  requestForm.get( "pageNo", None) 
        self.form["previous"] =  requestForm.get( "previous", None) 
        self.form["goto"] =  requestForm.get( "goto", None)
        self.form["ids"]= requestForm.getlist( "ids", None)
        


    def display(self,request,params={}):
        self.page_list = self.get_service().search(self.form)
        user_list = self.get_service().search(self.form)
        page = request.GET.get('page', 1)
        paginator = Paginator(user_list, 5)
        try:
            self.page_list = paginator.page(page)
        except PageNotAnInteger:
            self.page_list = paginator.page(1)
        except EmptyPage:
            self.page_list = paginator.page(paginator.num_pages)
        res = render(request,self.get_template(),{"pageList":self.page_list})
        return res

    def deleteRecord(self,request,params={}):
        for ids in self.form["ids"]:
            self.page_list = self.get_service().search(self.form)
            id=int(ids)
            if( id > 0):
                r = self.get_service().get(id)
                if r is not None:
                    self.get_service().delete(r.id)
                    self.form["error"] = False
                    self.form["message"] = "Data is delete"
                    res = render(request,self.get_template(),{"pageList":self.page_list})
                else:
                    self.form["error"] = False
                    self.form["message"] = "Data is not delete"
                    res = render(request,self.get_template(),{"pageList":self.page_list})
        return res

    def submit(self,request,params={}):
        self.request_to_form(request.POST)
        user_list = self.get_service().search(self.form)
        p=self.form["pageNo"]
        paginator = Paginator(user_list, 10)
        #try:
        self.page_list = paginator.page(p)
        #except PageNotAnInteger:
            #self.page_list = paginator.page(1)
        #except EmptyPage:
            #self.page_list = paginator.page(paginator.num_pages)
        res = render(request,self.get_template(),{"pageList":self.page_list, "form":self.form})
        return res
        
    def get_template(self):
        return "ors/UserList.html" 
    # Service of Role     
    def get_service(self):
        return UserService()        



