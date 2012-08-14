from django.db import models
from django.contrib import admin
import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    #created = models.DateTimeField(auto_now_add=True,black=True)
    created= models.DateField(default=datetime.date.today)
    updated = models.DateTimeField(auto_now_add=True,blank=True)
	
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length = 100,blank = True)
    time_created = models.DateField(default = datetime.date.today)
    time_updated = models.DateField(default = datetime.date.today)
    key = models.ForeignKey(Post, related_name = 'post')
	
    def __uncode__(self):
        return u'%s' %self.body

		
class CommentsInline(admin.TabularInline):
    model = Comment
    max_num = 1
    raw_id_fields = ('key',)
    can_delete = False
    fk_name = 'key'
class PostAdmin(admin.ModelAdmin):
    def body_first60(self):
        return self.body[:60]
    list_display = ('title','created','updated')
    list_filter =('title',)
    search_fields = ('title','body')
    inlines = [
    CommentsInline,
    ]
class CommentAdmin(admin.ModelAdmin):
    def body_first60(self):
        return self.body[:60]
    list_display = ('author','time_created')	

class Person(models.Model):
    name = models.CharField(max_length=128,blank=True)
    email = models.EmailField(blank=True)

class Group(models.Model):
    name = models.CharField(max_length=128,blank=True)
    members = models.ManyToManyField(Person, related_name='company',through = 'Membership')

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField(blank=False)
    invite_reason= models.CharField(max_length=64)

class MembershipInline(admin.TabularInline):
    model = Membership
    extra =2
    max_num = 2

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    inlines = (MembershipInline,)
	

class GroupAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    #exclude = ('members',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Group,GroupAdmin)

# origin models edited add added membership
'''
class Person(models.Model):
    name = models.CharField(max_length=128,blank=True)
    email = models.EmailField(blank=True)

class Group(models.Model):
    name = models.CharField(max_length=128,blank=True)
    members = models.ManyToManyField(Person, related_name='company')

class MembershipInline(admin.TabularInline):
    model = Group.members.through
    max_num = 2

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    inlines = [
        MembershipInline,
	]

class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('members',)
'''

