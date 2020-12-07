
from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORS.utility.DataValidator import DataValidator
from service.forms import CollegeForm
from service.models import College
from service.service.CollegeService import CollegeService

class CollegeListCtl(BaseCtl):

    def request_to_form(self,requestForm):
        self.form["collegeName"]=requestForm.get("collegeName",None)
        self.form["collegeAddress"]=requestForm.get("collegeAddress",None)
       

    def display(self,request,params={}):
        self.page_list = self.get_service().search(self.form)
        res = render(request,self.get_template(),{"pageList":self.page_list})
        return res

    def deleteRecord(self,request,params={}):
        self.page_list = self.get_service().search(self.form)
        if( params["id"] > 0):
            r = self.get_service().get(params["id"])
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
        self.page_list = self.get_service().search(self.form)
        res = render(request,self.get_template(),{"pageList":self.page_list, "form":self.form})
        return res
        
    def get_template(self):
        return "ors/CollegeList.html"          

    # Service of College     
    def get_service(self):
        return CollegeService()        




