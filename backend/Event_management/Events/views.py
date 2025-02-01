from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Event, Registration, Wishlist, User
from .serializers import EventSerializer, RegistrationSerializer, WishlistSerializer, UserSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "Attendee")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    user.role = role
    user.save()
    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def register_for_event(request, id):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    if event.registered_count() >= event.capacity:
        return Response({"error": "Event is full"}, status=status.HTTP_400_BAD_REQUEST)

    registration, created = Registration.objects.get_or_create(user=request.user, event=event)
    if not created:
        return Response({"message": "Already registered for this event"}, status=status.HTTP_200_OK)

    return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_wishlist(request, id):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    wishlist, created = Wishlist.objects.get_or_create(user=request.user, event=event)
    if not created:
        return Response({"message": "Event already in wishlist"}, status=status.HTTP_200_OK)

    return Response({"message": "Event added to wishlist"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view_wishlist(request):
    wishlist = request.user.wishlist.all()
    data = WishlistSerializer(wishlist, many=True).data
    return Response(data)
