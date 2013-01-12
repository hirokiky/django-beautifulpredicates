from django.views.generic import View


class PredicateProcessView(View):
    dispatch_config = {}
    def get(self, request, *args, **kwargs):
        self.dispatch_config

        for custom_receiver, predicate in self.dispatch_config.items():
            if predicate(request, *args, **kwargs):
                handler = getattr(self, custom_receiver)
                break
        else:
            handler = getattr(self, 'get_default', self.http_method_not_allowed)

        return handler(request, *args, **kwargs)
