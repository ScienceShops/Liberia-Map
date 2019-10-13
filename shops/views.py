from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from shops import forms
from shops import models


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            safe=False,
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class MapTemplateView(TemplateView):
    template_name = 'shops/index.html'


class PointListView(JSONResponseMixin, ListView):
    """
    Return JSON array of points. One point for each shop.


        [
          {
            "type": "Feature",
            "properties": {
              "Shop Name": "1",
              "Items": [],
            },
            "geometry": {
              "type": "Point",
              "coordinates": [
                -9.9376387894872,
                6.814259060308
              ]
            }
          }
        ]
    """
    model = models.Shop

    def get_data(self, context):
        object_list = context.get('object_list')
        return [obj.to_dict() for obj in object_list]


class NewShopFormView(FormView):
    template_name = 'shops/new_shop.html'
    form_class = forms.NewShopForm
    success_url = '/'
