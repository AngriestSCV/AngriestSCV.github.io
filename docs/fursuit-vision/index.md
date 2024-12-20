# Fursuit vision system experiments

## The idea

While playing with 3d models I realized that the eye placement on the 3d
printed head would not be good for seeing out of. This leaves me with 2
options. Either I get use to not seeing well, or I get clever. Getting clever
in this case I decided could be done with cameras, but where to start.

## Feeling out the problem.
To see I'll need 3 things. Cameras, displays, and a computer to connect them.

I decided to start testing with what I had on hand. I turned on my webcam and
started snapping in an effort to estimate latency. Likely somewhere around
100ms from the looks of it. I grabbed a Raspberry PI and checked it's camera
that looked to be about the same. These numbers aren't great, but will likely
do well enough even if I can't improve easily.

## Seeing is believing

Feeling pumped that I don't need special cameras or processing to get what I
suspect to be acceptable latency I start looking for displays. A VR headset
would be great, but I'm not sure how I'd drive one from what I hope will be a
low powered computer. They are also power hungry and I don't want multiple
massive power banks. Asking around I stumble into XReal AR glasses. They don't
really seem to do the AR part, but they are displays. I buy some along with a
pair $12 no-name of matching USB cameras. Slapping the cameras on a clipboard
and plugging it into a laptop I get a monstrosity to play with.

I cobbled together [some code](test.py) and got to testing. 

![Picture of proof of concept hardware setup](couch-proof-of-concept.png)

## Proof of concept conclusions

It turns out for
myself I don't need to be too careful on the alignment of the cameras as even
misalignment is tolerable. Walking around with the "IPD" of the cameras quite
wide is an interesting experience, but bringing them in makes it more normal. My
main issue with it was how careful I had to be as the cameras didn't really
grip the clipboard and I didn't even bother with tape. All in all I can't see a
reason not to proceed.

## Next steps

I think the next steps are to build and 3d print the head. Likely by printing a
camera rig first to further verify that the locations I'm picking are fine.

I'm picking a Raspberry PI 5 for a computer for this as it should support the
hardware I want. I have the option to use 2 pi cameras instead of webcams if
that turns out to perform better. Hopefully it's power draw will be acceptable
on a power bank. I still don't know the performance of it, but a worst case of
a more power hungry computer just means more batteries. Not ideal, but likely
acceptable.
