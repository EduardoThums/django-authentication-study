from django.core.cache import cache
from django.utils.functional import SimpleLazyObject
from pokedex import models
from django.conf import settings


def cache_trainer(request):
    if not request.user.is_authenticated:
        return

    user_id = request.user.id

    trainer_key = f'{settings.TRAINER_CACHE_PREFIX}/{user_id}'

    trainer = cache.get_or_set(
        trainer_key,
        models.Trainer.objects.filter(user_id=user_id).first,
        settings.TRAINER_CACHE_TTL
    )

    user_trainer = request.user
    user_trainer.trainer = trainer

    return user_trainer


class TrainerCacheMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user_trainer = SimpleLazyObject(lambda: cache_trainer(request))

        response = self.get_response(request)

        return response
