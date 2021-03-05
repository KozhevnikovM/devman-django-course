from django.contrib import admin
from .models import Place, Image
from django.utils.html import mark_safe, format_html
from adminsortable2.admin import SortableInlineAdminMixin

# admin.site.register(Image)
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    readonly_fields = ('get_preview',)
    fields = ('name', 'get_preview', 'order')

    def get_preview(self, obj):
        return format_html('<img src="{url}" height={height} />'.format(
            url = obj.image.url,
            height=200,
            )
        )
    
    get_preview.short_description = 'preview'
    extra = 1
    model = Image
    
    
    


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

