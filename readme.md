# Sport Timer

Simple python script to run a speficied pattern of sounds after some time. Used for me to time stretches or some activity interval.

The pattern can be provided in the config.ini file or as a command line argument behind -s and the syntax is as follows:

X:Ai,Bj;Y:Ck,Dl,Em

Where X and Y indicate how oftern the pattern until the next semicolon is repeated, A,B,C,D,E are the (int) number of seconds per interval and i,j,k,l,m are the sounds which are playing after the interval is finished (they can be repeated).

For example, for stretching, I am using:

7:10b,30c,10b,30e

Which means I do 7 intervals of 10 seconds pause, after which sound b is playing, 30 seconds on (sound c plays), 10 seconds off (sound b), 30 seconds on (sound e).

I had the audacity to create the sounds myself, they are basically simple sine waves. If you like them, use them for whatever you want.