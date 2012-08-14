from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from admin_tools.dashboard import modules, Dashboard


# Create your models here.
class MyDashboard(Dashboard):
    columns = 3
    def __init__(self,**kwargs):
	    self.children.append(modules.AppList(
            title = _('Applications'),
			exclude=('django.contrib.*',),
        ))
'''
        self.children.append(modules.AppList(
            title=_('Adminstration'),
            models=('django.contrib.*,',),
		))

        self.children.append(modules,RecentActions(
		    title=_('Recent Actions'),
			limit=10
		))
'''		
		
