from django.views.generic.base import TemplateView


class MapTemplateView(TemplateView):
    template_name = 'shops/index.html'
