


from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.models import College
from service.forms import CollegeForm
from service.service.CollegeService import CollegeService
from rest_framework.parsers import JSONParser
from service.Serializers import CollegeSerializers
from django.http.response import JsonResponse
import json
from django.core import serializers

class CollegeCtl(): 
    def get(self,request, params = {}):
        service=CollegeService()
        c=service.get(params["id"])
        res={}
        if(c!=None):
            res["data"]=c.to_json()
            res["error"]=False
            res["message"]="Data is found"
        else:
            res["error"]=True
            res["message"]="record not found"
        return JsonResponse({"data":res["data"]})

    def delete(self,request, params = {}):
        service=CollegeService()
        c=service.get(params["id"])
        res={}
        if(c!=None):
            service.delete(params["id"])
            res["data"]=c.to_json()
            res["error"]=False
            res["message"]="Data is Successfully deleted"
        else:
            res["error"]=True
            res["message"]="Data is not deleted"
        return JsonResponse({"data":res["data"]})

    def search(self,request, params = {}):
        service=CollegeService()
        c=service.search(params)
        res={}
        data=[]
        for x in c:
            data.append(x.to_json())
        if(c!=None):
            res["data"]=data
            res["error"]=False
            res["message"]="Data is found"
        else:
            res["error"]=True
            res["message"]="record not found"
        return JsonResponse({"data":res})

    def form_to_model(self,obj,request):
        pk = int(request["id"])
        if(pk>0):
            obj.id = pk
        obj.collegeName = request["collegeName"]
        obj.collegeAddress = request["collegeAddress"]
        obj.collegeState=request["collegeState"] 
        obj.collegeCity=request["collegeCity"] 
        obj.collegePhoneNumber=request["collegePhoneNumber"] 
        return obj

    def save(self,request, params = {}):        
        json_request=json.loads(request.body)     
        r=self.form_to_model(College(), json_request)
        service=CollegeService()
        c=service.save(r)
        res={}
        if(r!=None):
            res["data"]=r.to_json()
            res["error"]=False
            res["message"]="Data is Successfully saved"
        else:
            res["error"]=True
            res["message"]="Data is not saved"
        return JsonResponse({"data":res})

    # Template html of Role page    
    def get_template(self):
        return "orsapi/College.html"          

    # Service of Role     
    def get_service(self):
        return CollegeService()        


       



