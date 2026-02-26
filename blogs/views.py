from django.shortcuts import render , redirect #Redirect stays here
from .models import BlogPostTitle,BlogContent
from .forms import BlogPostTitleForm, BlogContentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    """Returns the homepage template"""

    #first save the headlines in a context dictionary
    #for display
    blog_headlines=BlogPostTitle.objects.order_by('-date_added')
    context={"blog_headlines":blog_headlines}

    return render(request,'blogs/index.html',context)

def display_headlines(request):
    """Display topics for blog_headlines template"""

    #first save the headlines in a context dictionary
    #for display
    blog_headlines=BlogPostTitle.objects.order_by('-date_added')
    context={"blog_headlines":blog_headlines}

    return render(request,'blogs/blog_topics.html',context)

def display_contents(request,blogposttitle_id):
    """Display content for each blog post"""
    #fetch the blog headline first
    blog_headline=BlogPostTitle.objects.get(id=blogposttitle_id)
    #fetch the entries connected to the blog headline
    blog_content=blog_headline.blogcontent_set.order_by('-date_added')
    #Put the blog head line and content in context dictionary for 
    # template rendering
    context={'blog_headline':blog_headline,'blog_content':blog_content}
    #now return the template for the content
    return render(request,'blogs/blog_content.html',context)


@login_required
def add_blog_headline(request):
    """View function that adds a blog headline"""
    
    if request.method != 'POST':
        #Probably a GET request, instantiate a form instance for display of blank form template
        form = BlogPostTitleForm()
        
    else:
        #Definitely a 'POST' request, do checks and save data
        form = BlogPostTitleForm(data=request.POST)
        #checks if data is valid, if not, skip the if-block for validity
        #and continue rest of code.
        if form.is_valid():
            headline =form.save(commit=False)
            headline.owner = request.user
            headline.save()
            #After saving data when valid, redirect user back to blog topics page
            return redirect('blogs:blog_topics')
    
    #display the created blank form when either GET request runs or form was invalid
    
    #create a context dictionary to save the unfilled data or blank data
    context = {'form':form}
    #return the blank form template (Block only runs for GET request or all fields wasn't filled)
    return render(request, 'blogs/add_headline.html',context)

@login_required
def add_each_content(request,blogposttitle_id):
    """Function adds content to a blog topic"""
    #Get the topic ID first
    blog_headline=BlogPostTitle.objects.get(id=blogposttitle_id)

    #Then create a form that adds data to that topic
    if blog_headline.owner != request.user:
        raise Http404
    
    if request.method != "POST":
        #Probably a GET request, create blank form
        form=BlogContentForm()
    else:
        #Definitely a POST request, do checks and save data
        #THEN IMPORTANTLY ASSIGN THAT ENTRY TO THE CONNECTED TOPIC
        form=BlogContentForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.blog_post_title=blog_headline
            new_entry.owner = request.user
            new_entry.save()

            #Now after saving, redirect user back to blog_content page
            #where they see the data and entries for each page
            return redirect("blogs:blog_content",blogposttitle_id=blogposttitle_id)#change the blogcontent_id variable to content_id to verify
        
    #Display a blank or invalid form
    context={'blog_headline':blog_headline,'form':form}
    return render(request,'blogs/add_each_content.html',context)

@login_required
def edit_an_entry(request,blogcontent_id):
    """Allows users to edit an existing entry."""

    #First, get a specified entry thats associated with blogcontent_id
    content=BlogContent.objects.get(id=blogcontent_id)
    connected_headline = content.blog_post_title
    #check if user is trying to access his own post

    if connected_headline.owner != request.user:
        raise Http404

    #Now supply form based on POST or GET request

    if request.method != 'POST':
        #If request isn't POST, it is either a GET request or another sort, then do the code in this block
        #first create a form instance with the  inital data populated in it
        form=BlogContentForm(instance=content)
    else:
        #Else, request is definitely POST, which implies that user has entered new data.
        
        #First, create a form instance and compare the initial data with the populated data
        form=BlogContentForm(instance=content,data=request.POST)
        if form.is_valid():
            #If form is valid, save data. No need to write the connection code cause its already 
            #connected to the topic. #Check add_each_content function. 
            form.save()
            return redirect('blogs:blog_content',blogposttitle_id=connected_headline.id)
        
    context={"form":form,"connected_headline":connected_headline, "content":content}
    return render(request,'blogs/edit_entry.html',context)



