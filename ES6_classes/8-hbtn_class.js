export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Getter & Setter

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  set size(newSize) {
    this._size = newSize;
  }

  set location(newLocation) {
    this._location = newLocation;
  }

  // Methods

  valueOf() {
    return `${this._size}`;
  }

  toString() {
    return `${this._location}`;
  }
}
