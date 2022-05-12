from binascii import Incomplete
import email
from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from app.models import FacultyMembers
from app.models import FacultyInfo
from app.models import FormProgress
from app.models import FormSix
from app.models import FormFive
from app.models import FormFour
from app.models import FormThree
from app.models import FormTwo
from app.models import FormOne
from django.contrib.auth import logout
from django.shortcuts import redirect
today = date.today()

def logout_view(request):
    logout(request)
    return redirect('signin')

def welcome(request):
    return render(request, 'app/welcome.html')

def credits(request):
    return render(request, 'app/credits.html')

def profileupdate(request):
    if request.method == "POST":
        pron = request.POST['pron']
        firstname = request.POST['firstname']
        lastName = request.POST['lastName']
        designation = request.POST['designation']
        FacultyID = request.POST['FacultyID']
        nameofInstitute = request.POST['nameofInstitute']
        nameofDepartment = request.POST['nameofDepartment']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        statelocation = request.POST['statelocation']
        dob = request.POST['dob']
        joiningdate = request.POST['joiningdate']
        expyears = request.POST['expyears']
        ndyexpyears = request.POST['ndyexpyears']
        yearofappraisel = request.POST['yearofappraisel']

        infodata = FacultyInfo(
            pron = pron,
            firstname = firstname,
            lastName = lastName,
            designation = designation,
            FacultyID = FacultyID,
            nameofInstitute = nameofInstitute,
            nameofDepartment = nameofDepartment,
            email = email,
            phone = phone,
            city = city,
            statelocation = statelocation,
            dob = dob,
            joiningdate = joiningdate,
            expyears = expyears,
            ndyexpyears = ndyexpyears,
            yearofappraisel = yearofappraisel
        )

        infodata.save()

        infosdata = FacultyMembers(
            email = email,
            name = firstname,
            claimedscore = 0,
            givenscore = 0,
            performace = "Excellent",
            formstatus = 0,
            FacultyID = FacultyID,
            nameofInstitute = nameofInstitute,
            nameofDepartment = nameofDepartment,
            lastupdated = today.strftime("%m/%d/%y")
        )
        
        infosdata.save()
        
        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.firstname = firstname
        FormProgressData.FacultyID = FacultyID
        FormProgressData.basicprofile = "Completed"
        FormProgressData.save()
        return redirect(home)

    return render(request, 'app/dashboard/forms/teaching_and_load_assesment.html')

# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        filleddata = FormProgress.objects.get(email= request.user.email)
        if filleddata.basicprofile == "Completed":
            return redirect('home')
        else:
          return render(request,'app/index.html',{'user':request.user})
        
    else:
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['pass1'] 

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request,user)
                if user.first_name == "FACULTY":
                    filleddata = FormProgress.objects.get(email=request.user.email)
                    if filleddata.basicprofile == "Completed":
                        return redirect('home')
                    return render(request,'app/index.html',{'user':request.user})
                elif user.first_name == "HOD":
                    return redirect('hod')
            else:
                messages.error(request,"Bad credentials")
                return redirect('signin')
        return render(request, 'app/sign-in.html')

def home(request):
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email= request.user.email)
        if filleddata.basicprofile == "Completed":
            if request.user.first_name == "FACULTY":    
                context = {
                    'filleddata': filleddata,
                    'user': request.user
                }
                return render(request, 'app/dashboard/firstpage.html', context)
            elif request.user.first_name == "HOD":
                return redirect('hod')
        else:
          return redirect('signin')
    else:
        return redirect('login')

def home2(request):
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email= request.user.email)
        if filleddata.basicprofile == "Completed":
            if request.user.first_name == "FACULTY":    
                context = {
                    'filleddata': filleddata,
                    'user': request.user
                }
                return render(request, 'app/dashboard/hometwo.html', context)
            elif request.user.first_name == "HOD":
                return redirect('hod')
        else:
          return redirect('signin')
    else:
        return redirect('login')


def hod(request):
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email= request.user.email)
        if filleddata.basicprofile == "Completed":
            email = request.user.email
            FacultyInfoData = FacultyInfo.objects.get(email = email)
            facdata = FacultyMembers.objects.filter(nameofDepartment = FacultyInfoData.nameofDepartment)
            
            context = {
                'facdata': facdata
            }


            return render(request, 'app/dashboard/hod_welcome.html', context)
        else:
          return redirect('signin')
    else:
        return redirect('login')
    
def fetchprofile(request, emailid):
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        facdata = FacultyInfo.objects.get(email = emailid)
        filleddata = FormProgress.objects.get(email= emailid)
        if filleddata.basicprofile == "Completed":
            context = {
                'filleddata': filleddata,
                'facultyinfodata': facdata
            }
            return render(request, 'app/dashboard/facultyinfo.html', context)
        else:
            context = {
                    'facdata': facdata
            }
            return render(request, 'app/dashboard/facultyinfo.html', context)
    else:
        return redirect('login')
    

def formone(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberoflectures = request.POST['numberoflectures']
        scoreclaimedbyfaculty = request.POST['scoreclaimedbyfaculty']
        collpolllink = request.POST['collpolllink']

        infodata = FormOne(
            email = email,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberoflectures = numberoflectures,
            scoreclaimedbyfaculty = scoreclaimedbyfaculty,
            collpolllink = collpolllink
        )
        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormOne = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/teaching_and_load_assesment.html')

def formtwo(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberofstudent = request.POST['numberofstudent']
        dateofexam = request.POST['dateofexam']
        appointedas = request.POST['appointedas']
        fclaimedmarks = request.POST['fclaimedmarks']

        infodata = FormTwo(
            email = email,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberofstudent = numberofstudent,
            dateofexam = dateofexam,
            appointedas = appointedas,
            fclaimedmarks = fclaimedmarks,
        )
        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormTwo = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/examination_and_evaluation_duties.html')

def formthree(request):
    if request.method == "POST":
        email = request.user.email
        studentactivityname = request.POST['studentactivityname']
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberofstudent = request.POST['numberofstudent']
        dateofactivity = request.POST['dateofactivity']
        fclaimedmarks = request.POST['fclaimedmarks']

        infodata = FormThree(
            email = email,
            studentactivityname = studentactivityname,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberofstudent = numberofstudent,
            dateofactivity = dateofactivity,
            fclaimedmarks = fclaimedmarks,
        )
        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormThree = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/student_related_activities.html')

def formfour(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        studentbatch = request.POST['studentbatch']
        numberofstudent = request.POST['numberofstudent']
        avgresult = request.POST['avgresult']
        adoncourse = request.POST['adoncourse']
        othercourse = request.POST['othercourse']
        allclear = request.POST['allclear']
        fclaimedmarks = request.POST['fclaimedmarks']

        infodata = FormFour(
            email = email,
            currentclass = currentclass,
            division = division,
            studentbatch = studentbatch,
            numberofstudent = numberofstudent,
            avgresult = avgresult,
            adoncourse = adoncourse,
            othercourse = othercourse,
            allclear = allclear,
            fclaimedmarks = fclaimedmarks,
        )
        infodata.save()
        
        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormFour = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/teacher_guardian_performance.html')

def formfive(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        academicyear = request.POST['academicyear']
        semester = request.POST['semester']
        subjectname = request.POST['subjectname']
        numberoftaught = request.POST['numberoftaught']
        lastyresult = request.POST['lastyresult']
        currentyresult = request.POST['currentyresult']
        fclaimedmarks = request.POST['fclaimedmarks']

        infodata = FormFive(
            email = email,
            currentclass = currentclass,
            division = division,
            academicyear = academicyear,
            semester = semester,
            subjectname = subjectname,
            numberoftaught = numberoftaught,
            lastyresult = lastyresult,
            currentyresult = currentyresult,
            fclaimedmarks = fclaimedmarks
        )

        infodata.save()
        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormFive = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/university_result_analysis.html')

def formsix(request):
    if request.method == "POST":
        email = request.user.email
        academicyear = request.POST['academicyear']
        semester = request.POST['semester']
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        fclaimedmarks = request.POST['fclaimedmarks']

        infodata = FormSix(
            email = email,
            academicyear = academicyear,
            semester = semester,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            fclaimedmarks = fclaimedmarks
        )

        infodata.save()
        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormSix = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/feedback_analysis.html')

def moreformone(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberoflectures = request.POST['numberoflectures']
        scoreclaimedbyfaculty = request.POST['scoreclaimedbyfaculty']
        collpolllink = request.POST['collpolllink']

        infodata = FormOne(
            email = email,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberoflectures = numberoflectures,
            scoreclaimedbyfaculty = scoreclaimedbyfaculty,
            collpolllink = collpolllink
        )
        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormOne = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/more/faculty_contribution.html')

def moreformtwo(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberoflectures = request.POST['numberoflectures']
        scoreclaimedbyfaculty = request.POST['scoreclaimedbyfaculty']
        collpolllink = request.POST['collpolllink']

        infodata = FormOne(
            email = email,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberoflectures = numberoflectures,
            scoreclaimedbyfaculty = scoreclaimedbyfaculty,
            collpolllink = collpolllink
        )

        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormOne = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/more/randfaculty_contribution.html')

def moreformthree(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberoflectures = request.POST['numberoflectures']
        scoreclaimedbyfaculty = request.POST['scoreclaimedbyfaculty']
        collpolllink = request.POST['collpolllink']

        infodata = FormOne(
            email = email,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberoflectures = numberoflectures,
            scoreclaimedbyfaculty = scoreclaimedbyfaculty,
            collpolllink = collpolllink
        )
        
        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormOne = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/more/published.html')

def moreformfour(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberoflectures = request.POST['numberoflectures']
        scoreclaimedbyfaculty = request.POST['scoreclaimedbyfaculty']
        collpolllink = request.POST['collpolllink']

        infodata = FormOne(
            email = email,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberoflectures = numberoflectures,
            scoreclaimedbyfaculty = scoreclaimedbyfaculty,
            collpolllink = collpolllink
        )
        
        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormOne = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/more/ictform.html')

def moreformfive(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberoflectures = request.POST['numberoflectures']
        scoreclaimedbyfaculty = request.POST['scoreclaimedbyfaculty']
        collpolllink = request.POST['collpolllink']

        infodata = FormOne(
            email = email,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberoflectures = numberoflectures,
            scoreclaimedbyfaculty = scoreclaimedbyfaculty,
            collpolllink = collpolllink
        )
        
        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormOne = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/more/researchconsultancy.html')

def moreformsix(request):
    if request.method == "POST":
        email = request.user.email
        currentclass = request.POST['currentclass']
        division = request.POST['division']
        subjectname = request.POST['subjectname']
        numberoflectures = request.POST['numberoflectures']
        scoreclaimedbyfaculty = request.POST['scoreclaimedbyfaculty']
        collpolllink = request.POST['collpolllink']

        infodata = FormOne(
            email = email,
            currentclass = currentclass,
            division = division,
            subjectname = subjectname,
            numberoflectures = numberoflectures,
            scoreclaimedbyfaculty = scoreclaimedbyfaculty,
            collpolllink = collpolllink
        )
        
        infodata.save()

        FormProgressData = FormProgress.objects.get(email = email)
        FormProgressData.FormOne = "Completed"
        FormProgressData.save()
        #After Completion of form we are redirected to homepage
        return redirect('home')

    return render(request, 'app/dashboard/forms/more/Faculty_Value.html')



def myprofile(request):
    # return render(request,'app/index.html',{'user':request.user})
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email= request.user.email)
        facultyinfodata = FacultyInfo.objects.get(email= request.user.email)
        if filleddata.basicprofile == "Completed":
            context = {
                'filleddata': filleddata,
                'user': request.user,
                'facultyinfodata': facultyinfodata
            }
            return render(request, 'app/profile.html', context)
        else:
          return redirect('signin')
    else:
        return redirect('login')

def fetchformone(request, emailid):
    # return render(request,'app/index.html',{'user':request.user})
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email= emailid)
        formonedata = FormOne.objects.get(email=emailid)
        context = {
            'filleddata': filleddata,
            'user': request.user,
            'formonedata': formonedata
        }
        return render(request, 'app/dashboard/fetchforms/teaching_and_load_assesment.html', context)
        
    else:
        return redirect('login')


def fetchformtwo(request, emailid):
    # return render(request,'app/index.html',{'user':request.user})
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email=emailid)
        formtwodata = FormTwo.objects.get(email=emailid)
        context = {
            'filleddata': filleddata,
            'user': request.user,
            'formtwodata': formtwodata
        }
        return render(request, 'app/dashboard/fetchforms/examination_and_evaluation_duties.html', context)

    else:
        return redirect('login')


def fetchformthree(request, emailid):
    # return render(request,'app/index.html',{'user':request.user})
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email=emailid)
        formThreedata = FormThree.objects.get(email=emailid)
        context = {
            'filleddata': filleddata,
            'user': request.user,
            'formThreedata': formThreedata
        }
        return render(request, 'app/dashboard/fetchforms/student_related_activities.html', context)

    else:
        return redirect('login')


def fetchformfour(request, emailid):
    # return render(request,'app/index.html',{'user':request.user})
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email=emailid)
        formFourdata = FormFour.objects.get(email=emailid)
        context = {
            'filleddata': filleddata,
            'user': request.user, 
            'formFourdata': formFourdata
        }
        return render(request, 'app/dashboard/fetchforms/teacher_guardian_performance.html', context)

    else:
        return redirect('login')

def fetchformfive(request, emailid):
    # return render(request,'app/index.html',{'user':request.user})
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email=emailid)
        formFivedata = FormFive.objects.get(email=emailid)
        context = {
            'filleddata': filleddata,
            'user': request.user,
            'formFivedata': formFivedata
        }
        return render(request, 'app/dashboard/fetchforms/university_result_analysis.html', context)

    else:
        return redirect('login')

def fetchformsix(request, emailid):
    # return render(request,'app/index.html',{'user':request.user})
    if request.user.is_authenticated:
        # filleddata = FormProgress.objects.all()
        filleddata = FormProgress.objects.get(email=emailid)
        formSixdata = FormSix.objects.get(email=emailid)
        context = {
            'filleddata': filleddata,
            'user': request.user,
            'formSixdata': formSixdata
        }
        return render(request, 'app/dashboard/fetchforms/feedback_analysis.html', context)

    else:
        return redirect('login')

def signup(request):
    if request.method == "POST":
        authority = request.POST['Authority']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = authority
        myuser.save()

        messages.success(request,"Your Account has been successfully created.")

        FormProgressdata = FormProgress(
            email = email,
            firstname = "firstname",
            FacultyID = "FacultyID",
            basicprofile = "Inompleted",
            FormOne = "Incomplete",
            FormTwo = "Incomplete",
            FormThree = "Incomplete",
            FormFour = "Incomplete",
            FormFive = "Incomplete",
            FormSix = "Incomplete",
            FormSeven = "Incomplete",
            FormEight = "Incomplete",
            NetCoutFormFilled = 0
        )

        FormProgressdata.save()

        return redirect('signin')

    return render(request, 'app/sign-up.html')

