import assert from 'node:assert/strict';
import vm from 'node:vm';
import {addMetaPixel} from '../meta_pixel.mjs';
const home = addMetaPixel('<head></head><body class="home"></body>');
const ordinary = addMetaPixel('<head></head><body class="blog"></body>');
assert.match(home,/function afterPaint/);
assert.doesNotMatch(ordinary,/function afterPaint/);
assert.equal(addMetaPixel(home),home,'Pixel must not be added twice');
for (const readyState of ['loading','complete']) {
 const listeners={}, frames=[],timers=[],insertions=[];
 const window={addEventListener:(name,fn,opts)=>{assert.equal(opts.once,true);listeners[name]=fn},requestAnimationFrame:fn=>frames.push(fn),setTimeout:fn=>timers.push(fn)};
 const document={readyState,createElement:tag=>({tag}),getElementsByTagName:()=>[{parentNode:{insertBefore:node=>insertions.push(node)}}]};
 const context=vm.createContext({window,document});
 Object.defineProperty(context,'fbq',{get:()=>window.fbq});
 const code=home.match(/<script>([\s\S]*?)<\/script>/)[1];
 vm.runInContext(code,context);
 window.fbq('track','Lead');
 assert.equal(window.fbq.queue.length,3,'Initial and conversion events must remain queued');
 assert.equal(insertions.length,0);
 if(readyState==='loading'){assert.equal(frames.length,0);listeners.load()}
 assert.equal(frames.length,1);frames[0]();assert.equal(insertions.length,0);
 assert.equal(timers.length,1);timers[0]();
 assert.equal(insertions.length,1);assert.equal(insertions[0].src,'https://connect.facebook.net/en_US/fbevents.js');
 assert.equal(insertions[0].async,true);
 assert.equal(window.fbq.queue.length,3,'Loading must not drop pending events');
}
console.log('PASS: existing pixel queues events immediately, loads after paint, and is not duplicated; non-home loader unchanged.');
