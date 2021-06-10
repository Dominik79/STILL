from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Oddzialy(models.Model):
    nazwa = models.TextField(max_length=50)
    long = models.DecimalField(max_digits=11, decimal_places=8)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    opis = models.TextField()


# Create your models here.
class Tugger(models.Model):
    SAP = models.TextField(max_length=10)
    Nazwa = models.TextField(max_length=50)
    Data = models.DateField()
    Produkt = models.TextField(max_length=50)
    Kodpocztowy = models.TextField(max_length=6)


# Create your models here.
class Klienci(models.Model):
    SAP = models.IntegerField()
    Nazwa = models.TextField(max_length=50)
    Ulica = models.TextField(max_length=100)
    Numer = models.TextField(max_length=10)
    Miejscowosc = models.TextField(max_length=50)
    Kodpocztowy = models.TextField(max_length=6)
    Branza = models.TextField(max_length=50)
    long = models.DecimalField(max_digits=11, decimal_places=8)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    Vxx = models.TextField(max_length=4)


# Create your models here.
class Telefony(models.Model):
    imie = models.TextField(max_length=50)
    nazwisko = models.TextField(max_length=50)
    stacjonarny = models.TextField(max_length=50)
    komorkowy = models.TextField(max_length=50)
    dzial = models.TextField(max_length=50)
    poddzial = models.TextField(max_length=50)
    stanowisko = models.TextField(max_length=50)
    oddzial = models.TextField(max_length=50)
    update = models.DateTimeField()


# Create your models here.
class RealizacjeTugger(models.Model):
    klient = models.ForeignKey(Klienci, on_delete=models.CASCADE, )

    numer_seryjny = models.TextField(max_length=12)

    class PODNOSZENIE(models.TextChoices):
        # BRAK = "", _('brak danych')
        # AUTARKICZNE = "A", _('Autarkiczne')
        ELEKTRYCZNE = "E", _('Elektryczne')
        HYDRAULICZNE = "H", _('Hydruliczne')
        PNEUMATYCZNE = "P", _('Peumatyczne')

    podnoszenie = models.CharField(
        max_length=1,
        choices=PODNOSZENIE.choices,
        # default=PODNOSZENIE.BRAK
    )

    class TYP(models.TextChoices):
        # BRAK = "", _('brak danych')
        JEDNOSTRONNA = "E", _('Typu E')
        DWUSTRONNA = "B", _('Typu B')
        ZEWNETRZNA = "C", _('Typu C')
        PORTYKOWA = "P", _('Typu P')

    typ = models.CharField(
        max_length=1,
        choices=TYP.choices,
        # default=TYP.BRAK
    )

    class WYMIAR(models.TextChoices):
        # BRAK = "", _('brak danych')
        _1200x800 = "E", _('1200x800')
        _3x800x600 = "3", _('3x800x600')
        _1200x1000 = "I", _('1200x1000')
        _1200x2000 = "C", _('1200x2000')
        SPECJALNA = "S", _('Specjalna')

    wymiar = models.CharField(
        max_length=1,
        choices=WYMIAR.choices,
    )


class RealizacjeRacks(models.Model):
    klient = models.ForeignKey(Klienci, on_delete=models.CASCADE, )

    class TYP(models.TextChoices):
        PALETOWE = "P", _('Paletowe')
        MOBILNE = "M", _('Mobilne')
        SHUTTLE = "S", _('Shuttle')
        ANTRESOLA = "A", _('Antresola')
        DRIVE_IN = "D", _('Drive-In')

    typ = models.CharField(
        max_length=1,
        choices=TYP.choices,
        # default=PODNOSZENIE.BRAK
    )

    class ILOSC(models.TextChoices):
        SMALL = "S", _('0-1000')
        MEDIUM = "M", _('1000-5000')
        LARGE = "L", _('5000-10000')
        EXTRALARGE = "X", _('10000-')

    ilosc = models.CharField(
        max_length=1,
        choices=ILOSC.choices,
        # default=TYP.BRAK
    )
    _ilosc = models.PositiveIntegerField()

    class WYSOKOSC(models.TextChoices):
        NISKIE = "N", _('0-6000')
        SREDNIE = "S", _('6000-9000')
        WYSOKIE = "W", _('9000-14000')
        BARDZOWYSOKIE = "B", _('14000-')

    wysokosc = models.CharField(
        max_length=1,
        choices=WYSOKOSC.choices,
    )
    _wysokosc = models.PositiveIntegerField()

    class KORYTARZ(models.TextChoices):
        SZEROKI = "S", _('Szeroki')
        WASKI = "V", _('Wąski')
        INNYE = "I", _('Inny')

    korytarz = models.CharField(
        max_length=1,
        choices=KORYTARZ.choices,
    )

    krata = models.BooleanField(verbose_name='Krata')
    siatka = models.BooleanField(verbose_name='Siatka')
    oslony = models.BooleanField(verbose_name='Ochrony')
    siatka_tylna = models.BooleanField(verbose_name='Siatka tylna')


class RealizacjeVNA(models.Model):
    klient = models.ForeignKey(Klienci, on_delete=models.CASCADE, )

    class TYP(models.TextChoices):
        MX_X = "M", _('MX-X')
        GX_X = "G", _('GX-X')
        EX_X = "E", _('EK-X 24/48')
        EK_X10 = "e", _('EK-X 10')
        JX0 = "J", _('JX0')

    typ = models.CharField(
        max_length=1,
        choices=TYP.choices,
        # default=PODNOSZENIE.BRAK
    )

    class WYSOKOSC(models.TextChoices):
        NISKIE = "N", _('0-6000')
        SREDNIE = "S", _('6000-9000')
        WYSOKIE = "W", _('9000-14000')
        BARDZOWYSOKIE = "B", _('14000-')

    wysokosc = models.CharField(
        max_length=1,
        choices=WYSOKOSC.choices,
    )

    class PROWADZENIE(models.TextChoices):
        MZF = "M", _('Mechaniczne')
        IZF = "I", _('Indukcyjne')
        BRAK = "N", _('Swobodnie prowadzone')

    prowadzenie = models.CharField(
        max_length=1,
        choices=PROWADZENIE.choices,
        # default=TYP.BRAK
    )

    class HAMOWANIE(models.TextChoices):
        MAGNET = "M", _('Magnesy')
        INDUKCYJNE = "B", _('Blachy')
        RFID = "R", _('RFID')
        OPTYCZNE = "O", _('Optyczne')

    hamowanie = models.CharField(
        max_length=1,
        choices=HAMOWANIE.choices,
        # default=TYP.BRAK
    )

    class TROG(models.TextChoices):
        SMALL = "S", _('Mały')
        MEDIUM = "M", _('Średni')
        LARGE = "L", _('Duży')

    trog = models.CharField(
        max_length=1,
        choices=TROG.choices,
        # default=TYP.BRAK
    )

    class TYPBATERII(models.TextChoices):
        ACID = "K", _('Kwasowo-ołowiowa')
        CSM = "C", _('Miedziane')
        GEL = "G", _('Żelowe')
        NEXSYS = "N", _('NexSys')
        LIION = "L", _('Li-ION')

    typbaterii = models.CharField(
        max_length=1,
        choices=TYPBATERII.choices,
        # default=TYP.BRAK
    )

    navigation = models.BooleanField(verbose_name='Nawigacja')
    safety = models.BooleanField(verbose_name='PSA')
    safetysystem = models.BooleanField(verbose_name='GSA')
    compensation = models.BooleanField(verbose_name='AFC')
    devided = models.BooleanField(verbose_name='Dzielony pulpit')
    tilting = models.BooleanField(verbose_name='Uchylne barierki')
    atachment = models.BooleanField(verbose_name='Osprzęt na głowicy')
    cold = models.BooleanField(verbose_name='Chłodnia')
    reach = models.BooleanField(verbose_name='Nadwysuw')
    kombi = models.BooleanField(verbose_name='Kombi')
    brakes = models.BooleanField(verbose_name='Hamulce')
    camera = models.BooleanField(verbose_name='Kamera')
    platform = models.BooleanField(verbose_name='Platforma do wyjścia')
    als = models.BooleanField(verbose_name='OS3.4 - ALS')
    fleetmanager = models.BooleanField(verbose_name='FleetManager')


class RealizacjeAGV(models.Model):
    klient = models.ForeignKey(Klienci, on_delete=models.CASCADE, )

    class TYP(models.TextChoices):
        STATIONERY = "S", _('Stacjonarna')
        MOBILLE = "M", _('Mobilna')

    typ = models.CharField(max_length=1, choices=TYP.choices)

    class TRUCK(models.TextChoices):
        MX_X = "M", _('MX-X')
        FM_X = "F", _('FX-X')
        EXV = "E", _('EKV')
        LTX = "L", _('LTX')
        INNY = "I", _('Inny')

    truck = models.CharField(max_length=1, choices=TYP.choices)
