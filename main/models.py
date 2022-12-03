from django.db import models


class JobCategory(models.Model):
    name  = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Country(models.Model):
    name  = models.CharField(max_length=300)
    code = models.CharField(max_length=300, blank=True, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name  = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    owner_name = models.CharField(max_length=300)
    location = models.ForeignKey('Country', on_delete=models.CASCADE)
    description = models.TextField(max_length=800)
    phone = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    website = models.CharField(max_length=300)
    logo = models.ImageField(blank=True, null=True)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, null = True)
    photo1 = models.ImageField(blank=True, null=True)
    photo2 = models.ImageField(blank=True, null=True)
    photo3 = models.ImageField(blank=True, null=True)

    
    def __str__(self):
        return self.name

class Employment(models.Model):
    name  = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE, blank=True, null=True)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, blank=True, null=True)
    salary = models.IntegerField(default=0)
    date_posted = models.TimeField(auto_now=True)
    job_description = models.TextField(max_length=800, null=True)
    qualification = models.TextField(max_length=800, null=True)

    def __str__(self):
        return f'{self.title} | {self.company.name} | {self.category.name}'