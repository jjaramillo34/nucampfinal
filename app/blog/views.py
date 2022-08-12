import os
import re

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post
from home.models import Home
from comment.forms import CommentForm
from django.views.generic import DetailView
from django.http import JsonResponse
from .models import SubscribedUsers
from django.core.mail import send_mail
from django.conf import settings

from next_prev import next_in_order, prev_in_order

# Create your views here.

def PostList(request):
    homepage = Home.objects.filter(status=1).order_by('id')
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    #object_list = get_object_or_404(Post, slug=slug)
    #comments = post.comments.filter(active=True)
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    #comments = post.comments.filter(active=True)
    page = request.GET.get('page')
    
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
        
    print(post_list.has_next())
    print(post_list.has_previous())
    
    context_dict = {
        'homepage': homepage,
        'page': page, 
        'post_list': post_list, 
        }
    
    print(context_dict)
    
    return render(request=request,
                template_name='home/blog-home-alt.html',
                context=context_dict
                )

def newsletter(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)
        subscribedUsers = SubscribedUsers()
        subscribedUsers.email = email
        subscribedUsers.name = name
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'NewsLetter Subscription'
        message = 'Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email.'
        email_from = 'contactme@datanaly.st'
        recipient_list = [email, ]
        #send_mail(subject, message, email_from, recipient_list)
        send_mail(
                    subject,
                    message,
                    email_from,
                    recipient_list,
                    fail_silently=False,
                )
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return res
    return render(request, 'home/blog-home-alt.html')

def post_detail(request, slug):
    template_name = 'home/blog-post.html'
    form_class = CommentForm
    homepage = Home.objects.filter(status=1).order_by('id')
    post = get_object_or_404(Post, slug=slug)
    #post = Post.objects.filter(slug=slug)
    #first_featured = post.first()
    #print(first_featured)
    #second_featured = next_in_order(first_featured, post=post)
    #print(second_featured)
    #comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            
    else:
        comment_form = CommentForm()
    
    
    context_dict = {'post': post,
                    'homepage': homepage,
                    #'first': first_featured,
                    #'second': second_featured,
                    #'comments': comments,
                    'new_comment': new_comment,
                    'comment_form': comment_form}

    #print(context_dict)

    return render(request=request, 
                  template_name=template_name, 
                  context=context_dict,
                  )
    
def validate_email(request): 
    email = request.POST.get("email", None)   
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif SubscribedUsers.objects.get(email = email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res
    
class PostDetailView(DetailView):
    model = Post
    template_name = "crm/deals/deal_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        activities= self.get_related_activities()
        context['related_activities'] = activities
        context['page_obj'] = activities 
        return context

    def get_related_activities(self):
        queryset = self.object.activity_rel.all() 
        paginator = Paginator(queryset,5) #paginate_by
        page = self.request.GET.get('page')
        activities = paginator.get_page(page)
        return activities
    