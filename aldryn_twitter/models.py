# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class TwitterPlugin(CMSPlugin):

    title = models.CharField(_('Title'), max_length=75, blank=True)
    username = models.CharField(_('Username'), max_length=50, blank=True,
                                help_text=_('If the username is given the twitter box will be personalized.'))
    query = models.CharField(_('Query'), max_length=200, blank=True, default='',
                             help_text=_('Example: "from:romeo AND to:julia AND thou": tweets from the user "romeo" to '
                                         'the user "julia" that contain the word "thou".'))
    count = models.PositiveSmallIntegerField(_('Count'), help_text=_('Number of entries to display.'), default=3)

    def __unicode__(self):
        return self.title or self.username or str(self.count)
