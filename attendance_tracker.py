import json

class AttendanceTracker:
    def __init__(self):
        self.attendance = {}

    def mark_attendance(self, student_id):
        if student_id in self.attendance:
            print("Student with ID", student_id, "is already marked present.")
        else:
            self.attendance[student_id] = True
            print("Student with ID", student_id, "marked present.")

    def check_attendance(self, student_id):
        if student_id in self.attendance:
            print("Student with ID", student_id, "is present.")
        else:
            print("Student with ID", student_id, "is absent.")

    def view_attendance(self):
        print("Attendance:")
        for student_id, present in self.attendance.items():
            status = "present" if present else "absent"
            print("Student ID:", student_id, "-", status)

    def save_attendance(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.attendance, file)
        print("Attendance data saved to", filename)

    def load_attendance(self, filename):
        try:
            with open(filename, 'r') as file:
                self.attendance = json.load(file)
            print("Attendance data loaded from", filename)
        except FileNotFoundError:
            print("File not found. No attendance data loaded.")

    def generate_attendance_report(self, report_filename):
        with open(report_filename, 'w') as report_file:
            report_file.write("Attendance Report:\n")
            for student_id, present in self.attendance.items():
                status = "Present" if present else "Absent"
                report_file.write(f"Student ID: {student_id} - {status}\n")
        print("Attendance report generated:", report_filename)


# Example usage:
tracker = AttendanceTracker()

# Mark attendance
tracker.mark_attendance(101)
tracker.mark_attendance(102)
tracker.mark_attendance(101)  # Already marked present

# Check attendance
tracker.check_attendance(101)
tracker.check_attendance(103)  # Not marked yet

# View overall attendance
tracker.view_attendance()

# Save attendance data to a file
tracker.save_attendance('attendance_data.json')

# Load attendance data from a file
tracker.load_attendance('attendance_data.json')

# Generate attendance report
tracker.generate_attendance_report('attendance_report.txt')
