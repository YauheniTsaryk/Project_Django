from django.db import models
from django.urls import reverse


# Create your models here.
class Catalogue(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Title")
    content = models.TextField(blank=True, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update date")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('view_catalogue', kwargs={"catalogue_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Catalogue"
        verbose_name_plural = "Catalogues"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Category title')

    def get_absolute_url(self):
        return reverse('category', kwargs={
            "category_id": self.pk})
# создание маршрута, через передачу вторичного ключа "self.pk" Функция reverse является аналогом функции url в html документах.

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

# class Book_categories(models.TextChoices):
#     Arts & Photography
#     Mystery, Thrillers, & Crime
#     Biography & Memoir
#     Nonfiction
#     Business & Investing
#     Poetry
#     Children
#     Romance
#     Comics & Graphic
#     Novels
#     Science
#     Fiction
#     Cooking & Wine
#     Science & Technology
#     Fantasy
#     Self
#     Development & Hobbies
#     History
#     Language
#     Horror
#     Spirituality & Religion
#     Humor & Games
#     Teen & Young
#     Adult
#     Literature & Fiction
#     Travel
#     Historical
#     Fiction
#     Manga
