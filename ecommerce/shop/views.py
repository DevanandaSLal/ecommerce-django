from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)

def allproducts(request,p):
    c=Category.objects.get(id=p)    #reads a particular cat id
    p=Product.objects.filter(category=c)   #reads a part cat obj using id
    context={'cat':c,'product':p}       # reads all prdcs under a particular cat obj
    return render(request,'product.html',context)
def detail(request,p):
    p=Product.objects.get(id=p)

    return render(request,'detail.html',{'product':p})


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        c=request.POST['c']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==c):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return HttpResponse("password are not matching")
        return redirect('shop:categories')
    return render(request,'register.html')



def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        print(u,p)
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)

            return redirect('shop:categories')

        else:
            messages.error(request,"invalid credentials")

    return render(request, 'login.html')





def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('shop:categories')

def addcategory(request):
    if request.method=='POST':
        name= request.POST['n']
        desc=request.POST['d']
        image=request.FILES['i']

        k=Category.objects.create(name=name,desc=desc,image=image)
        k.save()
        return redirect('shop:categories')
    return render(request,'addcategory.html')


def addproduct(request):
    if request.method=='POST':
        name= request.POST['n']
        desc=request.POST['d']
        image=request.FILES['i']
        price=request.POST['p']
        stock=request.POST['s']
        category = request.POST['c']
        m=Category.objects.get(name=category)
        k=Product.objects.create(name=name,desc=desc,image=image,price=price,stock=stock,category=m)
        k.save()

        return redirect('shop:categories')
    return render(request, 'addproduct.html')

def addstock(request,p):
    product=Product.objects.get(id=p)

    if request.method=="POST":
        product.stock=request.POST['n']
        product.save()
        return redirect('shop:categories')

    context={'pro':product}
    return render(request,'addstock.html',context)




