from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Auth(models.Model):
    auth_id = models.AutoField(db_column='Auth_id', primary_key=True)  # Field name made lowercase.
    auth_name = models.CharField(db_column='Auth_name', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'auth'

class User(models.Model):
    user_id = models.AutoField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_account', max_length=20)  # Field name made lowercase.
    user_password = models.CharField(db_column='User_password', max_length=20)  # Field name made lowercase.
    user_nickname = models.CharField(db_column='User_nickname', max_length=20)  # Field name made lowercase.
    user_email = models.CharField(db_column='User_email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_profileurl = models.CharField(db_column='User_profileurl', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'

class Store(models.Model):
    store_id = models.AutoField(db_column='Store_id', primary_key=True)  # Field name made lowercase.
    store_name = models.CharField(db_column='Store_name', max_length=50)  # Field name made lowercase.
    store_content = models.CharField(db_column='Store_content', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    store_businesshour = models.CharField(db_column='Store_businesshour', max_length=50, blank=True, null=True)  # Field name made lowercase.
    store_sinum = models.CharField(db_column='Store_sinum', max_length=10)  # Field name made lowercase.
    store_sggnum = models.CharField(db_column='Store_sggnum', max_length=10)  # Field name made lowercase.
    store_emdnum = models.CharField(db_column='Store_emdnum', max_length=10)  # Field name made lowercase.
    store_roadnum = models.CharField(db_column='Store_roadnum', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'store'
        

class AuthBoard(models.Model):
    ab_id = models.AutoField(db_column='Ab_id', primary_key=True)  # Field name made lowercase.
    ab_title = models.CharField(db_column='Ab_title', max_length=255)  # Field name made lowercase.
    ab_content = models.CharField(db_column='Ab_content', max_length=3000)  # Field name made lowercase.
    ab_reg_date = models.DateTimeField(db_column='Ab_reg_date')  # Field name made lowercase.
    ab_reply_yn = models.IntegerField(db_column='Ab_reply_YN')  # Field name made lowercase.
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'auth_board'

class Cafepicture(models.Model):
    cafepicture_id = models.AutoField(db_column='Cafepicture_id', primary_key=True)  # Field name made lowercase.
    cafepicture_url = models.CharField(db_column='Cafepicture_url', max_length=1000)  # Field name made lowercase.
    
    store = models.ForeignKey(Store, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cafepicture'


class Reply(models.Model):
    reply_id = models.AutoField(db_column='Reply_id', primary_key=True)  # Field name made lowercase.
    reply_content = models.CharField(db_column='Reply_content', max_length=300)  # Field name made lowercase.
    reply_date = models.DateTimeField(db_column='Reply_date')  # Field name made lowercase.
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    authboard = models.ForeignKey(AuthBoard, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reply'


class Review(models.Model):
    review_id = models.AutoField(db_column='Review_id', primary_key=True)  # Field name made lowercase.
    review_content = models.CharField(db_column='Review_content', max_length=300)  # Field name made lowercase.
    review_reg_date = models.DateTimeField(db_column='Review_reg_date', blank=True, null=True)  # Field name made lowercase.
    review_mod_date = models.DateTimeField(db_column='Review_mod_date', blank=True, null=True)  # Field name made lowercase.
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    store = models.ForeignKey(Store, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'review'


class StoreAuth(models.Model):
    store_auth_id = models.IntegerField(db_column='Store_Auth_id', primary_key=True)  # Field name made lowercase.
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    store = models.ForeignKey(Store, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'store_auth'


class Tag(models.Model):
    tag_id = models.AutoField(db_column='Tag_id', primary_key=True)  # Field name made lowercase.
    tag_name = models.CharField(db_column='Tag_name', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tag'


class StoreTag(models.Model):
    store_tag_id = models.AutoField(db_column='Store_Tag_id', primary_key=True)  # Field name made lowercase.

    store = models.ForeignKey(Store, on_delete=models.CASCADE)  # Field name made lowercase.
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 'store_tag'




class Bookmark(models.Model):
    bookmark_id = models.AutoField(db_column='Bookmark_id', primary_key=True)  # Field name made lowercase.
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    store = models.ForeignKey(Store, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bookmark'
