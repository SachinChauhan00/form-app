from django.db import models

# Create your models here.
# Create your models here.
class City(models.Model):
    city_name = models.CharField(null=False, max_length=30)

    def __str__(self):
        return self.city_name
    
class Student(models.Model):
    #student detail
    photo = models.ImageField(upload_to='profile_pics',null=False)
    fname = models.CharField(max_length=50,null=False)
    mname = models.CharField(max_length=50,null=False)
    lname = models.CharField(max_length=50,null=False)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=False)
    tob = models.TimeField(auto_now=False, auto_now_add=False,null=False)
    age = models.IntegerField(null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=False)
    disable = models.BooleanField(null=False)
    gender = models.CharField(max_length=50,null=False)
    #family details
    father_name = models.CharField(max_length=100,null=False)
    mother_name = models.CharField(max_length=100,null=False)
    father_occupation = models.CharField(max_length=100,null=False)
    mother_occupation = models.CharField(max_length=100,null=False)
    yearly_income = models.IntegerField(null=False)
    #recent education details
    collageorschool = models.CharField(max_length=50,null=False)
    percentage = models.IntegerField(null=False)
    course_name = models.CharField( max_length=50,null=False)
    year_of_passing = models.IntegerField(null=False)
    
    