from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

def ContentAddImages(content,images):
    contentHolder = content
    if images:
        for imageHolder in images:
            contentHolder = content.replace("![image]","<br><img src='%s' alt = '%s'><br>" % (imageHolder.image.url,imageHolder.image_alt))

    return contentHolder


class Post(models.Model):
    postFinishedChoices = (
        ('Y','Yes'),
        ('N','No'),
        )
    post_id = models.AutoField(primary_key = True)
    post_title = models.CharField(max_length = 255, unique=True)
    post_content = models.TextField()
    post_date = models.DateTimeField(auto_now = False, auto_now_add = True)
    post_slug = models.SlugField(unique = True)
    post_images = models.ManyToManyField('Image', blank=True, related_name='images')
    post_project = models.ForeignKey('Project',models.SET_NULL,blank=True,null=True, related_name='projectPost')
    post_finished = models.CharField(choices = postFinishedChoices,max_length =1)
    post_knowledge = models.CharField(choices = postFinishedChoices,max_length =1)

    class Meta:
        ordering = ["-post_date"]

    def post_content_html(self):
        return ContentAddImages(self.post_content,self.post_images.all())

    def save(self,*args, **kwargs):
        if not self.post_id:
            super(Post,self).save(*args,**kwargs)
        self.post_slug = slugify(self.post_title)
        self.post_content = ContentAddImages(self.post_content,self.post_images.all())
        super(Post,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.post_title

    def __str__(self):
        return self.post_title

class Tag(models.Model):
    tagTypeChoices = (
        ('PL','Programming Language'),
        ('OT','Other Technology'),
        ('TP','Time Period'),
        ('MT','Misc Tag'),)
    tagTypeColour = {'PL':'#637a8d',
                     'OT':'#8d6262',
                     'TP':'#628d78',
                     'MT':'#83628d',}
    tagTypeColourDefault = '#83628d'

    tag_id = models.AutoField(primary_key = True)
    tag_name = models.CharField(max_length = 255)
    tag_type = models.CharField(choices = tagTypeChoices,max_length = 2)
    tag_colour = models.CharField(max_length = 7,blank = True,null=True)

    def save(self,*args, **kwargs):
        if self.tag_type:
            self.tag_colour = self.tagTypeColour[self.tag_type]
            super(Tag,self).save(*args, **kwargs)
        else:
            self.tag_colour = self.tagTypeColourDefault
            super(Tag,self).save(*args, **kwargs)

    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ["tag_type"]

class Project(models.Model):
    projectStatusChoices = (('Complete','Complete'),
                            ('In Progress','In progress'),
                            ('Not Started','Not started'))

    projectStatusColour = {'Complete':'#628d78',
                          'In Progress':'#b6b649',
                          'Not Started':'#8d6262',}

    project_id = models.AutoField(primary_key = True)
    project_name = models.CharField(max_length = 255, unique = True)
    project_tags = models.ManyToManyField('Tag',blank=True, related_name = 'tags')
    project_slug = models.SlugField(unique = True)
    project_date = models.DateTimeField(auto_now = False, auto_now_add = True)
    project_status = models.CharField(choices = projectStatusChoices,max_length=11)
    project_status_colour = models.CharField(max_length = 7)
    project_colour = models.CharField(max_length = 7)
    project_summary = models.TextField()

    class Meta:
        ordering = ["-project_date"]

    def __str__(self):
        return self.project_name

    def save(self,*args, **kwargs):
        if not self.project_id:
            super(Project,self).save(*args,**kwargs)
        self.project_slug = slugify(self.project_name)
        self.project_status_colour = self.projectStatusColour[self.project_status]
        super(Project,self).save(*args, **kwargs)

class Image(models.Model):
    image_id = models.AutoField(primary_key= True)
    image_name = models.CharField(max_length = 255)
    image = models.ImageField()
    image_alt = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.image_name

    def __str__(self):
        return self.image_name
