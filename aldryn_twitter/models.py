# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class TwitterPlugin(CMSPlugin):

    widget_id = models.CharField(_('Widget ID'), max_length=75)
    href = models.CharField(_('Link Location'), max_length=75, blank=True,
                            help_text=_('Fallback link location. Displayed when Twitter is not able to display the widget.'))
    link_title = models.CharField(_('Link Title'), max_length=75, blank=True,
                                  help_text=_('Fallback link title. Displayed when Twitter is not able to display the widget.'))

    def __unicode__(self):
        return self.widget_id
