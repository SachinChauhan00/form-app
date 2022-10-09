from django import forms
from .models import *
# class StudentForm(forms.Form):
#     photo = forms.FileField(label='Photo',error_messages={'required':'Please Select Your Photo !'})
#     fname = forms.CharField(label='First Name', max_length=100,error_messages={'required':'Please Enter Your First Name !'})
#     mname = forms.CharField(label='Middle Name',max_length=100,error_messages={'required':'Please Enter Your Middle Name !'})
#     lname = forms.CharField(label='Last Name ',max_length=100,error_messages={'required':'Please Enter Your Last Name !'})
#     dob = forms.CharField(label='Date Of Birth',widget=forms.DateInput,error_messages={'required':'Please Enter Your Date Of Birth !'})
#     tob = forms.CharField(label='Time Of Birth',widget=forms.TimeInput,error_messages={'required':'Please Enter Your Time OF Birth !'})
#     age = forms.IntegerField(label='Age',error_messages={'required':'Please Enter Your Age !'})
#     city = forms.ModelChoiceField(label='City', queryset=City.objects, empty_label=None,widget=forms.Select,error_messages={'required':'Please Enter Your City !'})    
#     disable = forms.MultipleChoiceField(label='Physicaly Disabled ?', choices=[('Yes','Yes')],widget=forms.CheckboxSelectMultiple,error_messages={'required':'Please Select If You Are Physically Disable Or Not !'})
#     gender = forms.CharField(label='Gender',widget=forms.RadioSelect(choices=[('Male','Male'),('Female','Female')]),error_messages={'required':'Please Select Your Gender !'}) 
#     father_name = forms.CharField(label="Father's Name",max_length=100,error_messages={'required':"Please Enter Your Father's Name !"})
#     mother_name = forms.CharField(label="Mother's Name",max_length=100,error_messages={'required':"Please Enter Your Mother's Name !"})
#     father_occupation = forms.CharField(label="Father's Occupation",max_length=100,error_messages={'required':"Please Enter Your Father's Occupation !"})
#     mother_occupation = forms.CharField(label="Mother's Occupation",max_length=100,error_messages={'required':"Please Enter Your Mother's Occupation !"})
#     yearly_income = forms.IntegerField(label="Yearly Household Income",error_messages={'required':'Please Enter Your Yearly Income !'})
#     collageorschool = forms.CharField(label='Collage/School Name',max_length=100,error_messages={'required':'Please Enter Your School Or Collage Name !'})
#     percentage = forms.IntegerField(label='Percentage',error_messages={'required':'Please Enter Your Percentage !'})
#     course_name = forms.CharField(label='Course Name',max_length=100,error_messages={'required':'Please Enter Course Name !'})
#     year_of_passing = forms.CharField(label="Year Of Passing",error_messages={'required':'Please Enter Year Of Passing !'})
    

class StudentForm(forms.ModelForm):
    photo = forms.FileField(label='Photo',error_messages={'required':'Please Select Your Photo !'})
    fname = forms.CharField(label='First Name', max_length=100,error_messages={'required':'Please Enter Your First Name !'})
    mname = forms.CharField(label='Middle Name',max_length=100,error_messages={'required':'Please Enter Your Middle Name !'})
    lname = forms.CharField(label='Last Name ',max_length=100,error_messages={'required':'Please Enter Your Last Name !'})
    dob = forms.CharField(label='Date Of Birth',widget=forms.DateInput,error_messages={'required':'Please Enter Your Date Of Birth !'})
    tob = forms.CharField(label='Time Of Birth',widget=forms.TimeInput,error_messages={'required':'Please Enter Your Time OF Birth !'})
    age = forms.IntegerField(label='Age',error_messages={'required':'Please Enter Your Age !'})
    city = forms.ModelChoiceField(label='City', queryset=City.objects, empty_label=None,widget=forms.Select,error_messages={'required':'Please Enter Your City !'})    
    disable = forms.BooleanField(label='Physicaly Disabled ?',required=False)
    gender = forms.CharField(label='Gender',widget=forms.RadioSelect(choices=[('Male','Male'),('Female','Female')]),error_messages={'required':'Please Select Your Gender !'}) 
    father_name = forms.CharField(label="Father's Name",max_length=100,error_messages={'required':"Please Enter Your Father's Name !"})
    mother_name = forms.CharField(label="Mother's Name",max_length=100,error_messages={'required':"Please Enter Your Mother's Name !"})
    father_occupation = forms.CharField(label="Father's Occupation",max_length=100,error_messages={'required':"Please Enter Your Father's Occupation !"})
    mother_occupation = forms.CharField(label="Mother's Occupation",max_length=100,error_messages={'required':"Please Enter Your Mother's Occupation !"})
    yearly_income = forms.IntegerField(label="Yearly Household Income",error_messages={'required':'Please Enter Your Yearly Income !'})
    collageorschool = forms.CharField(label='Collage/School Name',max_length=100,error_messages={'required':'Please Enter Your School Or Collage Name !'})
    percentage = forms.IntegerField(label='Percentage',error_messages={'required':'Please Enter Your Percentage !'})
    course_name = forms.CharField(label='Course Name',max_length=100,error_messages={'required':'Please Enter Course Name !'})
    year_of_passing = forms.CharField(label="Year Of Passing",error_messages={'required':'Please Enter Year Of Passing !'})
    class Meta:
        model = Student
        fields = ['photo','fname','mname','lname','dob','tob','age','city','disable','gender','father_name','mother_name','father_occupation','mother_occupation','yearly_income','collageorschool','percentage','course_name','year_of_passing']
        # labels = {'photo':'Photo','fname':'First Name','mname':'Middle Name','lname':'Last Name','dob':'Date Of Birth','tob':'Time Of Birth','age':'Age','city':'City','disable':'Physically Disable','gender':'Gender','father_name':'Father Name','mother_name':'Mother Name','yearly_income':'Yearly Household Income','collageorschool':'Collage/School Name','percentage':'Percentage','course_name':'Course Name','year_of_passing':'Year Of Passing'}
        