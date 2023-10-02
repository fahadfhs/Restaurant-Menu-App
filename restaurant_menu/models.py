from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes "),  # left side used by code, the other by the front end
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=2000, choices=MEAL_TYPE)
    # many-to-one relationship
    author = models.ForeignKey(User, on_delete=models.PROTECT)  # if old meals should be deleted, pass models.cascade
    # if you don't want to delete the user, use PROTECT, also another option models.SET_NULL--> if author is deleted,
    # the auto field will set john to null but meals will be saved
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)  # when cook adds item, the timestamp gets recorded
    date_updated = models.DateTimeField(auto_now=True)  # records when the item is updated

    def __str__(self):
        return self.meal
