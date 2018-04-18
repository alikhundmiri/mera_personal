from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class redirect_elements(models.Model):
    appName = "redirect_elements"
    title = models.CharField(max_length=120, blank=False, null=False)   #<-- the name of the redirect
    slug = models.SlugField(unique=True, blank=True, null=True)         #<-- The slugified version of title
    count = models.PositiveIntegerField(default=0)                      #<-- count of how many times the links were clicked
    redirect_url = models.URLField(blank=False, null=False)             #<-- the redirecting URL.

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)   #<-- time of edit
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) #<-- time of creation

    
    def __str__(self):
        return self.slug

    # def get_absolute_url(self):
    #     return reverse("work:hosted", kwargs={"slug": self.slug})
    def redirect_user(self):
        return reverse('customredirect:redirect_link', kwargs={'slug':self.slug})
    class Meta:
        ordering = ["-timestamp", "-updated"]
        verbose_name = "Redirect Element"
        verbose_name_plural = "Redirect Elements"



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = redirect_elements.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s_%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=redirect_elements)
