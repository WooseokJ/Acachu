from django.db import models

# Create your models here.


class Auth(models.Model):
    auth_id = models.AutoField(db_column='Auth_id', primary_key=True)
    auth_name = models.CharField(db_column='Auth_name', max_length=10)

    class Meta:
        managed = True
        db_table = 'auth'


class Tag(models.Model):
    tag_id = models.AutoField(db_column='Tag_id', primary_key=True)
    tag_name = models.CharField(db_column='Tag_name', max_length=20)

    class Meta:
        managed = True
        db_table = 'tag'


class User(models.Model):
    user_id = models.AutoField(db_column='User_id',
                               primary_key=True)
    user_account = models.CharField(db_column='User_account',
                                    max_length=20,
                                    unique=True)
    user_password = models.CharField(db_column='User_password',
                                     max_length=255)
    user_nickname = models.CharField(db_column='User_nickname',
                                     max_length=20)
    user_email = models.CharField(db_column='User_email',
                                  max_length=50,
                                  blank=True,
                                  null=True)
    user_profileurl = models.ImageField(db_column='User_profileurl',
                                        upload_to='images/',
                                        blank=True,
                                        null=True)

    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'user'

    def __str__(self):
        return self.user_account


class Store(models.Model):
    store_id = models.AutoField(db_column='Store_id', primary_key=True)
    store_name = models.CharField(db_column='Store_name', max_length=50)
    store_content = models.CharField(db_column='Store_content',
                                     max_length=1000,
                                     blank=True,
                                     null=True)
    store_businesshour = models.CharField(db_column='Store_businesshour',
                                          max_length=50,
                                          blank=True,
                                          null=True)
    store_sinum = models.CharField(db_column='Store_sinum',
                                   max_length=10)
    store_sggnum = models.CharField(db_column='Store_sggnum',
                                    max_length=10)
    store_emdnum = models.CharField(db_column='Store_emdnum',
                                    max_length=10)
    store_roadnum = models.CharField(db_column='Store_roadnum',
                                     max_length=50)
    store_image = models.ImageField(db_column='Store_image',
                                    upload_to='cafe_images/',
                                    max_length=255)

    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = 'store'


class AuthBoard(models.Model):
    ab_id = models.AutoField(db_column='Ab_id', primary_key=True)
    ab_title = models.CharField(db_column='Ab_title', max_length=255)
    ab_content = models.CharField(db_column='Ab_content', max_length=3000)
    ab_reg_date = models.DateTimeField(db_column='Ab_reg_date')
    ab_reply_yn = models.IntegerField(db_column='Ab_reply_YN')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'auth_board'


class Authpicture(models.Model):
    authpicture_id = models.AutoField(db_column='Authpicture_id',
                                      primary_key=True)
    authpicture_img = models.ImageField(db_column='Authpicture_img',
                                        upload_to='ab_images/',
                                        blank=True,
                                        null=True)

    ab = models.ForeignKey(AuthBoard, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'authpicture'


class Cafepicture(models.Model):
    cafepicture_id = models.AutoField(db_column='Cafepicture_id',
                                      primary_key=True)
    cafepicture_url = models.CharField(db_column='Cafepicture_url',
                                       max_length=1000)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'cafepicture'


class Reply(models.Model):
    reply_id = models.AutoField(db_column='Reply_id', primary_key=True)
    reply_content = models.CharField(db_column='Reply_content', max_length=300)
    reply_date = models.DateTimeField(db_column='Reply_date')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    authboard = models.ForeignKey(AuthBoard, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'reply'


class Review(models.Model):
    review_id = models.AutoField(db_column='Review_id',
                                 primary_key=True)
    review_content = models.CharField(db_column='Review_content',
                                      max_length=300)
    review_reg_date = models.DateTimeField(db_column='Review_reg_date',
                                           blank=True,
                                           null=True)
    review_mod_date = models.DateTimeField(db_column='Review_mod_date',
                                           blank=True,
                                           null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'review'


class StoreAuth(models.Model):
    store_auth_id = models.IntegerField(db_column='Store_Auth_id',
                                        primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'store_auth'


class StoreTag(models.Model):
    store_tag_id = models.AutoField(db_column='Store_Tag_id', primary_key=True)

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'store_tag'


class Bookmark(models.Model):
    bookmark_id = models.AutoField(db_column='Bookmark_id', primary_key=True)
    bookmark_reg_date = models.DateTimeField(db_column='Bookmark_reg_date',
                                             blank=True,
                                             null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'bookmark'


class Adj(models.Model):
    adj_id = models.AutoField(primary_key=True)
    first = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = 'adj'
        managed = True


class Noun(models.Model):
    noun_id = models.AutoField(primary_key=True)
    second = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = 'noun'
        managed = True


class Searchpicture(models.Model):
    searchpicture_id = models.AutoField(db_column='Searchpicture_id',
                                        primary_key=True)
    searchpicture_url = models.ImageField(db_column='Searchpicture_url',
                                          upload_to='search_images/')

    class Meta:
        db_table = 'searchpicture'
        managed = True
