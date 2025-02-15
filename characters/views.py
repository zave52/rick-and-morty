import random

from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpRequest, HttpResponse
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from characters.models import Character
from characters.serializers import CharacterSerializer


def get_random_character() -> Character:
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    return Character.objects.get(pk=random_pk)


@extend_schema(responses={status.HTTP_200_OK, CharacterSerializer})
@api_view(["GET"])
def get_random_character_view(request: HttpRequest) -> HttpResponse:
    """Get random character from Rick & Morty world."""
    random_character = get_random_character()
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "name": ["icontains"]
    }

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name__icontains",
                type=OpenApiTypes.STR,
                description="Filter by name insensitive contains",
                required=False,
            )
        ]
    )
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """List characters with filter by name."""
        return super().get(request, *args, **kwargs)
