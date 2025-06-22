from django.test import TestCase
from core.models import Teacher
from django.contrib.auth.models import User

# Create your tests here.
class TeacherModelTest(TestCase):

    def test_teacher_model_creation(self):
        # case one: user exists
        teacher = Teacher.objects.create(
            full_name="Hiraman Chaudhary",
            email="hiraman@gmail.com",
            department="BCA",
            phone_no=980000000,
            join_date='2025-02-02',
            #user=User.objects.get(id=12) # Assuming user with id 12 exists
            # assuming not user exists so creating new user
            user=User.objects.create_user(username="testuser", password="nepal@123")
        )
        try:
            # case one: user exists
            print("Case one: user exists with same username")
            self.assertEqual(teacher.full_name, "Hiraman Chaudhary")
            self.assertEqual(teacher.email, "hiraman@gmail.com")
            self.assertEqual(teacher.department, "BCA")
            self.assertEqual(teacher.phone_no, 980000000)
            self.assertEqual(teacher.join_date, '2025-02-02')
            self.assertEqual(teacher.user, User.objects.get(username="testuser")) # same user
            print("Case one: user exists with same username passed")
        except Exception as e:
            print("Error: ", e)
        
        try:
            # case one: user with different username
            print("Case two: user exists with different username")
            self.assertEqual(teacher.full_name, "Hiraman Chaudhary")
            self.assertEqual(teacher.email, "hiraman@gmail.com")
            self.assertEqual(teacher.department, "BCA")
            self.assertEqual(teacher.phone_no, 980000000)
            self.assertEqual(teacher.join_date, '2025-02-02')
            self.assertEqual(teacher.user, User.objects.get(username="nirmal")) # different user
        except Exception as e:
            print("Error: ", e)
            print("Error: ", "User must be same for teacher.")
        
        # case three: phone number length
        try:
            # case one: user with different username
            print("Case three: phone number length")
            self.assertEqual(teacher.full_name, "Hiraman Chaudhary")
            self.assertEqual(teacher.email, "hiraman@gmail.com")
            self.assertEqual(teacher.department, "BCA")
            self.assertEqual(teacher.phone_no, 9800000000) # phone number length is 9 but passing 10
            self.assertEqual(teacher.join_date, '2025-02-02')
            self.assertEqual(teacher.user, User.objects.get(username="testuser")) # same user
        except Exception as e:
            print("Error: ", e)
            print("Error: ", "Required phone number length is 9.")
