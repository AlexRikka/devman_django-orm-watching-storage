from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.time_formatter import format_timestamp, format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        if visit.leaved_at is None:
            continue
        
        duration = visit.leaved_at - visit.entered_at
        is_strange_flag = visit.is_visit_long()
        
        visit_dict = {
            'entered_at': format_timestamp(visit.created_at),
            'duration': format_duration(duration),
            'is_strange': is_strange_flag
        }
        this_passcard_visits.append(visit_dict)
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
