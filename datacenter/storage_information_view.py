from datacenter.models import Visit
from django.shortcuts import render
from datacenter.time_formatter import format_timestamp, format_duration
import locale
locale.setlocale(locale.LC_ALL, "ru")


def storage_information_view(request):
    non_closed_visits = []
    current_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in current_visits:
        duration = visit.get_duration()
        entered_at = format_timestamp(visit.created_at)
        visit_dict = {
                'who_entered': visit.passcard.owner_name,
                'entered_at': entered_at,
                'duration': format_duration(duration),
                }
        non_closed_visits.append(visit_dict)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
