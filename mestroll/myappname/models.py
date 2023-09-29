from django.db import models


class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    Role_name = models.CharField(max_length=250)
    Role_id = models.IntegerField()
    Staff_type = models.CharField(max_length=250)
    staff_type_id = models.IntegerField()
    gender = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    mobile = models.DecimalField(max_digits=15, decimal_places=0)
    apartment = models.CharField(max_length=250)
    room = models.CharField(max_length=250)

    class Meta:
        managed = False  # Set managed to False to indicate that Django should not manage this table
        db_table = "users"  # Specify the actual table name


class sign_ins(models.Model):
    sign_in_id = models.BigIntegerField(primary_key=True)
    screated_at = models.DateTimeField()
    suser_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    Role_name = models.CharField(max_length=250)

    Staff_type = models.CharField(max_length=250)
    staff_type_id = models.IntegerField()
    gender = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    mobile = models.DecimalField(max_digits=15, decimal_places=0)
    apartment = models.CharField(max_length=250)
    room = models.CharField(max_length=250)

    class Meta:
        managed = False  # Set managed to False to indicate that Django should not manage this table
        db_table = "sign_ins"  # Specify the actual table name


class Classe(models.Model):
    user_id = models.CharField(max_length=250, null=True)
    classroom = models.CharField(max_length=250, null=True)
    lat = models.CharField(max_length=250)
    long = models.CharField(max_length=250)
    elevation = models.CharField(max_length=250)

    def __str__(self):
        return self.classroom + " " + self.elevation
    
