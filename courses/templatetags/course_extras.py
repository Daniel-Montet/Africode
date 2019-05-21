from django import template
from courses.models import Course

register  = template.Library()

@register.simple_tag
def newest_course():
    ''' Gets the most recent course that was added to the library. '''
    return Course.objects.filter(published=True).latest('created_at')
    
@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    ''' Returns dictionary of courses to display as navigation pane '''
    courses = Course.objects.filter(published=True).values()[:5]
    return {'courses': courses}
