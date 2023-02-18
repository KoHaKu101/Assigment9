from django.db import models
import datetime
# Create your models here.
class Product :

    def __init__(self,pdNumber,pdName,pdPrice,pdProfit,pdAmount,pdVat):
        self.pdNumber = pdNumber
        self.pdName = pdName
        self.pdPrice = pdPrice
        self.pdProfit = pdProfit
        self.pdAmount = pdAmount
        self.pdVat = pdVat
        self.setProfit()
        self.setTotal()
        self.setTaxPrice()
        self.setSalePrice()
    def setProfit(self):
        self.pdSaleProfit = self.pdPrice + (self.pdPrice * (self.pdProfit / 100))
    def setTotal(self):
        self.saleTotal = self.pdSaleProfit * self.pdAmount
    def setTaxPrice(self):
        self.taxPrice = self.pdSaleProfit * (self.pdVat/100)
    def setSalePrice(self):
        self.salePrice = self.pdSaleProfit + self.taxPrice
    def __str__(self):
        return "pdNumber:{},pdName:{},pdPrice:{},pdProfit:{},pdAmount:{},pdVat:{}" \
               "pdSaleProfit:{},saleTotal:{},taxPrice:{},salePrice:{}"\
            .format(self.pdNumber,self.pdName,self.pdPrice,self.pdProfit,
                    self.pdAmount,self.taxPrice,self.pdVat,self.pdSaleProfit,self.saleTotal,self.taxPrice,self.salePrice
        )

# - GoodsCategory เพื่อเก็บข้อมูลประเภทสินค้า (id, gc_name, desc)
# - Goods เพื่อเก็บข้อมูลสินค้า (goodscategory, gid, name, brand, model, price,net, property)
# - Customer เพื่อเก็บข้อมูลลูกค้า (cid, name, surname, address, telephone, gender, carreer, password)
# - Order เพื่อเก็บข้อมูลการสั่งซ้ือ(oid, date, customer, status)
# - OrderDetail เพื่อเก็บรายละเอียดการสั่งซ้ือ (id,order, goods, price, quantity)
class GoodsCategory(models.Model):
    id = models.CharField(max_length=13,primary_key=True)
    gc_name = models.CharField(max_length=100,null=False)
    desc = models.CharField(max_length=100,default="",null=True)
    def __str__(self):
        return self.id+ ' : '+self.gc_name
class Goods(models.Model):
    goodscategory = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE,default=None)
    gid = models.CharField(max_length=13,primary_key=True)
    name = models.CharField(max_length=100,null=False)
    brand = models.CharField(max_length=100,)
    model = models.CharField(max_length=100,)
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    property = models.TextField(null=True,default="")

class Customer(models.Model):
    cid = models.CharField(max_length=13,primary_key=True)
    name = models.CharField(max_length=100,null=False)
    surname = models.CharField(max_length=100,null=False)
    address = models.TextField(default="")
    telephone = models.CharField(max_length=10,default="")
    gender = models.CharField(max_length=10,default="")
    carreer = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=32, null=False)

class Order(models.Model):
    oid = models.CharField(max_length=13,primary_key=True)
    date = models.DateField(default=datetime.date.today())
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default=None)
    status = models.CharField(max_length=100,default="Start",null=False)
class OrderDetail(models.Model):
    id = models.CharField(max_length=13,primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,default=None)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,default=None)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
