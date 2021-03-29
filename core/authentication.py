from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.settings import api_settings
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class HeaderJWTAuthentication(JWTAuthentication):

    def get_user(self, validated_token):
        """
        Override implementation of JWTAuthentication.get_user. The idea is instead of retrieve the user
        every time from the database, use Redis's cache to avoid overload the database with trivial queries.
        The downside of this flow is the inconsistency between what is in the database and what is in the cache,
        hopefully a hook can be implemented using the Django's signals, to update the cached user every time he is
        updated in the database.
        """
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken(_('Token contained no recognizable user identification'))

        user = cache.get(f'{settings.USER_CACHE_PREFIX}/{user_id}')

        if user is None:
            try:
                user = User.objects.get(**{api_settings.USER_ID_FIELD: user_id})
            except User.DoesNotExist:
                raise AuthenticationFailed(_('User not found'), code='user_not_found')

            else:
                cache.set(f'user/{user_id}', user, settings.USER_CACHE_TTL)

        if not user.is_active:
            raise AuthenticationFailed(_('User is inactive'), code='user_inactive')

        return user
