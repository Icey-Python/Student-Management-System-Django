from django.shortcuts import render, redirect
from score.models import Score
from score.forms import ScoreForm
from django.core.exceptions import ValidationError

def index(request):
    # Adding functionality for adding students
    if request.method == 'POST' and 'add_student' in request.POST:
        return redirect('add_student')

    # Adding functionality for managing users
    if request.method == 'POST' and 'manage_users' in request.POST:
        return redirect('manage_users')

    context = {}
    form = ScoreForm()
    scores = Score.objects.all()
    context['scores'] = scores
    context['title'] = 'Home'
    context['form'] = form
    return render(request, 'view_data.html', context)

def add_student(request):
    context = {}
    context['title'] = 'Add Student'
    # Add your add student logic here
    return render(request, 'add_student.html', context)


def manage_users(request):
    context = {}
    scores = Score.objects.all()
    context['scores'] = scores
    context['title'] = 'Manage Users'

    if request.method == 'POST':
        form = ScoreForm(request.POST)  # Initialize form with POST data

        if 'edit' in request.POST:
            pk = request.POST.get('edit')
            score_to_edit = Score.objects.get(id=pk)
            form = ScoreForm(instance=score_to_edit)  # Pre-fill the form with score data for editing
            context['edit_score'] = score_to_edit  # Pass the score object to the context for rendering in the template

        elif 'save' in request.POST:
            pk = request.POST.get('save')
            if pk:  # If pk exists, it's an existing score being edited
                score_to_update = Score.objects.get(id=pk)
                form = ScoreForm(request.POST, instance=score_to_update)  # Bind form to existing score instance
            else:
                form = ScoreForm(request.POST)  # Otherwise, it's a new score being created

            try:
                if form.is_valid():
                    form.save() 
                    return redirect('index')  # Redirect back to manage_users view after saving
            except ValidationError as e:
                context['error'] = str(e)

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            score_to_delete = Score.objects.get(id=pk)
            score_to_delete.delete()
            return redirect('index')  # Redirect back to manage_users view after deleting

    else:
        form = ScoreForm()  # Initialize an empty form for GET requests

    context['form'] = form
    return render(request, 'index.html', context)
def view_data(request):
    scores = Score.objects.all()
    return render(request, 'view_data.html', {'scores': scores})

