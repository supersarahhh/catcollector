from django.shortcuts import render, redirect
# Add UpdateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
from .forms import FeedingForm

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

# Add new view
def cats_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'cats/index.html', {
    'cats': Cat.objects.all()
  })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form': FeedingForm()                             
})

def add_feeding(request, cat_id):
   # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  # success_url = '/cats/{cat_id}'

class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'


