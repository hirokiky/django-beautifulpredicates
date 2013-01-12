from django.views.generic import View


class PredicateProcessView(View):
    dispatch_config = {}
    def get(self, request, *args, **kwargs):
        handler = getattr(self, 'get_default', self.http_method_not_allowed)

        for custom_receiver, predicaties in self.dispatch_config.items():
            for predicate in predicaties:
                if not predicate(request, *args, **kwargs):
                    break
            else:
                handler = getattr(self, custom_receiver)

        return handler(request, *args, **kwargs)
