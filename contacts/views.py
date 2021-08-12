from django.shortcuts import render, redirect
from .forms import FeedbackForm

def contacts(request):
  if request.method == "POST":
    form = FeedbackForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data.get('name')
      feedback = form.save()
      num = feedback.number
      return redirect('/')
  else:
    form = FeedbackForm()
    context = {
      'form': form,
    }
  return render(request, 'contacts/contacts.html', context)
