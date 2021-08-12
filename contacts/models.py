from django.db import models
import uuid

STATUS = (
  (0, "Оформлена"),
  (1, "Принята"),
)

class Feedback(models.Model):

  def generateUUID():
    return str(uuid.uuid4().hex[:4].upper())

  
  name = models.CharField("Имя", max_length=120)
  phone = models.CharField("Телефон", max_length=30, default="")
  created_on = models.DateTimeField("Дата оформления", auto_now_add=True)
  number = models.CharField("Номер заказа", primary_key=True, default=generateUUID, max_length=50, editable=False)
  status = models.IntegerField(choices=STATUS, default=0)

  def __str__(self) -> str:
    return f'{self.name} - {self.number}'

  class Meta:
    ordering = ['-created_on']
    verbose_name = "Заявка"
    verbose_name_plural = "Заявки"
