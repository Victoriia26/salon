from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=25)
    email = models.EmailField(max_length=60)


    def __str__(self):
        return f'{self.name}'

class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} --> {self.price}'

class Master(models.Model):
    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    specialization = models.CharField(max_length=50)
    branch_master = models.ForeignKey(Branch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='masters')

    def __str__(self):
        return f'{self.name}'

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    number = models.CharField(max_length=25, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.name}'

class Record(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='Филиал')
    service = models.ManyToManyField(Services, related_name='service_record', verbose_name='Услуги')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    record_time = models.DateTimeField(verbose_name='Время записи', unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

