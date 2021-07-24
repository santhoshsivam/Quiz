from django.db import models

# Create your models here.

''' 
    Here the databases are allocated 
    Questions are the sample database.
    Fifth standard is for fifth standard.
    Sixth standard is for sixth standard.
    Seventh standard is for sevnth standard.
    Signin is for getting user details.
    
'''



class questions(models.Model):
    Question_no = models.IntegerField()
    Question = models.CharField(max_length=1000)
    Answer = models.CharField(max_length=100)
    Option_A = models.CharField(max_length=30)
    Option_B = models.CharField(max_length=30)
    Option_C = models.CharField(max_length=30)
    Option_D = models.CharField(max_length=30)

    def __unicode__(self):
      return self.Question


class fifth_standard(models.Model):
    Question_no = models.IntegerField()
    Question = models.CharField(max_length=1000)
    Answer = models.CharField(max_length=100)
    Option_A = models.CharField(max_length=30)
    Option_B = models.CharField(max_length=30)
    Option_C = models.CharField(max_length=30)
    Option_D = models.CharField(max_length=30)

    def __unicode__(self):
      return self.Question

class sixth_standard(models.Model):
    Question_no = models.IntegerField()
    Question = models.CharField(max_length=1000)
    Answer = models.CharField(max_length=100)
    Option_A = models.CharField(max_length=30)
    Option_B = models.CharField(max_length=30)
    Option_C = models.CharField(max_length=30)
    Option_D = models.CharField(max_length=30)

    def __unicode__(self):
      return self.Question

class seventh_standard(models.Model):
    Question_no = models.IntegerField()
    Question = models.CharField(max_length=1000)
    Answer = models.CharField(max_length=100)
    Option_A = models.CharField(max_length=30)
    Option_B = models.CharField(max_length=30)
    Option_C = models.CharField(max_length=30)
    Option_D = models.CharField(max_length=30)

    def __unicode__(self):
      return self.Question
class signin(models.Model):
    Full_Name = models.CharField(max_length=30)
    Register_number = models.CharField(max_length=30,unique=True)
    Password = models.CharField(max_length=20)
    Mobile_number = models.IntegerField()
    Email_Id = models.CharField(max_length=20)
    
    
    def __unicode__(self):
      return self.Full_Name