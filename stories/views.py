from django.shortcuts import render, get_object_or_404
from .models import Stories

from .forms import StoryForm

# Create your views here.


def all_stories(request):
    """ A view to show all stories, including search function """

    stories = Stories.objects.all()

    context = {
        'stories': stories,
    }

    return render(request, 'stories/stories.html', context)
    

def story_detail(request, story_id):
    """ A view to show individual story detail """

    story = get_object_or_404(Stories, pk=story_id)

    context = {
        'story': story,
    }

    return render(request, 'stories/story_detail.html', context)


def add_stories(request):
    """ Add a story to customer stories"""
    form = StoryForm()
    template = 'stories/add_story.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
