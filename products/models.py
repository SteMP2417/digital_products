from django.db import models
from django.utils.translation import gettext_lazy as _
class category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class  Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    categories = models.ManyToManyField('category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
class File(models.Model):
    product = models.ForeignKey('product', verbose_name=_('product'), on_delete=models.CASCADE)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
    title = models.CharField(_('title'), max_length=50)
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')