from django.contrib import admin
from .models import Menu, Categories

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'prior', 'id_parent')


admin.site.register(Menu, MenuAdmin)


# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('code', 'id_parent', 'status', 'sort_order')
    search_fields = ['code', ]
    none_type = type(None)

    def get_form(self, request, obj=None, **kwargs):
        request.obj = obj

        if isinstance(obj, self.none_type) is True:
            self.exclude = ("sort_order",)
        else:
            self.exclude = None

        return super(CategoriesAdmin, self).get_form(request, obj, **kwargs)
