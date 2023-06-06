from django.db import models

from django.core.validators import MinValueValidator
from django.utils import timezone

from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


# from django.utils import timezone
# from django.utils.translation import gettext as _
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,null=True)
    
    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    
    def __str__(self):
        return self.name
    


class SiteUser(AbstractUser):
    money = models.PositiveIntegerField(default=0)
    
    # def save(self, **kwargs):
    #     self.money = 10000
    #     super().save(**kwargs)


class Product(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True)
    content = models.TextField(max_length=10000, null=True)
    img_url = models.ImageField()
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    # slug = models.SlugField(max_length=50, null=True, unique=True, db_index=True)
    slug = models.SlugField(unique=True)
    
    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super().save(**kwargs)
    
    def __str__(self):
        return "Title: {}; quantity: {}; price:{}".format(self.title, self.quantity, self.price)


class Buy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, related_name='buy_product')
    site_user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=False, related_name='buy_users')
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    summ = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.created_at = timezone.now()
    #     return super().save(*args, **kwargs)
    
    def __str__(self):
        return "product: {}; siteUser: {}; quantity:{}".format(self.product, self.site_user, self.quantity)


class ReturnConfirmation(models.Model):
    buy = models.OneToOneField(Buy, on_delete=models.CASCADE, null=False, related_name='returns_buys')
    site_user = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=False, related_name='return_users')
    created_at = models.DateTimeField(default=timezone.now)
    
    # def save(self, **kwargs):
    #     self.created_at = timezone.now()
    #     super().save(**kwargs)
    
    def __str__(self):
        return "buy: {}; created_at:{}".format(self.buy, self.created_at)
    
    # если подтвержден возврат то удалить покупку, вернуть количество товару, удалить возрват
    # если отклонен возврат то удалить обьект возврата



