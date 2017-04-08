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
        return super(SortManager, self).filter(cat_0 = 0)
    def alma(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def achievements(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def aoi(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def eduActiv(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def workip(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def nowWork(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def skill(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def lectures(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def books(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def special(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def competition(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def blank1(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)
    def blank2(self, *args, **kwargs):
        return super(SortManager, self).filter(cat_0 = 0)

class document_data(models.Model):
    cat_0 = models.IntegerField(choices=TYPES)
    cat_1 = models.TextField(blank=True, null=True, default="")
    cat_2 = models.TextField(blank=True, null=True, default="")
    cat_3 = models.TextField(blank=True, null=True, default="")
    cat_4 = models.TextField(blank=True, null=True, default="")
    cat_5 = models.TextField(blank=True, null=True, default="")
    cat_6 = models.TextField(blank=True, null=True, default="")
    cat_7 = models.TextField(blank=True, null=True, default="")
    cat_8 = models.TextField(blank=True, null=True, default="")
    cat_9 = models.TextField(blank=True, null=True, default="")

    time_of_record = models.DateField(auto_now=False, auto_now_add=False)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = SortManager()

    def __str__(self):
        return self.cat_1

    class Meta:
        ordering = ["-time_of_record","-timestamp", "-updated"]

