from cgitb import text
from mmap import PAGESIZE
from pprint import pprint
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.models import Details
from myapp.models import cDetails

from django.contrib.auth.decorators import login_required
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#home1 page
def home1(request):
    return render(request, "home1.html")

# Generate a pdf File Venue List
@login_required
def pdf(request):
    # create Bytestrem buffer
    buf =io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some lines in text
    li =[
        "WATER BILLING SYSTEM",
        "waterbilling@gmail.com, 01567189",
        " ",
        "==============================================================",
        " ",
    ]
    for lie in li:
        textob.textLine(lie)

    # Designate The model
    client = Details.objects.all()

    # Create blank list
    lines = []

    for venue in client:
        name= lines.append(venue.fullname)
        lines.append(str(venue.email))
        lines.append(venue.supplier)
        lines.append(str(venue.phone_number))
        lines.append(str(venue.unit))
        lines.append(venue.location)    
        lines.append("=============================== ")
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='client.pdf')

@login_required
# pdf for supplier
def supplier_pdf(request):
    buff =io.BytesIO()
    # Create a canvas
    caa = canvas.Canvas(buff, pagesize=letter, bottomup=0)
    # Create text object
    textobj = caa.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    li =[
        "WATER BILLING SYSTEM",
        "waterbilling@gmail.com, 01567189",
        " ",
        "==============================================================",
        " ",
    ]
    for lie in li:
        textobj.textLine(lie)

    # Designate The model
    supplier = cDetails.objects.all()

    # Create blank list
    line = []

    for venue in supplier:
        line.append(venue.cname)
        line.append(str(venue.cemail))
        line.append(str(venue.cphone_number))
        line.append(venue.clocation)    
        line.append("=============================== ")
        line.append(" ")

    for lines in line:
        textobj.textLine(lines)

    caa.drawText(textobj)
    caa.showPage()
    caa.save()
    buff.seek(0)

    return FileResponse(buff, as_attachment=True, filename='supplier.pdf')


# Create your views here.
#Log In
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

# Logout
# def logout(request):
#     logout(request)
#     messages.success(request, "Successfully Logged Out")
#     return HttpResponseRedirect('index')
    # return redirect('home1')
    # return render(request, "index.html")

#signup
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname =request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        psw =request.POST['psw']
        psw_repeat =request.POST['psw_repeat']
        phone_number =request.POST['phone_number']

        myuser = User.objects.create_user(username, email, psw)
        myuser.first_name = fname
        myuser.lasr_name = lname 

        myuser.save()

        messages.success(request, "Your Account has been Created Successfully. ")

        return redirect('index')


    return render(request, "signup.html")

@login_required
def indexD(request):
    return render(request, "indexD.html")

# Clients Detail
@login_required
def client(request):

    data = Details.objects.all()

    context = {
        'table' : data
    }

    return render(request, 'client.html', context)
    
@login_required
def addClient(request):
    return render(request, "addClient.html")


@login_required
def details(request):
    data = Details.objects.all()

    context = {
        'table' : data
    }

    return render(request, 'client.html', context)

@login_required
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

@login_required
def edit_item(request, id):
    data = Details.objects.get(id = id)
    data_list = Details.objects.all()
    context = {
        "data" : data,
        "data_list" : data_list
    }

    return render(request, "addClient.html", context)

@login_required
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

@login_required
def delete_item(request, id):
    data = Details.objects.filter(id = id)
    data.delete()

    return redirect("client")


# company views
@login_required
def suppliers(request):

    cdata = cDetails.objects.all()

    context = {
        'ctable' : cdata
    }

    return render(request, 'suppliers.html', context)

@login_required
def addSuppliers(request):
    return render(request, "addSuppliers.html")

@login_required
def cdetail(request):

    cdata = cDetails.objects.all()

    context = {
        'ctable' : cdata
    }

    return render(request, 'suppliers.html', context)

@login_required
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

@login_required
def cedit_item(request, cid):
    cdata = cDetails.objects.get(id = cid)
    cdata_list = cDetails.objects.all()
    context = {
        "cdata" : cdata,
        "cdata_list" : cdata_list
    }

    return render(request, "addSuppliers.html", context)

@login_required
def cupdate_item(request, cid):
    cdata = cDetails.objects.get(id = cid)
    cdata.cname = request.POST.get('cname')
    cdata.cemail = request.POST.get('cemail')
    cdata.cphone_number = request.POST.get('cphone_number')
    cdata.clocation = request.POST.get('clocation')
    cdata.save()
    return redirect("suppliers")

@login_required
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

@login_required
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
@login_required
def bh(request):
    return render(request, "billing.html")

# profile
@login_required
def profile(request):
    return render(request, "profile.html")


# def signin(request):
#     return render(request, "signin.html")

# def signout(request):
#     pass
    # return render(request, "myapp/signout.html")
