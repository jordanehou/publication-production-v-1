from django.contrib import admin
from .models import Comment, Response, Subject, Course, Module, SubProposal, ModuleProposal, CourseProposal

# Register your models here.

#admin.site.register(Subject)
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
#admin.site.register(Course)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Module)
admin.site.register(Comment)
admin.site.register(Response)


#admin.site.register(CourseProposal)
@admin.register(CourseProposal)
class CourseProposalAdmin(admin.ModelAdmin):
    list_display = ['owner','subject','name','price','description', 'created']


admin.site.register(ModuleProposal)

@admin.register(SubProposal)
class SubProposalAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name','description', 'created']
   