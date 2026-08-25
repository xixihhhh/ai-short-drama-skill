# Physics, Anatomy, and Failure Modes

## Action feasibility gate

Before writing a generation prompt, replace abstract actions with visible physical primitives.

For every object-moving action record:

- actor and body part;
- approach path;
- contact point;
- force direction;
- support and balance;
- expected object/body response;
- stable end state.

The visible order is `approach → contact → force → response → outcome`.

## Human, creature, and object anatomy

For humans, track handedness, joint limits, grip, gaze, balance, foot placement, body support, and object hand-offs. Avoid extra fingers, merged hands, reversed phones, and impossible body/object intersections.

For animals, use species-appropriate locomotion and manipulation. For machines/vehicles, show control input, traction, inertia, collision response, and mechanical constraints. For cloth, liquid, smoke, hair, and VFX, maintain source, flow direction, occlusion, and environmental response.

### Cat-specific overlay

Use walk, run, crouch, stalk, jump, land, paw, bat, hook briefly with claws, bite, head-push, body-push, knead, squeeze through a truly open gap, and tail balance. Avoid prolonged bipedal stance, human wrists/fingers, precise tool grip, adult-style carrying, or unsupported heavy lifting.

If an animal must do precise work, redesign the mechanism: species-appropriate control, bite-pull loop, weight-triggered pedal, magnet, pulley, rolling object, cooperative human, or explicit magic that moves the object while the animal triggers it.

## Frequent rejection failures

- subject intersects a box, glass, wall, vehicle, clothing, prop, or another body;
- closed window traversal without opening;
- motion before contact or force;
- weightless heavy prop or taut rope without tension path;
- extra animal/person/object appears; an actor disappears or duplicates;
- phone flips front/back or changes hands without a cut;
- clothing changes topology, not just folds;
- prop count, scale, damage, wetness, or orientation resets;
- character falls, then resumes a prior state without recovery;
- generated text becomes malformed or changes between frames;
- static talking face fills unused duration.

## Complexity budget

Allow one precision contact challenge per block. Split multi-object manipulation into separate beats or shots. Use inserts and reaction shots to preserve clarity.
