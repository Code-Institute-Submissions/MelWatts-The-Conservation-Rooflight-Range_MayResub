from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save()
            messages.success(request, 'Great! Thanks for the Story!')
            return redirect(reverse('story_detail', args=[story.id]))
        else:
            messages.error(request, 'Opps! Please check your form is valid.')
    else:
        form = StoryForm()
    template = 'stories/add_story.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_story(request, story_id):
    """ User to edit thier story """

    story = get_object_or_404(Stories, pk=story_id)
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            messages.success(request, 'Story updated, well done!')
            return redirect(reverse('story_detail', args=[story.id]))
        else:
            messages.error(request, 'Opps! Please check your form is valid.')
    else:
        form = StoryForm(instance=story)
        messages.info(request, f'you are editing {story.name}')

    template = 'stories/edit_story.html'
    context = {
        'form': form,
        'story': story,
    }

    return render(request, template, context)


def delete_story(request, story_id):
    """ User to delate a story """
    story = get_object_or_404(Stories, pk=story_id)
    story.delete()
    messages.success(request, 'Your story is deleted!')
    return redirect(reverse('stories'))
