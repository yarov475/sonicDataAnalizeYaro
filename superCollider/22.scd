data src.
sentemetallic analize from
from  the dostoevski lib
topic modelling
the prozhito diaries


воиска -> {'neutral': 0.9991804361343384, 'skip': 0.003085370408371091}
города -> {'neutral': 0.9976868629455566, 'positive': 0.01972912810742855}
воина -> {'neutral': 1.0000100135803223, 'skip': 0.003386611817404628}
дома -> {'neutral': 0.9993638396263123, 'positive': 0.008857354521751404}
наши -> {'neutral': 0.9995927214622498, 'negative': 1.0000003385357559e-05}
дома -> {'neutral': 0.9993638396263123, 'positive': 0.008857354521751404}
день -> {'neutral': 0.8634016513824463, 'positive': 0.014513582922518253}






(
SynthDef.new(\pos,{
	var sig, amp;
	amp=SinOsc.kr([ 0.01972912810742855,0.008857354521751404,0.008857354521751404,0.008857354521751404,0.014513582922518253]).range(0,1);
	sig = SinOsc.ar([300,500,700,900,110]);
	sig= sig * amp;
	sig = Splay.ar(sig) * 0.5;
	Out.ar(0,sig);
}).add;
)
(
SynthDef.new(\0,{
	var sig, amp;
	amp=SinOsc.kr([ 0.9991804361343384,0.9976868629455566,1.0000100135803223,0.9993638396263123,0.9995927214622498,
		0.9993638396263123,0.8634016513824463]).range(0,1);
	sig = SinOsc.ar([300,500,700,900,110]);
	sig= sig * amp;
	sig = Splay.ar(sig) * 0.5;
	Out.ar(0,sig);
}).add;
)

(
SynthDef.new(\neg,{
	var sig, amp;
	amp=SinOsc.kr([ 1.0000003385357559e-05]).range(0,1);
	sig = SinOsc.ar([300,500,700,900,110]);
	sig= sig * amp;
	sig = Splay.ar(sig) * 0.5;
	Out.ar(0,sig);
}).add;
)

x = Synth.new(\0);
x = Synth.new(\pos)
x = Synth.new(\neg);


