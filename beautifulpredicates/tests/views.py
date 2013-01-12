from django.test import TestCase, RequestFactory
from django.http import HttpResponse

from beautifulpredicates.views import PredicateProcessView

def simple_head_predicate(request, dispatch_flag_pair):
    return dispatch_flag_pair[0]

def simple_tail_predicate(request, dispatch_flag_pair):
    return dispatch_flag_pair[1]

class SimplePredicateProcessView(PredicateProcessView):
    dispatch_config = {'get_simple': (simple_head_predicate, simple_tail_predicate)}

    def get_simple(self, request, *args, **kwargs):
        return HttpResponse('This is a get simple')

    def get_default(self, request, *args, **kwargs):
        return HttpResponse('This is a get default')


class PredicateProcessViewTest(TestCase):
    rf = RequestFactory()

    def test_get(self):
        request = self.rf.get('/', REQUEST_METHOD='GET')

        response = SimplePredicateProcessView.as_view()(request, (True, True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'This is a get simple')

        response = SimplePredicateProcessView.as_view()(request, (True, False))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'This is a get default')

        response = SimplePredicateProcessView.as_view()(request, (False, False))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'This is a get default')
