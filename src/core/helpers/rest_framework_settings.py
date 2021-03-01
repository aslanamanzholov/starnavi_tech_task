from types import MappingProxyType


REST_FRAMEWORK_SETTINGS: MappingProxyType = MappingProxyType({
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ), 'DEFAULT_FILTER_BACKENDS': (),
})
