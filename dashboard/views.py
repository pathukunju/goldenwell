from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from . forms import LoginForm
from django.views.generic import View,CreateView,FormView,TemplateView
from django.contrib import messages
# Create your views here.




# def admin_login(request):

#         if request.method == 'POST':


#                 email = request.POST.get('email')
#                 password = request.POST.get('password')
#                 #     user_obj = User.objects.filter(email=email)

#                 user_obj = authenticate(request,email=email,password=password)
#                 print(user_obj,'===============')
                
#                 if user_obj.is_staff :
                        
#                         login(request, user_obj)
#                         return redirect('admin_dashboard')

                       
#                 elif user_obj.is_superuser:
                        
#                         login(request, user_obj)
#                         return redirect('admin_dashboard')

#         else:
#                 return render(request,'dashboard/login.html')



class LoginView(TemplateView):
    template_name='dashboard/login.html'
    def post(self,request):
        email= request.POST.get('email')
        password= request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        print('*******************',user)
        if user:
            login(request,user)
            # messages.success(request,'Login successful')
            return redirect("admin_dashboard")
        messages.error(request,"Invalid username or password")
        return render(request,self.template_name)







    
def signout(request):
    logout(request)
    return render(request,'dashboard/login.html')     
    

def dashboard_index(request):

        return render(request,'dashboard/dashboard-index.html')


def admin_dashboard(request):
        return render(request,'dashboard/admin_dashboard.html')




