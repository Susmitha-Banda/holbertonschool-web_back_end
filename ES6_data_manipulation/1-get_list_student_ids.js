export default function getListStudentIds(array) {
  let array2 = [];

  // check if the argument passed in is NOT an array
  if (!Array.isArray(array)) {
  // return an empty array
    return [];
  // if the argument passed in is an array use map function
  }
  // Iterate over each element of the array and extract the id
  array2 = array.map((elementofarray) => elementofarray.id);
  return array2;
}
