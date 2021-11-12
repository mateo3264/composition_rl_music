s.boot;
//cambiar el timbre
//grado de tonalidad
//
(
SynthDef.new(\hum1,{
	|freq=400,freqFactor=1,freqTime=1,amp=0.1,time1=0.5,time2=0.5,curve1=100,curve2=100|
	var env,envFreq,sig,freqs;
	freqs = [freqFactor,freqFactor];
	env = EnvGen.kr(Env.circle([0,amp,0],[time1,time2],[curve1,curve2]));

	//sig = FreeVerb.ar(sig,0.7,0.7,0.7);
	envFreq = EnvGen.kr(Env.circle(freqs*freq,[freqTime]));
	sig = SinOsc.ar(envFreq)*env;
	Out.ar(0,sig);
}).add;
)

(

~n_points = 5;
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

(
~n_points.do{
	arg i;
	~lista_synths[i].set('freqFactor',1.2,'curve1',1,'freqTime',2,
		'curve2',-1,'time1',~times[i]*1.1,'time2',~times[i]*1.1);
}
)

(
~lista_synths = [];
~lista_synths = ~lista_synths.add(Synth(\hum1));
~lista_synths = ~lista_synths.add(333);
)



{Splay.ar(SinOsc.ar([100,200,300,400]))*0.1}.play
