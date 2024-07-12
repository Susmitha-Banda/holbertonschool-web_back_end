import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  // Getter and Setter

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    this.sqft = newSqft;
  }

  get floors() {
    return this._floors;
  }

  set floors(newFloors) {
    this.floors = newFloors;
  }

  // Overriding method named evacuationWarningMessage
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
