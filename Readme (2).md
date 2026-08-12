# LTX 2.5 Director

A ComfyUI timeline node for building multi-shot LTX videos: drop images and prompts
onto a timeline, set a window, render. Built on
[WhatDreamsCost's LTX Director](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI).

This is the **LTX 2.5** build. If you are on LTX 2.3, use
[WhatDreamsCost-CSGlide](https://github.com/CGlide/WhatDreamsCost-CSGlide) instead —
that version keeps the reference features listed below.

---

## Early version — expect bugs

LTX 2.5 is days old and so is this. It works, and it is what I am using myself, but it
has not been through much testing beyond my own machine. Expect rough edges, and please
open an issue if you hit one — a console log (F12) helps enormously.

## What works

- Timeline with image, text, audio and video segments
- Prompt zones and prompt relay
- Image anchors and end frames
- Chunk render for long videos, with audio
- Packed timelines (save a timeline with its assets embedded)

## What is disabled on 2.5

The reference features are **hidden in this build**, not removed:

- `@ref` reference sheets
- Ghost Mask / Licon MSR reference modes
- MSR prefix frames
- The Analyze backend (Ollama / LM Studio captioning)

These depend on behaviour LTX 2.3 was trained for. LTX 2.5 has not learned it, and
leaving them reachable corrupts the render rather than degrading it — so they are
switched off at both the UI and the point where they are applied. A timeline saved on
2.3 that still carries reference data will load and render fine; the reference part is
ignored with a note in the console.

If Lightricks adds support, flipping `REFERENCE_FEATURES` to true in `ltx_director.js`
and `ltx_director.py` brings all of it back.

## Install

Clone into your ComfyUI custom nodes folder:

```
cd ComfyUI/custom_nodes
git clone https://github.com/CGlide/LTX-2.5-Director.git
```

Then restart ComfyUI.

### Running alongside the 2.3 pack

Safe from **v0.2** onwards. Every node in this pack registers under its own name
(`LTXDirectorCS25`, `LTXDirectorGuideCS25`, and so on) and appears in the node menu as
*... CS (2.5)*, under the `WhatDreamsCost CS 2.5` category.

Earlier builds shared node names with the 2.3 pack, so ComfyUI silently loaded only one
of them — often 2.3's front-end driving 2.5's Python, which looks like random breakage.
If you installed a build before v0.2, load the example workflow again: the node names
inside it changed with this release.

## Requirements

From [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) — the repo is
gated, so accept the licence there first or the downloads will fail:

| File | Goes in |
| --- | --- |
| `ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors` | `models/diffusion_models/` |
| `gemma4-12b-with-proj-ltx-2.5-bf16.safetensors` | `models/text_encoders/` |
| `ltx-2.5-video-vae-bf16.safetensors` | `models/vae/` |
| `ltx-2.5-audio-vae-bf16.safetensors` | `models/vae/` |
| `ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors` | `models/latent_upscale_models/` |

2.5 uses a **Gemma 4** text encoder and will not load a 2.3 one. Video and audio use
separate VAEs.

## A note on frame counts

LTX renders in blocks of 8 frames plus one, so the frame count is snapped up to the next
`8n + 1`. A 10 s timeline at 24 fps asks for 240 frames and renders **241**. This is
normal, not a bug — but it is why dragging an image to "the end" never quite lands on the
last frame. Use **Pin to Last Frame** from the right-click menu instead, which does the
arithmetic for you.

## Example workflows

In `example_workflows/`.

## Credits

Based on [WhatDreamsCost's LTX Director](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI)
— the original node this is forked from.

LTX models by [Lightricks](https://github.com/Lightricks).

Development assistance from Claude (Anthropic).
