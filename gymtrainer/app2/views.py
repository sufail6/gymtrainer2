from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
from app2.forms import TrainerForm, UserForm, Product, AddBill
from app2.models import Login, Equipments, Bill


def home(request):
    return render(request,'home.html')


def adminhome(request):
    return render(request,'adminhome.html')


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
    return render(request,'trainer_register.html',{'login_form':login_form})


def trainer_view(request):
    data = Login.objects.filter(is_trainer=True)
    return render(request,'trainer_view.html',{'data':data})


def trainer_update(request, id):
    data = Login.objects.get(id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST or None,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('trainer_view')
    else:
        form = TrainerForm(instance=data)
    return render(request, 'trainer_update.html', {'form': form})


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
    return render(request, 'user_view.html', {'data': data})


def equipments_add(request):
    form = Product()
    if request.method == 'POST':
        form = Product(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipments_add')
    return render(request,'equipments.html',{'form':form})


def equipments_view(request):
    data = Equipments.objects.all()
    return render(request,'equipments_view.html',{'data':data})


def equipments_update(request, id):
    data = Equipments.objects.get(id=id)
    if request.method == 'POST':
        form = Product(request.POST or None,request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('equipments_view')
    else:
        form = Product(instance=data)
    return render(request, 'equipments_update.html', {'form': form})


def equipments_delete(request, id):
    data = Equipments.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('equipments_view')
    else:
        return redirect('equipments_view')


def bill(request):
    form = AddBill()
    if request.method == 'POST':
        form = AddBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bill')
    return render(request,'bill.html',{'form':form})


def bill_view(request):
    bill = Bill.objects.all()
    return render(request,'bill_view.html',{'bill': bill})


def equipments_user_view(request):
    data = Equipments.objects.all()
    return render(request,'equipments_user_view.html',{'data':data})

