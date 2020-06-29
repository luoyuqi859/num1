from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 用户信息
class UserInfo(models.Model):
    headImg = models.ImageField()
    nickName = models.CharField()
    belong = models.OneToOneField(User)

    def __int_(self):
        return self.id


# 文章分类
class Category(models.Model):
    name = models.CharField()
    belong = models.ForeignKey(self)

    def __int_(self):
        return self.id


# 文章
class Artical(models.Model):
    title = models.CharField()
    cover = models.CharField()
    text = models.TextField()
    belog = models.ForeignKey(UserInfo)

    def __int_(self):
        return self.id

# 收藏
class Favorite(models.Model):
    belong_user = models.ForeignKey(UserInfo)
    belong_artical = models.ForeignKey(Artical)

    def __int_(self):
        return self.id

# 点赞
class Like(models.Model):
    belong_user = models.ForeignKey(UserInfo)
    belong_artical = models.ForeignKey(Artical)
    num = models.IntegerField()


    def __int_(self):
        return self.id

# 打赏
class PayOrder(models.Model):
    order = models.CharField()
    price = models.CharField()
    status = models.BooleanField()

    def __int_(self):
        return self.id

