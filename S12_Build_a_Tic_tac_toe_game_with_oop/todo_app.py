from datetime import datetime
from enum import Enum
from typing import List, Optional


class Priority(Enum):
    """Enum for to-do priorities"""

    URGENT = "Urgent"
    INTERMEDIATE = "Intermediate"
    OPTIONAL = "Optional"


class Category(Enum):
    """Enum for to-do categories"""

    PERSONAL = "Personal"
    ACADEMIC = "Academic"
    WORK = "Work"
    LEISURE = "Leisure"


class Course:
    """
    Represents a university course.

    Attributes:
        code (str): The course code (e.g., "CS101")
        professor (str): The name of the professor teaching the course
        start_time (str): The start time of the course (e.g., "09:00")
        end_time (str): The end time of the course (e.g., "10:30")
        classroom (str): The classroom location (e.g., "Room 101")
    """

    def __init__(
        self, code: str, professor: str, start_time: str, end_time: str, classroom: str
    ):
        self.code = code
        self.professor = professor
        self.start_time = start_time
        self.end_time = end_time
        self.classroom = classroom

    def __str__(self):
        return f"{self.code} - {self.professor} ({self.start_time}-{self.end_time}) in {self.classroom}"

    def __repr__(self):
        return f"Course(code='{self.code}', professor='{self.professor}')"


class Todo:
    """
    Represents a to-do item.

    Attributes:
        title (str): The title/name of the to-do
        description (str): A description of the to-do
        due_date (datetime): The due date for the to-do
        priority (Priority): The priority level (Urgent, Intermediate, Optional)
        category (Category): The category (Personal, Academic, Work, Leisure)
        is_complete (bool): Whether the to-do has been completed
        course (Course, optional): Associated course if it's academic-related
        classroom (str, optional): Associated classroom if it's academic-related
    """

    def __init__(
        self,
        title: str,
        description: str,
        due_date: datetime,
        priority: Priority,
        category: Category,
        course: Optional[Course] = None,
        classroom: Optional[str] = None,
    ):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.is_complete = False
        self.course = course
        self.classroom = classroom
        self.created_date = datetime.now()

    def mark_complete(self):
        """Mark the to-do as complete"""
        self.is_complete = True
        print(f"✅ To-do '{self.title}' marked as complete!")

    def mark_incomplete(self):
        """Mark the to-do as incomplete"""
        self.is_complete = False
        print(f"↩️ To-do '{self.title}' marked as incomplete!")

    def update_priority(self, new_priority: Priority):
        """Update the priority of the to-do"""
        self.priority = new_priority
        print(f"📌 Priority updated to {new_priority.value}")

    def update_due_date(self, new_date: datetime):
        """Update the due date of the to-do"""
        self.due_date = new_date
        print(f"📅 Due date updated to {new_date.strftime('%Y-%m-%d')}")

    def assign_course(self, course: Course):
        """Assign a course to the to-do"""
        if self.category == Category.ACADEMIC:
            self.course = course
            print(f"📚 Course {course.code} assigned to '{self.title}'")
        else:
            print("⚠️ Can only assign courses to academic to-dos")

    def is_overdue(self):
        """Check if the to-do is overdue"""
        return datetime.now() > self.due_date and not self.is_complete

    def __str__(self):
        status = "✅" if self.is_complete else "⭕"
        course_info = f" [{self.course.code}]" if self.course else ""
        return f"{status} {self.title}{course_info} - {self.priority.value} ({self.category.value}) - Due: {self.due_date.strftime('%Y-%m-%d')}"

    def __repr__(self):
        return f"Todo(title='{self.title}', priority={self.priority.name})"


class Student:
    """
    Represents a student with to-dos and courses.

    Attributes:
        name (str): The student's name
        student_id (str): The student's ID
        todos (List[Todo]): List of to-dos
        courses (List[Course]): List of enrolled courses
    """

    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.todos: List[Todo] = []
        self.courses: List[Course] = []

    def add_todo(self, todo: Todo):
        """Add a new to-do to the list"""
        self.todos.append(todo)
        print(f"✨ To-do '{todo.title}' added!")

    def remove_todo(self, todo: Todo):
        """Remove a completed to-do from the list"""
        if todo in self.todos:
            self.todos.remove(todo)
            print(f"🗑️ To-do '{todo.title}' removed!")
        else:
            print(f"⚠️ To-do '{todo.title}' not found in list")

    def add_course(self, course: Course):
        """Add a new course to the student's schedule"""
        self.courses.append(course)
        print(f"📚 Course {course.code} added!")

    def remove_course(self, course: Course):
        """Remove a course from the student's schedule"""
        if course in self.courses:
            self.courses.remove(course)
            print(f"📚 Course {course.code} removed!")
        else:
            print(f"⚠️ Course {course.code} not found")

    def get_pending_todos(self) -> List[Todo]:
        """Get all incomplete to-dos"""
        return [todo for todo in self.todos if not todo.is_complete]

    def get_completed_todos(self) -> List[Todo]:
        """Get all completed to-dos"""
        return [todo for todo in self.todos if todo.is_complete]

    def get_todos_by_category(self, category: Category) -> List[Todo]:
        """Get to-dos filtered by category"""
        return [todo for todo in self.todos if todo.category == category]

    def get_todos_by_priority(self, priority: Priority) -> List[Todo]:
        """Get to-dos filtered by priority"""
        return [todo for todo in self.todos if todo.priority == priority]

    def get_urgent_todos(self) -> List[Todo]:
        """Get all urgent to-dos"""
        return self.get_todos_by_priority(Priority.URGENT)

    def get_overdue_todos(self) -> List[Todo]:
        """Get all overdue to-dos"""
        return [todo for todo in self.todos if todo.is_overdue()]

    def get_course_by_code(self, code: str) -> Optional[Course]:
        """Get a course by its code"""
        for course in self.courses:
            if course.code == code:
                return course
        return None

    def display_todos(self):
        """Display all to-dos"""
        print(f"\n{'='*50}")
        print(f"📋 To-dos for {self.name} ({len(self.todos)} total)")
        print(f"{'='*50}")
        if self.todos:
            for i, todo in enumerate(self.todos, 1):
                print(f"{i}. {todo}")
        else:
            print("No to-dos yet!")

    def display_courses(self):
        """Display all enrolled courses"""
        print(f"\n{'='*50}")
        print(f"📚 Courses for {self.name} ({len(self.courses)} total)")
        print(f"{'='*50}")
        if self.courses:
            for i, course in enumerate(self.courses, 1):
                print(f"{i}. {course}")
        else:
            print("No courses enrolled!")

    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"

    def __repr__(self):
        return f"Student(name='{self.name}', student_id='{self.student_id}')"


# Example usage
if __name__ == "__main__":
    # Create a student
    student = Student("Marco Silva", "S123456")
    print(student)
    print()

    # Create courses
    cs101 = Course("CS101", "Dr. Johnson", "09:00", "10:30", "Room 101")
    math201 = Course("MATH201", "Prof. Smith", "11:00", "12:30", "Room 205")

    # Add courses to student
    student.add_course(cs101)
    student.add_course(math201)
    print()

    # Create to-dos
    todo1 = Todo(
        "Study for CS101 exam",
        "Review chapters 1-5 and practice problems",
        datetime(2026, 2, 28),
        Priority.URGENT,
        Category.ACADEMIC,
        course=cs101,
    )

    todo2 = Todo(
        "Buy groceries",
        "Milk, bread, eggs, and vegetables",
        datetime(2026, 2, 20),
        Priority.INTERMEDIATE,
        Category.PERSONAL,
    )

    todo3 = Todo(
        "Complete project assignment",
        "Implement the to-do list app",
        datetime(2026, 2, 25),
        Priority.URGENT,
        Category.ACADEMIC,
        course=cs101,
    )

    # Add to-dos to student
    student.add_todo(todo1)
    student.add_todo(todo2)
    student.add_todo(todo3)
    print()

    # Display information
    student.display_courses()
    print()
    student.display_todos()
    print()

    # Mark a to-do as complete
    todo2.mark_complete()
    print()

    # Get pending to-dos
    pending = student.get_pending_todos()
    print(f"\n⭕ Pending to-dos: {len(pending)}")
    print()

    # Get urgent to-dos
    urgent = student.get_urgent_todos()
    print(f"🔥 Urgent to-dos: {len(urgent)}")
    for todo in urgent:
        print(f"  - {todo}")
