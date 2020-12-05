from . models import Notification


def create_notification(request, recipient, which, identifier=0):
    Notification.objects.create(
        recipient=recipient,
        which=which,
        creator=request.user,
        identifier=identifier
    )
