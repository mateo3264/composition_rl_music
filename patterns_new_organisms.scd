(
SynthDef.new(\spe7,{
	|freq=400,amp=0.1,total_dur=1,atk_proportion,atk,rel,atk_curve=10,rel_curve=10|
	var env,sig;
	atk = total_dur*atk_proportion;
	rel = total_dur - atk;
	rel.postln;
	env = EnvGen.kr(Env.circle([0,amp,0],[atk,rel],[atk_curve,rel_curve]),doneAction:2);
	sig = SinOsc.ar(freq)*env;
	Out.ar(0,sig);
}).add
)
(
Synth(\spe7,['total_dur',0.5,
	'atk_proportion',0.001]);
Synth(\spe7,['total_dur',0.53,
	'atk_proportion',0.001,'freq',300]);
)
Env.new([0,0.1,0],[1,1],[100,100]).plot
(
Pbind(\instrument,\spe7,
	'total_dur',Pseq()
)
)


s.boot;
{EnvGen.kr(Env.perc(0.1,0.9,curve:100))}.plot

Env.perc(0.1,0.9,curve:-10).plot

{SinOsc.ar(200,0,Impulse.ar(5))!2}.play

{Impulse.ar(SinOsc.ar(200))!2}.play


Env.circle([0,0.1,0],[0.1,0.2]).plot