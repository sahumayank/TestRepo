from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render,redirect
from service.utility.DataValidator import DataValidator
from service.service.ForgetPasswordService import ForgetPasswordService
from service.service.EmailService import EmailService
from service.service.EmailMessage import EmailMessage
from service.models import User
class ForgetPasswordCtl(BaseCtl):

    def request_to_form(self,requestFrom):
        self.form["loginId"]  = requestFrom["loginId"]
    
    def input_validation(self):
        super().input_validation()
        inputError =  self.form["inputError"]
        if(DataValidator.isNull(self.form["loginId"])):
            inputError["loginId"] = "Login can not be null"
            self.form["error"] = True
        return self.form["error"]

    def display(self,request,params={}):
        res = render(request,self.get_template())
        return res

    def submit(self,request,params={}):
        if(self.input_validation()):
            return render(request,self.get_template(),{"form":self.form})
        else:     
            q= User.objects.filter( login = self.form["loginId"])
            userList=""
            for userData in q:
                userList=userData
            if(userList!=""):
                emsg=EmailMessage()
                emsg.to= [userList.login]
                emsg.subject= "Forget Password"
                mailResponse=EmailService.send(emsg,"forgotPassword",userList)
                if(mailResponse==1):
                    self.form["error"] = False
                    self.form["message"] = "Password is send on your Mail"
                    res = render(request,self.get_template(),{"form":self.form})
                    request.session["user"] = userList
                    res = render(request,self.get_template(),{"form":self.form})
                else:
                    self.form["error"] = True
                    self.form["message"] = "Please Check Your Internet Connection"
                    res = render(request,self.get_template(),{"form":self.form})
            else:
                self.form["error"] = True
                self.form["message"] = "login id is not correct"
                res = render(request,self.get_template(),{"form":self.form})

        
        return res

    # Template html of Role page    
    def get_template(self):
        return "ors/ForgetPassword.html"        

    # Service of Role     
    def get_service(self):
        return ForgetPasswordService()        


