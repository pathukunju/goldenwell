from django.db import models

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models 
from django_countries.fields import CountryField
from babel.numbers import list_currencies
from languages.fields import LanguageField




# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Role(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateField(auto_now_add=True)
    order = models.BooleanField(_('order'),default=False)
    catolog = models.BooleanField(_('catolog'),default=False)
    pages = models.BooleanField(_('pages'),default=False)
    subscribers_list = models.BooleanField(_('subscribers_list'),default=False)
    report = models.BooleanField(_('report'),default=False)

    def __str__ (self):
        return self.name


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=30)
    # first_name=models.CharField(max_length=120)
    # last_name=models.CharField(max_length=123)
    # is_staff = models.BooleanField(default=True)
    role = models.ForeignKey(to=Role, on_delete=models.CASCADE,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def _str_(self):
        """ Return string representation of our user """
        return self.email






class Store(models.Model):
    meta_title = models.CharField(max_length=30)
    meta_description = models.TextField()
    store_logo = models.ImageField(upload_to='media',null=True,blank=True)
    store_name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)


    def __str__(self):
        return self.store_name


class Local(models.Model):
    LOCAL_CHOICES = (
        ('ACDT', 'ACST'),
        ('ACT', 'ACWST'),
    )

    timezone = models.CharField(max_length=50, choices=LOCAL_CHOICES)
    # language = LanguageField(max_length=30, blank= True)

    country = CountryField(blank=True)
    CURRENCY_CHOICES = [(currency, currency) for currency in list_currencies()] 
    currency = models.CharField(
        max_length=3, null=True, blank=True, choices=CURRENCY_CHOICES
    )
    currency_with_default = models.CharField(
        max_length=3, default='USD', choices=CURRENCY_CHOICES
    )
  
    def __str__(self):
        return self.timezone




class Tax(models.Model):
    TAX_CHOICES = (
        ('VAT', 'VAT'),
        ('GST', 'GST'),
    )

    tax_name = models.CharField(max_length=50)
    tax_rate = models.DecimalField(decimal_places=2, max_digits=10)
    type = models.CharField(max_length=50, choices=TAX_CHOICES)
    date_joined =models.DateField()
    date_modified = models.DateField()

    def __str__(self):
        return self.tax_name

class Coins(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
    )

    CURRENCY_CHOICES = [(currency, currency) for currency in list_currencies()] 
    currency_title = models.CharField(
        max_length=3, null=True, blank=True, choices=CURRENCY_CHOICES
    )
    code = models.CharField(max_length=30)
    decimal_places= models.DecimalField(decimal_places=2, max_digits=10)
    symbol = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    

class OrderStatus(models.Model):
    
    ORDER_CHOICES = (
        ('PENDING', 'PENDING'),
        ('SUCCESS', 'SUCCESS'),
    )

    status =  models.CharField(
    max_length=10,
    choices=ORDER_CHOICES,
    default= 'PENDING')

class StockStatus(models.Model):
    STOCK_CHOICES = (
        ('PENDING', 'PENDING'),
        ('SUCCESS', 'SUCCESS'),
    )
    status =  models.CharField(
    max_length=10,
    choices=STOCK_CHOICES,
    )

class Social(models.Model):
    SOCIAL_CHOICES = (
        ('ACTIVE', 'ACTIVE'),
        ('DEACTIVE', 'DEACTIVE'),
    )


    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=SOCIAL_CHOICES)

