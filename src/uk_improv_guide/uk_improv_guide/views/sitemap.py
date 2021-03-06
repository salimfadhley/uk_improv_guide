import itertools

from django.shortcuts import render
from uk_improv_guide.models.event import get_all_events
from uk_improv_guide.models.performer import get_all_performers
from uk_improv_guide.models.school import get_all_schools
from uk_improv_guide.models.team import get_all_teams


def robots_txt(request):
    return render(request, "robots.txt", content_type="text/plain")


def sitemap(request):
    everything = itertools.chain(
        get_all_schools(),
        get_all_teams(),
        get_all_events(),
        get_all_performers(),
        get_all_teams(),
    )

    objects = [o.sitemap_url_data(request) for o in everything]

    return render(
        request, "sitemap.html", {"objects": objects}, content_type="application/xml"
    )
