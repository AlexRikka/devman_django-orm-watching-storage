def format_duration(duration):
    seconds = duration.total_seconds()
    duration_formatted = '{hour}ч {minute}мин'.format(
        hour=int(seconds // 3600),
        minute=int((seconds % 3600) // 60))
    return duration_formatted


def format_timestamp(timestamp):
    timestamp_formatted = timestamp.strftime('%d %b %Y г. %H:%M')
    return timestamp_formatted
