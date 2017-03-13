from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fieldsets每个元组的第一个元素是字段集的标题
    #可以为每个字段集指定HTML样式类
    fieldsets = [('Hello', {'fields' : ['question_text']}), ('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']})]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
