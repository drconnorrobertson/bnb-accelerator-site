export const specs={
 payout:{gross:[0],fees:[0],refunds:[0],cohost:[0],adjustments:[null],bank:[null]},
 change:{oldRent:[0],oldFees:[0],oldTax:[0],newRent:[0],newFees:[0],newTax:[0],paid:[0],credit:[0]},
 allocation:{cash:[0],excluded:[0],bills:[0],reserve:[0]},
 turnover:{jobs:[0,true],clean:[0],inspect:[0],travel:[0],teams:[1,true],window:[0,false,true]},
 linen:{beds:[0,true],guests:[0,true],laundry:[0,true],spare:[0,true],sheets:[0,true],towels:[0,true]},
 reorder:{use:[0],nights:[0],lead:[0],safety:[0],onHand:[0],onOrder:[0],targetWeeks:[0],pack:[1,true]},
 quote:{calloutA:[0],rateA:[0],hoursA:[0],materialsA:[0],markupA:[0],taxA:[0],calloutB:[0],rateB:[0],hoursB:[0],materialsB:[0],markupB:[0],taxB:[0]},
 fx:{source:[null],rate:[0,false,true],fee:[0],received:[null]}
};
export function calculate(kind,input){
 const spec=specs[kind];if(!spec)throw new Error('Unknown calculator.');
 for(const [key,[min,integer,positive]] of Object.entries(spec)){
  const value=input[key];if(typeof value!=='number'||!Number.isFinite(value))throw new Error('Enter a finite number in every field.');
  if(min!==null&&value<min)throw new Error('A value is below its permitted minimum.');
  if(integer&&(!Number.isSafeInteger(value)||value>1000000))throw new Error('Counts must be whole numbers no greater than 1,000,000.');
  if(positive&&value<=0)throw new Error('The window or exchange rate must be greater than zero.');
 }
 const v=input;let result;
 if(kind==='payout'){const expected=v.gross-v.fees-v.refunds-v.cohost-v.adjustments;result={expected,difference:v.bank-expected};}
 if(kind==='change'){const original=v.oldRent+v.oldFees+v.oldTax,revised=v.newRent+v.newFees+v.newTax;result={original,revised,change:revised-original,netDue:revised-v.credit-v.paid};}
 if(kind==='allocation'){const remainder=v.cash-v.excluded-v.bills-v.reserve;result={designatedBalance:remainder,allocation:Math.max(0,remainder),shortfall:Math.max(0,-remainder)};}
 if(kind==='turnover'){const task=v.clean+v.inspect,required=v.jobs*task+Math.max(0,v.jobs-v.teams)*v.travel,capacity=v.teams*v.window;const laneJobs=Math.ceil(v.jobs/v.teams),lane=laneJobs*task+Math.max(0,laneJobs-1)*v.travel;result={required,capacity,slack:capacity-required,utilization:required/capacity*100,singleJob:task,balancedLaneMinutes:lane,laneHeadroom:v.window-lane};}
 if(kind==='linen'){const rounds=1+v.laundry+v.spare,requiredSheets=v.beds*rounds,requiredTowels=v.guests*rounds;result={rounds,requiredSheets,requiredTowels,sheetGap:Math.max(0,requiredSheets-v.sheets),towelGap:Math.max(0,requiredTowels-v.towels)};}
 if(kind==='reorder'){const weekly=v.use*v.nights,point=weekly*v.lead+v.safety,target=weekly*v.targetWeeks+v.safety,position=v.onHand+v.onOrder;result={weekly,reorderPoint:point,inventoryPosition:position,reorderGap:Math.max(0,point-position),packs:Math.ceil(Math.max(0,target-position)/v.pack),coverageWeeks:weekly===0?null:v.onHand/weekly};}
 if(kind==='quote'){const totalA=v.calloutA+v.rateA*v.hoursA+v.materialsA*(1+v.markupA/100)+v.taxA,totalB=v.calloutB+v.rateB*v.hoursB+v.materialsB*(1+v.markupB/100)+v.taxB;result={totalA,totalB,difference:totalA-totalB};}
 if(kind==='fx'){const converted=v.source*v.rate,expected=converted-v.fee;result={converted,expected,difference:v.received-expected};}
 if(Object.values(result).some(x=>x!==null&&!Number.isFinite(x)))throw new Error('These inputs exceed the calculator range.');
 return result;
}
function setup(){
 const form=document.querySelector('[data-operating-calculator]');if(!form)return;
 const kind=form.dataset.operatingCalculator,output=document.querySelector('[data-results]'),error=document.querySelector('[data-error]');
 const labels=JSON.parse(document.querySelector('[data-output-labels]').textContent);
 const render=()=>{
  error.textContent='';output.replaceChildren();
  try{
   const values={};for(const field of form.querySelectorAll('input[data-field]')){if(field.value.trim()==='')throw new Error('Complete every field; enter 0 where appropriate.');values[field.dataset.field]=field.valueAsNumber;}
   const results=calculate(kind,values);const dl=document.createElement('dl');
   for(const [key,value] of Object.entries(results)){const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=labels[key][0];dd.textContent=value===null?'Not defined when use is zero':value.toLocaleString('en-US',{minimumFractionDigits:labels[key][1]==='count'?0:2,maximumFractionDigits:labels[key][1]==='count'?0:2})+' '+labels[key][2];dl.append(dt,dd);}
   output.append(dl);
  }catch(e){error.textContent=e.message;}
 };
 form.addEventListener('submit',event=>{event.preventDefault();render();});
 form.addEventListener('input',()=>{output.replaceChildren();error.textContent='';});
 document.querySelector('[data-reset-example]').addEventListener('click',()=>{form.reset();render();});render();
}
if(typeof document!=='undefined'){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',setup);else setup();}
