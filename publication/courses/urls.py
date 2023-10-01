from django.urls import path
from .views import *

app_name ="courses"
urlpatterns =[
    path('',SubjectListView.as_view(), name="subjectlist"),
    path('proposal/subject', subPro, name='subpro'),
    path('proposal/list_proposal', listSubProposal.as_view(), name='listpro'),

    path('proposal/course', coursePro, name='coursepro'),
    path('proposal/list_course_proposal', listCourseProposal.as_view(), name='listcourpro'),

    path('proposal/module', modulePro, name='modulepro'),
    path('proposal/list_module_proposal', listModProposal.as_view(), name='listmodpro'),


    path('<slug:slug>',CourseListViews.as_view(), name="courselist"),
    path('<str:subject>/<slug:slug>',ModuleListView.as_view(), name="modulelist"),
    path('<str:subject>/<str:slug>/create/',ModuleCreateView.as_view(), name="modulecreate"),
    path('<str:subject>/<str:course>/<slug:slug>',ModuleListViewDetail.as_view(), name="modulelistdetail"),
    path('<str:subject>/<str:course>/<slug:slug>/update',ModuleUpdateView.as_view(), name="moduleupdate"),
    path('<str:subject>/<str:course>/<slug:slug>/delete',ModuleDeleteView.as_view(), name="moduledelete"),
    
]