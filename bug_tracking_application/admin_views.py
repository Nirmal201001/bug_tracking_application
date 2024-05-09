from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bugapp.models import CustomUser, customer, staff, bug_report, bug_status, projects


@login_required(login_url='login')
def admin_home(request):
    return render(request, 'administrator/admin_home.html')


@login_required(login_url='login')
def admin_add_user(request):

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

    return render(request, 'administrator/admin_add_user.html')


@login_required(login_url='login')
def admin_user(request):
    customers = customer.objects.all()
    
    context = {
        'customers': customers
    }

    return render(request, 'administrator/admin_user.html', context)


@login_required(login_url='login')
def edit_user(request, id):
    customer = customer.objects.filter(id=id)

    context = {
        'customer': customer
    }

    return render(request, 'administrator/edit_user.html', context)


@login_required(login_url='login')
def admin_staff(request):
    employee = staff.objects.all()

    context = {
        'employees': employee
    }
    return render(request, 'administrator/admin_staff.html', context)


@login_required(login_url='login')
def add_staff(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        position = request.POST.get('position')
        password = request.POST.get('password')

        # print(user_type, username, firstname, lastname, email, gender)
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('admin_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect('admin_staff')
        else:
            user = CustomUser(
                username=username,
                email=email,
                first_name=firstname,
                last_name=lastname,
                user_type=2
            )

            user.set_password(password)
            user.save()

            staff_var = staff(
                admin=user,
                gender=gender,
                position=position
            )

            staff_var.save()
            messages.success(request, "User created successfully")

    return render(request, 'administrator/add_staff.html')


@login_required(login_url='login')
def delete_staff(request):
    # get all the id's of all the staff whose checkboxes are checked with the name 'staff_to_delete' value 'id

    if request.method == 'POST':
        staff_to_delete = request.POST.getlist('staff_to_delete')

        print("deleted staff: ", staff_to_delete)

        for staff_id in staff_to_delete:
            staff.objects.filter(id=staff_id).delete()
            CustomUser.objects.filter(id=staff_id).delete()

        return render(request, 'administrator/admin_staff.html')

    return render(request, 'administrator/admin_staff.html')


@login_required(login_url='login')
def view_bug(request):
    bugs = bug_report.objects.all()

    for bug in bugs:
        try:
            bug.status = bug_status.objects.get(bug=bug)
        except bug_status.DoesNotExist:
            bug.status = None

    context = {
        'bugs': bugs
    }

    return render(request, 'administrator/admin_bug.html', context)

