from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category', null=True, default=None, on_delete=models.PROTECT)

    @property
    def news(self):
        return News.objects.filter(categori=self)

    @property
    def has_child(self):
        return Category.objects.filter(parent=self).exists()

    @property
    def childs(self):
        return Category.objects.filter(parent=self).order_by('id')



class Avtor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)

    @property
    def name(self):
        return (self.last_name, self.first_name)

    def __repr__(self):
        return f"{self.last_name} {self.first_name}"

class Tags(models.Model):
    tags = models.CharField(max_length=100)

    @property
    def teg_news(self):
        return News.objects.filter(tags=self)



class News(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    categori = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tags)
    author = models.ForeignKey(Avtor,default=None, on_delete=models.CASCADE)










