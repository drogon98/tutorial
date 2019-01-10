from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from posts.forms import PostForm
from posts.models import Post,Friend

class HomeView(TemplateView):
    template_name="posts/home.html"


    def get(self,request):
        form=PostForm()
        post=Post.objects.all().order_by("-created")# orders from the latest
        users=User.objects.exclude(id=request.user.id) # this is the logged in user
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friends = None
        context={'form':form,'post':post,'users':users,'friends':friends}
        return render(request,self.template_name,context)

    def post(self,request):
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('posts:home')

        else:
            form=PostForm()
        return render(request,self.template_name,{'form':form})

def change_friend(request,operation,pk):
    new_friend=User.objects.get(pk=pk)
    if operation=="add":
        Friend.create_friend(request.user,new_friend)
    elif operation=="remove":
        Friend.loose_friend(request.user,new_friend)
    return redirect("posts:home")
