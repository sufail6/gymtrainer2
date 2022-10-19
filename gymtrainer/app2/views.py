import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


# Create your views here.
from app2.forms import TrainerForm, UserForm, Product, AddBill
from app2.models import Login, Equipments, Bill, Attendance


def home(request):
    return render(request,'home.html')

###############ADMINPANEL###############
def adminhome(request):
    return render(request,'admintemp/adminhome.html')


def userhome(request):
    return render(request,'userhome.html')

def trainerhome(request):
    return render(request,'trainertemp/trainerhome.html')


def trainer_register(request):
    login_form = TrainerForm()
    if request.method == 'POST':
        login_form=TrainerForm(request.POST,request.FILES)
        if login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_trainer = True
            user.save()
            messages.info(request,'registration succesfully')
            return redirect('trainer_register')
    return render(request,'admintemp/trainer_register.html',{'login_form':login_form})


def trainer_view(request):
    data = Login.objects.filter(is_trainer=True)
    return render(request,'admintemp/trainer_view.html',{'data':data})


def trainer_update(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST or None,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('trainer_view')
    else:
        form = TrainerForm(instance=data)
    return render(request, 'admintemp/trainer_update.html', {'form': form})


def trainer_delete(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('trainer_view')
    else:
        return redirect('trainer_view')


def user_register(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_user = True
            user.save()
            messages.info(request, 'register successfully')
            return redirect('user_register')
    return render(request,'user_register.html', {'user_form':user_form})


def user_login(request):
    return render(request, 'user_login.html')


def user_view(request):
    data = Login.objects.filter(is_user=True)
    return render(request, 'admintemp/user_view.html', {'data': data})


def equipments_add(request):
    form = Product()
    if request.method == 'POST':
        form = Product(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipments_add')
    return render(request,'admintemp/equipments.html',{'form':form})


def equipments_view(request):
    data = Equipments.objects.all()
    return render(request,'admintemp/equipments_view.html',{'data':data})


def equipments_update(request, id):
    data = Equipments.objects.get(id=id)
    if request.method == 'POST':
        form = Product(request.POST or None,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('equipments_view')
    else:
        form = Product(instance=data)
    return render(request, 'admintemp/equipments_update.html', {'form': form})


def equipments_delete(request, id):
    data = Equipments.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('equipments_view')
    else:
        return redirect('equipments_view')


def equipments_user_view(request):
    data = Equipments.objects.all()
    return render(request,'equipments_user_view.html',{'data':data})


def bill(request):
    form = AddBill()
    if request.method == 'POST':
        form = AddBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_view')
    return render(request,'admintemp/bill.html',{'form':form})


def bill_view(request):
    bill = Bill.objects.all()
    return render(request,'admintemp/bill_view.html',{'bill': bill})


def view_bill_user(request):
    bill = Bill.objects.all()
    print(bill)
    return render(request,'view_bill_user.html',{'bill':bill})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminhome')
            elif user.is_trainer:
                return redirect('trainerhome')
        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')

def add_attendance(request):
    user = Login.objects.filter(is_user=True)
    return render(request,'add_attendance.html',{'user':user})



now = datetime.datetime.now()


def mark(request, id):
    user = Login.objects.get(id=id)
    att = Attendance.objects.filter(name=user, date=datetime.date.today())
    if att.exists():
        messages.info(request,'today attendance already marked')
        return redirect('add_attendance')
    else:
        if request.method =='POST':
            attndc = request.POST.get('attendance')
            Attendance(name=user, date=datetime.date.today(), attendance=attndc, time=now.time()).save()
            messages.info(request,'Attendance Added Successfully')
            return redirect('add_attendance')
        return render(request,'mark_attendance.html')


def view_attendance(request):
    value_list = Attendance.objects.values_list('date',flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request,'view_attendance.html',{'attendance':attendance})


def day_attendance(request,date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendance': attendance,
        'date' :date
    }
    return render(request,'day_attendance.html',context)









