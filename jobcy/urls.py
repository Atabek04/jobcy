from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexHandler, name='index'),
    path('job-list/', jobListHandler, name='job-list'),
    path('job-grid/', jobGridHandler, name='job-grid'),
    path('job-details/<int:job_id>/', jobDetailsHandler),
    path('job-categories/', jobCategoriesHandler, name='job-categories'),


    path('candidate-list/', candidateListHandler, name='candidate-list'),
    path('candidate-grid/', candidateGridHandler, name='candidate-grid'),
    path('candidate-details/', candidateDetailsHandler),

    path('company-list/', companyListHandler, name='company-list'),
    path('company-details/<int:company_id>/', companyDetailsHandler, name='company-details'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
