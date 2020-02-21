from django.db import models
from django.urls import reverse


class Hotel(models.Model):
    """That class-model for hotels"""
    number = models.PositiveIntegerField(verbose_name="Номер отеля", unique=True)
    count_of_floors = models.IntegerField(verbose_name="Кол-во этажей")
    count_of_numbers = models.IntegerField(verbose_name="Кол-во комнат")
    country = models.CharField(verbose_name="Страна", max_length=30)
    city = models.CharField(verbose_name="Город", max_length=30)
    street = models.CharField(verbose_name="Улица", max_length=30)
    house = models.CharField(verbose_name="Номер дома", max_length=30)

    def __str__(self):
        return 'hotel ' + str(self.number)


class Resedent(models.Model):
    """docstring for Resendt"""
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    second_name = models.CharField(verbose_name="Фамилия", max_length=30)
    father_name = models.CharField(verbose_name="Отчество", max_length=30)
    burn_date = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(
        verbose_name="Пол",
        max_length=1,
        choices=(
            ('m', 'мужской'),
            ('f', 'женский')
        )
    )
    phone_number = models.CharField(max_length=30, verbose_name="Телефон")
    pasport_seria = models.CharField(max_length=4, verbose_name="Паспорт серия")
    pasport_number = models.CharField(max_length=6, verbose_name="Паспорт номер")
    count_of_living = models.IntegerField(default=0, verbose_name="Количество заселений")
    in_bucket = models.BooleanField(default=True)

    def __str__(self):
        return str(self.first_name + " " + self.second_name + " " + self.pasport_number)

    def get_absolute_url(self):
        return reverse('resedent_detail', args=[str(self.id)])

    def increase_count_of_living(self):
        self.count_of_living = self.count_of_living + 1

    def is_living(self):
        '''кароче если пользователь заселен, то возращает тру, иначе фолз'''
        return Checkin.objects.filter(resedent=self).exists()


class Nomer(models.Model):
    """docstring for Nomer"""
    number = models.PositiveIntegerField(verbose_name="Номер комнаты в гостинице")
    count_of_rooms = models.PositiveIntegerField(verbose_name="Количество комнат")
    square = models.PositiveIntegerField(verbose_name="Площадь")
    hotel = models.ForeignKey(
        'core.Hotel',
        verbose_name="Выберите отель",
        on_delete=models.PROTECT,
        null=True,
    )

    def __str__(self):
        return 'nomer ' + str(self.number)

    def get_absolute_url(self):
        return reverse('nomer_detail', args=[str(self.id)])

    def is_living(self):
        """кароче если пользователь заселен, то возращает тру, иначе фолз"""
        return Checkin.objects.filter(nomer=self).exists()


class Checkin(models.Model):
    """Docstring for Living"""
    resedent = models.OneToOneField(
        'core.Resedent',
        verbose_name="Постоялец",
        on_delete=models.PROTECT,
        null=True,
    )
    nomer = models.OneToOneField(
        'core.Nomer',
        verbose_name="Номер",
        on_delete=models.PROTECT,
        null=True,
    )
    date_chekin = models.DateField(
        verbose_name='Дата заселения',
        null=True,
    )
    date_checkout = models.DateField(
        verbose_name='Дата выселения',
        null=True,
    )

    def give_full_name(self):
        return str(self.resedent) + ' ' + str(self.nomer)

    def __str__(self):
        return str(self.resedent) + ' ' + str(self.nomer)

    def get_absolute_url(self):
        return reverse('checkin_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Заселение'
        verbose_name_plural = "Заселения"


class Document(models.Model):
    document = models.FileField(upload_to='documents/', verbose_name="Добавьте файл формата .xls")
