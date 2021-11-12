s.boot;
//cambiar el timbre
//grado de tonalidad
//
(
SynthDef.new(\hum1,{
	|freq=400,freqFactor=1,freqTime=1,amp=0.1,time1=0.5,time2=0.5,curve1=100,curve2=100,timeFactor=1,times,timeTime=1|
	var env,envFreq,sig,freqs,envTime1,envTime2;
	freqs = [freqFactor,freqFactor];
	times = [timeFactor,timeFactor];
	envTime1 = EnvGen.kr(Env.circle(times*time1,[timeTime]));
	envTime2 = EnvGen.kr(Env.circle(times*time2,[timeTime]));
	env = EnvGen.kr(Env.circle([0,amp,0],[envTime1,envTime2],[curve1,curve2]));

	//sig = FreeVerb.ar(sig,0.7,0.7,0.7);
	envFreq = EnvGen.kr(Env.circle(freqs*freq,[freqTime]));
	sig = SinOsc.ar(envFreq)*env;
	Out.ar(0,sig);
}).add;
)

(

~n_points = 15;
~lista_synths = Array.new(~n_points);
~freqs = Array.new(~n_points);
~times = Array.new(~n_points);
~root = rrand(100,500);
~n_points.do{
	arg i,time,freq;
	i.postln;
	time = rrand(0.1,0.9);

	freq = rrand(100,1000).round(~root);
	~lista_synths = ~lista_synths.add(Synth('hum1',
		['freq',freq,'time1',time,'time2',time,
			'curve2',-100,'amp',0.3
		]
	));
	~freqs = ~freqs.add(freq);
	~times = ~times.add(time);
}
)
//change rythm,frequency,attack,release etc
(
~n_points.do{
	arg i;
	~lista_synths[i].set('freqFactor',1.8,'freqTime',5,'curve1',100,
		'curve2',-100,'time1',~times[i]*1,'time2',~times[i]*1,
		'timeFactor',2.1,'timeTime',5,'freq',~freqs[i]*1
	);
}
)

(
~lista_synths = [];
~lista_synths = ~lista_synths.add(Synth(\hum1));
~lista_synths = ~lista_synths.add(333);
)



{Splay.ar(SinOsc.ar([100,200,300,400]))*0.1}.play

