from django.conf import settings
from django.contrib import messages
from gym.views import get_only_requests
from gym.models import UserProfile


def friend_request(request):
    actual_user = ''
    requests = ''
    friends = ''
    friends_list = []
    try:
        if not request.user.is_anonymous:
            actual_user = UserProfile.objects.get(
                pk=request.user.userprofile.pk)
            requests = get_only_requests(
                actual_user, 1)
            friends = actual_user.followers.filter(
                to_people__status=settings.RELATIONSHIP_FOLLOWING,
                to_people__from_person=actual_user,
                from_people__status=settings.RELATIONSHIP_BLOCKED,
                from_people__to_person=actual_user)
        for x in requests:
            friends_list.append(x)
        for x in friends_list:
            if x in friends:
                friends_list.remove(x)
    except UserProfile.DoesNotExist:
        actual_user = ''
        requests = ''
        friends = ''

    return {
        'requests': friends_list,
        'friends': friends,
    }
