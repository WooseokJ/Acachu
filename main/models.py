from django.db import models

# Create your models here.
class Auth(models.Model):
    auth_id = models.IntegerField(db_column='Auth_id', primary_key=True)  # Field name made lowercase.
    auth_name = models.CharField(db_column='Auth_name', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth'


class AuthBoard(models.Model):
    ab_num = models.IntegerField(db_column='Ab_num', primary_key=True)  # Field name made lowercase.
    ab_title = models.CharField(db_column='Ab_title', max_length=255)  # Field name made lowercase.
    ab_content = models.CharField(db_column='Ab_content', max_length=3000)  # Field name made lowercase.
    ab_reg_date = models.DateTimeField(db_column='Ab_reg_date')  # Field name made lowercase.
    ab_reply_yn = models.IntegerField(db_column='Ab_reply_YN')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_board'


class Bookmark(models.Model):
    bookmark_id = models.IntegerField(db_column='Bookmark_id', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.
    store_id = models.IntegerField(db_column='Store_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookmark'


class Cafepicture(models.Model):
    cafepicture_id = models.IntegerField(db_column='Cafepicture_id', primary_key=True)  # Field name made lowercase.
    store_id = models.IntegerField(db_column='Store_id')  # Field name made lowercase.
    cafepicture_url = models.CharField(db_column='Cafepicture_url', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cafepicture'


class Reply(models.Model):
    reply_id = models.IntegerField(db_column='Reply_id', primary_key=True)  # Field name made lowercase.
    reply_content = models.CharField(db_column='Reply_content', max_length=300)  # Field name made lowercase.
    reply_date = models.DateTimeField(db_column='Reply_date')  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.
    ab_num = models.IntegerField(db_column='Ab_num')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reply'


class Review(models.Model):
    review_id = models.IntegerField(db_column='Review_id', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.
    store_id = models.IntegerField(db_column='Store_id')  # Field name made lowercase.
    review_content = models.CharField(db_column='Review_content', max_length=300)  # Field name made lowercase.
    review_reg_date = models.DateTimeField(db_column='Review_reg_date', blank=True, null=True)  # Field name made lowercase.
    review_mod_date = models.DateTimeField(db_column='Review_mod_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'


class Store(models.Model):
    store_id = models.IntegerField(db_column='Store_id', primary_key=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='Store_name', max_length=50)  # Field name made lowercase.
    store_content = models.CharField(db_column='Store_content', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    store_businesshour = models.CharField(db_column='Store_businesshour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    store_sinum = models.CharField(db_column='Store_sinum', max_length=10)  # Field name made lowercase.
    store_sggnum = models.CharField(db_column='Store_sggnum', max_length=10)  # Field name made lowercase.
    store_emdnum = models.CharField(db_column='Store_emdnum', max_length=10)  # Field name made lowercase.
    store_roadnum = models.CharField(db_column='Store_roadnum', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'


class StoreAuth(models.Model):
    store_auth = models.IntegerField(db_column='Store_Auth', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.
    store_id = models.IntegerField(db_column='Store_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store_auth'


class StoreTag(models.Model):
    store_tag_id = models.IntegerField(db_column='Store_Tag_id', primary_key=True)  # Field name made lowercase.
    store_id = models.IntegerField(db_column='Store_id')  # Field name made lowercase.
    tag_id = models.IntegerField(db_column='Tag_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store_tag'


class Tag(models.Model):
    tag_id = models.IntegerField(db_column='Tag_id', primary_key=True)  # Field name made lowercase.
    tag_name = models.CharField(db_column='Tag_name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tag'


class User(models.Model):
    user_num = models.IntegerField(db_column='User_num', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_id', max_length=20)  # Field name made lowercase.
    user_password = models.CharField(db_column='User_password', max_length=20)  # Field name made lowercase.
    user_nickname = models.CharField(db_column='User_nickname', max_length=20)  # Field name made lowercase.
    user_email = models.CharField(db_column='User_email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_profileurl = models.CharField(db_column='User_profileurl', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    auth_id = models.IntegerField(db_column='Auth_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'