from django import forms
# from django.contrib.auth.models import User
from . models import Role,User,Store,Local,OrderStatus,StockStatus,Tax,Social,Coins



class RoleForm(forms.ModelForm):
   

    class Meta:
        model= Role
        fields = '__all__'


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields =['full_name','email','role']


        widgets={
            'full_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}),
            
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}),
            
            'role': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select', 'min': 8}),
        }


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['meta_title','meta_description','email','store_logo','store_name','address','phone']

        widgets = {
            'meta_title':forms.TextInput(attrs={'class':'form-control','placeholder': 'meta_title'}),
            'meta_description':forms.TextInput(attrs={'class':'form-control','placeholder': 'meta_description'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}),
            'store_logo':forms.FileInput(attrs={'class':'form-control','placeholder': 'store_logo'}),
            'store_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'store_name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder': 'address'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder': 'phone'}),
        }

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['country','currency','timezone']

        widgets = {
            'country':forms.Select(attrs={'class':'form-control','placeholder': 'country'}),
            'currency':forms.Select(attrs={'class':'form-control','placeholder': 'currency'}),
            'timezone':forms.Select(attrs={'class':'form-control','placeholder': 'timezone'}),
            # 'language':forms.textInput(attrs={'class':'form-control','placeholder': 'store_logo'}),
            
        }

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = ['status']

        widgets = {
            'status':forms.Select(attrs={'class':'form-control','placeholder':'status'})
        }

class StockStatusForm(forms.ModelForm):
    class Meta:
        model = StockStatus
        fields = ['status']

        widgets = {
            'status':forms.Select(attrs={'class':'form-control','placeholder':'status'})
        }


class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = '__all__'

        widgets = {
            'tax_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'title'}),
            'tax_rate':forms.NumberInput(attrs={'class':'form-control','placeholder': 'rate'}),
            'type':forms.Select(attrs={'class':'form-control','placeholder': 'type'}),
            'date_joined':forms.DateInput(attrs={'class':'form-control','placeholder': 'date'}),
            'date_modified':forms.DateInput(attrs={'class':'form-control','placeholder': 'date_added'}),
            
        }
class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder': 'name'}),
            'icon':forms.TextInput(attrs={'class':'form-control','placeholder': 'icon'}),
            'status':forms.Select(attrs={'class':'form-control','placeholder': 'status'}),
            'url':forms.TextInput(attrs={'class':'form-control','placeholder': 'url'}),
            
        }

class CoinsForm(forms.ModelForm):
    class Meta:
        model=Coins
        fields='__all__'   
        widgets = {
            'currency_title':forms.Select(attrs={'class':'form-control','placeholder': 'currency_title'}),
            'code':forms.TextInput(attrs={'class':'form-control','placeholder': 'code'}),
            'decimal_places':forms.NumberInput(attrs={'class':'form-control','placeholder': 'decimal_places'}),
            'symbol':forms.TextInput(attrs={'class':'form-control','placeholder': 'symbol'}),
            'status':forms.Select(attrs={'class':'form-control','placeholder': 'status'}),
        }
   