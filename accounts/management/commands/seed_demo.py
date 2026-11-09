from datetime import date, datetime, time
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from schools.models import School
from students.models import Student
from staff.models import Staff
from devices.models import Device
from attendance.models import DailyAttendance, AttendanceLog
from audit.models import AuditLog

User = get_user_model()


class Command(BaseCommand):
    help = "Seeds initial demo school, superuser, devices, staff, and demo students."

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("Seeding demo data for Attendance System..."))

        # 1. Demo School
        school, created = School.objects.get_or_create(
            code="AHS001",
            defaults={
                "name": "Alliance High School",
                "county": "Kiambu",
                "phone": "+254711223344",
                "email": "info@alliancehigh.ac.ke",
                "is_active": True,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created demo school: {school.name} ({school.code})"))
        else:
            self.stdout.write(self.style.WARNING(f"Demo school already exists: {school.name}"))

        # 2. Superuser (admin)
        admin_user, admin_created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@alliancehigh.ac.ke",
                "role": User.Role.SUPER_ADMIN,
                "school": school,
                "is_staff": True,
                "is_superuser": True,
            }
        )
        if admin_created:
            admin_user.set_password("adminpassword123")
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Created Super Admin: admin (password: adminpassword123)"))
        else:
            admin_user.role = User.Role.SUPER_ADMIN
            admin_user.school = school
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.set_password("adminpassword123")
            admin_user.save()
            self.stdout.write(self.style.WARNING("Updated Super Admin: admin (password: adminpassword123)"))

        # School Admin user
        school_admin, sa_created = User.objects.get_or_create(
            username="principal",
            defaults={
                "email": "principal@alliancehigh.ac.ke",
                "first_name": "David",
                "last_name": "Kariuki",
                "role": User.Role.SCHOOL_ADMIN,
                "school": school,
                "is_staff": True,
            }
        )
        if sa_created:
            school_admin.set_password("password123")
            school_admin.save()
            self.stdout.write(self.style.SUCCESS("Created School Admin: principal (password: password123)"))

        # Teacher user
        teacher_user, t_created = User.objects.get_or_create(
            username="teacher",
            defaults={
                "email": "teacher@alliancehigh.ac.ke",
                "first_name": "Sarah",
                "last_name": "Wambui",
                "role": User.Role.TEACHER,
                "school": school,
                "is_staff": False,
            }
        )
        if t_created:
            teacher_user.set_password("password123")
            teacher_user.save()
            self.stdout.write(self.style.SUCCESS("Created Teacher: teacher (password: password123)"))

        # 3. Biometric Devices
        gate_dev, _ = Device.objects.get_or_create(
            serial_number="ZK-GATE-001",
            defaults={
                "school": school,
                "name": "Main Gate Terminal (IN01-A)",
                "ip_address": "192.168.1.201",
                "location": "gate",
                "last_seen": timezone.now(),
                "is_active": True,
            }
        )
        dining_dev, _ = Device.objects.get_or_create(
            serial_number="ZK-DINE-002",
            defaults={
                "school": school,
                "name": "Dining Hall Reader (K40)",
                "ip_address": "192.168.1.202",
                "location": "dining",
                "last_seen": timezone.now(),
                "is_active": True,
            }
        )

        # 4. Demo Students
        demo_students_data = [
            {
                "admission_number": "10421",
                "full_name": "Kevin Mwangi Omondi",
                "gender": "M",
                "class_name": "Form 4",
                "stream": "East",
                "dorm": "Lenana House",
                "guardian_name": "James Mwangi",
                "guardian_phone": "+254722123456",
                "consent_given": True,
                "consent_date": date(2026, 1, 10),
            },
            {
                "admission_number": "10422",
                "full_name": "Brian Kiprop Cheruiyot",
                "gender": "M",
                "class_name": "Form 4",
                "stream": "West",
                "dorm": "Aggrey House",
                "guardian_name": "David Kiprop",
                "guardian_phone": "+254722123457",
                "consent_given": True,
                "consent_date": date(2026, 1, 10),
            },
            {
                "admission_number": "10550",
                "full_name": "Emmanuel Mutua Musyoka",
                "gender": "M",
                "class_name": "Form 3",
                "stream": "North",
                "dorm": "Wilberforce House",
                "guardian_name": "Paul Mutua",
                "guardian_phone": "+254733987654",
                "consent_given": True,
                "consent_date": date(2026, 1, 12),
            },
            {
                "admission_number": "10610",
                "full_name": "Faith Wanjiku Kamau",
                "gender": "F",
                "class_name": "Form 2",
                "stream": "South",
                "dorm": "Day Scholar",
                "guardian_name": "Grace Wanjiku",
                "guardian_phone": "+254711456789",
                "consent_given": True,
                "consent_date": date(2026, 1, 15),
            },
            {
                "admission_number": "10735",
                "full_name": "Samuel Odhiambo Otieno",
                "gender": "M",
                "class_name": "Form 1",
                "stream": "Blue",
                "dorm": "Smith House",
                "guardian_name": "John Otieno",
                "guardian_phone": "+254700345678",
                "consent_given": True,
                "consent_date": date(2026, 1, 20),
            },
        ]

        created_students = []
        for s_data in demo_students_data:
            adm = s_data["admission_number"]
            student, s_created = Student.objects.get_or_create(
                school=school,
                admission_number=adm,
                defaults={**s_data, "school": school}
            )
            created_students.append(student)
            if s_created:
                self.stdout.write(f"  Added student: {student.full_name} ({adm})")

        # 5. Demo Staff
        Staff.objects.get_or_create(
            school=school,
            staff_number="TSC-489201",
            defaults={
                "full_name": "Peter Kamau",
                "department": "Sciences & Physics",
                "phone": "+254722998877",
                "is_active": True,
            }
        )
        Staff.objects.get_or_create(
            school=school,
            staff_number="TSC-512034",
            defaults={
                "full_name": "Mary Achieng",
                "department": "Languages & English",
                "phone": "+254733445566",
                "is_active": True,
            }
        )

        # 6. Sample Attendance & Punches
        today = timezone.localdate()
        for idx, student in enumerate(created_students):
            status = DailyAttendance.Status.PRESENT if idx != 2 else DailyAttendance.Status.LATE
            first_in = time(6, 45 + idx * 5)
            DailyAttendance.objects.get_or_create(
                school=school,
                student=student,
                date=today,
                defaults={
                    "status": status,
                    "first_in": first_in,
                }
            )
            AttendanceLog.objects.get_or_create(
                device=gate_dev,
                user_id=student.admission_number,
                timestamp=timezone.now(),
                defaults={
                    "school": school,
                    "punch_type": "CHECK_IN",
                    "raw_payload": f"{student.admission_number}\t{timezone.now().strftime('%Y-%m-%d %H:%M:%S')}\t1\t0",
                }
            )

        # 7. Audit Log
        AuditLog.objects.create(
            user=admin_user,
            action="INITIALIZE_DEMO_SEED",
            object_repr=f"School: {school.name}",
            ip_address="127.0.0.1",
        )

        self.stdout.write(self.style.SUCCESS("\nDemo data seeding completed successfully!"))
        self.stdout.write("--------------------------------------------------")
        self.stdout.write(f"School:      {school.name} ({school.code})")
        self.stdout.write(f"Admin User:  admin  /  adminpassword123")
        self.stdout.write(f"Principal:   principal  /  password123")
        self.stdout.write(f"Teacher:     teacher  /  password123")
        self.stdout.write("--------------------------------------------------")
