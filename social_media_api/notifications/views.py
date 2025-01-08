from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all()
        data = [
            {
                "id": n.id,
                "actor": n.actor.username,
                "verb": n.verb,
                "target": str(n.target),
                "timestamp": n.timestamp,
                "read": n.read
            }
            for n in notifications
        ]
        return Response(data)

class MarkNotificationReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        notification = Notification.objects.filter(pk=pk, recipient=request.user).first()
        if notification:
            notification.read = True
            notification.save()
            return Response({"message": "Notification marked as read"})
        return Response({"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND)
