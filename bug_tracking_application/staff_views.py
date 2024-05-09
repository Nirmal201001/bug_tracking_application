from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bugapp.models import CustomUser, customer, staff, bug_report, bug_status

@login_required(login_url='login')
def staff_home(request):
    return render(request, 'staff/staff_bug_details.html')

@login_required(login_url='login')
def staff_bug_details(request):
    bugs = bug_report.objects.all()
    
    for bug in bugs:
        try:
            bug.status = bug_status.objects.get(bug=bug)
        except bug_status.DoesNotExist:
            bug.status = None
    
    context = {
        'bugs': bugs
    }
    
    return render(request, 'staff/staff_bug_details.html', context)

@login_required(login_url='login')
def update_bug_status(request):
    if request.method == 'POST':
        bug_id = request.POST.get('bug_id')
        updated_status = request.POST.get('bug_status')
        bug = bug_report.objects.get(id=bug_id)
        
        if bug_status.objects.filter(bug=bug).exists():
            bug_status.objects.filter(bug=bug).update(status=updated_status)
        else:
            bug_status.objects.create(bug=bug, status=updated_status)
            
        messages.success(request, "Bug status updated successfully")
        
    return render(request, 'staff/update_bug_status.html')

@login_required(login_url='login')
def assign_bug(request):
    
    # get all user with type staff and position developer
    developers = staff.objects.filter(position='developer')
    # developers = staff.objects.all()
    
    context = {
        'developers': developers
    }
    
    if request.method == 'POST':
        bug_id = request.POST.get('bug_id')
        staff_id = request.POST.get('developer')
        
        bug = bug_report.objects.get(id=bug_id)
        
        staffObj = staff.objects.get(id=staff_id)
        
        if bug_status.objects.filter(bug=bug).exists():
            bug_status.objects.filter(bug=bug).update(assigned_to=staffObj)
        else:
            bug_status.objects.create(bug=bug, assigned_to=staffObj)
        
        
        messages.success(request, "Bug assigned successfully")
        
    return render(request, 'staff/staff_assign_bug.html', context)