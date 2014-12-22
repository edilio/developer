from django.db import models
from django.utils.translation import gettext_lazy as _


class Technology(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = _("Technologies")

    def __unicode__(self):
        return self.name


class DevModule(models.Model):
    name = models.CharField(max_length=20)
    PH = models.BooleanField(default=False)
    S8 = models.BooleanField(default=False)
    PBS8 = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _('Modules')

    @property
    def submodules(self):
        subs = [s.name for s in self.submodule_set.all()]
        return ','.join(subs)

    def __unicode__(self):
        return self.name


class SubModule(models.Model):
    name = models.CharField(max_length=20, verbose_name='Sub-Module')
    dev_module = models.ForeignKey(DevModule,db_column=u'module_id',verbose_name='Module')
    PH = models.BooleanField(default=False)
    S8 = models.BooleanField(default=False)
    PBS8 = models.BooleanField(default=False)
    technology = models.ForeignKey(Technology)

    def __unicode__(self):
        return self.name