from PIL import Image
from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe
from .models import *


class NotebookAdminForm(ModelForm):
    """Проверка загружаемого изображения на соответствие минимальному и максимальному разрешению"""
    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (1200, 1200)
    MAX_IMAGE_SIZE = 3145728

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe('<span style="color:red; font-size:14px;">Загружайте изображения с '
                                                   'минимальным разрешением {}x{}</span>'.format(*self.MIN_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if image.size > self.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3МБ!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Разрешение изображения больше максимального')
        return image


class NotebookAdmin(admin.ModelAdmin):

    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
