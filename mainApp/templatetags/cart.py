from itertools import product
from django import template
from mainApp.models import Product,CheckoutProducts,Checkout
register = template.Library()

@register.filter(name="cartQty")
def cartQty(request,num):
    cart = request.session.get("cart",None)
    if(cart):
        return cart[str(num)]
    else:
        return None

@register.filter(name="cartTotal")
def cartTotal(request,num):
    cart = request.session.get("cart",None)
    p = Product.objects.get(id=num)
    if(cart):
        return cart[str(num)]*p.finalPrice
    else:
        return None

@register.filter(name="showCheckButton")
def showCheckButton(request,final):
    if(final==0):
        return False
    else:
        return True


@register.filter(name="checkoutProduct")
def checkoutProduct(request,num):
    products = CheckoutProducts.objects.filter(checkout=Checkout.objects.get(id=num))
    return products

@register.filter(name="checkoutProductImage")
def checkoutProductImage(request,num):
    p = Product.objects.get(id=num)
    return p.pic1.url

@register.filter(name="checkoutProductName")
def checkoutProductName(request,num):
    p = Product.objects.get(id=num)
    return p.name

@register.filter(name="checkoutProductPrice")
def checkoutProductPrice(request,num):
    p = Product.objects.get(id=num)
    return p.finalPrice

@register.filter(name="checkoutProductColor")
def checkoutProductColor(request,num):
    p = Product.objects.get(id=num)
    return p.color

@register.filter(name="checkoutProductSize")
def checkoutProductSize(request,num):
    p = Product.objects.get(id=num)
    return p.size

@register.filter(name="checkoutOrderStatus")
def checkoutOrderStatus(request,num):
    if(num==1):
        return "Not Packed"
    elif(num==2):
        return "Packed"
    elif(num==3):
        return "Out For Delivery"
    else:
        return "Delivered"

@register.filter(name="checkoutPaymentStatus")
def checkoutPaymentStatus(request,num):
    if(num==1):
        return "Pending"
    else:
        return "Done"

@register.filter(name="checkoutPaymentStatusCon")
def checkoutPaymentStatusCon(mode,num):
    if(num==1 and mode=="Net Banking"):
        return True
    else:
        return False