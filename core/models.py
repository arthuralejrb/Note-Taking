from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model): 
    """User generated topic"""
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Returns model representation in string format"""
        
        return self.text
    
    
class Entry(models.Model):
    """Entry in a topic"""
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """Returns model representation in string format"""
        
        if len(self.text) < 50:
            return self.text
        
        else:
            return self.text[:50] + "..."