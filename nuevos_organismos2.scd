//Falta silencios
//Falta volumen
(
SynthDef.new(\ianx,{
	|density=10,grain_dur=0.025,cell_density=10,
	freq_var=100,freq_mean=300,n_amp_changes=10,amp=1,
	n_freq_changes_per_sec=10,rev=0.5|
	var env,ampArray,ampTimes,sig,trig,freqVariator;
	ampArray=Array.rand(10,1,10).stutter(2).normalizeSum*amp;
	ampTimes = Array.rand(10*2-1,1,10).normalizeSum;
	env = EnvGen.kr(Env.circle(ampArray,ampTimes));
	trig = Dust.ar(density);
	freqVariator = LFNoise0.ar(Line.kr(1,400,10),freq_var,freq_mean);
	sig = GrainSin.ar(1,trig,1/density,freqVariator,mul:env);
	sig = FreeVerb.ar(sig,rev,rev,rev);
	Out.ar(0,sig!2);
}).add
)


~amps = Array.rand(10,0.0,1.0)
(
var array_size = 5;
x = Synth(\ianx);


~freqs = Array.rand(array_size,500,1000);
~freq = Array.series(array_size,1,0.1);
~freq_vars = Array.rand(array_size,10,100);
~densities = Array.rand(array_size,0,100);
~dts = Array.rand(array_size,1,100).normalizeSum*1;
~revs = Array.rand(array_size,1,100).normalizeSum*(array_size/15);
~amps = Array.rand(array_size,0.0,1.0);
r = Routine.new({
	|freq,freq_var,density|
	freq = rrand(0.2,2);
	rrand(5,10).do{
		rrand(30,70).do{
			arg i;

			//freq.postln;
			//freq_var = rrand(10,100);
			//density = rrand(10,100);

			x.set(\freq_mean,~freqs[i%array_size]*freq,\freq_var,~freq_vars[i%array_size],\density,~densities[i%array_size],
				\rev,~revs[i%array_size],\amp,~amps[i%array_size]
			);
			~dts[i%array_size].wait;
		};
		x.set(\amp,rrand(0.0,1.0));
		rrand(0.1,5.0).wait;
	}
});
r.play
)




(
SynthDef.new(\ianx2,{
	|n_trigs=10,grain_dur=0.025,cell_density=10,
	freq_var=100,freq_mean=300,n_amp_changes=10,n_freq_changes_per_sec=10|
	var env,ampArray,ampTimes,sig,trig,freqVariator;
	ampArray=Array.rand(10,1,10).stutter(2).normalizeSum;
	ampTimes = Array.rand(10*2-1,1,10).normalizeSum;
	env = EnvGen.kr(Env.circle(ampArray,ampTimes));
	trig = Impulse.ar(n_trigs);
	freqVariator = LFNoise0.ar(n_freq_changes_per_sec,freq_var,freq_mean);
	sig = GrainSin.ar(1,trig,1/n_trigs,freqVariator,mul:env);
	Out.ar(0,sig!2);
}).add
)
x = Synth(\ianx2,[\freq_mean,rrand(100,700)]);
x.set(\freq_mean,10,\n_trigs,100)
