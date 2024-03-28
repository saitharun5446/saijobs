from django.shortcuts import render
from testapp.models import HydJobs,BngJobs,PuneJobs
# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')
def hydjobs_view(request):
    jobs_list=HydJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjob.html',my_dict)
def bngjobs_view(request):
    jobs_list=BngJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/bngjob.html',my_dict)
def Punejobs_view(request):
    jobs_list=PuneJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejob.html',my_dict)