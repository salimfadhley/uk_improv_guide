from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models import Team
from uk_improv_guide.models.performer import (
    Performer,
    get_performer_by_id,
)

def performer(request, id: int):
    this_performer: Performer = get_performer_by_id(id)
    teams: Sequence[Team] = []

    return render(
        request,
        "performer.html",
        {
            "title": f"{this_performer.full_name()}",
            "performer": this_performer,
            "teams": teams,
        },
    )
