from django.shortcuts import render, redirect
from .models import FAQ
from .forms import FAQForm
from .utils import boolean_model, extended_boolean_model, vector_space_model

# Home View
def home(request):
    return render(request, 'faq_app/home.html')

# Add Question View
def add_question(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FAQForm()
    return render(request, 'faq_app/add_question.html', {'form': form})

from .models import FAQ
from .utils import boolean_model, extended_boolean_model, vector_space_model

def search_question(request):
    query = request.GET.get('q', '')
    algorithm = request.GET.get('algorithm', 'boolean')
    results = []

    faqs = FAQ.objects.all()

    if query:
        if algorithm == 'boolean':
            results = boolean_model(query, faqs)
        elif algorithm == 'extended_boolean':
            results = extended_boolean_model(query, faqs)
        elif algorithm == 'vector_space':
            results = vector_space_model(query, faqs)

    return render(request, 'faq_app/search.html', {'results': results, 'query': query, 'algorithm': algorithm})
