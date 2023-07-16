#from tkinter import Widget
from django import forms 
from .models import Module, Course, Subject, Comment, Response, SubProposal, ModuleProposal, CourseProposal

#__all__
class ModuleForm(forms.ModelForm):
    class Meta():
        model = Module 
        fields = ['module_id','name', 'video', 'present_file', 'pdf_course', 'position' ]

class CourseProForm(forms.ModelForm):
    class Meta():
        model = CourseProposal
        fields = ['owner','subject', 'name', 'price', 'description']

class SubjectProForm(forms.ModelForm):
    class Meta():
        model = SubProposal
        fields = ['owner','name', 'description']

class ModuleProForm(forms.ModelForm):
    class Meta():
        model = ModuleProposal
        fields = ['owner','subject','course','name', 'video', 'present_file', 'pdf_course', 'position', 'description' ]    


class ComForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'body'}
        labels = {'body': 'Comment'} 
        widgets = {
            'body':forms.Textarea(attrs={
                'class': 'form-control',
                'rows':4,
                'cols':70,
                'placeholder':'Entrez votre commentaire ici.'
            })
        }


class RepForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = {'body',}
        labels = {'body': 'responses'}
        widgets = {
            'body':forms.Textarea(attrs={
                'class': 'form-control',
                'rows':2,
                'cols':10,
                'placeholder':'Response here'
            })
        }