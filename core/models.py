from django.db import models
from django.conf import settings





class Post(models.Model):
    title = models.CharField(max_length=100, null=False )
    content = models.TextField(null=False)
    image = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.SET_NULL )

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


#class Like(models.Model):
    
    
    
   # created_at = models.DateField()
   # updated_at = models.DateField()