from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post,Project
from django.views import generic
from .forms import CreatePostForm, ContactForm
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.shortcuts import redirect,render_to_response
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib import messages

class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(post_finished = "Y").filter(post_knowledge = "N")
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'
    paginate_by = 5

class PostView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(post_finished = "Y").filter(post_knowledge = "N")
    slug_field = 'post_slug'
    template_name = 'blog/post.html'

class EditView(generic.edit.UpdateView):
    model = Post
    slug_field = 'post_slug'
    fields = ['post_title','post_content']
    template_name = 'blog/edit.html'
    success_url = '/blog/'

class RemoveView(generic.edit.DeleteView):
    model = Post
    slug_field = 'post_slug'
    template_name='blog/delete.html'
    success_url = '/blog/'

class PostCreateView(generic.edit.CreateView):
    model = Post
    slug_field = 'post_slug'
    template_name = 'blog/create.html'
    success_url = '/blog/'
    fields = ['post_title','post_content']

class OneProjectView(generic.DetailView):
    model = Project
    slug_field = 'project_slug'
    template_name = 'blog/oneproject.html'

class KnowledgePostView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(post_finished = "Y").filter(post_knowledge = "Y")
    slug_field = 'post_slug'
    template_name = 'blog/knowledgepost.html'

def InfoView(request):
    template_name = 'blog/info.html'
    return render(request,template_name)

def ContactThanksView(request):
    template_name = 'blog/contactthanks.html'
    return render (request,template_name)

def NotFound(request):
    template_name = 'blog/NotFound.html'
    return render(request,template_name)

# Removed sensitive information, won't work
def ContactView(request):
    form_class = ContactForm

    if request.method == 'POST': #If form is submitted
        form = form_class(data=request.POST)
        if form.is_valid(): #If form is valid
            contact_name = request.POST.get('contact_name','')
            contact_email = request.POST.get('contact_email','')
            form_content = request.POST.get('content','')
            # Placed data in variables, could be put directly into tuple
            return HttpResponseRedirect('/contact/thanks')
        messages.warning(request,'Email failed, please ensure information is correct')
    return render(request, 'blog/contact.html', {'form' : form_class,})

def ProjectsView(request):
    template_name = 'blog/projects.html'
    all_projects = Project.objects.all()
    context = {'all_projects':all_projects}
    return render(request,template_name, context)

def CreatePostView(request):
    if request.method =='POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            try:
                description = content[0:750] + " ..."
            except:
                description = content
            postHolder = Post(post_title = form.cleaned_data['title'],
                              post_desc = description,
                              post_content = content,)
            postHolder.save()
            return HttpResponseRedirect('/blog/')
    else:
        form = CreatePostForm()

    template_name = 'blog/create-post.html'
    return render(request,template_name, {'form' : form})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


# Create your views here.
