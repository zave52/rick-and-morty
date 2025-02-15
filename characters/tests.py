from django.test import TestCase

from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from characters.models import Character
from characters.views import get_random_character


def sample_character(**params: dict) -> Character:
    defaults = {
        "api_id": 1,
        "name": "test",
        "status": "unknown",
        "species": "test",
        "gender": "unknown",
        "image": "test_path"
    }
    defaults.update(params)
    return Character.objects.create(**defaults)


class CharacterApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.character = sample_character()

    @patch(
        "random.choice",
        return_value=1
    )
    def test_get_random_character(self, mock_function) -> None:
        character = get_random_character()
        self.assertEqual(character, Character.objects.get(pk=mock_function()))

    def test_get_random_character_view(self) -> None:
        response = self.client.get(reverse("characters:character-random"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["api_id"], self.character.api_id)
        self.assertEqual(response.data["name"], self.character.name)
        self.assertEqual(response.data["status"], self.character.status)
        self.assertEqual(response.data["species"], self.character.species)
        self.assertEqual(response.data["gender"], self.character.gender)
        self.assertEqual(response.data["image"], self.character.image)
