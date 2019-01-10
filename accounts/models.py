from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from django.dispatch import receiver

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(city="Nairobi")

class UserProfile(models.Model):# we are adding a profile containing data releted to the User
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    website=models.URLField(default='')
    phone=models.IntegerField(default=0)
    image=models.ImageField(upload_to="profile_image",blank=True) # making the image field optional

    nairobi=UserProfileManager()

    def __str__(self):
        return self.user.username
#@receiver(post_save,sender=User)
def create_profile(sender,**kwargs):# receiver function, the sender must be a python object or None
    # if the sender=None or empty in the signal connect the update will be carried out in every saved model
    # kwargs include created,instance
    if kwargs['created']:# accessing items from  a dictionary
        user_profile=user.UserProfile.objects.create(user=kwargs['instance']) # instance is the obj created
        # by a new user

# listening to a signal
post_save.connect(create_profile,sender=User) # this signal will be fired when User instance is created and saved
# at some points one can have a number of signals to be fired on particular actions
# eg @receiver([post_save,post_delete],sender=None) This signals will be applied when respective actions are done on any model
# instance

#the above code can be written as:
#@receiver(post_save,sender=User)
#def create_profile(sender,**kwargs):
    #if kwargs['created']:
        #user_profile=UserProfile.objects.create(user=kwargs['instance'])
