from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Personal_Details
from .models import Favourite_Details
from .models import Address_Details
from .models import Skills_Details

def p_d(request):
    if request.method=="POST":
        first_name=request.POST.get("First_Name")
        middle_name=request.POST.get("Middle_Name")
        last_name=request.POST.get("Last_Name")
        age=request.POST.get("Age")
        gender=request.POST.get("Gender")
        contact_number=request.POST.get("Contact_Number")
        email_address=request.POST.get("Email_Address")
        Personal_Details.objects.create(First_Name=first_name,Contact_Number=contact_number,Middle_Name=middle_name,Last_Name=last_name,Age=age,Gender=gender,EMail_Address=email_address)
        return redirect("f2")
    return render(request,"form1.html")


def f_d(request):
    if request.method=="POST":
        fav_singer=request.POST.get("Fav_Singer")
        fav_food=request.POST.get("Fav_Food")
        fav_teacher=request.POST.get("Fav_Teacher")
        fav_car=request.POST.get("Fav_Car")
        Favourite_Details.objects.create(Fav_Singer=fav_singer,Fav_Food=fav_food,Fav_Teacher=fav_teacher,Fav_Car=fav_car)
        return redirect("f3")
    return render(request,"form2.html")

def a_d(request):
    if request.method=="POST":
        building_name=request.POST.get("Building_Name")
        room_number=request.POST.get("Room_Number")
        sector=request.POST.get("Sector")
        city=request.POST.get("City")
        land_mark=request.POST.get("Land_Mark")
        pincode=request.POST.get("Pincode")
        Address_Details.objects.create(Building_Name=building_name,Room_Number=room_number,Sector=sector,City=city,Land_Mark=land_mark,Pincode=pincode)
        return redirect("f4")
    return render(request,"form3.html")

def s_d(request):
    if request.method=="POST":
        tech_skills=request.POST.get("Tech_Skills")
        non_tech_skills=request.POST.get("Non_Tech_Skills")
        sports_skills=request.POST.get("Sports_Skills")
        Skills_Details.objects.create(Tech_Skills=tech_skills,Non_Tech_Skills=non_tech_skills,Sports_Skills=sports_skills)
        return redirect("TY")
    return render(request,"form4.html")

def t_y(request):
    if request.method=="POST":
        return redirect("f1")
    return render(request,"thankyou.html")

def fetch_all(request):
    f1=Personal_Details.objects.all()
    f2=Favourite_Details.objects.all()
    f3=Address_Details.objects.all()
    f4=Skills_Details.objects.all()
    return render(request,"fetch.html",{"Personal_Details":f1,"Favourite_Details":f2,"Address_Details":f3,"Skills_Details":f4})

