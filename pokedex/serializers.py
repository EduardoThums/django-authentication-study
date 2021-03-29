from abc import ABC

from dj_rest_auth.registration.serializers import RegisterSerializer

from pokedex import models


class TrainerRegistrationSerializer(RegisterSerializer):

    def save(self, request):
        user = super(TrainerRegistrationSerializer, self).save(request)

        models.Trainer(user=user).save()

        return user

    def update(self, instance, validated_data):
        super(TrainerRegistrationSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        super(TrainerRegistrationSerializer, self).create(validated_data)
