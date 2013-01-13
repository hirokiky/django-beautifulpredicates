from django.test import TestCase, RequestFactory
from django.http import HttpResponse

from beautifulpredicates.views import PredicateProcessView

def simple_head_predicate(request, dispatch_flag_trio):
    return dispatch_flag_trio[0]

def simple_body_predicate(request, dispatch_flag_trio):
    return dispatch_flag_trio[1]

def simple_tail_predicate(request, dispatch_flag_trio):
    return dispatch_flag_trio[2]

class SimplePredicateProcessView(PredicateProcessView):
    dispatch_config = (
                          ('get_first', (simple_head_predicate, simple_tail_predicate)),
                          ('get_second', (simple_body_predicate, simple_tail_predicate)),
                      )

    def get_first(self, request, *args, **kwargs):
        return HttpResponse('This is a get first')

    def get_second(self, request, *args, **kwargs):
        return HttpResponse('This is a get second')

    def get_default(self, request, *args, **kwargs):
        return HttpResponse('This is a get default')


class PredicateProcessViewTest(TestCase):
    rf = RequestFactory()

    def test_get(self):
        request = self.rf.get('/', REQUEST_METHOD='GET')
        for pair in (
                        (b'first', (True, True, True)),
                        (b'first', (True, False, True)),
                        (b'second', (False, True, True)),
                        (b'default', (False, False, True)),
                        (b'default', (False, False, False)),
                    ):
            name, conditions = pair
            response = SimplePredicateProcessView.as_view()(request, conditions)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content, b'This is a get ' + name)
