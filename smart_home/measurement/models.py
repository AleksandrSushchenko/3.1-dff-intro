from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=128, verbose_name='Датчик')
    description = models.CharField(max_length=255, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    measurement_time = models.DateTimeField(auto_now_add=True, verbose_name='Время измерения')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return self.name