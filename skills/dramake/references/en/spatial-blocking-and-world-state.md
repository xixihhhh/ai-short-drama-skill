# Spatial maps, blocking, and world state

Character consistency alone does not create scene continuity. Without stable relationships among doors, mirrors, ride cabins, giant objects, foregrounds, and paths, footage produces teleportation, wrong exits, duplicated objects, scale drift, and unmotivated camera moves. Use [spatial-plan.csv](../../assets/templates/spatial-plan.csv) for risky scenes.

## Build spatial anchors first

Define a small set of named anchors per location: entrances, exits, center, fixed machinery, danger boundaries, reflective surfaces, occluders, movable-prop parking points, and valid camera zones. Record:

- front/back/left/right, elevation, distance, and connectivity relative to the origin or other anchors;
- fixed or movable status, allowed occupants, visibility, and occlusion rules;
- real scale references such as door height, cabin width, shoulder height, or landmark size;
- state ID and approved reference.

False-precision coordinates are unnecessary. Relative relationships must answer where action comes from, where it goes, what occludes what, and what a reflection contains. Build real locations from inspected photography or video rather than inventing their base geography.

## Write blocking state per block

For each story block, record `start_anchor → path_anchors → end_anchor`, facing, eyeline target, contacted props, camera anchor, screen direction, entry state, and exit state. Compile action prompts from this state rather than inventing positions during generation.

A path must explain why a device or attraction is used: why the character enters, what information or threat forces movement, why the ride matters, and where the character exits. A location change is a choice or consequence, not a scenery reel.

## Mirrors, giants, and impossible spaces

- Define reflection topology: real subject, reflected subject, mirror normal, required/forbidden contents, and any delay rule.
- Give giant scale at least two anchors: a familiar object such as a character, door, or cabin, plus environmental occlusion or perspective falloff. “Huge” alone is not executable.
- Give repeated units variation rules in position, state, pose, light, or damage; lock cast and creature counts separately.
- A surreal world may violate reality, but it needs one declared rule and observable consequences. The rule cannot change opportunistically per shot.

## Reverse spatial pass

Before generation, reason backward from the planned exit state:

1. can the endpoint be reached through the anchor graph;
2. do action, world vector, screen vector, and camera agree;
3. does the prompt opening match the accepted parent tail;
4. are occlusion, reflection, entrances, contacts, and cast counts valid;
5. can the next block continue without an unexplained spatial jump.

Repair blocking or camera design before adding negative wording. If crossing the axis is necessary, provide a neutral transition, stable landmark, or visible turn.
