from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)
    agency = models.CharField(max_length=50, null=True)

class Customer(models.Model):
    VICID = models.AutoField(primary_key=True)
    ACCTNO = models.CharField(max_length=10)
    NO_IDEN = models.CharField(max_length=16)
    NAMA_NASABAH = models.CharField(max_length=50)

class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    Nama_Field = models.CharField(max_length=15)
    Field_Awal = models.CharField(max_length=50)
    Field_Update = models.CharField(max_length=50)
    Record_DEL = models.CharField(max_length=1,default='')
    TGL_UPDT = models.CharField(max_length=8,default='')
    JM_UPDT = models.CharField(max_length=6,default='')
    TGL_APPRV_UPDT = models.CharField(max_length=8,default='')
    JM_APPRV_UPDT = models.CharField(max_length=6,default='')
    USR_UPDT = models.CharField(max_length=15,default='')
    APPRV_UPDT = models.CharField(max_length=15,default='')
    TGL_DELET = models.CharField(max_length=8,default='')
    JM_DELET = models.CharField(max_length=6,default='')
    TGL_APPRV_DELET = models.CharField(max_length=8,default='')
    JM_APPRV_DELET = models.CharField(max_length=6,default='')
    USR_DELET = models.CharField(max_length=15,default='')
    APPRV_DELET = models.CharField(max_length=15,default='')


