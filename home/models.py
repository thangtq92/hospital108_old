from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import date
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Menu(models.Model):
    # id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField()
    prior = models.SmallIntegerField(blank=True, null=True)
    id_parent = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.code = self.slug
        super(Menu, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('list-menus', kwargs={})




from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import date
from django.utils.text import slugify

# Create your models here.
class Categories(models.Model):
    code = models.CharField(max_length=100, verbose_name=_('Code'))
    name_vi = models.CharField(max_length=255, blank=True, verbose_name=_('Name_vi'))
    name_en = models.CharField(max_length=255, blank=True, verbose_name=_('Name_en'))
    unit = models.CharField(max_length=100, blank=True, verbose_name=_('Unit'))
    min_value = models.FloatField(blank=True, null=True, verbose_name=_('Min_value'))
    max_value = models.FloatField(blank=True, null=True, verbose_name=_('Max_value'))
    string_value = models.CharField(blank=True, max_length=100, verbose_name=_('String value'))
    sort_order = models.PositiveSmallIntegerField(default=1, blank=True, verbose_name=_('Sort order'))
    type = models.BooleanField(default=0, blank=True, verbose_name=_('Type'))
    status = models.BooleanField(default=0, blank=True, verbose_name=_('Status'))
    is_number = models.BooleanField(default=0, blank=True, verbose_name=_('Is Number'))
    id_parent = models.ForeignKey("self", verbose_name=_('Parent category'),
                                  null=True, blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.code


    @staticmethod
    def extra_filters(obj):
        if not obj.id_parent:
            return {'id_parent__isnull': True}
        return {'id_parent': obj.id_parent}


    def save(self, *args, **kwargs):
        if self.id_parent is not None:
            Categories.objects.filter(id_parent=self.id).update(id_parent=None)

        if not self.id:
            try:
                filters = self.__class__.extra_filters(self)
                self.sort_order = self.__class__.objects.filter(
                    **filters
                ).order_by("-sort_order")[0].sort_order + 10
            except IndexError:
                self.sort_order = 0

        super(Categories, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['sort_order']




