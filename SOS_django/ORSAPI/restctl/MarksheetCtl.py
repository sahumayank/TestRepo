
from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Marksheet
from service.forms import MarksheetForm
from service.service.MarksheetService import MarksheetService
from rest_framework.parsers import JSONParser
from service.Serializers import MarksheetSerializers
from django.http.response import JsonResponse
import json
from django.core import serializers

class MarksheetCtl(): 
    def get(self,request, params = {}):
        service=MarksheetService()
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
        service=MarksheetService()
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
        service=MarksheetService()
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
        obj.rollNumber = request["rollNumber"]
        obj.name = request["name"]
        obj.physics=request["physics"]
        obj.physics=request["physics"] 
        obj.chemistry=request["chemistry"] 
        obj.maths=request["maths"] 
        obj.student_ID=request["student_ID"]
        return obj

    def save(self,request, params = {}):        
        json_request=json.loads(request.body)     
        r=self.form_to_model(Marksheet(), json_request)
        service=MarksheetService()
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
        return "orsapi/Marksheet.html"          

    # Service of Role     
    def get_service(self):
        return MarksheetService()        


       



