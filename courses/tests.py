from django.test import TestCase
from django.utils import timezone

from .models import Course, Step
# Create your tests here.

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title= "Python regular Expressions",
            description = "Learn to write regular expressions"
        )
        now = timezone.now()
        self.course=course
        self.assertLess(course.created_at, now)

    # def test_step_creation(self):
    #     step = Step.objects.create(
    #         title = "Sample test",
    #         description = "This is a sample test",
    #         content = "This is some sample content",
    #         course= self.course
    #     )
    #     now = timezone.now()
    #     self.assertLess(course.created_at, now)
