from django import template
from gym.views import get_related_to
from gym.models import UserProfile

register = template.Library()


@register.simple_tag
def friend_request(request):
    """
    Templatetag to obtain the requests in a template
    """
    actual_user = UserProfile.objects.get(pk=11)
    requests = get_related_to(actual_user, 1)
    return requests
