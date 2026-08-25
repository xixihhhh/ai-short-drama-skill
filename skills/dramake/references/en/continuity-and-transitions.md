# Continuity and Transitions

Continuity is state transfer, not visual similarity.

## State categories

- identity: coat map, eyes, body shape, marks, wardrobe construction;
- space: location, axis, screen direction, camera side, subject positions;
- action: contact phase, velocity, pose, gaze, intention;
- props: count, owner, orientation, open/closed, wet/dry, intact/damaged;
- environment: time, weather, light direction, floor condition, crowd;
- audio: room tone, music phrase, active dialogue, tail sound.

## Parent gate

A continuity-dependent block must point to an `accepted_parent_clip`. Before unlocking it:

1. review the parent contact sheet and critical motion;
2. confirm its last usable state;
3. export the accepted tail frame;
4. update the ledger;
5. restate the exit state as the child's entry state.

If the tail frame contains drift, do not propagate it. Use a bridge frame or canonical re-anchor.

## Motivated transitions

Good joins preserve at least two of action, direction, shape, gaze, sound, or light. Useful transitions include:

- action match;
- foreground occlusion or body crossing lens;
- whip/pan motion match;
- gaze to object/reaction;
- sound bridge with J-cut or L-cut;
- matched hand/paw/object shape;
- doorway or location reveal after visible travel.

Avoid simultaneous unexplained changes in location, action, camera scale, direction, wardrobe, and weather.

## Re-anchor cadence

For long-generation chains, include canonical identity/material reference on every block when supported. At minimum re-anchor after a location change, wardrobe change, any detected drift, or every two long blocks.

When one output becomes the next input, default the output-sourced chain depth to 2 and hard-cap it at 3. Restart from canon plus accepted transient state at the cap, at every scene boundary, or at the first identity/wardrobe/material drift. Never propagate a flawed tail indefinitely.
