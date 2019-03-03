from pyramid.security import Allow, DENY_ALL, ALL_PERMISSIONS


class RootFactory:

    def __acl__(self):
        return [(Allow, 'bar', 'WHAT_EVER_YOU_LIKE'),
                (Allow, 'group:users', 'WHAT_EVER_YOU_LIKE'),
                (Allow, 'admin', ALL_PERMISSIONS),
                DENY_ALL]

    def __init__(self, request):
        pass
