from django.urls import path,include
from . import views
from dashboard.views import LoginView

urlpatterns = [
    # path('gw-admin/',views.admin_login, name='gw-admin'),
    path('dashboard-index/',views.dashboard_index, name='index_dashboard'),
    path('admin_dashboard/',views.admin_dashboard, name='admin_dashboard'),
    path('signout/',views.signout, name='logout'),
    path('gw-admin/',views.LoginView.as_view(),name='gw-admin')
   
    
]
