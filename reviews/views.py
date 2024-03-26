from django.shortcuts import render, redirect

from .forms import ReviewForm
from .models import TouristReview


# Create your views here.
def review_list(request):
    if request.method == 'GET':
        reviews = TouristReview.objects.all()
        return render(request, 'reviewpage.html',{'reviews': reviews})

from django.shortcuts import render, redirect
from .forms import ReviewForm  # Assuming ReviewForm is imported from forms.py

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            if request.user.is_authenticated:
                review.user = request.user
                review.save()
                return redirect('review_list')
            else:
                return redirect('login')  # Redirect to login page if user is not authenticated
    else:
        form = ReviewForm()

    return render(request, 'reviewpage.html', {'form': form})
