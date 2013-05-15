# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from aldryn_twitter import models


class TwitterPlugin(CMSPluginBase):

    render_template = 'aldryn_twitter/twitter.html'
    name = _('Twitter')
    model = models.TwitterPlugin
    module = _('Social')

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(TwitterPlugin)
