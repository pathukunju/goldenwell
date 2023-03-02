from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from . forms import RoleForm,UserForm,StoreForm,LocalForm,OrderStatusForm,StockStatusForm,TaxForm,SocialForm,CoinsForm
from django.views.generic import View,CreateView,FormView,TemplateView
from django.contrib import messages
from . models import Store,Local,Tax,Coins,OrderStatus,Social,StockStatus,User,Role
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.




def admin_login(request):

        if request.method == 'POST':


                email = request.POST.get('email')
                password = request.POST.get('password')
                #     user_obj = User.objects.filter(email=email)

                user_obj = authenticate(request,email=email,password=password)
                print(user_obj,'===============')
                
                if user_obj.is_staff :
                        
                        login(request, user_obj)
                        return redirect('index')

                       
                elif user_obj.is_superuser:
                        
                        login(request, user_obj)
                        return redirect('index')

        else:
                return render(request,'dashboard/login.html')



# class LoginView(TemplateView):
#     template_name='dashboard/login.html'
#     def post(self,request):
#         email= request.POST.get('email')
#         password= request.POST.get('password')
#         user=authenticate(request,email=email,password=password)
#         print('*******************',user)
#         if user:
#             login(request,user)
#             # messages.success(request,'Login successful')
#             return redirect("admin_dashboard")
#         messages.error(request,"Invalid username or password")
#         return render(request,self.template_name)

    
def signout(request):
    logout(request)
    return render(request,'dashboard/login.html')     
    
def dashboard(request):
    return render(request,'dashboard/base.html')

def index(request):

        user = User.objects.all()
        if request.method == 'POST':

                form = UserForm(request.POST,request.FILES)
                
                print(form)
                
                if form.is_valid()  :
                        form.save()
                        
                        return redirect('dash_board')
       
        form= UserForm()
        return render(request,'dashboard/user.html',{'form':form,'user':user})

def role(request):
        return render(request,'dashboard/role.html')

def general(request):
        store = Store.objects.all()
        if request.method == 'POST':
                form = StoreForm(request.POST,request.FILES)
                print(form)
                if form.is_valid()  :
                        form.save()
                        return redirect('general')
       
        form= StoreForm()
        return render(request,'dashboard/settings_general.html',{'store':store,'form':form})

def local(request):
        items = Local.objects.all()
        if request.method == 'POST':
                form = LocalForm(request.POST,request.FILES)
                print(form)
                if form.is_valid()  :
                        form.save()
                        return redirect('local')
       
        form= LocalForm()

        return render(request,'dashboard/settings_local.html',{'items':items,'form':form})

def server(request):
        return render(request,'dashboard/settings_server.html')

def stock(request):
        stocks = StockStatus.objects.all()
        if request.method == 'POST':
                form = StockStatusForm(request.POST,request.FILES)
                print(form)
                if form.is_valid()  :
                        form.save()
                        return redirect('stock')
       
        form= StockStatusForm()
        return render(request,'dashboard/settings_stock_status.html',{'stocks':stocks,'form':form})

def order_status(request):
        orders = OrderStatus.objects.all()
        if request.method == 'POST':
                form = OrderStatusForm(request.POST,request.FILES)
                print(form)
                if form.is_valid()  :
                        form.save()
                        return redirect('order_status')
       
        form= OrderStatusForm()


        return render(request,'dashboard/settings_order.html',{'orders':orders,'form':form})

def tax(request):
        taxes = Tax.objects.all()

        if request.method == 'POST':
                form = TaxForm(request.POST,request.FILES)
                print(form)
                if form.is_valid()  :
                        form.save()
                        return redirect('tax')
       
        form= TaxForm()
        return render(request,'dashboard/settings_tax.html',{'taxes':taxes,'form':form})

def currency(request):
        current = Coins.objects.all()
        if request.method == 'POST':
                form = CoinsForm(request.POST,request.FILES)
                print(form)
                if form.is_valid()  :
                        form.save()
                        return redirect('currency')
        form= CoinsForm()               
        return render(request,'dashboard/settings_currency.html',{'current':current,'form':form})

def detail(request,id):
        detail = Table_user.objects.get(id=id)
        return render(request,'dashboard/users_detail.html',{'detail':detail})

def social(request):
        icons = Social.objects.all()
        if request.method == 'POST':
                form = SocialForm(request.POST,request.FILES)
                print(form)
                if form.is_valid()  :
                        form.save()
                        return redirect('social')
       
        form= SocialForm()

        return render(request,'dashboard/social.html',{'icons':icons,'form':form})

class UserRoleCreateView(UserPassesTestMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'dashboard/role.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        data = super(UserRoleCreateView, self).get_context_data(**kwargs)
        users = [{'data': roll, 'edit_form': self.form_class(instance=roll)} for roll in self.model.objects.all()]
        data.update({"roles": users})
        data['roles']=Role.objects.all()
        return data

    def get_success_url(self):
        return reverse_lazy('role')