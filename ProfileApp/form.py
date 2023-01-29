from django import forms

class ProductForm(forms.Form):
    pdNumber = forms.CharField(max_length = 13, label="รหัสสินค้า",required = True,
                                widget=forms.TextInput(attrs={'size':'15','class' : 'form form-control'}))

    pdName = forms.CharField(max_length=255, label="ชื่อสินค้า", required=True,
                                widget=forms.TextInput(attrs={'size': '55','class' : 'form form-control'}))

    pdPrice = forms.FloatField(max_value = 100000.00, label="ราคาต่อหน่วย", required=True,
                                widget=forms.NumberInput(attrs={'size': '10','class' : 'form form-control'}))

    pdProfit = forms.IntegerField( label="กำไรที่ต้องการ",required=True,max_value= 100,min_value=1,
                                widget=forms.NumberInput(attrs={'class' : 'form form-control'}))

    pdAmount = forms.IntegerField( max_value = 1000,label="จำนวน",required=True,
                                widget=forms.NumberInput(attrs={'size': '10','class' : 'form form-control'}))

    pdVat = forms.IntegerField(max_value=30, label="ภาษี",required=True,
                                widget=forms.NumberInput(attrs={'size': '10','class' : 'form form-control'}))