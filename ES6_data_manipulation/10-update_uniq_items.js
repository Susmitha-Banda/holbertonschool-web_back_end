/* Create a function named updateUniqueItems that returns an
updated map for all items with initial quantity at 1. */

export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  // iterate over key-value pairs
  for (const [key, value] of map) {
    // check if value is 1
    if (value === 1) {
      // update value to 100
      map.set(key, 100);
    }
  }
}
