from django.shortcuts import render
from django.utils import timezone
from .models import Record, Site
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from decimal import *

getcontext().prec = 2

def app(request):
    records = Record.objects.order_by('site')
    sites = Site.objects.all()
    return render(request, 'app/app.html', {'records': records,'sites': sites})

def site_detail(request, pk):
    sites = get_object_or_404(Site, pk=pk)
    records = Record.objects.filter(site=sites.id)
    return render(request, 'app/site_detail.html', {'records': records,'sites': sites})

def summary(request):    
    # Aggregation obtained with raw SQL
    join = Record.objects.raw('SELECT apptask_record.id, apptask_record.created_date, SUM(apptask_record.a_record) AS a_record, SUM(apptask_record.b_record) AS b_record FROM apptask_record INNER JOIN apptask_site ON (apptask_record.site_id = apptask_site.id) GROUP BY apptask_record.site_id ORDER BY apptask_site.id')
    
    return render(request, 'app/summary.html', {'summary':join})

def summary_average(request):
    # Aggregation obtained with Python
    sites = Site.objects.all()
    average = []
    for site in sites:
    	a = Record.objects.filter(site=site.id).aggregate(Avg('a_record'))
    	b = Record.objects.filter(site=site.id).aggregate(Avg('b_record'))   	
    	avg_site = {'site':site.site_name,'a_value':a,'b_value':b}
    	average.append(avg_site)
    return render(request, 'app/summary_average.html', {'average': average})
