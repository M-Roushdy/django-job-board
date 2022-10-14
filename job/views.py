from django.shortcuts import render, reverse
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm
# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'job/job_list.html', {
        'jobs':page_obj
        })
    
def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.job=job_detail
            myForm.save()
    else:
        form = ApplyForm()
        
    return render(request, 'job/job_detail.html', {
        'job':job_detail, 'form':form
    })