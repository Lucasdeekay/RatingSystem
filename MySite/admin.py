from django.contrib import admin

from MySite.models import Course, Student, Rating, Ranking


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'department', 'lecturer')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name', 'matric_no', 'email')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'mode_of_teaching', 'communication', 'relationship')


class RankingAdmin(admin.ModelAdmin):
    list_display = ('course', 'points')


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Ranking, RankingAdmin)