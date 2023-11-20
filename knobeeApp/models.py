from django.db import models

class JobListings(models.Model):
    Job_ID = models.AutoField(primary_key=True)
    Job_Title = models.CharField(max_length=100)
    Job_Description = models.TextField()

    def __str__(self):
        return self.Job_Title

class JobApplications(models.Model):
    App_ID = models.AutoField(primary_key=True)
    Job_ID = models.ForeignKey(JobListings, on_delete=models.CASCADE)#title
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Contact = models.CharField(max_length=15)

    def __str__(self):
        return f"Application for {self.Job_ID.Job_Title} by {self.App_Name}"

