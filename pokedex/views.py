from rest_framework import viewsets, permissions
from rest_framework.response import Response


class PokedexViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        data = {
            'pokemons': [
                {
                    'name': 'Charizard',
                    'type': 'fire'
                },
                {
                    'name': 'Bulbassar',
                    'type': 'grass'
                }
            ]
        }

        self.request.user.id

        return Response(data=data)
