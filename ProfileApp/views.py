from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
import requests
# Create your views here.
from .form import *
from .models import *


def home(request):
    return render(request,'home.html')
def MyHistory(request):
    return render(request,'myHistory.html')
def MyEducation(request):
    return render(request,'education.html')
def MyInterests(request):
    return render(request,'interests.html')
def MyProducts(request):
    return render(request,'product.html')
def MyRoleModel(request):
    return render(request,'roleModel.html')
def showMyData(request):
    IdNumber = "65342310147-4"
    fullName = "พิชิตชัย ธรรมชัย"
    age = 21
    birthday = "14/02/2545"
    sex = 'ชาย'
    bloodType = "O"
    like = "การเขียนโค้ด"
    hate = "งานสังสรรค์"
    status = "นักเรียน"
    futurecareer = "โปรแกรมเมอร์"

    pd1 = ["Prime Vandal",1775.00,'images/Products/PD1.jpg']
    pd2 = ["Spectrum Phantom", 2675.00,'images/Products/PD2.jpg']
    pd3 = ["Glitchpop Bulldog", 2175.00,'images/Products/PD3.jpg']
    pd4 = ["Gltichpop Vandal", 2175.00,'images/Products/PD4.jpg']
    pd5 = ["Ruination Phantom", 2175.00,'images/Products/PD5.jpg']
    pd6 = ["Orange Ruination Vandal", 4550.00,'images/Products/PD6.jpg']
    pd7 = ["RGX Vandal", 2175.00,'images/Products/PD7.jpg']
    pd8 = ["Prime 2.0 Phantom", 1011.51,'images/Products/PD8.jpg']
    pd9 = ["ElderFlame Operator", 3150.00,'images/Products/PD9.jpg']
    pd10 = ["ElderFlame Vandal", 3150.00,'images/Products/PD10.jpg']
    myproduct = [pd1,pd2,pd3,pd4,pd5,pd6,pd7,pd8,pd9,pd10,]
    mydata = {'IdNumber': IdNumber, 'fullName': fullName, 'age': age, 'birthday': birthday, 'sex': sex,
              'bloodType': bloodType, 'like': like, 'hate': hate, 'status': status, 'futurecareer': futurecareer,
              'myproduct':myproduct}
    return  render(request,'showMyData.html',mydata)

lstOurProduct = []
def listProduct(request):
    context = {'products':lstOurProduct}
    return render(request,"listProduct.html",context)
def inputProduct(request) :
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid() :
            form = form.cleaned_data
            pdNumber = form.get('pdNumber')
            pdName = form.get('pdName')
            pdPrice = float(form.get('pdPrice'))
            pdProfit = form.get('pdProfit')
            pdAmount = form.get('pdAmount')
            pdVat = form.get('pdVat')
            product= Product(pdNumber,pdName,pdPrice,pdProfit,pdAmount,pdVat)
            lstOurProduct.append(product)
            return redirect('listProduct')

        else:
            form =ProductForm(form)
    else:
        form =ProductForm()
    context = {'form':form,"CHECK":request.method}
    return render(request,'inputProduct.html',context)
def showGoodsList(request):
    goods = Goods.objects.all().order_by("gid")
    context = {'goods':goods}
    return render(request, 'work12/showGoodsList.html', context)
def showGoodsOne(request,gid):
    goods = Goods.objects.get(gid=gid)
    context = {'goods':goods}
    return render(request, 'work12/showGoodOne.html', context)
def showCustomerList(request):

    customer = Customer.objects.all().order_by('cid')
    context = {'Customers':customer}
    return render(request, 'work12/showCustomerList.html', context)
def showCustomerOne(request,cid):
    customer = Customer.objects.get(cid=cid)
    context = {'customer':customer}
    return render(request, 'work12/showCustomerOne.html', context)
def newGoods(request):
    if request.method == "POST":
        form = GoodsForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('showGoodsList')
        else:
            form = GoodsForm(form)
    else:
        form = GoodsForm()
    context = {'form': form}
    return render(request,'work12/crud/newGoods.html',context)
def updateGoods(request,gid):
    goods = get_object_or_404(Goods,gid = gid)
    if request.method == "POST":
        form = GoodsForm(data=request.POST or None, instance=goods)
        if form.is_valid() :
            form.save()
            return redirect('showGoodsList')
    else:
        form = GoodsForm(instance=goods)
        form.updateForm()
        context = {'form': form,'gid':gid}
        return render(request,'work12/crud/updateGoods.html',context)
def deleteGoods(request,gid):
    goods = Goods.objects.get(gid=gid)
    if request.method == "POST":
        goods.delete()
        return redirect('showGoodsList')
    context = {'goods': goods}
    return render(request,'work12/crud/deleteGoods.html',context)
def newCustomer(request):
    if request.method == "POST":
        form = CustomerForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('showCustomerList')
        else:
            form = CustomerForm(form)
    else:
        form = CustomerForm()
    context = {'form': form}
    return render(request,'work12/crud/newCustomer.html',context)
def updateCustomer(request,cid):
    customer = get_object_or_404(Customer, cid=cid)
    if request.method == "POST":
        form = CustomerForm(data=request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('showCustomerList')
    else:
        form = CustomerForm(instance=customer)
        form.updateForm()
        context = {'form': form, 'cid': cid}
        return render(request, 'work12/crud/updateCustomer.html',context)
def deleteCustomer(request,cid):
    customer = Customer.objects.get(cid=cid)
    if request.method == "POST":
        customer.delete()
        return redirect('showCustomerList')
    context = {'customer': customer}
    return render(request,'work12/crud/deleteCustomer.html',context)

def senNotify(message):
    url = "https://notify-api.line.me/api/notify"
    LINE_ACCESS_TOKEN = 'mVzkUSo7gk9XtOgu03D3m33YPUINQpcNMlIHNcbaa5w'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + LINE_ACCESS_TOKEN}
    r = requests.post(url, headers=headers, data={'message': message})
    # print(r.text)
