from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def aboutpage(request):
    return render(request, 'about.html')


def createaccountpage(request):
    user = 'none'
    error = 'none'
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repeatpasssword = request.POST['repeatpassword']
        gender = request.POST['gender']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        birthdate = request.POST['dateofbirth']
        bloodgroup = request.POST['bloodgroup']

        try:
            if password == repeatpasssword:
                Patient.objects.create(name=name, email=email,
                                       gender=gender, phonenumber=phonenumber, address=address, birthdate=birthdate,
                                       bloodgroup=bloodgroup)

                user = User.objects.create_user(
                    first_name=name, email=email, password=password, username=email)
                pat_group = Group.objects.get(name='Patient')
                pat_group.user_set.add(user)
                user.save()
                error = 'no'

            else:
                error = 'yes'

        except Exception as e:
            #raise e
            error = 'yes'
    d = {'error': error}
    return render(request, 'createaccount.html', d)


def loginpage(request):

    error = ""
    page = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        print(u, p)
        user = authenticate(request, username=u, password=p)
        try:
            if user is not None:
                print('user is not none')
                login(request, user)
                error = "no"
                g = request.user.groups.all()[0].name
                if g == 'Doctor':
                    page = "doctor"
                    d = {'error': error, 'page': page}
                    return render(request, 'doctorhome.html', d)
                elif g == 'Receptionist':
                    page = "reception"
                    d = {'error': error, 'page': page}
                    return render(request, 'receptionhome.html', d)
                elif g == 'Patient':
                    print('am in patients')
                    page = "patient"
                    d = {'error': error, 'page': page}
                    print('i want to render the patient page')
                    print(d)
                    return render(request, 'patienthome.html', d)
            else:
                error = "yes"
        except Exception as e:
            error = "yes"
            print('it came out here')
            # print(e)
            #raise e
    return render(request, 'login.html')


def login_admin(request):
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('loginpage')
