from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

TYPES = (
    (1, "Website"),
    (2, "Android"),
    (3, "iOS"),
)
ROLE = (
    (1, "Design"),
    (2, "Backend"),
    (3, "Frontend"),
    (4, "Design & Backend"),
    (5, "Design & Frontend"),
    (6, "Backend & Frontend"),
    (10, "Design, Backend & Frontend"),

)
PURPOSE = (
    (1, "Personal"),
    (2, "Commercial"),
    (3, "Contract"),
)


class PostManager(models.Manager):
    def website(self, *args, **kwargs):
        return super(PostManager, self).filter(type_work=1)

    def android(self, *args, **kwargs):
        return super(PostManager, self).filter(type_work=2)

    def ios(self, *args, **kwargs):
        return super(PostManager, self).filter(type_work=3)


def upload_location(mywork, filename):
    return "%s/%s/%s" % (mywork.appName, mywork.type_work, filename)


class mywork(models.Model):
    appName = "Projects"
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)

    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field",
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    type_work = models.IntegerField(choices=TYPES)
    role = models.IntegerField(choices=ROLE)
    purpose = models.IntegerField(choices=PURPOSE)

    detail = models.TextField(blank=True, null=True, default="")
    youtube = models.TextField(blank=True, null=True, default="")
    item_url = models.TextField(blank=True, null=True, default="")

    created = models.DateField(auto_now=False, auto_now_add=False)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("work:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = mywork.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=mywork)
