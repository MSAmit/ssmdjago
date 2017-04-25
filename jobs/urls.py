
from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from jobs.models import Jobs

urlpatterns = [
        url(r'^alljobs/$', ListView.as_view(queryset = Jobs.objects.all().order_by('-date')[:50],
                                            template_name = "jobs/alljobs.html")),
        url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Jobs,
                                                  template_name = "jobs/job.html")),
]
