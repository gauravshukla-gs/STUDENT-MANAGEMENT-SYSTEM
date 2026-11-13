"""
PS No. 99 - Student Record Management System
Rungta International Skills University - B.Tech CSE (IBM), First Semester

Concepts used:
  - Dictionary : records = {roll_no: (name, course, marks)}  -> unique roll numbers
  - Tuple      : each student's data is stored as an immutable tuple
  - List       : used to build sorted rows for the table display
  - CRUD       : one separate function per operation
"""

# Global storage: dictionary  { roll_no (int) : (name, course, marks) }
records = {}


# ---------------------------------------------------------------- helpers
def read_int(prompt):
    """Read an integer from the user. Returns None if input is not a number."""
    value = input(prompt).strip()
    try:
        return int(value)
    except ValueError:
        return None


def valid_marks(marks):
    """Marks must be a number between 0 and 100."""
    return marks is not None and 0 <= marks <= 100


# ------------------------------------------------------------------- CREATE
def add_record():
    roll = read_int("Enter Roll Number: ")
    if roll is None:
        print("Invalid roll number. Please enter digits only.")
        return
    name = input("Enter Name: ").strip()
    course = input("Enter Course: ").strip()
    marks = read_int("Enter Marks: ")

    if roll in records:                       # unique roll number check
        print(f"Roll number {roll} already exists.")
        return
    if not valid_marks(marks):                # marks range check
        print("Marks must be between 0 and 100.")
        return
    if not name or not course:
        print("Name and course cannot be empty.")
        return

    records[roll] = (name, course, marks)     # tuple stored in dictionary
    print(f"Record added: {roll} | {name} | {course} | {marks}")


# --------------------------------------------------------------------- READ
def view_records():
    if not records:
        print("No records to display.")
        return

    rows = [(roll,) + data for roll, data in sorted(records.items())]  # list of tuples
    line = "+" + "-" * 10 + "+" + "-" * 22 + "+" + "-" * 14 + "+" + "-" * 8 + "+"
    print(line)
    print(f"| {'Roll No':<8} | {'Name':<20} | {'Course':<12} | {'Marks':<6} |")
    print(line)
    for roll, name, course, marks in rows:
        print(f"| {roll:<8} | {name:<20} | {course:<12} | {marks:<6} |")
    print(line)
    print(f"Total records: {len(rows)}")


def search_record():
    roll = read_int("Enter Roll Number to search: ")
    if roll is None or roll not in records:
        print(f"Roll number {roll} not found.")
        return
    name, course, marks = records[roll]
    print(f"{roll} | {name} | {course} | {marks}")


# ------------------------------------------------------------------- UPDATE
def update_record():
    roll = read_int("Enter Roll Number to update: ")
    if roll is None or roll not in records:
        print(f"Roll number {roll} not found.")
        return
    marks = read_int("Enter new Marks: ")
    if not valid_marks(marks):
        print("Marks must be between 0 and 100.")
        return
    name, course, _ = records[roll]
    records[roll] = (name, course, marks)     # tuples are immutable -> replace
    print(f"Marks updated: {marks}")


# ------------------------------------------------------------------- DELETE
def delete_record():
    roll = read_int("Enter Roll Number to delete: ")
    if roll is None or roll not in records:
        print(f"Roll number {roll} not found.")
        return
    del records[roll]
    print(f"Record with roll number {roll} deleted.")


# --------------------------------------------------------------------- MENU
def show_menu():
    print("\n===== Student Record Management System =====")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Update Marks")
    print("5. Delete Record")
    print("6. Exit")


def main():
    actions = {
        "1": add_record,
        "2": view_records,
        "3": search_record,
        "4": update_record,
        "5": delete_record,
    }
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
