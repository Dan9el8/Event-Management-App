from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, register_user, register_for_event, add_to_wishlist, view_wishlist

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="events")

urlpatterns = [
    path("auth/register/", register_user, name="register_user"),
    path("events/<int:id>/register/", register_for_event, name="register_for_event"),
    path("events/<int:id>/wishlist/", add_to_wishlist, name="add_to_wishlist"),
    path("wishlist/", view_wishlist, name="view_wishlist"),
    path("", include(router.urls)),
]
