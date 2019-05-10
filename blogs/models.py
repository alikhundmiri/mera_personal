from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone
from django.conf import settings

class PostBlogManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostBlogManager, self).filter(draft = False).filter(publish__lte = timezone.now())

def upload_location(Post, filename):
    return "%s/%s/%s" %(Post.app_name,Post.user, filename)

class taggers(models.Model):
    tag_name = models.CharField(max_length=20)
    tag_slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse("blogs:tag_list", kwargs={"slug" : self.tag_slug})

    class Meta:
        ordering = ["-tag_name",]
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Post(models.Model):
    app_name = "Blogs"
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=300)
    detail = models.TextField(max_length=23000)
    tags = models.ManyToManyField(taggers, null=True, blank=True)
    image = models.ImageField(
        upload_to=upload_location,
        null = True,
        blank = True,
        height_field = "height_field",
        width_field = "width_field",
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogs:detail", kwargs={"slug" : self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

    objects = PostBlogManager()

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_jd_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_jd_receiver, sender=Post)