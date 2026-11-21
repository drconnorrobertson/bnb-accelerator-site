import test from 'node:test';import assert from 'node:assert/strict';import {calculate,specs} from '../assets/operating-calculators.mjs';
const cases={
 payout:{input:{gross:1000,fees:100,refunds:50,cohost:200,adjustments:25,bank:625},expected:{expected:625,difference:0}},
 change:{input:{oldRent:600,oldFees:100,oldTax:50,newRent:800,newFees:100,newTax:60,paid:750,credit:20},expected:{original:750,revised:960,change:210,netDue:190}},
 allocation:{input:{cash:3000,excluded:500,bills:1000,reserve:2000},expected:{designatedBalance:-500,allocation:0,shortfall:500}},
 turnover:{input:{jobs:3,clean:80,inspect:10,travel:20,teams:2,window:180},expected:{required:290,capacity:360,slack:70,utilization:290/360*100,singleJob:90,balancedLaneMinutes:200,laneHeadroom:-20}},
 linen:{input:{beds:3,guests:4,laundry:1,spare:1,sheets:8,towels:10},expected:{rounds:3,requiredSheets:9,requiredTowels:12,sheetGap:1,towelGap:2}},
 reorder:{input:{use:2,nights:10,lead:2,safety:10,onHand:25,onOrder:15,targetWeeks:4,pack:12},expected:{weekly:20,reorderPoint:50,inventoryPosition:40,reorderGap:10,packs:5,coverageWeeks:1.25}},
 quote:{input:{calloutA:50,rateA:60,hoursA:2,materialsA:100,markupA:20,taxA:0,calloutB:30,rateB:70,hoursB:2,materialsB:90,markupB:10,taxB:0},expected:{totalA:290,totalB:269,difference:21}},
 fx:{input:{source:1000,rate:1.1,fee:5,received:1095},expected:{converted:1100,expected:1095,difference:0}}
};
for(const [name,{input,expected}] of Object.entries(cases)){
 test(name+' worked example',()=>assert.deepEqual(calculate(name,input),expected));
 test(name+' invalid field values',()=>{const key=Object.keys(specs[name])[0];for(const value of [undefined,NaN,Infinity,''])assert.throws(()=>calculate(name,{...input,[key]:value}));});
}
test('payout signed adjustments and currency fractions',()=>{const x=calculate('payout',{gross:0.3,fees:0.1,refunds:0,cohost:0,adjustments:-1,bank:1.2});assert.ok(Math.abs(x.difference)<1e-12);});
test('change credit and paid balance may produce refund',()=>assert.equal(calculate('change',{...cases.change.input,paid:1000,credit:20}).netDue,-60));
test('allocation exact reserve leaves zero',()=>assert.equal(calculate('allocation',{cash:3500,excluded:500,bills:1000,reserve:2000}).allocation,0));
test('turnover zero work, exact capacity and indivisible counts',()=>{assert.equal(calculate('turnover',{...cases.turnover.input,jobs:0}).required,0);assert.equal(calculate('turnover',{jobs:2,clean:80,inspect:10,travel:0,teams:1,window:180}).slack,0);for(const update of [{jobs:1.5},{teams:0},{window:0}])assert.throws(()=>calculate('turnover',{...cases.turnover.input,...update}));});
test('linen zero inventory requirements and count validation',()=>{assert.equal(calculate('linen',{...cases.linen.input,beds:0,guests:0}).sheetGap,0);assert.throws(()=>calculate('linen',{...cases.linen.input,laundry:-1}));});
test('reorder zero demand and full-pack rounding',()=>{const x=calculate('reorder',{...cases.reorder.input,use:0});assert.equal(x.coverageWeeks,null);assert.equal(x.packs,0);assert.equal(calculate('reorder',{...cases.reorder.input,onHand:90,onOrder:0}).packs,0);assert.throws(()=>calculate('reorder',{...cases.reorder.input,pack:0}));});
test('quote equal total and no hidden tax assumptions',()=>{assert.equal(calculate('quote',{...cases.quote.input,calloutB:51}).difference,0);assert.equal(calculate('quote',{...cases.quote.input,taxB:21}).difference,0);});
test('FX negative refund and invalid rate',()=>{assert.equal(calculate('fx',{source:-100,rate:1.2,fee:0,received:-120}).difference,0);assert.throws(()=>calculate('fx',{...cases.fx.input,rate:0}));});

for(const [name,{input}] of Object.entries(cases))test(name+' rejects negative nonnegative fields',()=>{for(const [key,[minimum]] of Object.entries(specs[name]))if(minimum!==null)assert.throws(()=>calculate(name,{...input,[key]:-1}));});
test('overflow cannot render an infinite result',()=>assert.throws(()=>calculate('fx',{source:1e308,rate:1e308,fee:0,received:0})));
import {readFileSync} from 'node:fs';
test('form fields and displayed metrics match calculator contracts',()=>{for(const item of JSON.parse(readFileSync(new URL('../content/operating-calculators.json',import.meta.url)))){assert.deepEqual(item.fields.map(f=>f.key).sort(),Object.keys(specs[item.kind]).sort());const result=calculate(item.kind,Object.fromEntries(item.fields.map(f=>[f.key,f.value])));assert.deepEqual(Object.keys(result).sort(),Object.keys(item.outputs).sort());}});
