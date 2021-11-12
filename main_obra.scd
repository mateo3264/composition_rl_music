s.boot
s.makeWindow;
s.meter;

(
~sins = [\sin1,\sin3,\sin4,\sin5,\sin6,\sin7];

//Organismo
SynthDef.new(\spe1,{
|freq=550,gesture=#[1,1,1,1,1,1,1],times=#[0.1,0.1,0.1,0.1,0.1,0.1],amp=0.1,nHarms=0,t_ga=1,out=0,curva='step',pan,
rateOfChange=1,se=1|
var envFreq,envPan,envAmp,sig,sig2,sigs,envChange;
envFreq = EnvGen.kr(
Env.new(
gesture[..gesture.size]*freq,times,curve:curva),t_ga);
//envPan = EnvGen.kr(Env.circle([{Rand(-1,1)},{Rand(-1,1)}],[{Rand(1,5)},{Rand(1,5)}]));
envAmp = EnvGen.kr(Env.circle([0.01*amp,amp],[{Rand(2,5)}]));
sig = Blip.ar(envFreq,nHarms);
sig = FreeVerb.ar(sig,0.6,0.6,0.6);

sig = Pan2.ar(sig,pan);
sig = sig*envAmp;
sig2 = VarSaw.ar(envFreq);
sig2 = FreeVerb.ar(sig2,0.6,0.6,0.6);
sig2 = Pan2.ar(sig2,pan);
sig2 = sig2*envAmp;

envChange = EnvGen.kr(Env.circle([se,1,se],
[rateOfChange,rateOfChange]));

sigs = [Pan2.ar(XFade2.ar(sig,sig2,envChange
),pan),sig];


Out.ar(out,XFade2.ar(sig2,sig,envChange));
}).add;



SynthDef.new(\spe2,{
|freq=550,gesture=#[1,1,1,1,1,1,1],times=#[0.1,0.1,0.1,0.1,0.1,0.1],amp=0.1,nHarms=0,t_ga=1,out=0,curva='step',pan,
rateOfChange=1,se=1|
var envFreq,envPan,envAmp,sig,sig2,sigs,envChange;
envFreq = EnvGen.kr(
Env.new(
gesture[..gesture.size]*freq,times,curve:curva),t_ga);
//envPan = EnvGen.kr(Env.circle([{Rand(-1,1)},{Rand(-1,1)}],[{Rand(1,5)},{Rand(1,5)}]));
envAmp = EnvGen.kr(Env.perc(0.1,0.99,amp),gate:t_ga,doneAction:0);
sig = Blip.ar(envFreq,nHarms);
sig = FreeVerb.ar(sig,0.6,0.6,0.6);

sig = Pan2.ar(sig,pan);
sig = sig*envAmp;
sig2 = VarSaw.ar(envFreq);
sig2 = FreeVerb.ar(sig2,0.6,0.6,0.6);
sig2 = Pan2.ar(sig2,pan);
sig2 = sig2*envAmp;

envChange = EnvGen.kr(Env.circle([se,1,se],
[rateOfChange,rateOfChange]));

sigs = [Pan2.ar(XFade2.ar(sig,sig2,envChange
),pan),sig];


Out.ar(out,XFade2.ar(sig2,sig,envChange));
}).add;



SynthDef.new(\spe3,{
|freq,lowFilterThreshold=440,noiseChange=3,midRange=40,amp,decay,density=10,timeToLive=10,pan=0|
var noiseGen,decayEnv,sig,sig2,chain,chain2,sigs,which_sig;

noiseGen = LFNoise1.kr(
noiseChange,
rrand(Line.kr(4,midRange,10)/2,
Line.kr(80,midRange*2)),
rrand(0.5,2.0)*freq);
decayEnv = 2*Decay.ar(Dust.ar(freq/20),Line.kr(0.005,0.5,timeToLive));
sig = sum({Pulse.ar(noiseGen,0.3,decayEnv).tanh}!7);
sig = LPF.ar(sig,lowFilterThreshold);
sig2 = sum({SinOsc.ar(noiseGen,0,decayEnv).tanh}!7);
sigs = [sig,sig2];
which_sig = [0,1].choose;
'WHICH_SIG'.postln;
which_sig.postln;
sig = Select.ar(which_sig,sigs);
chain = sig;
/*chain2 = 8.do{|i|
chain = LeakDC.ar(AllpassL.ar(LPF.ar(chain*0.9,3000),
0.2,{0.19.rand+0.01}!2,3));
};*/
//sig = Limiter.ar(sig+chain)*0.5;
sig = Pan2.ar(sig,pan);
sig = Limiter.ar(sig,0.4);
Out.ar(0,sig*amp);
}).add;



SynthDef.new(\spe4,{
|freq,amp,pan=0|
var sig,sig2,feedback=0.6*pi;
sig = SinOscFB.ar(LFNoise1.ar(LFNoise0.kr(2,1,2),10,XLine.kr(10,freq/rrand(8,12),10)),pan+2.0);
//sig = HPF.ar(sig,freq);
sig = FreeVerb.ar(sig,0.8,0.8,0.8);
sig = Pan2.ar(sig,pan);
Out.ar(0,sig*amp);
}).add;


SynthDef.new(\spe5,{
|freq=550,gesture=#[1,1,1,1,1,1,1],times=#[0.1,0.1,0.1,0.1,0.1,0.1],amp=0.1,nHarms=0,t_ga=1,out=0,curva='step',pan,
rateOfChange=1,se=1|
var envFreq,envPan,envAmp,sig,sig2,sigs,envChange;
envFreq = EnvGen.kr(
Env.new(
gesture[..gesture.size]*freq,times,curve:curva),t_ga);
//envPan = EnvGen.kr(Env.circle([{Rand(-1,1)},{Rand(-1,1)}],[{Rand(1,5)},{Rand(1,5)}]));
envAmp = EnvGen.kr(Env.perc(0.5,0.5,amp*0.05),gate:t_ga,doneAction:0);
sig = DynKlank.ar(`[(1..rrand(5,6))*freq/Line.kr(6,2,10),1/(1..rrand(5,6)),5*[rrand(1,10)]],PinkNoise.ar(0.1));
sig = FreeVerb.ar(sig,0.9,0.9,0.9);

sig = Pan2.ar(sig,pan);
sig = sig*envAmp;
sig = Limiter.ar(sig,0.1);
sig2 = DynKlank.ar(`[(1..5)*2*freq/Line.kr(6,2,10),1/(1..5),5*[rrand(1,10)]],PinkNoise.ar(0.1));//VarSaw.ar(envFreq);
sig2 = FreeVerb.ar(sig2,0.8,0.8,0.8);
sig2 = Pan2.ar(sig2,pan);
sig2 = sig2*envAmp;
sig2 = Limiter.ar(sig2,0.1);

envChange = EnvGen.kr(Env.circle([se,1,se],
[rateOfChange,rateOfChange]));

sigs = [Pan2.ar(XFade2.ar(sig,sig2,envChange
),pan),sig];


Out.ar(out,XFade2.ar(sig2,sig,envChange));
}).add;




SynthDef.new(\spe6,{
|freq,amp,se=1,rateOfChange=1,pan=0,out=0,
gesture=#[1,1,1,1,1,1,1],times=#[1,1,1,1,1,1],lifeSpan=10|
var sig,sig2,sigs,for,envChange,envCircle;

for = XLine.kr(10,100,lifeSpan)/(1+exp(-1*(rrand(freq*0.4,freq*0.6)-100)/10));
sig = Impulse.ar(for,0,0.4);
sig = Formlet.ar(sig,rrand(500,1000),0.01,0.1);
envCircle = EnvGen.kr(Env.circle([amp,amp],[1]));
sig = VarSaw.ar(2*freq - 50)*sig;
sig = Pan2.ar(sig,pan)*envCircle;
sig2 = Impulse.ar(for,0,0.4);
sig2 = Formlet.ar(sig,100,0.01,0.1);
sig2 = VarSaw.ar(freq - 50)*sig2;
sig2 = FreeVerb.ar(sig2,0.6,0.6,0.6);
sig2 = Pan2.ar(sig2,pan);
sig2 = sig2*amp;

envChange = EnvGen.kr(Env.circle([se,1,se],
[rateOfChange,rateOfChange]));

sigs = [Pan2.ar(XFade2.ar(sig,sig2,envChange,amp
),pan),sig];


Out.ar(out,Limiter.ar(XFade2.ar(sig2,sig,envChange),0.4));
//Out.ar(0,sig);
}).add;




//food
SynthDef.new(\sin2,{
|freq=300,modFreq=300,modAmp=50,amp=0.01,atk=0.01,rel=0.99,out=8,t_ga=1,pan=0|
var sig,env,env2;
//env = EnvGen.kr(Env.perc(atk,rel,amp),doneAction:2);
env = EnvGen.kr(Env.circle([amp,amp*2.5],[{Rand(0.05,0.7)}]),doneAction:2);
env2 = EnvGen.kr(Env.circle([1,10,1],[{Rand(0.5,5)},{Rand(0.5,5)}]));
sig = Blip.ar(freq,env2);
sig = Pan2.ar(sig,pan)*env;

Out.ar(out,sig);
}).add;

SynthDef.new(\reverb,{
|in,out=0|
var sig;
sig = In.ar(in,2);
sig = FreeVerb.ar(sig,0.9,0.9,0.9);
Out.ar(out,sig);
}).add;





Synth(\reverb,[\in,8,\out,0]);


~osc = OSCdef;
~lista_orgs = [];
~lista_orgs_synths = [];
~lista_food = [];
~lista_food_synths = [];
//~evolution_timesteps = 1;

~get_index = {
arg lista,list_item;
var theidx;
lista.do{
arg item,count;

//i.postln;
if(lista[count] == list_item){
theidx = count;
};
};
theidx;
};

~fun = {
arg msg,isFood,gesture_idx,times_idx,is_organism_dead;
//var modF=rrand(10,10*~evolution_timesteps),modA=rrand(10,10*~evolution_timesteps);
//if(~evolution_timesteps<2500){
//~evolution_timesteps = ~evolution_timesteps*1.1;};
//'~evolution_timesteps'.postln;
//~evolution_timesteps.postln;
//'modF'.postln;
//modF.postln;
//'modA'.postln;
//modA.postln;
//'EL MMMMMSSSSGGGGG'.postln;
//msg.postln;
//'msg[1]'.postln;
//msg[1].postln;
isFood = msg[1].asString[0];
//'is foooooodd'.postln;
//isFood.postln;
if(isFood.asString == "F"){
//'Yes'.postln;
//'TRUUUUEEEEE'.postln;
'msg?????'.postln;
msg[4..].postln;
~lista_food_synths = ~lista_food_synths.add(
Synth(\sin2,
/*[*msg[4..],


\out,0
]*/
msg[4..]++[\out,0]
);
);

~lista_food = ~lista_food.add(OSCdef(msg[1],{
arg msg;
   'msg foood'.postln;
msg.postln;
//~lista_food_synths[msg[1]].set(\freq,msg[2],\amp,msg[3]);
~lista_food_synths[msg[1]].set(*msg[2..]);
},msg[3]));
//'oscdef food creado'.postln;
//~lista_food.postln;
}{
'msg[4..]????'.postln;
msg[4..].postln;
~lista_orgs_synths = ~lista_orgs_synths.add(
Synth(msg[4],
/*[
/*\freq,msg[4],\amp,msg[5],\pan,msg[6],\nHarms,msg[7],
\gesture,msg[8],\times,[0.5],*/
*msg[4..],

\out,0
]*/
msg[5..]++[\out,0]
);
);
~lista_orgs = ~lista_orgs.add(OSCdef(msg[1],{
arg msg;
   //'msg ooooorgggggsssss'.postln;
//msg.postln;
//'msg[..]'.postln;
//msg[2..].postln;
//msg[]
gesture_idx = ~get_index.value(msg,'gesture');
times_idx = ~get_index.value(msg,'times');
is_organism_dead = ~get_index.value(msg,'dead') != nil;
//'gesture_idx'.postln;
//gesture_idx.postln;

/*~lista_orgs_synths[msg[1]].set(
*msg[2..gesture_idx - 1],msg[gesture_idx],msg[gesture_idx+1..times_idx-1],
msg[times_idx],msg[times_idx+1..]);*/
//'mateo'.postln;
//msg.postln;
~lista_orgs_synths[msg[1]].set(*msg[2..gesture_idx-1]);
~lista_orgs_synths[msg[1]].set(msg[gesture_idx],msg[gesture_idx..times_idx-1]);
~lista_orgs_synths[msg[1]].set(msg[times_idx],msg[times_idx+1..]);

if(is_organism_dead){
~lista_orgs_synths[msg[1]].free};
/*\freq,msg[2],\amp,msg[3],
\pan,msg[4],\nHarms,msg[5],\gesture,msg[6..9],\times,msg[10..12]*/
//*msg[2..]);
},msg[3]));
'oscdef creado'.postln;

   };
~lista_orgs.postln;
~lista_food.postln;
};


~osc.new('listener_creator',~fun,'/msg00');

)


