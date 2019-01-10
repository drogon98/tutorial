from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True) #will assign the date to the date created but not on subsequent saves
    updated=models.DateTimeField(auto_now=True) # will assign the object date to the date it is created after update


    def __str__(self):
        return self.post


class Friend(models.Model):
    users=models.ManyToManyField(User) # links many users to each other
    current_user=models.ForeignKey(User,related_name="owner",null=True,on_delete=models.CASCADE)



    @classmethod
    def create_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
         current_user=current_user
        )
        friend.users.add(new_friend)




    @classmethod
    def loose_friend(cls,current_user,new_friend):
         friend,created=cls.objects.get_or_create(
          current_user=current_user
         )
         friend.users.remove(new_friend)
