from django.db import models

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