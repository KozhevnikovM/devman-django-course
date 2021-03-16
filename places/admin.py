from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)
    autocomplete_fields = ['place']


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    readonly_fields = ('get_preview',)
    fields = ('image', 'get_preview', 'order')

    def get_preview(self, obj):
        if not obj.__str__():
            return format_html('Здесь будет превью, когда вы выберете файл')
        return format_html(
            '<img src="{}" style="max-height: {}px; max-width: {}px;"/>',
            obj.image.url,
            200,
            200
            )

    get_preview.short_description = 'preview'
    extra = 1
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    search_fields = ('title',)
