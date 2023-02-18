"""djangoProj_147 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProfileApp import views
urlpatterns = [
    path('admin',admin.site.urls),
    path('', views.home),
    path('Home', views.home,name="Home"),
    path('MyHistory', views.MyHistory, name="MyHistory"),
    path('MyEducation', views.MyEducation, name="MyEducation"),
    path('MyInterests', views.MyInterests, name="MyInterests"),
    path('MyProducts', views.MyProducts, name="MyProducts"),
    path('MyRoleModel', views.MyRoleModel, name="MyRoleModel"),
    path('ShowMyData', views.showMyData, name="ShowMyData"),
    path('inputProduct', views.inputProduct, name="inputProduct"),
    path('listProduct', views.listProduct, name="listProduct"),

    path('showGoodsList',views.showGoodsList,name="showGoodsList"),
    path('<gid>/showGoodsOne',views.showGoodsOne,name="showGoodsOne"),
    path('showCustomerList',views.showCustomerList,name="showCustomerList"),
    path('<cid>/showCustomerOne',views.showCustomerOne,name="showCustomerOne"),
    path('newGoods',views.newGoods,name="newGoods"),
    path('<gid>/updateGoods',views.updateGoods,name="updateGood"),
    path('<gid>/deleteGoods',views.deleteGoods,name="deleteGood"),
    path('newCustomer',views.newCustomer,name="newCustomer"),
    path('<cid>/updateCustomer',views.updateCustomer,name="updateCustomer"),
    path('<cid>/deleteCustomer',views.deleteCustomer,name="deleteCustomer"),


]
