// return an array of students for a specific city with their new grade

export default function updateStudentGradeByCity(array, city, newGrades) {
  // filter students by city
  const filteredStudents = array.filter(({ location }) => location === city);
  // Iterate (map) over the filtered students to update their grades
  const updatedStudents = filteredStudents.map((student) => {
    const studentGrades = newGrades.filter((grade) => grade.studentId === student.id);
    const newStudent = student;
    // check if student has a grade, if not it should be N/A
    if (studentGrades.length > 0) {
      newStudent.grade = studentGrades[0].grade;
    } else {
      newStudent.grade = 'N/A';
    }
    return newStudent;
  });
  return updatedStudents;
}
