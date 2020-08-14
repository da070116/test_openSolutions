from django.db import models
from tokenusers.models import Visitor


class Order(models.Model):
    date = models.DateField()
    person = models.ForeignKey(Visitor, on_delete=models.CASCADE, to_field="username")
    reason = models.CharField(max_length=255)
    answer_set = (
        ("undefined", "undefined"),
        ("allowed", "allowed"),
        ("restricted", "restricted"),
    )
    answer = models.CharField(choices=answer_set, max_length=25, default="undefined")

    def __str__(self):
        return f" Request on {self.date} from {self.person}"
