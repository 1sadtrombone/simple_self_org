# simple_self_org

These are a couple of examples that continue in a sense my hackathon project.
They are meant to illustrate how two random systems with interaction between them can lead to order.
First off, these systems are random and thus chaotic. I wish to move away from randomness towards chaotic but nonetheless deterministic systems.
So, I will be moving away from random walks for the BLUE fellowship.

Why did I create these then? I believe in iteration. A parable: a pottry instructor assigned grades to the two halves of their class differently. One half was graded on the quality of one vase they made, while the other half was graded on the sheer quantity of vases they could produce. In the end, after much planning, mulling, and discussion, the former half finally created their vase, which, as you may expect, paled in comparison to the later vases of the latter half of the class.

On to the code:

dual_walkers.py:

The point's motion in both directions (x and y) is determined by two separate, intertwined random walks. It has even chance of going left/right and up/down, but the step size in the x direction is equal to the y position, and vice-versa.

The files produced by this script:
             return.mp4: an animation showing how this point likes to return to 0,0 and stay there (as step sizes in both directions are 0).
             runaway.png: after some milling about in the middle, the point strikes out in a diagonal direction.
             triangles.png: interesting repeating triangular pattern that appears occasionally.
             
dual_walkers_prob.py:

The same idea as dual_walkers, except instead of step size, it's probability to go right (up) that depends on the position of the walk in the y (x) direction. Note the probability has to be less than one, so we divide by diagonal distance to the origin, and probability can't be negative, so we look at the absolute value of the position.

The files produced by this script:
            diag.mp4 and diag2.mp4: The point starts in the middle, then drifts more or less northeast. This could show that two walks, when working together in this way, produce something that looks 'on purpose,' or orderly. This could also be an artifact of the way I've ensured the probability is never greater than one (by dividing by distance to the origin). This is not my last vase.
