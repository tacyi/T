# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=30)
    introduce = models.CharField(max_length=300)
    state = models.IntegerField()
    money = models.IntegerField()
    adminid = models.IntegerField()
    starttime = models.DateField()
    endtime = models.DateField()
    addtime = models.DateField()
    address = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'activity'


class Cadmin(models.Model):
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    state = models.PositiveIntegerField()
    clubid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cadmin'


class Club(models.Model):
    clubid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)
    introduce = models.CharField(max_length=300)
    state = models.PositiveIntegerField()
    img = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=30)
    birthday = models.DateField()
    star = models.IntegerField(blank=True, null=True)
    staruser = models.IntegerField(blank=True, null=True)
    wurl = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'club'


class Coach(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=30)
    state = models.IntegerField()
    astate = models.IntegerField()
    usestate = models.IntegerField()
    clubid = models.IntegerField()
    introduce = models.CharField(max_length=300)
    img = models.CharField(max_length=60)
    date = models.DateField()
    gender = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coach'


class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=300)
    pid = models.IntegerField()
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment'


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)
    clubid = models.IntegerField()
    introduce = models.CharField(max_length=300)
    state = models.IntegerField()
    startdate = models.DateField()
    endtime = models.DateField()
    cid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'


class Coursevideo(models.Model):
    cvid = models.AutoField(primary_key=True)
    introduce = models.CharField(max_length=300)
    courseid = models.IntegerField()
    video = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'coursevideo'


class Match(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=30)
    introduce = models.CharField(max_length=300)
    data = models.DateTimeField()
    usersid = models.CharField(max_length=300)
    state = models.IntegerField()
    starttime = models.DateField()
    endtime = models.DateField()
    addtime = models.DateField()
    address = models.CharField(max_length=60)
    money = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'match'


class Orders(models.Model):
    oid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    mid = models.IntegerField(blank=True, null=True)
    tid = models.IntegerField(blank=True, null=True)
    aid = models.IntegerField(blank=True, null=True)
    ordertime = models.DateField()
    other = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Picture(models.Model):
    pid = models.AutoField(primary_key=True)
    pic = models.CharField(max_length=180)
    uid = models.IntegerField()
    date = models.DateField()
    times = models.IntegerField()
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'picture'


class Sadmin(models.Model):
    sname = models.CharField(max_length=30)
    sid = models.AutoField(primary_key=True)
    spwd = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sadmin'


class Signclub(models.Model):
    sid = models.AutoField(primary_key=True)
    cid = models.IntegerField()
    uid = models.IntegerField()
    applystate = models.IntegerField()
    accessstate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'signclub'


class Training(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=30)
    introduce = models.CharField(max_length=300)
    clubid = models.IntegerField()
    state = models.IntegerField()
    startdate = models.DateField()
    enddate = models.DateField()
    deadline = models.DateField()
    cid = models.IntegerField()
    money = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'training'


class User(models.Model):
    upwd = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    uid = models.AutoField(primary_key=True)
    state = models.IntegerField()
    gender = models.IntegerField()
    birthday = models.DateField()
    phone = models.CharField(max_length=30)
    clubid = models.IntegerField()
    mstate = models.IntegerField()
    astate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
