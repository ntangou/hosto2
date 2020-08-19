from django.db import models
from datetime import date, datetime
from django.core.exceptions import ValidationError
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

class Heure(models.Model):
    heure = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.heure



class Rdv(models.Model):

    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150, blank=True)

    def validate_date(date):
        if date < date.today():
            raise ValidationError("Date cannot be in the past")


    date = models.DateField(validators=[validate_date], default= date.today)
    heure= models.ForeignKey('Heure', on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)



    class Meta:
        verbose_name = 'Rendez-vous'
        verbose_name_plural = 'Rendez-vous'

    

    def __str__(self):
        return self.nom


    def save(self):
        nom = self.nom.upper()+"\n"
        prenom = self.prenom.title()+"\n"
        date =(str(self.date.strftime('%d-%m-%Y')))+"\n"
        heure =str(self.heure)
        infos = nom+prenom+date+heure
        qrcode_img = qrcode.make(infos)
        canvas = Image.new('RGB', (650, 550), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qrcode_rdv.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save()