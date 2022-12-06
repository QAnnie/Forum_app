from django.db import models

# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table ='post'
        
        
    name = models.CharField(
        'Name', blank=False, null=False, max_length=20, db_index=True, default='Anonymous'
    )
    
    
    body = models.CharField(
        'Body' , blank=True , null=False, db_index=True , max_length=140
    )
    
    
    created_at = models.DateTimeField(
        'Created DateTime' , blank=True , auto_now_add=True
    )
        
        
        