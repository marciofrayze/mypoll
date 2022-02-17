from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    # By default, it displays only a str(). Let's make it a little better by defining a list_display.
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Giving each fields a title and ordering it. Also, add the Choices by default.
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # Adding filtering by pub_date on Admin page.
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
