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
    change_form_template = 'aldryn_twitter/admin/twitter_change_form.html'

    fieldsets = [
        (
            None,
            {'fields': ['widget_id', 'href', 'link_title']}
        ),
        (
            _('Display customization options'),
            {'fields': [
                'theme',
                'link_color',
                'border_color',
                'width',
                'height',
                'header',
                'footer',
                'borders',
                'scrollbar',
                'transparent',
                'language_code',
                'tweet_limit',
                'related_users',
                'aria_politeness',
            ]}
        )
    ]

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(TwitterPlugin)
