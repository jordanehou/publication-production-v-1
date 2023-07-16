from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, FormView
from .forms import ModuleForm, ComForm, RepForm
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from carts.forms import CartAddCourseForm
# Create your views here.

class SubjectListView(ListView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'courses/subject_list.html'


class CourseListViews(DetailView): # car chq suject est lier a un cour 
    context_object_name = 'subject' #(ie on peut utiliser Subject au lieu de Cour )
    model = Subject
    
    template_name = 'courses/subject_detail.html'
   
    



class ModuleListView(DetailView):
    context_object_name = 'courses'
    model = Course
    template_name = 'courses/course_detail.html'


class ModuleListViewDetail(DetailView, FormView):
    context_object_name = 'module'
    model = Module
    template_name = 'courses/module_detail.html'
    form_class = ComForm
    second_form_class = RepForm
    
    def get_context_data(self, **kwargs):
        context = super(ModuleListViewDetail, self).get_context_data(**kwargs)

        if 'form' not in context :  #si le form est dans le context
            context['form'] =self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()  

        return context
    
    

    # ces fonctions permette de valider
    def form_valid(self, form):
        self.object = self.get_object() 
        fv = form.save(commit=False)
        fv.owner = self.request.user
        fv.name_module = self.object.comments.name
        fv.name_module_id = self.object.id
        fv.save()
        return HttpResponseRedirect(self.get_success_url())  

    def form_valid2(self, form):
        self.object = self.get_object()
        fv = form.save(commit=False)
        fv.owner = self.request.user
        fv.name_com_id = self.request.POST.get('comment_id')
        fv.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        self.object = self.get_object()
        subject = self.object.subject
        course = self.object.course
        return reverse_lazy('courses:modulelistdetail', kwargs={
            'subject':subject,
            'course':course, 
            'slug': self.object
        })         


    #lorsque l'utilisateur doit poster
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.form_class

            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'  
        form = self.get_form(form_class) 

        if form_name =='form'and form.is_valid():
            print('nouveau commentaire')
            return self.form_valid(form)  

        if form_name =='form2'and form.is_valid():
            print('nouvelle reponse')
            return self.form_valid2(form)   

                      

 #creer un objet de course
class ModuleCreateView(CreateView):
    form_class = ModuleForm
    context_object_name = 'courses'
    model = Course
    template_name = 'courses/module_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        subject = self.object.subject
        #course = self.object.course
        return reverse_lazy('courses:modulelist', kwargs= {'subject':subject, 'slug': self.object.slug})
        

    def form_valid(self, form, *args,**kwargs):
        self.object = self.get_object()
        md =form.save(commit= False)
        md.owner = self.request.user      # object que je veux enregistrer
        md.subject = self.object.subject
        md.course = self.object
        md.save()
        return HttpResponseRedirect(self.get_success_url())

class ModuleUpdateView(UpdateView):
    fields = ('name','position', 'present_file','pdf_course')
    context_object_name = 'module'
    model = Module
    template_name = 'courses/module_update.html'

class ModuleDeleteView(DeleteView):
    model = Module
    context_object_name = "module"
    template_name = 'courses/module_delete.html'

    def get_success_url(self):
        subject = self.object.subject
        course = self.object.course
        return reverse_lazy("courses:modulelist", kwargs ={'subject':subject, 'slug':course.slug})




def subPro(request):
    #sub_pro = SubjectProForm(request)
    if request.method == 'POST':
        #here we join the two form, to get only one form, 
        # reason while we have only user_form to get the form
        user_form = SubjectProForm(data=request.POST)
    
        if user_form.is_valid():
            
            user = user_form.save()
            user.save()
            content={
                'owner':request.POST.get('owner'),
                'name': request.POST.get('name'),
                'desc': request.POST.get('description')
            }
            
            return render(request,'courses/proposals/examinations/examin_subject.html', content)
        else:
            #pricise the error to the user
            print('incorrect field')
    else:
        user_form = SubjectProForm
        
    content = {
        'form1': user_form,
        
    }
    return render(request, 'courses/proposals/pro_subject.html', content)

class listSubProposal(ListView):
    context_object_name = 'proposals'
    model = SubProposal
    template_name = 'courses/proposals/examinations/list_proposal.html'



class listCourseProposal(ListView):
    context_object_name = 'proposals'
    model = CourseProposal
    template_name = 'courses/proposals/examinations/list_course_proposal.html'

def coursePro(request):
    #sub_pro = CourseProForm(request)
    if request.method=='POST':
        form = CourseProForm(data=request.POST)
        if form.is_valid():
            courPro = form.save()
            courPro.save()

            content={
                'subject': request.POST.get('subject'),
                'name': request.POST.get('name'),
                'owner': request.POST.get('owner'),
                'price': request.POST.get('price'),
                'desc': request.POST.get('description'),
            }
            return render(request,'courses/proposals/examinations/result_course.html', content)
        else:
            print('error')
    else:
        form = CourseProForm

    return render(request, 'courses/proposals/pro_course.html', {'form': form})
            


class listModProposal(ListView):
    context_object_name = 'proposals'
    model = ModuleProposal
    template_name = 'courses/proposals/examinations/list_module_proposal.html'

def modulePro(request):
    if request.method=='POST':
        form = ModuleProForm(data=request.POST)
        if form.is_valid():
            modPro = form.save()
            modPro.save()

            content={
                'subject': request.POST.get('subject'),
                'course': request.POST.get('course'),
                'name': request.POST.get('name'),
                'video': request.POST.get('video'),
                'present_file': request.POST.get('present_file'),
                'pdf_course': request.POST.get('pdf_course'),
                'position': request.POST.get('position'),
                'desc': request.POST.get('description'),
                
            }
            return render(request,'courses/proposals/examinations/result_module.html', content)
        else:
            print('error')
    else:
        form = ModuleProForm

    return render(request, 'courses/proposals/pro_module.html', {'form': form})
