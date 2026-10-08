const assert = require('node:assert/strict');
const {calculateRevpar: calc} = require('../assets/revpar-calculator.js');
assert.deepEqual(calc(4200,21,30), {revpar:140,adr:200,occupancy:70});
assert.deepEqual(calc(0,0,30), {revpar:0,adr:null,occupancy:0});
assert.equal(calc(4200,21,24).revpar,175);
assert.equal(calc(8700,40,59).revpar.toFixed(2),'147.46');
for (const args of [[10,0,30],[-1,1,30],[10,31,30],[10,1,0],[Infinity,1,30],[10,1.5,30],[10,1,30.5]]) assert.throws(()=>calc(...args),RangeError);
console.log('PASS: RevPAR reconciliation, blocked calendar, weighted periods, no bookings and invalid inputs.');
