from django.contrib import admin
from .models import Place, Image
from django.utils.html import mark_safe, format_html

# admin.site.register(Image)
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

class ImageInline(admin.TabularInline):
    readonly_fields = ('get_preview',)
    fields = ('image', 'get_preview', 'order')
    
    def get_preview(self, obj):
        return format_html('<img src="{url}" height={height} />'.format(
            url = obj.image.url,
            height=200,
            )
        )
    
    get_preview.short_description = 'preview'
    model = Image
    
    
    


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

