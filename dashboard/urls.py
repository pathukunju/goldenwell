from django.urls import path,include
from . import views
from dashboard.views import UserRoleCreateView

urlpatterns = [
    path('',views.admin_login, name='gw-admin'),
    path('signout/',views.signout, name='logout'),
    # path('',views.LoginView.as_view(),name='gw-admin'),
    path('base/',views.dashboard, name='index'),
    path('user/',views.index, name='dash_board'),
    # path('role/',views.role,name='role'),
    path('general/',views.general,name='general'),
    path('local/',views.local,name='local'),
    path('server/',views.server,name='server'),
    path('stock/',views.stock,name='stock'),
    path('order_status/',views.order_status,name='order_status'),
    path('tax/',views.tax,name='tax'),
    path('currency/',views.currency,name='currency'),
    path('detail/',views.detail,name='detail'),
    path('detail<int:id>/',views.detail,name='detail'),
    path('social/',views.social,name='social'),
    path('role/',views.UserRoleCreateView.as_view(),name='role')
]

