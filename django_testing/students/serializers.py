from rest_framework import serializers

from students.models import Course, Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'birth_date')

        def validate(self, attrs):
            student_count = Student.objects.count()
            if student_count >= 20:
                raise serializers.ValidationError('Достигнуто максимальное значение 20')
            return attrs