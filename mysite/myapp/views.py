from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  
from django.contrib import messages
from django.http import HttpResponse
from myapp.models import Details
from myapp.models import cDetails


# Create your views here.
def index(request):
    # return HttpResponse("this is me!!!")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('indexD')
        else:
            messages.success(request, ("There was an error Logging In, Try Again...."))
            return redirect('index')
    else:
        return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def indexD(request):
    return render(request, "indexD.html")

# Clients Detail

def client(request):

    data = Details.objects.all()

    context = {
        'table' : data
    }

    return render(request, 'client.html', context)
    

def addClient(request):
    return render(request, "addClient.html")

def details(request):
    data = Details.objects.all()

    context = {
        'table' : data
    }

    return render(request, 'client.html', context)

def add(request):
    #Setting data from the HTML and accepting
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        supplier = request.POST.get('supplier')
        phone_number = request.POST.get('phone_number')
        unit = request.POST.get('unit')
        location = request.POST.get('location')
        # print(fullname, email, supplier, phone_number,unit, location)
        #Creating the object of record every time user clicks on 'save'
        data = Details(
            fullname= fullname,
            email =  email,
            supplier = supplier,
            phone_number = phone_number,
            unit = unit,
            location = location
        )
        data.save()
        return redirect("client")

    return render(request, 'client.html')

def edit_item(request, id):
    data = Details.objects.get(id = id)
    data_list = Details.objects.all()
    context = {
        "data" : data,
        "data_list" : data_list
    }

    return render(request, "addClient.html", context)

def update_item(request, id):
    data = Details.objects.get(id = id)
    data.fullname = request.POST.get('fullname')
    data.email = request.POST.get('email')
    data.supplier = request.POST.get('supplier')
    data.phone_number = request.POST.get('phone_number')
    data.unit = request.POST.get('unit')
    data.location = request.POST.get('location')
    data.save()
    return redirect("client")


def delete_item(request, id):
    data = Details.objects.filter(id = id)
    data.delete()

    return redirect("client")


# company views

def suppliers(request):

    cdata = cDetails.objects.all()

    context = {
        'ctable' : cdata
    }

    return render(request, 'suppliers.html', context)

def addSuppliers(request):
    return render(request, "addSuppliers.html")

def cdetail(request):

    cdata = cDetails.objects.all()

    context = {
        'ctable' : cdata
    }

    return render(request, 'suppliers.html', context)

def cadd(request):
    #Setting data from the HTML and accepting
    if request.method == 'POST':
        cname = request.POST.get('cname')
        cemail = request.POST.get('cemail')
        cphone_number = request.POST.get('cphone_number')
        clocation = request.POST.get('clocation')
        # print(fullname, email, supplier, phone_number,unit, location)
        #Creating the object of record every time user clicks on 'save'
        cdata =  cDetails(
            cname= cname,
            cemail =  cemail,
            cphone_number = cphone_number,
            clocation = clocation
        )
        cdata.save()
        return redirect("suppliers")

    return render(request, 'suppliers.html')

def cedit_item(request, cid):
    cdata = cDetails.objects.get(id = cid)
    cdata_list = cDetails.objects.all()
    context = {
        "cdata" : cdata,
        "cdata_list" : cdata_list
    }

    return render(request, "addSuppliers.html", context)

def cupdate_item(request, cid):
    cdata = cDetails.objects.get(id = cid)
    cdata.cname = request.POST.get('cname')
    cdata.cemail = request.POST.get('cemail')
    cdata.cphone_number = request.POST.get('cphone_number')
    cdata.clocation = request.POST.get('clocation')
    cdata.save()
    return redirect("suppliers")

def cdelete_item(request, cid):
    cdata = cDetails.objects.filter(id = cid)
    cdata.delete()

    return redirect("suppliers")

# ################################################

def home(request):
    return render (request, 'indexD.html')

########################################################

# def view_client(request):
#     return render (request, 'client.html')

# def view_supplier(request):
#     return render (request, 'suppliers.html')

# For Dashboard

# def suppliers(request):

#     cdata = cDetails.objects.all()

#     context = {
#         'ctable' : cdata
#     }

#     return render(request, 'indexD.html', context)


# def cdetail(request):

#     cdata = cDetails.objects.all()

#     context = {
#         'ctable' : cdata
#     }

#     return render(request, 'indexD.html', context)

def companyD(request):
    #Setting data from the HTML and accepting
    if request.method == 'POST':
        cname = request.POST.get('cname')
        
        # print(fullname, email, supplier, phone_number,unit, location)
        #Creating the object of record every time user clicks on 'save'
        cdata =  cDetails(
            cname= cname,
            
        )
        cdata.save()
        return redirect("indexD")

    return render(request, 'indexD.html')


# billing and history
def bh(request):
    return render(request, "billing.html")

# profile
def profile(request):
    return render(request, "profile.html")

# Logout
def logout(request):
    return render(request, "index.html")


# def signin(request):
#     return render(request, "signin.html")

# def signout(request):
#     pass
    # return render(request, "myapp/signout.html")
