from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact ,MemberShipPlan,Enrollment,Trainer,Gallery,Attendance
# Create your views here.

def home(request):
    return render(request,'index.html')

def attendance(request):
    if not request.user.is_authenticated :
        messages.warning(request,'Please Login and try again')
        redirect('login')
    trainers = Trainer.objects.all()
    # queryset = Attendance.objects.all()
    return render(request,'attendance.html',{
        'trainers': trainers,
    })


def gallery(request):
    gallery = Gallery.objects.all()

    return render(request,'gallery.html',{
        'gallery' : gallery,
    })


def profile(request):
    if not request.user.is_authenticated :
        messages.warning(request,'Please Login and try again')
        redirect('login')
    
    print(request.user)

    user_phone = Enrollment.objects.filter(phoneNumber = request.user)
    print(user_phone)
    return render(request,'profile.html',{
        'profile':user_phone
    })


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2 :
            messages.info(request,'password is not matching')
            return redirect('signup')
        
        if len(username)!= 10 :
            messages.info(request,'Phone number must be 10 Digits')
            return redirect('signup')
        
        try:
            if User.objcts.get(username = username):
                messages.warning(request,'Phone number is Taking')
                return redirect('signup')
        except Exception as identifier:
            pass
        
        try:
            if User.objcts.get(email = email):
                messages.warning(request,'E-mail is Taking')
                return redirect('signup')
        except Exception as identifier:
            pass

        user = User.objects.create_user(username,email,pass1)
        # user.first_name = first_name
        # user.last_name = last_name
        user.save()
        messages.success(request,'user is created please Log in ')
        return redirect('login')

    return render(request,'signup.html')


def handleLogin(request):

    if request.method == 'POST':
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')
        user = authenticate(request,username = username,password = pass1)

        if user is not None:
            login(request,user)
            messages.success(request,'login successfully')
            print(request.user.is_authenticated)
            return redirect('/')
        
        
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

    return render(request,'handleLogin.html')

def handleLgout(request):
    logout(request)
    messages.success(request,'Logout success')
    return redirect('login')


def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('num')
        desc = request.POST.get('desc')
        queryset = Contact.objects.create(name = fullname, email = email,description = desc, phoneNumber = phoneNumber)
        queryset.save()

        messages.info(request,'Thanks for contacting us , we will reach you as soon as possible')
        return redirect('/')

    return render(request,'contact.html')


def enrollment(request):
    if not request.user.is_authenticated :
        messages.warning(request,'Please Login and try again')
        redirect('login')


    memberShip = MemberShipPlan.objects.all()
    selectTrainer = Trainer.objects.all()
    context = {'memberShip' : memberShip , 'selectTrainer':selectTrainer}

    if request.method == 'POST':
        fullName = request.POST.get('FullName')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phoneNumber =request.POST.get('PhoneNumber')
        doB =request.POST.get('DOB')
        member =request.POST.get('member')
        trainer =request.POST.get('trainer')
        reference = request.POST.get('reference')
        address = request.POST.get('address')

        queryset = Enrollment.objects.create(fullName =fullName,
                                             email = email,
                                             gender = gender,
                                             phoneNumber = phoneNumber,
                                             DOB =doB, 
                                             selectMemberShipPlans = member,
                                             selectTrainer = trainer,
                                             refrence = reference,
                                             address = address,
                                             )
        queryset.save()


    return render(request,'enroll.html',context)