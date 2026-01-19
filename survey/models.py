from django.db import models

class Personal_Details(models.Model):
    First_Name=models.CharField( max_length=50)
    Middle_Name=models.CharField( max_length=50)
    Last_Name=models.CharField( max_length=50)
    Age=models.IntegerField()
    Gender=models.CharField( max_length=50)
    Contact_Number=models.IntegerField()
    EMail_Address=models.EmailField( max_length=50)

    def __str__(self):
        return self.First_Name


class Favourite_Details(models.Model):
    Fav_Singer=models.CharField( max_length=50)
    Fav_Food=models.CharField( max_length=50)
    Fav_Teacher=models.CharField( max_length=50)
    Fav_Car=models.CharField( max_length=50)

    def __str__(self):
        return self.Fav_Singer


class Address_Details(models.Model):
    Building_Name=models.CharField( max_length=50)
    Room_Number=models.CharField( max_length=50)
    Sector=models.IntegerField()
    City=models.CharField( max_length=50)
    Land_Mark=models.CharField( max_length=50)
    Pincode=models.IntegerField()

    def __str__(self):
        return self.Building_Name 


class Skills_Details(models.Model):
    Tech_Skills=models.CharField( max_length=50)
    Non_Tech_Skills=models.CharField( max_length=50)
    Sports_Skills=models.CharField( max_length=50)
    def __str__(self):
        return self.Tech_Skills
    
