from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class Region(models.Model):
    region_keyr = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_cities(self):
        return Cities.objects.filter(region=self.id).order_by('name')


class Cities(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Cities"

    objects = models.Manager()

    def __str__(self):
        return self.name
    print(name)


# cities = {"ANDIJAN": ["Andijon tuman", "Asaka tumani", "Baliqchi tumani", "Boʻston tuman", "Buloqboshi tumani",
#                       "Izboskan tuman", "Jalaquduq tuman", "Xoʻjaobod tumani", "Qoʻrgʻontepa tumani",
#                       "Marhamat tumani", "Oltinkoʻl tuman", "Paxtaobod tumani", "Shahrixon tuman", "Ulugʻnor tuman",
#                       "Xonobod shahar", "Andijon shahar"],
#
#          "BUKHARA": ["Olot tumani", "Buxoro tumani", "Gʻijduvon tumani", "Jondor tumani", "Kogon tumani",
#                      "Qorakoʻl tumani", "Qorovulbozor tumani", "Peshku tumani", "Romitan tumani",
#                      "Shofirkon tumani", "Vobkent tumani"],
#
#          "FERGHANA": ["Oltiariq tumani", "Bagʻdod tumani", "Beshariq tumani", "Buvayda tumani", "Dangʻara tumani",
#                       "Fargʻona tumani", "Furqat tumani", "Qoʻshtepa tumani", "Quva tumani", "Rishton tumani",
#                       "Soʻx tumani", "Toshloq tumani", "Uchkoʻprik tumani", "Oʻzbekiston tumani", "Yozyovon tumani"],
#
#          "JIZZAKH": ["Arnasoy tumani", "Baxmal tumani", "Doʻstlik tumani", "Forish tumani", "Gʻallaorol tumani",
#                      "Sharof Rashidov tumani", "Mirzachoʻl tumani", "Paxtakor tumani", "Yangiobod tumani",
#                      "Zomin tumani", "Zafarobod tumani", "Zarbdor tumani"],
#
#          "KHOREZM": ["Bogʻot tumani", "Gurlan tumani", "Xonqa tumani", "Hazorasp tumani", "Xiva tumani",
#                      "Qoʻshkoʻpir tumani", "Shovot tumani", "Urganch tumani", "Yangiariq tumani", "Yangibozor tumani",
#                      "Tupproqqalʼa tumani"],
#
#          "NAMANGAN": ["Chortoq tumani", "Chust tumani", "Kosonsoy tumani", "Mingbuloq tumani", "Namangan tumani",
#                       "Norin tumani Oʻzbekiston", "Pop tumani", "Toʻraqoʻrgʻon tumani", "Uchqoʻrgʻon tumani",
#                       "Uychi tumani", "Yangiqoʻrgʻon tumani", "Davlatobod tumani", "Yangi Namangan tumani"],
#
#          "NAVOI": ["Konimex tumani", "Karmana tumani", "Qiziltepa tumani", "Xatirchi tumani", "Navbahor tumani",
#                    "Nurota tumani", "Tomdi tumani", "Uchquduq tumani"],
#
#          "QASHQADYO": ["Dehqonobod tumani", "Kasbi tumani", "Kitob tumani","Koson tumani", "Koʻkdala tumani",
#                        "Mirishkor tumani", "Muborak tumani", "Nishon tumani", "Qamashi tumani", "Qarshi tumani",
#                        "Yakkabogʻ tumani", "Gʻuzor tumani", "Shahrisabz tumani", "Chiroqchi tumani"],
#
#          "KARAKALPAKSTAN": ["Amudaryo tumani", "Beruniy tumani", "Chimboy tumani", "Ellikqalʼa tumani",
#                             "Kegeyli tumani", "Moʻynoq tumani", "Nukus tumani", "Qanlikoʻl tumani", "Qoʻngʻirot tumani",
#                             "Qoraoʻzak tumani", "Shumanay tumani", "Taxtakoʻpir tumani", "Toʻrtkoʻl tumani",
#                             "Xoʻjayli tumani"],
#
#          "SAMARQAND": ["Bulungʻur tumani", "Ishtixon tumani", "Jomboy tumani", "Kattaqoʻrgʻon tumani",
#                        "Qoʻshrabot tumani", "Narpay tumani", "Nurobod tumani","Oqdaryo tumani", "Paxtachi tumani",
#                        "Payariq tumani", "Pastdargʻom tumani", "Samarqand tumani", "Toyloq tumani", "Urgut tumani"],
#
#          "SIRDARYO": ["Oqoltin tumani", "Boyovut tumani", "Guliston tumani", "Xovos tumani", "Mirzaobod tumani",
#                       "Sardoba tumani", "Sayxunobod tumani", "Sirdaryo tumani"],
#
#          "SURKHANDARYO": ["Angor tumani", "Bandixon tumani", "Boysun tumani", "Denov tumani", "Jarqoʻrgʻon tumani",
#                           "Qiziriq tumani", "Qumqoʻrgʻon tumani", "Muzrabod tumani", "Oltinsoy tumani",
#                           "Sariosiyo tumani", "Sherobod tumani", "Shoʻrchi tumani", "Termiz tumani", "Uzun tumani"],
#          "TASHKENT": ["Bekobod tumani", "Boʻstonliq tumani", "Boʻka tumani", "Chinoz tumani",
#                       "Qibray tumani", "Ohangaron tumani", "Oqqoʻrgʻon tumani", "Parkent tumani",
#                       "Piskent tumani", "Quyi Chirchiq tumani", "Oʻrta Chirchiq tumani",
#                       "Yangiyoʻl tumani", "Yuqori Chirchiq tumani", "Zangiota tumani"],
#
#          "TASHKENT_C": ["Bektemir tumani", "Chilonzor tumani", "Hamza Iroqiy tumani", "Mirobod tumani",
#                         "Mirzo Ulug‘bek tumani", "Olmazor tumani", "Samarqand-Darvoza tumani", "Sergeli tumani",
#                         "Shayxontohur tumani", "Uchtepa tumani"]}

# regions = [
#     ("ANDIJAN", "Andijon"),
#     ("BUKHARA", "Buxoro"),
#     ("FERGHANA", "Farg'ona"),
#     ("JIZZAKH", "Jizzax"),
#     ("KHOREZM", "Xorazm"),
#     ("NAMANGAN", "Namangan"),
#     ("NAVOI", "Navoi"),
#     ("QASHQADYO", "Qashqadaryo"),
#     ("KARAKALPAKSTAN", "Qoraqalpog'iston"),
#     ("SAMARQAND", "Samarqand"),
#     ("SURKHANDARYO", "Surxandaryo"),
#     ("SIRDARYO", "Sirdaryo"),
#     ("TASHKENT", "Toshkent viloyat"),
#     ("TASHKENT_C", "Toshkent shahar"),
# ]
# for id, name in regions:
#     x = Region.objects.create(region_keyr=id, name=name)
#     x.save()
#
# for key, names in cities.items():
#     region = Region.objects.get(region_keyr=key)
#     for namee in names:
#         x = Cities.objects.create(region=region, name=namee)
#         x.save()
#         print(key, names)

class CustomUser(AbstractUser):
    regions = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    cities = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(('email address'), max_length=254, unique=True, null=True)
    address = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=20)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    password1 = models.CharField(max_length=32)
    password2 = models.CharField(max_length=32)
    avatar = models.ImageField(upload_to='thumbpath', blank=True, null=True)
    bio = models.CharField(max_length=1200, blank=True)

    # USERNAME_FIELD = 'email'
    class Meta:
        swappable = 'AUTH_USER_MODEL'



