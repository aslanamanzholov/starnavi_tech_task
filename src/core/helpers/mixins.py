from rest_framework import exceptions


class ActionSerializerViewSetMixin(object):
    """
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('list', ): MyModelListViewSerializer,
        ('create', 'update'): MyModelCreateUpdateSerializer
    }
    """
    serializer_classes = None

    def get_serializer_class(self):
        assert self.serializer_classes is not None, (
                'Expected viewset %s should contain serializer_classes '
                'to get right serializer class.' %
                (self.__class__.__name__,)
        )
        for actions, serializer_cls in self.serializer_classes.items():
            if self.action in actions:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)


class ActionPermissionViewSetMixin(object):
    """
    Utility class for get different permission class by method.
    For example:
    method_permission_classes = {
        ('list', ): [AllonAny],
        ('create', 'update'): [IsOwner],
    }
    """
    permission_classes = None

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        assert self.permission_classes is not None, (
                'Expected viewset %s should contain serializer_classes '
                'to get right serializer class.' %
                (self.__class__.__name__,)
        )
        for actions, permission_classses in self.permission_classes.items():
            if self.action in actions:
                return [permission() for permission in permission_classses]

        raise exceptions.MethodNotAllowed(self.request.method)
