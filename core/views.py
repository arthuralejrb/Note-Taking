from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404 
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'index.html')


@login_required
def topics(request):
    """show the topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


@login_required
def topic(request, topic_id):
    """Show topic entries"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    
    
    entries = topic.entry_set.order_by('-date_added') # - sign inverts the date_added order
    context = {'topic' : topic, 'entries' :entries}
    return render(request, 'topic.html', context)


@login_required
def new_topic(request):
    """let the user create a new topic"""
    if request.method != 'POST':
        # creates blank form
        form = TopicForm()
        
    else: 
        # process data
        form = TopicForm(request.POST)
        
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    
    context = {'form': form}
    return render(request,'new_topic.html' ,context)


@login_required
def new_entry(request, topic_id):
    """Adds a new entry for a specific topic"""
    topic = Topic.objects.get(id=topic_id) #linha 24
    
    if request.method != 'POST':
        # creates blank form
        form = EntryForm()
    else:
        # process data
        form = EntryForm(data=request.POST)
        
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', 
                                                args=[topic_id]))
            
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edits existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    
    if request.method != 'POST':
        # inicial request, fill form with actual entry
        form = EntryForm(instance=entry)
    else:
        # process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'edit_entry.html', context)    