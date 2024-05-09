import random
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from bugapp.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings
from bugapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from bugapp.models import CustomUser, customer, bug_report, bug_status

def BASE(request):
    return render(request, 'base.html')

def INDEX(request):
    return render(request, 'index.html')

def LOGIN(request):
    return render(request, 'login.html')

def send_otp_email(email, otp):
    """
    Sends OTP to the specified email address.
    """
    message = f"Your OTP is {otp}."
    send_mail(
        "Email OTP Verification",
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

def doLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        
        if user != None:
            # Generate OTP and send it to the provided email
            otp = random.randint(100000, 999999)
            request.session["email_otp"] = otp
            request.session["user_email"] = email

            # Send OTP via email
            send_otp_email(email, otp)

            messages.info(request, f"An OTP has been sent to {email}. Please enter it to proceed.")
            return render(request, "verif_otp.html")
        # return redirect("/otp")

    return render(request, "login.html")

def otpLogin(request):
    if request.method == "POST":
        u_otp = request.POST.get("otp")
        otp = request.session.get("email_otp")
        email = request.session.get("user_email")
        user = CustomUser.objects.get(email=email)
        
        if int(u_otp) == otp:
            print("otp successfull")    
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_user')
            elif user_type == '2':
                return redirect('staff_bug_details')
            elif user_type == '3':
                return redirect('userbugreports')
            else:
                messages.error(request, "Invalid Login Details")
        else:
            print("otp failed")
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('login')

    return render(request, "verif_otp.html")


        
@login_required(login_url='/')
def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user" : user
    }
    
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def update_profile(request):
    if request.method == "POST":
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(profile_pic, first_name, last_name)
        
        try:
            user = CustomUser.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            # user.email = email
            # user.username = username
            
            if password != None and password != "":
                user.set_password(password)
                
            if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic

            user.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('update_profile')
    
    return render(request, 'update_profile.html')