from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bugapp.models import CustomUser, customer, bug_report, bug_status
import joblib
        

@login_required(login_url='login')
def user_home(request):
    return render(request, 'user/user_bug_report.html')

@login_required(login_url='login')
def user_bug_reports(request):
    
    # load bug_priority_model.sav file
    bug_priority_model = joblib.load('bug_priority_model.sav')
    parameters = []
    if request.method == 'POST':
        title = request.POST.get('bugTitle')
        description = request.POST.get('bugDesc')
        urgencyLevel = request.POST.get('urgencyLevel')
        impactOnUser = request.POST.get('impact')
        department = request.POST.get('department')
        bug_image = request.FILES.get('myFile')
        user = CustomUser.objects.get(id=request.user.id)
        
        if urgencyLevel == 'low':
            urgency = 0
        elif urgencyLevel == 'medium':
            urgency = 1
        else:
            urgency = 2
            
        if impactOnUser == 'minor':
            impact = 0
        elif impactOnUser == 'moderate':
            impact = 1
        else:
            impact = 2
        
        parameters.append(impact)
        parameters.append(urgency)
        
        pridict_priority = bug_priority_model.predict([parameters])
        
        if bug_image is None:
            bug_image = 'uploads/default_bug_img.jpg'
        
        bugs = bug_report(
            title = title,
            description = description,
            urgency_level = urgencyLevel,
            impact_on_user = impactOnUser,
            department = department,
            created_by = user,
            bug_image = bug_image,
            priority = pridict_priority[0],
        )
        
        bugs.save()
    return render(request, 'user/user_bug_report.html')


@login_required(login_url='login')
def bug_update(request):
    # code for to show all the bug reports submitted by the logged in user
    user = CustomUser.objects.get(id=request.user.id)
    bug_reports = bug_report.objects.filter(created_by=user)
    context = {
        'bugs': bug_reports
    }
    
    
    return render(request, 'user/user_bug_update.html', context)


def register_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        
        # print(user_type, username, firstname, lastname, email, gender)
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('admin_user')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect('admin_user')
        else:
            user = CustomUser(
                            username=username, 
                            email=email, 
                            first_name=firstname, 
                            last_name=lastname, 
                            user_type= 3
                        )
            
            user.set_password(password)
            user.save()
                
            cust = customer(
                admin = user,
                gender = gender
            )
                
            cust.save()
            messages.success(request, "User created successfully")
        
    
    return render(request, 'user/user_registration.html')