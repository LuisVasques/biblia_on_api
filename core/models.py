from django.db import models


class Book(models.Model):
    class Testament(models.TextChoices):
        NEW = "N"
        OLD = "O"

    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,

    )
    name = models.CharField(
        db_column='tx_name',
        max_length=60,
        null=False
    )
    order = models.IntegerField(
        db_column='nb_order',
        null=False,

    )
    testament = models.CharField(
        db_column='cs_testament',
        max_length=1,
        choices=Testament.choices,
        null=False,
        default='O'
    )

    class Meta:
        db_table = 'book'


class Chapter(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,

    )
    number = models.IntegerField(
        db_column='nb_number',
        null=False,

    )
    chronology = models.IntegerField(
        db_column='nb_chronology',
        null=False,

    )
    book = models.ForeignKey(
        to=Book,
        on_delete=models.DO_NOTHING,
        db_column='id_book',
    )

    class Meta:
        db_table = 'chapter'


class Rule(models.Model):
    class ReadingType(models.TextChoices):
        FRONT_TO_BACK = "1"
        CHRONOLOGY = "2"
        PARALLEL = "3"

    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,

    )

    period = models.IntegerField(
        db_column='nb_period',
        null=False,

    )
    pause = models.IntegerField(
        db_column='nb_pause',
        null=False,

    )
    reading_type = models.CharField(
        db_column='cs_reading_type',
        max_length=1,
        choices=ReadingType.choices,
        null=False,
        default='2'
    )

    class Meta:
        db_table = 'rule'


class Event(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,

    )
    name = models.CharField(
        db_column='tx_name',
        max_length=40,
        null=False
    )
    start_date = models.DateField(
        db_column='dt_start_date',
        null=False,

    )
    end_date = models.DateField(
        db_column='dt_end_date',
        null=False,

    )
    rule = models.ForeignKey(
        to=Rule,
        on_delete=models.DO_NOTHING,
        db_column='id_rule',
    )

    class Meta:
        db_table = 'event'


class Plan(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,

    )
    date = models.DateField(
        db_column='dt_date',
        null=False,

    )
    chapter = models.ForeignKey(
        to=Chapter,
        on_delete=models.DO_NOTHING,
        db_column='id_chapter',
    )
    event = models.ForeignKey(
        to=Event,
        on_delete=models.DO_NOTHING,
        db_column='id_event',
    )

    class Meta:
        db_table = 'plan'


class User(models.Model):
    class UserType(models.TextChoices):
        COORDINATOR = "1"
        ADVISOR = "2"
        GA_LEADER = "3"
        HEADED = "4"

    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,

    )
    name = models.CharField(
        db_column='tx_name',
        max_length=100,
        null=False
    ),

    username = models.CharField(
        db_column='tx_username',
        max_length=100,
        null=False
    )
    password = models.CharField(
        db_column='tx_password',
        max_length=40,
        null=False
    )

    date_registration = models.DateTimeField(
        db_column='dt_date_registration',
        null=False,

    )
    phone = models.CharField(
        db_column='tx_phone',
        max_length=32,
        null=False
    )
    email = models.CharField(
        db_column='tx_email',
        max_length=128,
        null=False
    )

    user_type = models.CharField(
        db_column='cs_user_type',
        max_length=1,
        choices=UserType.choices,
        null=False,
        default='4'
    )

    class Meta:
        db_table = 'user'


class Control(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,

    )

    plan = models.ForeignKey(
        to=Plan,
        on_delete=models.DO_NOTHING,
        db_column='id_plan',
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
        db_column='id_user',
    )
    date = models.DateField(
        db_column='dt_date',
        null=False,

    )

    class Meta:
        db_table = 'control'
