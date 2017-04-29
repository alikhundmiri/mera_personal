from django.db import models

TYPES = (
    (1, "Industrial Exposure & Experience"),
    (2, "Alma Mater"),
    (3, "Achievement"),
    (4, "Area of Interest"),

    (5, "Educational Activities"),
    (6, "Work In Process"),
    (7, "Activities at the moment"),
    (8, "Personality, Qualities & Skills"),

    (9, "Guest Lectures"),
    (10, "Books Author"),
    (11, "Special Recognised"),
    (12, "Competitions"),

    (13, "field 13"),
    (14, "field 14"),
)
class SortManager(models.Manager):
    def iee(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 1)
    def alma(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 2)
    def achievements(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 3)
    def aoi(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 4)
    def eduActiv(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 5)
    def workip(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 6)
    def nowWork(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 7)
    def skill(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 8)
    def lectures(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 9)
    def books(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 10)
    def special(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 11)
    def competition(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 12)
    def blank1(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 13)
    def blank2(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 14)

class document_data(models.Model):
    cat_0 = models.IntegerField(choices=TYPES)
    cat_1 = models.CharField(max_length=100, blank=True, null=True, default="")
    cat_2 = models.CharField(max_length=100, blank=True, null=True, default="")
    cat_3 = models.CharField(max_length=100, blank=True, null=True, default="")
    cat_4 = models.CharField(max_length=100, blank=True, null=True, default="")
    cat_5 = models.CharField(max_length=100, blank=True, null=True, default="")
    cat_6 = models.CharField(max_length=100, blank=True, null=True, default="")
    cat_7 = models.CharField(max_length=100, blank=True, null=True, default="")
    cat_8 = models.CharField(max_length=100, blank=True, null=True, default="")
    cat_9 = models.CharField(max_length=100, blank=True, null=True, default="")

    time_of_record = models.DateField(auto_now=False, auto_now_add=False)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = SortManager()

    def __str__(self):
        return self.cat_1

    class Meta:
        ordering = ["-time_of_record","-timestamp", "-updated"]

