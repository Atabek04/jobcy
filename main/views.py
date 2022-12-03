from django.shortcuts import render
from . models import *


def indexHandler(request):
    jobs = Job.objects.all()
    job_categories  = JobCategory.objects.filter(status = 0)
    countries = Country.objects.all()

    
    return render(request, 'index-2.html', context= {
        'job_categories':job_categories,
        'countries':countries,
        'jobs':jobs,

    })


def jobListHandler(request):
    
    experience = int(request.GET.get('experience', -1))
    employment = int(request.GET.get('employment', -1))
    q = request.GET.get('q', None)
    location = request.GET.get('location', None)
    category = int(request.GET.get('category', 0))
    jobs = Job.objects.all()

    if q:
        jobs = Job.objects.filter(title__contains = q).filter(category__id = category).filter(company__location__code = location)
    elif experience and employment:
        jobs = Job.objects.filter(experience__id = experience).filter(employment__id = employment)
    elif experience:
        jobs = Job.objects.filter(experience__id = experience)
    elif employment:
        jobs = Job.objects.filter(employment__id = employment)
    

    
    job_categories  = JobCategory.objects.filter(status = 0)
    countries = Country.objects.all()  
    experience  = Experience.objects.all()
    employment = Employment.objects.all()
    return render(request, 'job-list.html', context={
        'jobs':jobs,
        'job_categories':job_categories,
        'countries':countries,
        'zapros':q,
        'experience':experience,
        'employment':employment
    })


def jobGridHandler(request):
    jobs = Job.objects.all()


    return render(request, 'job-grid.html', context={
        'jobs':jobs,
    })


def jobDetailsHandler(request, job_id):
    job = Job.objects.get(id = job_id)
    jobs = Job.objects.all()[:3]


    return render(request, 'job-details.html', context={
    'job':job,
    'jobs':jobs,
    })


def jobCategoriesHandler(request):
    return render(request, 'job-categories.html')


def candidateListHandler(request):
    return render(request, 'candidate-list.html')


def candidateGridHandler(request):
    return render(request, 'candidate-grid.html')


def candidateDetailsHandler(request):
    return render(request, 'candidate-details.html')


def companyListHandler(request):
    companies = Company.objects.all()

    return render(request, 'company-list.html', context = {
        'companies':companies,
    })


def companyDetailsHandler(request, company_id):
    company = Company.objects.get(id = company_id)
    related_jobs = Job.objects.filter(company__id = company_id)[:4]

    return render(request, 'company-details.html', context={
        'company':company,
        'related_jobs':related_jobs,
    })