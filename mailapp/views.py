from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.conf import settings
from mailapp.models import tbl_user,tbl_didnt
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def create(request):
    return render(request,'createaccount.html')
def adduser(request):
    a=User()
    a.username=request.POST.get('user_name')   
    password=request.POST.get('pass')
    a.set_password(password)
    a.email=request.POST.get('email')
    b=tbl_user()
    b.Name=request.POST.get('Name')
    b.User_name=request.POST.get('user_name')
    b.Phone=request.POST.get('Phone')
    b.Email=request.POST.get('email')
    b.Address=request.POST.get('Address')
    b.Department=request.POST.get('Department')
    a.save()
    b.save()
    return redirect("/")
def login1(request):
    uname = request.POST.get('user_name')
    pwd = request.POST.get('pass')
    data = authenticate(username=uname, password=pwd)
    request.session['username'] = uname
    if data is not None:
        if data.is_superuser:
            return redirect('/admin1/')
        else:
            try:
                a = tbl_user.objects.get(User_name=uname)
                department = a.Department.lower()
                if department == "sales":
                    return redirect('/sales/')
                elif department == "student":
                    return redirect('/user1/')
                elif department == "tutor":  # Python is case-sensitive. Make sure these match exactly.
                    return redirect('/tutor1/')
                elif department == "accountant":  # Same as above, watch your case sensitivity.
                    return redirect('/accountant1/')
                else:
                    # If department is not recognized, you might want to redirect to a default page or show an error.
                    return HttpResponse('Department not recognized')
            except tbl_user.DoesNotExist:
                # Handle case where the user doesn't exist in your custom user table.
                return HttpResponse('User not found in tbl_user')
    else:
        return HttpResponse('Invalid user')

    # Default return in case none of the above conditions are met.
    # Adjust the message or redirect as needed for your application.
    return HttpResponse('Unexpected error, please try again')
# def login1(request):
#     uname=request.POST.get('user_name')
#     pwd=request.POST.get('pass')
#     data=authenticate(username=uname,password=pwd)
#     request.session['username']=uname
#     if data is not None and data.is_superuser==1:
#         return redirect('/admin1/')
#     elif data is not None and data.is_superuser==0:
#         a=tbl_user.objects.get(uname=data)
#         if a.Department=="sales":
#             return redirect('/sales/')
#         elif a.Department=="student":
#             return redirect('/student/')
#         else:
#             pass
#     else:
#         return HttpResponse('invaliduser')
def admin1(request):
    return render(request,'admin.html')
def user1(request):
    b=request.session['username']
    c=tbl_user.objects.get(User_name=b)
    d=User.objects.get(username=b)
    return render(request,'user.html',{'x':b,'y':c,'n':d})
def viewuser(request):
    a=tbl_user.objects.all()
    return render(request,'viewuser.html',{'x':a})
def deleteuser(request,id):
    a=tbl_user.objects.get(id=id)
    a.delete()
    return redirect('/viewuser/')
def updateprofile(request,id):
    a=tbl_user.objects.get(id=id)
    return render(request,'updateprofile.html',{'x':a})
def profile(request,id):
    b=tbl_user.objects.get(id=id)
    b.Name=request.POST.get('Name')
    b.Phone=request.POST.get('Phone')
    b.Email=request.POST.get('email')
    b.Address=request.POST.get('Address')
    b.save()
    return redirect("/user1/")
def sendmail(request):
    return render(request,'sendmail.html')
def sendmail1(request):
    users = tbl_user.objects.all()
    email_addresses = [user.Email for user in users]
    if request.method == 'POST':
        EmailTitle = request.POST['EmailTitle'] 
        Message = request.POST['Message']   
        send_mail(
        EmailTitle,
        Message,
        'settings.EMAIL_HOST_USER',
        email_addresses,
        fail_silently=False
        )
        return HttpResponse('Mail send successfully')
def sales(request):
    b=request.session['username']
    c=tbl_user.objects.get(User_name=b)
    d=User.objects.get(username=b)
    return render(request,'sales.html',{'x':b,'y':c,'n':d})
def viewsales(request):
    sales_users = tbl_user.objects.filter(Department="sales")
    return render(request, 'viewuser.html', {'x': sales_users})
def sendsales(request):
    return render(request,'sendsales.html')
def sendsales1(request):
    sales_users = tbl_user.objects.filter(Department="sales")
    email_addresses = [user.Email for user in sales_users]  # List of email addresses for sales department users

    if request.method == 'POST':
        EmailTitle = request.POST.get('EmailTitle')  # Use get() method to avoid KeyError if not found
        Message = request.POST.get('Message')   
        
        # Make sure to import settings and use settings.EMAIL_HOST_USER for the from_email argument
        send_mail(
            EmailTitle,
            Message,
            settings.EMAIL_HOST_USER,  # Use the EMAIL_HOST_USER from your settings
            email_addresses,
            fail_silently=False,
        )
        return HttpResponse('Mail sent successfully to the sales department.')
def accountant1(request):
    b=request.session['username']
    c=tbl_user.objects.get(User_name=b)
    d=User.objects.get(username=b)
    return render(request,'accountant.html',{'x':b,'y':c,'n':d})
def tutor1(request):
    b=request.session['username']
    c=tbl_user.objects.get(User_name=b)
    d=User.objects.get(username=b)
    return render(request,'tutor.html',{'x':b,'y':c,'n':d})
def sendtutor(request):
    return render(request,'sendtutor.html')
def sendstudent(request):
    return render(request,'sendstudent.html')
def sendaccountant(request):
    return render(request,'sendaccountant.html')
def sendtutor1(request):
    sales_users = tbl_user.objects.filter(Department="Tutor")
    email_addresses = [user.Email for user in sales_users]  # List of email addresses for sales department users

    if request.method == 'POST':
        EmailTitle = request.POST.get('EmailTitle')  # Use get() method to avoid KeyError if not found
        Message = request.POST.get('Message')   
        
        # Make sure to import settings and use settings.EMAIL_HOST_USER for the from_email argument
        send_mail(
            EmailTitle,
            Message,
            settings.EMAIL_HOST_USER,  # Use the EMAIL_HOST_USER from your settings
            email_addresses,
            fail_silently=False,
        )
        return HttpResponse('Mail sent successfully to the Tutor department.')
def sendstudent1(request):
    sales_users = tbl_user.objects.filter(Department="student")
    email_addresses = [user.Email for user in sales_users]  # List of email addresses for sales department users

    if request.method == 'POST':
        EmailTitle = request.POST.get('EmailTitle')  # Use get() method to avoid KeyError if not found
        Message = request.POST.get('Message')   
        
        # Make sure to import settings and use settings.EMAIL_HOST_USER for the from_email argument
        send_mail(
            EmailTitle,
            Message,
            settings.EMAIL_HOST_USER,  # Use the EMAIL_HOST_USER from your settings
            email_addresses,
            fail_silently=False,
        )
        return HttpResponse('Mail sent successfully to the student department.')
def sendaccountant1(request):
    sales_users = tbl_user.objects.filter(Department="Accountant")
    email_addresses = [user.Email for user in sales_users]  # List of email addresses for sales department users

    if request.method == 'POST':
        EmailTitle = request.POST.get('EmailTitle')  # Use get() method to avoid KeyError if not found
        Message = request.POST.get('Message')   
        
        # Make sure to import settings and use settings.EMAIL_HOST_USER for the from_email argument
        send_mail(
            EmailTitle,
            Message,
            settings.EMAIL_HOST_USER,  # Use the EMAIL_HOST_USER from your settings
            email_addresses,
            fail_silently=False,
        )
        return HttpResponse('Mail sent successfully to the Accountant department.')
def didntconnect(request):
     return render(request,'didntconnect.html')
def adddidnt(request):
    a=tbl_didnt()
    a.Name=request.POST.get('Name')
    a.Email=request.POST.get('Emailid')
    a.save()
    return redirect('/')
def viewdidnt(request):
    a=tbl_didnt.objects.all()
    return render(request,'viewdidnt.html',{'x':a})
def deletedidnt(request,id):
    a=tbl_didnt.objects.get(id=id)
    a.delete()
    return redirect('/viewdidnt/')
def sendmaildidnt(request):
    return render(request,'senddidnt.html')
def senddidint1(request):
    users = tbl_didnt.objects.all()
    email_addresses = [user.Email for user in users]
    if request.method == 'POST':
        Name=request.POST['Name']
        EmailTitle = request.POST['EmailTitle'] 
        Message = request.POST['Message']   
        send_mail(
        EmailTitle,
        f"sender name:{Name} from Sales Department\n\n{Message}",
        
        'settings.EMAIL_HOST_USER',
        email_addresses,
        fail_silently=False
        )
        return HttpResponse('Mail send successfully')
def about(request):
    return render(request,'about.html')
def team(request):
    return render(request,'team.html')
def updatesales(request,id):
    a=tbl_user.objects.get(id=id)
    return render(request,'updatesale.html',{'x':a})
def updatetutor(request,id):
    a=tbl_user.objects.get(id=id)
    return render(request,'updatetutor.html',{'x':a})
def updatetutor1(request,id):
    b=tbl_user.objects.get(id=id)
    b.Name=request.POST.get('Name')
    b.Phone=request.POST.get('Phone')
    b.Email=request.POST.get('email')
    b.Address=request.POST.get('Address')
    b.save()
    return redirect("/tutor1/")
def updateaccountant(request,id):
    a=tbl_user.objects.get(id=id)
    return render(request,'updateaccountant.html',{'x':a})
def updateaccountant1(request,id):
    b=tbl_user.objects.get(id=id)
    b.Name=request.POST.get('Name')
    b.Phone=request.POST.get('Phone')
    b.Email=request.POST.get('email')
    b.Address=request.POST.get('Address')
    b.save()
    return redirect("/accountant1/")





    
    

