from django.contrib import admin
from . models import *

class SingleModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(JobCategory, SingleModelAdmin)
admin.site.register(Country, SingleModelAdmin)
admin.site.register(Skill, SingleModelAdmin)
admin.site.register(Company, SingleModelAdmin)
admin.site.register(Employment, SingleModelAdmin)
admin.site.register(Job, SingleModelAdmin)
admin.site.register(Experience, SingleModelAdmin)