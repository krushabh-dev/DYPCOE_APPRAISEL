from statistics import mode
from unicodedata import name
from django.db import models

class FacultyMembers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, default='example@example.in')
    claimedscore = models.IntegerField()
    givenscore = models.IntegerField()
    performace = models.CharField(max_length=20)
    formstatus = models.IntegerField()
    FacultyID = models.CharField(max_length=20, default='FACULTYID')
    nameofInstitute = models.CharField(max_length=200, default="DYP")
    nameofDepartment = models.CharField(max_length=200, default='Information Technology')
    lastupdated = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class FormOne(models.Model):
    email = models.EmailField()
    currentclass = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    subjectname = models.CharField(max_length=200)
    numberoflectures = models.IntegerField()
    scoreclaimedbyfaculty = models.IntegerField()
    collpolllink = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class FormTwo(models.Model):
    email = models.EmailField()
    currentclass = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    subjectname = models.CharField(max_length=200)
    numberofstudent = models.IntegerField()
    dateofexam = models.CharField(max_length=200)
    appointedas = models.CharField(max_length=200)
    fclaimedmarks = models.IntegerField()

    def __str__(self):
        return self.email

class FormThree(models.Model):
    email = models.EmailField()
    studentactivityname = models.CharField(max_length=200)
    currentclass = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    subjectname = models.CharField(max_length=200)
    numberofstudent = models.IntegerField()
    dateofactivity = models.CharField(max_length=200)
    fclaimedmarks = models.IntegerField()

    def __str__(self):
        return self.email

class FormFour(models.Model):
    email = models.EmailField()
    currentclass = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    studentbatch = models.CharField(max_length=200)
    numberofstudent = models.IntegerField()
    avgresult = models.IntegerField()
    adoncourse = models.IntegerField()
    othercourse = models.IntegerField()
    allclear = models.IntegerField()
    fclaimedmarks = models.IntegerField()

    def __str__(self):
        return self.email

class FormFive(models.Model):
    email = models.EmailField()
    currentclass = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    academicyear = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)
    subjectname = models.CharField(max_length=200)
    numberoftaught =  models.IntegerField()
    lastyresult =  models.IntegerField()
    currentyresult =  models.IntegerField()
    fclaimedmarks =  models.IntegerField()

    def __str__(self):
        return self.email
 
class FormSix(models.Model):
    email = models.EmailField()
    academicyear = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)
    currentclass = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    subjectname = models.CharField(max_length=200)
    fclaimedmarks = models.IntegerField()

    def __str__(self):
        return self.email
 
class FormProgress(models.Model):
    email = models.EmailField(max_length=200)
    firstname = models.CharField(max_length=200)
    basicprofile = models.CharField(max_length=20)
    FormOne = models.CharField(max_length=20)
    FormTwo = models.CharField(max_length=20)
    FormThree = models.CharField(max_length=20)
    FormFour = models.CharField(max_length=20)
    FormFive = models.CharField(max_length=20)
    FormSix = models.CharField(max_length=20)
    FormSeven = models.CharField(max_length=20)
    FormEight = models.CharField(max_length=20)
    FacultyID = models.CharField(max_length=200)
    NetCoutFormFilled = models.IntegerField()

    def __str__(self):
        return self.FacultyID

        
class FacultyInfo(models.Model):
    pron = models.CharField(max_length=20)
    firstname = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    designation = models.CharField(max_length=200) 
    FacultyID = models.CharField(max_length=200)
    nameofInstitute = models.CharField(max_length=200)
    nameofDepartment = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    city = models.CharField(max_length=200)
    statelocation = models.CharField(max_length=200)
    dob = models.DateField()
    joiningdate = models.DateField()
    expyears = models.IntegerField()
    ndyexpyears = models.IntegerField()
    yearofappraisel = models.IntegerField()

    def __str__(self):
        return self.FacultyID       

class BFormProgress(models.Model):
    email = models.EmailField(max_length=200)
    basicprofile = models.CharField(max_length=20, default="incomplete")
    FormOneA = models.CharField(max_length=20)
    FormOneB = models.CharField(max_length=20, default="incomplete")
    FormOneC = models.CharField(max_length=20, default="incomplete")
    FormTwo = models.CharField(max_length=20)
    FormThree = models.CharField(max_length=20)
    FormFour = models.CharField(max_length=20)
    FormFive = models.CharField(max_length=20)
    FormSix = models.CharField(max_length=20)
    NetCoutFormFilled = models.IntegerField()

    def __str__(self):
        return self.FacultyID 

class BformOneA(models.Model):
    email = models.EmailField()
    ptmeet = models.FileField()
    inductionProgram = models.FileField()
    defaulterCoordinator = models.FileField()
    internalExam = models.FileField()
    guestLecture = models.FileField()
    industrialVisit = models.FileField()
    timeTableCoordinator = models.FileField()
    nbaNaacCoordi = models.FileField()
    deptAcademic = models.FileField()
    tpoCordinate = models.FileField()
    fclaimedmarks =  models.IntegerField()
    totalmarks =  models.IntegerField()

    def __str__(self):
        return self.email

class BformOneB(models.Model):
    email = models.EmailField()
    interviewCoordinator = models.CharField(max_length=200)
    annualEvent = models.CharField(max_length=200)
    admissionProcess = models.CharField(max_length=200)
    ceo = models.CharField(max_length=200)
    guestLecture = models.CharField(max_length=200)
    nbaNaacCoordi = models.CharField(max_length=200)
    tpoCordinate = models.CharField(max_length=200)
    fclaimedmarks =  models.IntegerField()
    totalmarks =  models.IntegerField()

    def __str__(self):
        return self.email

class BformOneC(models.Model):
    email = models.EmailField()
    mediaPublicity = models.FileField()
    admission = models.FileField()
    socialWelfare = models.FileField()
    fclaimedmarks =  models.IntegerField()
    totalmarks =  models.IntegerField()
    def __str__(self):
        return self.email

class BformTwo(models.Model):
    email = models.EmailField()
    nameofpaper = models.CharField(max_length=200)
    nameofjournal = models.CharField(max_length=200)
    paperlink = models.CharField(max_length=200)
    journallink = models.CharField(max_length=200)
    fclaimedmarks =  models.IntegerField()
    totalmarks =  models.IntegerField()

    def __str__(self):
        return self.email

class BformThree(models.Model):
    email = models.EmailField()
    NoOFBookPatent = models.CharField(max_length=200)
    EcopyofBookPatent = models.CharField(max_length=200)
    journallink = models.CharField(max_length=200)
    publisherName = models.CharField(max_length=200)
    publisherCategory = models.CharField(max_length=200)
    fclaimedmarks =  models.IntegerField()
    totalmarks =  models.IntegerField()

    def __str__(self):
        return self.email
 
class BformThreeB(models.Model):
    email = models.EmailField()
    Econtent = models.CharField(max_length=200)
    UploadEvidance = models.CharField(max_length=200)
    UploadCopy = models.CharField(max_length=200)
    fclaimedmarks =  models.IntegerField()
    totalmarks =  models.IntegerField()

    def __str__(self):
        return self.email
 
class BformFour(models.Model):
    email = models.EmailField()
    NoOfPHDGuided = models.CharField(max_length=200)
    NoOfPGguided = models.CharField(max_length=200)
    NoOfBEPrjGuided = models.CharField(max_length=200)
    ResearchProjectCompleted = models.CharField(max_length=200)
    InProdDevelopment = models.CharField(max_length=200)
    Consultancy = models.CharField(max_length=200)
    EditorialBoard = models.CharField(max_length=200)
    PaperPublishedwithIndustry = models.CharField(max_length=200)
    EvidanceOne = models.CharField(max_length=200)
    EvidanceTwo = models.CharField(max_length=200)
    EvidanceThree = models.CharField(max_length=200)
    EvidanceFour = models.CharField(max_length=200)
    fclaimedmarks =  models.IntegerField()
    totalmarks =  models.IntegerField()

    def __str__(self):
        return self.email
 
class BformFive(models.Model):
    email = models.EmailField()
    EOrganised = models.CharField(max_length=200)
    EAttended = models.CharField(max_length=200)
    UploadReport = models.CharField(max_length=200)
    UploadCertificate = models.CharField(max_length=200)
    NameEvent = models.CharField(max_length=200)
    UploadEventCertificate = models.CharField(max_length=200)
    NPTELName = models.CharField(max_length=200)
    NPTELCert = models.CharField(max_length=200)
    IEnchanchedQualification = models.CharField(max_length=200)
    IEnchanchedQualificationProof = models.CharField(max_length=200)
    fclaimedmarks =  models.IntegerField()
    totalmarks =  models.IntegerField()

    def __str__(self):
        return self.email