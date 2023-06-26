class User:
    def __init__(self, name):
        self.name = name


class Student(User):
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name


class Teacher(User):
    def __init__(self, name, subject, classes):
        self.name = name
        self.subject = subject
        self.classes = classes


class ClassTeacher(User):
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name


class SchoolManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.class_teachers = []

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Wybierz opcję: ")
            if choice == "1":
                self.create_users()
            elif choice == "2":
                self.manage_users()
            elif choice == "3":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

    def display_main_menu(self):
        print("===== MENU GŁÓWNE =====")
        print("1. Utwórz")
        print("2. Zarządzaj")
        print("3. Koniec")

    def create_users(self):
        while True:
            self.display_create_menu()
            choice = input("Wybierz typ użytkownika lub wpisz 'koniec': ")
            if choice == "1":
                self.create_student()
            elif choice == "2":
                self.create_teacher()
            elif choice == "3":
                self.create_class_teacher()
            elif choice == "koniec":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

    def display_create_menu(self):
        print("===== TWORZENIE UŻYTKOWNIKÓW =====")
        print("1. Uczeń")
        print("2. Nauczyciel")
        print("3. Wychowawca")
        print("4. Koniec")

    def create_student(self):
        name = input("Podaj imię i nazwisko ucznia: ")
        class_name = input("Podaj nazwę klasy: ")
        student = Student(name, class_name)
        self.students.append(student)
        print("Utworzono ucznia.")

    def create_teacher(self):
        name = input("Podaj imię i nazwisko nauczyciela: ")
        subject = input("Podaj nazwę przedmiotu: ")
        classes = []
        while True:
            class_name = input("Podaj nazwę klasy (wpisz 'koniec' aby zakończyć): ")
            if class_name == "koniec":
                break
            classes.append(class_name)
        teacher = Teacher(name, subject, classes)
        self.teachers.append(teacher)
        print("Utworzono nauczyciela.")

    def create_class_teacher(self):
        name = input("Podaj imię i nazwisko wychowawcy: ")
        class_name = input("Podaj nazwę klasy: ")
        class_teacher = ClassTeacher(name, class_name)
        self.class_teachers.append(class_teacher)
        print("Utworzono wychowawcę.")

    def manage_users(self):
        while True:
            self.display_manage_menu()
            choice = input("Wybierz opcję lub wpisz 'koniec': ")
            if choice == "1":
                self.display_class()
            elif choice == "2":
                self.display_student()
            elif choice == "3":
                self.display_teacher()
            elif choice == "4":
                self.display_class_teacher()
            elif choice == "5":
                break
            else:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

    def display_manage_menu(self):
        print("===== ZARZĄDZANIE UŻYTKOWNIKAMI =====")
        print("1. Klasa")
        print("2. Uczeń")
        print("3. Nauczyciel")
        print("4. Wychowawca")
        print("5. Koniec")

    def display_class(self):
        class_name = input("Podaj nazwę klasy: ")
        print(f"===== Uczniowie klasy {class_name}=====")
        for student in self.students:
            if student.class_name == class_name:
                print(f"Imię i nazwisko: {student.name}")
        print(f"===== Wychowawca klasy {class_name} =====")
        for class_teacher in self.class_teachers:
            if class_teacher.class_name == class_name:
                print(f"Imię i nazwisko: {class_teacher.name}")

    def display_student(self):
        name = input("Podaj imię i nazwisko ucznia: ")
        print(f"===== Lekcje ucznia {name} =====")
        for teacher in self.teachers:
            for class_name in teacher.classes:
                for student in self.students:
                    if student.name == name and student.class_name == class_name:
                        print(f"Przedmiot: {teacher.subject}, Nauczyciel: {teacher.name}")

    def display_teacher(self):
        name = input("Podaj imię i nazwisko nauczyciela: ")
        print(f"===== Klasy nauczyciela {name} =====")
        for teacher in self.teachers:
            if teacher.name == name:
                for class_name in teacher.classes:
                    print(f"Klasa: {class_name}")

    def display_class_teacher(self):
        name = input("Podaj imię i nazwisko wychowawcy: ")
        print(f"===== Uczniowie prowadzeni przez wychowawcę {name} =====")
        for class_teacher in self.class_teachers:
            if class_teacher.name == name:
                class_name = class_teacher.class_name
                for student in self.students:
                    if student.class_name == class_name:
                        print(f"Imię i nazwisko: {student.name}")


# Uruchomienie programu
sms = SchoolManagementSystem()
sms.run()
