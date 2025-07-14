# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActionsTb(models.Model):
    action_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    action_name = models.CharField(max_length=200, blank=True, null=True)
    action_desc = models.TextField(blank=True, null=True)
    action_channel = models.CharField(max_length=100, blank=True, null=True)
    action_date_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actions_tb'


class AdoptantsTb(models.Model):
    adoptant_id = models.AutoField(primary_key=True)
    sex = models.ForeignKey('SexTb', models.DO_NOTHING)
    country = models.ForeignKey('CountryTb', models.DO_NOTHING)
    status = models.ForeignKey('StatusTb', models.DO_NOTHING)
    adoptant_fname = models.CharField(max_length=255)
    adoptant_lname = models.CharField(max_length=255)
    adoptant_mail = models.CharField(max_length=255)
    adoptant_tel = models.CharField(max_length=20)
    adoptant_dob = models.DateField()
    adoptant_pob = models.CharField()
    adoptant_address = models.TextField()
    adoptant_image = models.TextField()
    adoptant_date_created = models.DateTimeField()
    adoptant_date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adoptants_tb'


class AdoptionsTb(models.Model):
    adoption_id = models.AutoField(primary_key=True)
    orphelin = models.ForeignKey('OrphelinsTb', models.DO_NOTHING)
    adoptant = models.ForeignKey(AdoptantsTb, models.DO_NOTHING)
    adoption_date = models.DateField()
    status = models.ForeignKey('StatusTb', models.DO_NOTHING)
    adoption_desc = models.TextField(blank=True, null=True)
    adoption_date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'adoptions_tb'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CountryTb(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=100)
    country_currency_code = models.CharField(max_length=3, blank=True, null=True)
    country_fips_code = models.CharField(max_length=2, blank=True, null=True)
    country_iso_numeric = models.CharField(max_length=4, blank=True, null=True)
    country_north = models.CharField(max_length=30, blank=True, null=True)
    country_south = models.CharField(max_length=30, blank=True, null=True)
    country_east = models.CharField(max_length=30, blank=True, null=True)
    country_west = models.CharField(max_length=30, blank=True, null=True)
    country_capital = models.CharField(max_length=100, blank=True, null=True)
    country_continent_name = models.CharField(max_length=100, blank=True, null=True)
    country_continent = models.CharField(max_length=2, blank=True, null=True)
    country_languages = models.CharField(max_length=100, blank=True, null=True)
    country_iso_alpha3 = models.CharField(max_length=3, blank=True, null=True)
    country_geoname_id = models.IntegerField(blank=True, null=True)
    country_telephone_prefix = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'country_tb'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentsTb(models.Model):
    doc_id = models.AutoField(primary_key=True)
    orphelin = models.ForeignKey('OrphelinsTb', models.DO_NOTHING)
    doc_type = models.CharField(max_length=100)
    doc_url = models.TextField()
    doc_description = models.TextField(blank=True, null=True)
    doc_date_uploaded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documents_tb'


class DonatorsTb(models.Model):
    donator_id = models.AutoField(primary_key=True)
    sex = models.ForeignKey('SexTb', models.DO_NOTHING)
    country = models.ForeignKey(CountryTb, models.DO_NOTHING)
    status = models.ForeignKey('StatusTb', models.DO_NOTHING)
    donator_fname = models.CharField(max_length=255)
    donator_lname = models.CharField(max_length=255)
    donator_mail = models.CharField(max_length=255)
    donator_tel = models.CharField(max_length=20)
    donator_dob = models.DateField()
    donator_pob = models.CharField()
    donator_image = models.TextField()
    donator_date_created = models.DateTimeField()
    donator_date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donators_tb'


class EducationTb(models.Model):
    edu_id = models.AutoField(primary_key=True)
    orphelin = models.ForeignKey('OrphelinsTb', models.DO_NOTHING)
    school_name = models.CharField(max_length=255)
    academic_level = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=20)
    education_notes = models.TextField(blank=True, null=True)
    edu_date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'education_tb'


class GiftsTb(models.Model):
    gift_id = models.AutoField(primary_key=True)
    donator = models.ForeignKey(DonatorsTb, models.DO_NOTHING)
    status = models.ForeignKey('StatusTb', models.DO_NOTHING)
    gift_name = models.CharField(max_length=255)
    gift_desc = models.CharField(max_length=255)
    gift_date_created = models.DateTimeField()
    gift_date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gifts_tb'


class MedicalVisitsTb(models.Model):
    visit_id = models.AutoField(primary_key=True)
    orphelin = models.ForeignKey('OrphelinsTb', models.DO_NOTHING)
    visit_date = models.DateField()
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    visit_notes = models.TextField(blank=True, null=True)
    visit_date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medical_visits_tb'


class MessagesTb(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey('UsersTb', models.DO_NOTHING)
    receiver = models.ForeignKey('UsersTb', models.DO_NOTHING, related_name='messagestb_receiver_set')
    message_subject = models.CharField(max_length=255)
    message_content = models.TextField()
    message_sent_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages_tb'


class OrphelinatsTb(models.Model):
    orphelinat_id = models.AutoField(primary_key=True)
    orphelinat_name = models.CharField(max_length=255)
    orphelinat_address = models.TextField()
    orphelinat_phone = models.CharField(max_length=20)
    orphelinat_email = models.CharField(max_length=100, blank=True, null=True)
    orphelinat_date_created = models.DateField()

    class Meta:
        managed = False
        db_table = 'orphelinats_tb'


class OrphelinsTb(models.Model):
    orphelin_id = models.AutoField(primary_key=True)
    orphelinat = models.ForeignKey(OrphelinatsTb, models.DO_NOTHING)
    sex = models.ForeignKey('SexTb', models.DO_NOTHING)
    country = models.ForeignKey(CountryTb, models.DO_NOTHING)
    status = models.ForeignKey('StatusTb', models.DO_NOTHING)
    orphelin_fname = models.CharField(max_length=255)
    orphelin_lname = models.CharField(max_length=255)
    orphelin_father_name = models.CharField(max_length=255)
    orphelin_mother_name = models.CharField(max_length=255)
    orphelin_dob = models.DateField()
    orphelin_pob = models.CharField(max_length=255)
    orphelin_image = models.TextField()
    orphelin_first_day_at_orphan = models.DateField()
    orphelin_date_created = models.DateTimeField()
    orphelin_date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orphelins_tb'


class RolesTb(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    role_desc = models.CharField(max_length=255)
    role_date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'roles_tb'


class SexTb(models.Model):
    sex_id = models.AutoField(primary_key=True)
    sex_name = models.CharField(max_length=255)
    sex_char = models.CharField(max_length=2)
    sex_date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sex_tb'


class StatusTb(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=255)
    status_desc = models.CharField(max_length=255)
    status_date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status_tb'


class UsersTb(models.Model):
    user_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(RolesTb, models.DO_NOTHING)
    sex = models.ForeignKey(SexTb, models.DO_NOTHING)
    country = models.ForeignKey(CountryTb, models.DO_NOTHING)
    status = models.ForeignKey(StatusTb, models.DO_NOTHING)
    user_fname = models.CharField(max_length=255)
    user_lname = models.CharField(max_length=255)
    user_mail = models.CharField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=255)
    user_tel = models.CharField(max_length=20)
    user_dob = models.DateField()
    user_pob = models.CharField()
    user_pswd = models.CharField(max_length=255)
    user_image = models.TextField()
    user_date_created = models.DateTimeField()
    user_date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_tb'
