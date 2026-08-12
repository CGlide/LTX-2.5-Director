
# LTX 2.5 Director

A ComfyUI timeline node for building multi-shot LTX videos: drop images and prompts
onto a timeline, set a window, render. Built on
[WhatDreamsCost's LTX Director](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI).

This is the **LTX 2.5** build. If you are on LTX 2.3, use
[WhatDreamsCost-CSGlide](https://github.com/CGlide/WhatDreamsCost-CSGlide) instead —
that version keeps the reference features listed below.


<img width="665" height="669" alt="Capture d&#39;écran 2026-08-12 160229" src="https://github.com/user-attachments/assets/dfb8ebbd-9956-4142-b07b-af7d505a06a7" />

<img width="795" height="804" alt="Capture d&#39;écran 2026-08-12 145713" src="https://github.com/user-attachments/assets/899b237c-8761-40ff-a293-a6551087e631" />
---

## Early version 

Experimental for now!

Image to video, text to video work.

First last frame work.(for the last frame, you can right click "pin to last frame")

Multiple key frames work! pretty cool

Prompt relay, text and image work as well



Need to check this : nodes_lt.py, class LTXVDualCFGGuider but it is late
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

**Do not run this alongside the 2.3 pack.** Both register the same node names, and
ComfyUI will silently load only one of them. Keep one or the other in `custom_nodes`.

## Requirements

LTX 2.5 model, VAE, spatial upscaler and text encoder. See
[Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) — note that 2.5 uses a
Gemma 4 text encoder and will not load a 2.3 one.

## Example workflows

In `example_workflows/`.

## Credits

## Credits

## Credits

Based on [WhatDreamsCost's LTX Director](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI)
— the original node this is forked from.

LTX models by [Lightricks](https://github.com/Lightricks).

Development assistance from Claude (Anthropic).
