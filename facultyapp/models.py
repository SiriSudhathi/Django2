from django.db import models


class Comment(models.Model):
      
      Student_ID = models.CharField(max_length=200)
      Comments = models.CharField(max_length = 2000)
      

     
