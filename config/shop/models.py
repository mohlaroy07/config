from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi", unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="categories/photos/", null=True, blank=True, verbose_name="Rasmi")
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Kategoriya")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ('pk',)


QUALITY = [
    ('or', 'organic'),
    ('gmo', 'GMO'),
]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Mahsulot nomi")
    slug = models.SlugField(max_length=160, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="Mahsulot haqida...")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Narxi")
    discount = models.IntegerField(null=True, blank=True, verbose_name="Chegirma (%)")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Ombordagi soni")
    weight = models.PositiveIntegerField(verbose_name="Vazni")
    made_in = models.CharField(max_length=100, verbose_name="Yetishtirilgan")
    quality = models.CharField(max_length=3, choices=QUALITY, verbose_name="Sifati")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ('-pk',)