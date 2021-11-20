s.boot;

//~buf = Buffer.readChannel(s,"C:/Users/mateo/Desktop/obra/composition_rl_music/mivoz.wav",channels:1);
~buf = Buffer.readChannel(s,"C:/Users/mateo/Desktop/obra/composition_rl_music/car.wav",channels:1);

(
SynthDef(\brickwall,{
	var sig,chain,size=2048;
	sig = PlayBuf.ar(1,\buf.kr(0),BufRateScale.ir(\buf.kr(0)),loop:1);
	chain = FFT(LocalBuf(size),sig);
	chain = PV_BrickWall(chain,\wipe.kr(0));
	sig = IFFT(chain)*\amp.kr(0.5)!2;
	Out.ar(\out.kr(0),sig);
}).add;
)

x = Synth(\brickwall,[\buf,~buf,\wipe,0]);
x.set(\wipe,0.15,\amp,1);


/////////////////


~buf = Buffer.readChannel(s,"C:/Users/mateo/Desktop/obra/composition_rl_music/car.wav",channels:1);


(
SynthDef(\brickwall2,{
	var sig,chain,size=2048;
	sig = PlayBuf.ar(1,\buf.kr(0),BufRateScale.ir(\buf.kr(0)),loop:1);
	chain = FFT(LocalBuf(size),sig);
	chain = PV_BrickWall(chain,\lpf.kr(20000).linlin(20,20000,-1,0));
	chain = PV_BrickWall(chain,\hpf.kr(20).linlin(20,20000,0,1));
	sig = IFFT(chain)*\amp.kr(0.5)!2;
	Out.ar(\out.kr(0),sig);
}).add;
)

x = 20.collect({Synth(\brickwall2,[\buf,~buf,\amp,-18.dbamp])});



(

x = 5.collect({Synth(\brickwall2,[\buf,~buf,\amp,-18.dbamp])});


5.do{
	arg i,low_freq;
	low_freq = (i+1)*100+100*(i);
	low_freq.postln;
	x[i].set(\hpf,low_freq,\lpf,low_freq+5,\amp,2);
}
)

///////////////////

~buf = Buffer.readChannel(s,"C:/Users/mateo/Desktop/obra/composition_rl_music/mivoz.wav",channels:1);

(
SynthDef(\scramble,{
	var sig,chain,size=2048;
	sig = PlayBuf.ar(1,\buf.kr(0),BufRateScale.ir(\buf.kr(0)),loop:1);
	chain = FFT(LocalBuf(size),sig);
	chain = PV_BinScramble(chain,\wipe.kr(0),\width.kr(0),\trig.kr(0));
	sig = IFFT(chain)*\amp.kr(0.5)!2;
	Out.ar(\out.kr(0),sig);
}).add;
)


x = Synth(\scramble,[\buf,~buf]);
x.set(\wipe,1,\width,0.2,\trig,1);
