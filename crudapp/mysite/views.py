from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Avg


def home(request):
    """
    Rendert de homepage.
    """
    return render(request, 'index.html', {})

def contact(request):
    kleur = 'groen'
    return render(request, 'contact.html', {'kleur': kleur})

def about(request):
    # Studentenlijst (kan gebruikt worden voor leeftijdscheck)
    students = {
        'student_0': 12,
        'student_1': 16,
        'student_2': 18,
        'student_3': 15,
        'student_4': 21,
        'student_5': 20
    }

    # Teamleden dynamisch laden
    team = [
        {
            'name': 'Jan de Vries',
            'role': 'CEO & Oprichter',
            'bio': 'Met meer dan 10 jaar ervaring in de industrie, leidt Jan ons bedrijf met een duidelijke visie en een passie voor duurzame oplossingen.',
            'image': 'https://via.placeholder.com/150'
        },
        {
            'name': 'Sophie Jansen',
            'role': 'Hoofd Ontwikkeling',
            'bio': 'Sophie is de drijvende kracht achter al onze innovaties. Haar creativiteit en technische expertise zorgen ervoor dat we altijd voorop lopen.',
            'image': 'https://via.placeholder.com/150'
        }
    ]

    context = {
        'students': students,
        'team': team
    }
    return render(request, 'about.html', context)

def students(request):
    # Lijst van studenten met naam en cijfer
    students = [
        {'name': 'Anna', 'grade': 88},
        {'name': 'Bram', 'grade': 72},
        {'name': 'Clara', 'grade': 95},
        {'name': 'David', 'grade': 50},
        {'name': 'Eva', 'grade': 60},
        {'name': 'Finn', 'grade': 82},
        {'name': 'Gijs', 'grade': 40},
        {'name': 'Hanne', 'grade': 77},
        {'name': 'Iris', 'grade': 91},
        {'name': 'Joris', 'grade': 55},
    ]

    # Sorteer studenten alfabetisch op naam
    students_sorted = sorted(students, key=lambda x: x['name'])

    # Bereken gemiddeld cijfer
    avg_grade = sum(student['grade'] for student in students_sorted) / len(students_sorted)

    context = {
        'students': students_sorted,
        'avg_grade': avg_grade
    }
    return render(request, 'students.html', context)




def student_list(request):
    """Haalt alle studenten op, sorteert ze en berekent het gemiddelde cijfer."""
    students = Student.objects.order_by('name')
    avg_grade = students.aggregate(Avg('grade'))['grade__avg']

    context = {
        'students': students,
        'avg_grade': avg_grade
    }
    return render(request, 'students/student_list.html', context)


def add_student(request):
    """Voegt een nieuwe student toe via een formulier."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})


def update_student(request, pk):
    """Werkt de gegevens van een bestaande student bij."""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form})


def delete_student(request, pk):
    """Verwijdert een student na bevestiging."""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})