from django.db import models
from django.contrib.auth.models import User

# Create your models here.

NEWS_TYPE = [
    ('NWS', 'Новость'),
    ('ART', 'Статья')
]

class Author(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating():
        articles = sum(Articles.objects.filter(author_id=self.id).values('rating'))*3
        comments = sum(Comments.objects.filter(user_id=self.id).values('rating'))
        art_comments = 0
        for id in Articles.objects.filter(author_id=self.id).values('id'):
            art_comments += sum(Comments.objects.filter(art_id=id))
        total = articles + comments + art_comments
        return total

class Category(models.Model):
    category = models.CharField(max_length = 64, unique=True )

class Articles(models.Model):
    category = models.ManyToManyField(Category, through = PostCategory)
    type = models.CharField(max_length = 3, choices=NEWS_TYPE, default = 'NWS' )
    header = models.CharField(max_length = 255)
    text = models.TextField(max_length = 15000)
    rating = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add)
    author_id = models.ForeignKey(Author)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save() 

    def preview(self):
        text = self.text[0,124] + '...'
        return text


class PostCategory(models.Model):
    art_cat = models.ForeignKey(Category, on_delete = models.CASCADE)
    art_id = models.ForeignKey(Articles, on_delete = models.CASCADE)

class Comments(models.Model):
    text = models.TextField(max_length = 5000)
    rating = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add)
    art_id = models.ForeignKey(Articles)
    user_id = models.ForeignKey(User)

    def like(self):
        self.rating += 1
        self.save() 

    def dislike(self):
        self.rating -= 1
        self.save()