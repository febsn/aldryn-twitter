# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class TwitterPlugin(CMSPlugin):

    THEMES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    POLITENESS = [
        ('polite', 'Polite'),
        ('assertive', 'Assertive'),
    ]

    widget_id = models.CharField(_('Widget ID'), max_length=75)
    href = models.CharField(_('Link Location'), max_length=75, blank=True,
                            help_text=_('Fallback link location. '
                                        'The link is isplayed when Twitter is not able to display the widget. '
                                        '(e.g. "https://twitter.com/_username_")'))
    link_title = models.CharField(_('Link Title'), max_length=75, blank=True,
                                  help_text=_('Fallback link title. '
                                              'The link is displayed when Twitter is not able to display the widget. '
                                              '(e.g. "See my tweets!")'))

    theme = models.CharField(_('Theme'), max_length=5, choices=THEMES, default=THEMES[0][0])
    link_color = models.CharField(_('Link Color'), max_length=6, blank=True, help_text=_('The color to display the links in.'))
    border_color = models.CharField(_('Border Color'), max_length=6, blank=True, help_text=_('The color to display the borders in.'))
    width = models.PositiveIntegerField(_('Widgth'), blank=True, null=True, help_text=_('In pixels.'))
    height = models.PositiveIntegerField(_('Height'), blank=True, null=True, help_text=_('In pixels.'))
    header = models.BooleanField(_('Header'), default=True)
    footer = models.BooleanField(_('Footer'), default=True)
    borders = models.BooleanField(_('Borders'), default=True)
    scrollbar = models.BooleanField(_('Scrollbar'), default=True)
    transparent = models.BooleanField(_('Transparent Background'), default=False)
    language_code = models.CharField(max_length=10, blank=True, help_text=_('Language in which display the time-line.'))
    tweet_limit = models.PositiveIntegerField(blank=True, null=True, help_text=_('How many tweets to display in the time-line.'))
    related_users = models.TextField(blank=True,
                                     help_text=_('Comma-separated list of users you want to suggest the user to follow '
                                                 'after he has taken an action in the timeline '
                                                 '(e.g. "user_1,user_2").'))
    aria_politeness = models.CharField(max_length=9, choices=POLITENESS, default=POLITENESS[0][0],
                                       help_text=_('ARIA is an accessibility system that aids people using assistive '
                                                   'technology interacting with dynamic web content.'))

    def __unicode__(self):
        return self.widget_id
