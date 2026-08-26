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

## Visible physical-event contract

“Reverse,” “veer left,” “the helmet falls,” and “collide” are intentions, not filmable directions. For every key physical event define:

- `physical_start_state`: starting position/pose of subject, prop, vehicle, and attachment;
- `control_input`: actor/body part, steering wheel, pedal, rope, button, or external force that starts it;
- `world_motion_vector`: direction relative to road, gravity, and set;
- `screen_motion_vector`: left/right/toward/away relative to frame—never only “left”;
- `phase_sequence`: prepare → initiate → redirect/detach → peak → visible response;
- `physical_end_state`: final position, orientation, attached/detached state, damage, and owner.

A reversing vehicle must visibly leave rest, displace backward relative to the background, and finish farther behind in set space; a turn defines both world and screen direction. A falling helmet must loosen, separate from the head, follow gravity or a plausible arc, strike a surface, and remain in the new location. It cannot disappear or reset in the next shot.

Give one generation block only one high-risk precision physics event. If a passage combines reversing, steering, collision, helmet detachment, and character reaction, split it into causally joined setup, peak, and consequence/reaction shots. Use a shorter hero block, motion reference, or local post repair where appropriate. If the prompt says reverse but the pixels move forward, reject it; described intent is not observed evidence.

## Human, creature, and object anatomy

For humans, track handedness, joint limits, grip, gaze, balance, foot placement, body support, and object hand-offs. Avoid extra fingers, merged hands, reversed phones, and impossible body/object intersections.

For animals, use species-appropriate locomotion and manipulation. For machines/vehicles, show control input, traction, inertia, collision response, and mechanical constraints. For cloth, liquid, smoke, hair, and VFX, maintain source, flow direction, occlusion, and environmental response.

## Animated exaggeration is not a physics error

When `animated_actor_hybrid` is selected, permit brief anthropomorphic stance, exaggerated facial/ear/tail reaction, anticipation, overshoot, settle, and squash/stretch within the locked range. Exaggeration needs preparation and recovery while the character silhouette remains identifiable.

The prop world still passes real-physics QA. Food cannot change identity or spring from a closed container, a plate cannot flip without a handoff, tongs cannot move an item before contact, counts cannot multiply, and a tail cannot grow a dispenser opening. Exaggerate how the character reacts, not how objects exist or move.

### Cat-specific overlay

Use walk, run, crouch, stalk, jump, land, paw, bat, hook briefly with claws, bite, head-push, body-push, knead, squeeze through a truly open gap, and tail balance. In naturalistic modes avoid prolonged bipedal stance, human wrists/fingers, precise tool grip, adult-style carrying, or unsupported heavy lifting. In an explicitly locked animated-actor hybrid, brief bipedal performance is allowed only with visible support, weight, balance, and a designed entry/exit pose; it does not grant human fingers or unlimited strength.

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

Frame-step start, 25%, peak, 75%, and end. Compare observed world/screen motion vectors, attachment state, contact order, and stable outcome against the contract.
