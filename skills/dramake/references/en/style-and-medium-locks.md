# Style and Medium Locks

Choose the medium before prompting motion. A style lock defines what the image is made of, how it is photographed/drawn/rendered, and which changes are forbidden. It is independent from story genre.

## Live-action human drama

- real photographed performers, skin texture, hair, practical wardrobe, real-scale environments;
- plausible lenses, depth of field, exposure, motion blur, shadows, reflections, and motivated light;
- restrained production design and natural material wear;
- VFX integrated with contact, occlusion, matching light, and environment response;
- prohibit plastic faces, beauty-filter identity drift, extra fingers, wax skin, game cinematic rendering, and unexplained wardrobe topology changes.

## Live-action creature or pet hybrid

Lock one performance mode and do not switch between blocks:

- `natural_photographic`: a photographed real animal with ordinary species capability; cuteness comes from timing and behavior;
- `heightened_realism`: real animal anatomy and fur with clearer anthropomorphic eyelines, timing, and simple poses;
- `animated_actor_hybrid`: photoreal environment, fur, wardrobe, and props, while the animal performs like an animated actor through anthropomorphic stance, paw gestures, expressions, anticipation, overshoot, settle, and controlled 5–12% squash/stretch.

The hybrid is not anime rendering or plastic CGI. Silhouette may exaggerate briefly for comedy, but fur strands, seams, lighting, ground contact, prop weight, and world scale remain photographic. Animation changes performance amplitude; it never permits teleportation, penetration, count drift, spontaneous substitution, or impossible force response.

## Positive anchors

- live-action full-frame cinema photography;
- real cat with individually resolved fur strands and natural whiskers;
- real-scale room/street/workshop with ordinary wear and texture;
- practical sewn wardrobe with believable seams, weight, folds, contact, and wetness;
- restrained cinematic color, real depth of field, plausible exposure and motion blur;
- cute expression through ears, tail, posture, timing, gaze, paws, and scale contrast;
- physically integrated VFX with matching light, shadow, reflection, and contact.

### Negative medium constraints

Avoid: fully illustrated or anime-rendered worlds, manga, storybook art, children's-animation backgrounds, 3D games, game cinematics, plastic fur, toys, dolls, plush, clay, chibi proportion drift, miniature sets, outlines, cel shading, and oversaturation. When `animated_actor_hybrid` is selected, do not place animated performance itself in the negative prompt.

Use trademarks only as negative shorthand when allowed by the provider; descriptive terms are safer.

### Wardrobe lock

Describe construction, not only color:

`short yellow rain cape; front legs and belly visible; one dark snap below neck; matte waterproof woven fabric; no sleeves; no hood; does not grow into a coat or sweater.`

### Acceptance

Sample 12 frames for a 30-second block. Reject the block when more than half visibly drift to animated/CG rendering, or when any identity-critical frame becomes a different subject.

## Animation and motion comic

Do not use live-action negatives when animation is intentional. Instead lock:

- character proportions, silhouette, facial feature library, line weight, shading, texture, and palette;
- background perspective/detail rules and layer depth;
- motion cadence, smear-frame policy, camera grammar, and lighting logic;
- what may deform for expression and what must stay on-model.

Reject unplanned switches between 2D, 3D, photoreal, painterly, toy, or game-render media.

## UGC and social realism

Lock phone/lens perspective, handheld behavior, exposure imperfections, compression, autofocus behavior, performance naturalism, and room tone. “Authentic” still requires deliberate continuity; random camera errors are not realism.

## Product and brand visuals

Lock geometry, material, color, logo/label policy, scale, reflection, liquid level, package damage, and hand contact. Use blank or post-safe label plates when generated text is unreliable.
