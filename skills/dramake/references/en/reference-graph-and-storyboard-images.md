# Reference graph and storyboard-image method

References are a production graph, not an attachment pile. Story, cast, location, prop, motion, storyboard image, video, and audio nodes have explicit dependencies; downstream work reads only connected, approved upstream state.

## Recommended graph

`story contract → cast/location/prop masters → coverage audition → frozen storyboard image → video block → accepted tail/audio state → next block`

- Story controls causality, beats, and exit state—not appearance.
- Character masters control identity, wardrobe, and performance boundaries—not scene composition.
- Location masters control layout, materials, light, and scale without adding cast.
- Prop masters control geometry, materials, parts, and state without redesign.
- Motion reference controls motion language or contact phase, not actor, background, wardrobe, or camera.
- A storyboard image controls one moment's blocking and composition, not the whole motion passage.
- An accepted tail controls short-term state but never replaces the long-term identity master.

Remove any reference that lacks one duty, competes for a controlled dimension, or is not consumed downstream.

## Character design sheets

Create clean, comparable character sheets before identifying a character inside a story scene. Include:

- front, side, back, and three-quarter full-body views;
- neutral plus four to six project-relevant performance states;
- species/anatomy-appropriate walk, run, stop, turn, crouch, and jump studies;
- face, hand/paw, tail, fastener, and identity-mark details;
- one scale comparison with a cast mate or standard object.

Multiple poses on a sheet are one character, not multiple cast members. A video request states `EXACT CAST COUNT` and forbids transfer of the white background, layout, labels, or pose duplication. Wardrobe, wetness, dirt, or story transformation creates a legal new `state_id`; it does not overwrite canon.

## Location and prop sheets

Build an empty location and map first: entrances/exits, traversable path, key-light direction, threat source, hero fixtures, and scale anchors. For recognizable places, use real photographs to establish perspective, materials, and local specificity before controlled anomaly; do not turn them into generic CG sets.

Recurring props use neutral-light turnarounds locking front/back, thickness, part count, connectors, scale reference, and allowed states. Make exact story text as a clean post layer; video generates the text-free plate.

## Storyboard-image generation

Every storyboard image derives from approved cast, location/prop, and one story moment. Its prompt solves only this frame:

1. who stands where and faces which direction;
2. one visible action in progress;
3. the cause or information the audience must see first;
4. camera height, scale, lens, and subject occupancy;
5. motivated light, environment material, and real scale;
6. composition room for the next action;
7. reference content that must not transfer.

Generate one composition master first. Approve identity, count, blocking, eyelines, props, and space, then use scoped edits. Never batch an entire storyboard from a broken master.

## From storyboard image to video

The image controls first state; the video prompt controls time: motion onset, camera motivation, physical response, sound source, and end state. Do not ask the model to redesign faces, wardrobe, and location already locked by the frame.

For internal multi-shot generation, each sub-shot gets `entry → primary action → camera response → visible result → exit handoff`. A continuous one-take uses a location map, character masters, and one accurate first state rather than a stack of competing storyboard images.

## Reference compilation check

Before submission, print:

`asset_id | media_type | controls | must_not_transfer | connected_to | approved_version`

Then verify that Image/Video/Audio numbering matches upload order; every reference connects to the request; pose sheets do not multiply cast; drifted outputs do not propagate; schema limits are respected; and a reference whose removal changes nothing is removed permanently.
