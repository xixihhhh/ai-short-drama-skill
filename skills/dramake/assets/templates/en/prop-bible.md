# Recurring Prop Bible

Create this file and canonical masters before storyboarding or video generation for every prop that appears more than once, crosses scenes, drives a key action, or carries text/logo.

## Identity

- `prop_id`:
- Name / story function:
- First appearance / recurring scenes:
- Owner / operator:
- Cross-scene: yes / no
- Carries exact text, numbers, or logo: yes / no

## Canonical geometry and material lock

- Front / back / left / right / top / three-quarter masters:
- Scale reference and key dimensions:
- Silhouette, proportions, thickness, and part count:
- Exact count and contents (plate count, food identity/count, inside/outside container):
- Front/back/top orientation marks and pickup side:
- Material, color, reflection, wear, and seams:
- Moving parts, hinges, buttons, lids, straps, and attachment method:
- Forbidden changes:

Use a user-selected, validated high-fidelity image generation/editing route—such as a GPT Image-class model—to create neutral-light, clean-background, low-distortion prop masters. Once accepted, freeze the `prop_id` and files instead of redesigning the prop per scene.

## Text and graphic layers

- Exact copy:
- Font / weight / color / layout / orientation:
- `text_plate_id` and transparent PNG / vector master:
- Position, size, perspective, and occlusion on the prop:
- Video strategy: blank plate plus post / validated reference texture / never direct-generate
- Accepted composited frame:

Store geometry canon separately from the text layer. Let the video model handle the prop, motion, occlusion, and light; track and composite the same `text_plate_id` in post by default so the model does not redraw and mutate copy every frame.

## State machine

| state_id | owner/location | exact count/contents | orientation/pickup side | open/attached | intact/damaged | wet/dirty | text plate | one allowed change | allowed next states |
|---|---|---|---|---|---|---|---|---|---|
| P0 |  |  |  |  |  |  |  |  |  |

## Contact and physics

- Allowed grip, press, wear, placement, and collision points:
- Weight, support, friction, inertia, or center-of-mass notes:
- Visible attachment / detachment phases:
- Character anatomy and action limits:
- Safer coverage for high-risk shots:

## Before each use

- `prop_id` / `state_id` / `text_plate_id` referenced by this shot:
- Exact count, contents, and pickup side at start / peak / end:
- The one allowed change from the last accepted state:
- Scene style or malformed text that must not transfer:
- Canon views to compare at start, action peak, and end:
