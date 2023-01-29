from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from ProfileApp.form import ProductForm
from ProfileApp.models import Product


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
def listProduct(requset):
    context = {'products':lstOurProduct}
    return render(requset,"listProduct.html",context)
def inputProduct(requset) :
    if requset.method == "POST":
        form = ProductForm(requset.POST)
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
    context = {'form':form,"CHECK":requset.method}
    return render(requset,'inputProduct.html',context)