from django.db import models





class Contacts(models.Model):  
        Name= models.CharField(max_length= 100)  
        Email= models.EmailField(max_length=100 )  
        Message= models.CharField(max_length=15 )  
        class Meta:  
            db_table = "contact"      


