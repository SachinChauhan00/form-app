from django.contrib import messages
from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    if request.method == "POST":
        if 'submit' in request.POST:
            filled_student = StudentForm(request.POST,request.FILES)
            
            # if filled_student.fname in request.POST:
            #     if filled_student.is_valid():
            #         obj  = Student()
            if filled_student.is_valid():
                filled_student.save()
                messages.success(request,"Student Added Successfully ✔")
            else:
                
                if len(filled_student.errors) == 3 or len(filled_student.errors) < 3 :
                    for field, errors in filled_student.errors.items():
                        for error in errors:
                            messages.error(request,filled_student.fields[field].label + " : " + error)
                else:
                    messages.error(request,"You Have Left To Much Field Blank May Be In This Tab Or In Other Two Tabs Fill Them First !")
        elif 'delete' in request.POST:
            delid = request.POST.get('delete')
            deldata = Student.objects.get(pk=delid)
            try:
                delquery = Student.objects.filter(pk=delid).delete()
                messages.success(request,deldata.fname+" Deleted Successfully ✔")
            except:
                messages.error(request,"Something Went Wrong When Deleting "+deldata.fname)
    # student_info = Student.objects.get(pk=1)
    stud_list = Student.objects.all()
    student = StudentForm()
    
    return render(request,"index.html",{'stud':student,'stud_list':stud_list})

def edit_student(request,pk):
    stud_obj = get_object_or_404(Student,pk=pk)
    if request.method == "POST":
        filled_student = StudentForm(request.POST,request.FILES,instance=stud_obj)
        if filled_student.is_valid():
            filled_student.save()
            messages.success(request,"Student Data Updated Successfully ✔")
        else: 
            if len(filled_student.errors) == 3 or len(filled_student.errors) < 3 :
                for field, errors in filled_student.errors.items():
                    for error in errors:
                        messages.error(request,filled_student.fields[field].label + " : " + error)
            else:
                messages.error(request,"You Have Left To Much Field Blank May Be In This Tab Or In Other Two Tabs Fill Them First !")
    student = StudentForm(instance=stud_obj)
    disable = stud_obj.disable
    
    return render(request,"edit_student.html",{'stud':student,'disable':disable})