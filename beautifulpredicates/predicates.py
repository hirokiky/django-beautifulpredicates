class RequestParamPredicate(object):
    def __init__(self, val):
        k = val
        v = None
        if '=' in val:
            k, v = val.split('=', 1)
            k, v = k.strip(), v.strip()
        self.k = k
        self.v = v

    def __call__(self, request, *args, **kwargs):
        params = getattr(request, request.method)
        actual = params.get(self.k)
        if actual is None:
            return False
        if self.v is not None and actual != self.v:
            return False
        return True
