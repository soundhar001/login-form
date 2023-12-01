from django.shortcuts import render
from django.http import HttpResponse
from .models import Login, SignUp

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']

        login_obj = Login()

        login_obj.User_name = name
        login_obj.Password = password
   
    return render(request, "login.html")

def signupPage(request):
    print("signup_data---------------")
    
    return render(request, "signup.html")

def homePage(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']

        signup = SignUp()

        signup.Full_name = full_name
        signup.Age = age
        signup.Email = email
        signup.Phone = phone
        signup.save()
        
        signup_data = SignUp.objects.all()
        if (signup_data != ""):
            return render(request, "home.html" , {'signup_data': signup_data})

    return render(request, "home.html")


# def success(request):
#     if request.method == 'POST':
#         Name = request.POST['name']
#         Age = request.POST['age']
#         Address = request.POST['address']
#         Mobile = request.POST['mobile']

#         datas = Datas()
#         datas.name = Name
#         datas.age = Age
#         datas.address = Address
#         datas.mobile = Mobile
#         datas.save()

#         myDatas = Datas.objects.all()
#         if (myDatas != ""):
#             return render(request, "success.html", {'myDatas' : myDatas})   
#         else:
#             return render(request, "success.html")