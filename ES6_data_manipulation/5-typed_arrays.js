export default function createInt8TypedArray(length, position, value) {
  // Create a new ArrayBuffer of the specified length
  const buffer = new ArrayBuffer(length);
  // Create a DataView to manipulate the buffer
  const view = new DataView(buffer);
  // Check if the position is valid
  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }
  // Set the Int8 value at the specified position
  view.setInt8(position, value);
  // Return the DataView
  return view;
}
