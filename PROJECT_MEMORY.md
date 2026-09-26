# PROJECT_MEMORY.md

## Project identity
- Repository: auxz2jz/Slot-13
- Working title: Android 3D Adventure Platformer
- Platform target: Android
- Project status: IN PROGRESS
- Current phase: Phase 1 - Original 3D characters
- Current version/build: none yet
- Last user-verified working version: NONE
- Latest unverified candidate: NONE

## Canonical startup instructions
Before substantial work:
1. Read auxz2jz/master-instruction-library/INSTRUCTION_INDEX.md.
2. Read CORE_DEVELOPMENT_RECOVERY_RULES.md.
3. Read DIAGNOSTICS_STANDARD.md.
4. Read GUIDED_TESTING_STANDARD.md.
5. Read this file.
6. Read ANDROID_GAME_ROADMAP.md.
7. Read TESTING_DIAGNOSTICS.md.
8. Identify the last user-verified baseline before modifying code/assets.

Recovery commands from the master library are dormant standing procedures. Do not execute them merely because this repository references them. Execute them only if the user explicitly issues one or if the defined anti-loop/recovery condition actually occurs.

## High-level game direction
Create an original 3D Android adventure/platform game that takes mechanical inspiration from the NES-era design language of The Legend of Zelda and Super Mario Bros:
- exploration, secrets, item-gated progression, simple combat, overworld/dungeon structure
- readable platforming, jumps, hazards, moving enemies, collectible-driven progression
- short, clear gameplay loops suitable for mobile

The project must use original characters, names, models, textures, maps, music, and story. Do not copy or rip Nintendo characters, models, sprites, maps, audio, logos, or other protected assets. Public/open-source repositories may be used only when their licenses are compatible and attribution/redistribution requirements are recorded.

## Provisional technical direction
- Game engine: Godot 4.x unless later changed by the user
- 3D interchange format: glTF 2.0 / GLB
- Source-model format: Blender-compatible and/or procedural source scripts
- Mobile-first geometry/material budgets
- GitHub stores source, project documentation, generated models where practical, and license records

## Current task
Create the first original 3D character set before building the environment.

Initial character targets:
1. Player hero - original stylized low-poly humanoid
2. Ground enemy - original simple creature
3. Flying enemy - original simple creature
4. Neutral NPC base - reusable humanoid variation

Each character should be:
- visually distinct from Nintendo characters
- readable on a phone screen
- low-poly/mobile-friendly
- prepared for later animation/rigging
- exported as GLB when possible
- accompanied by source-generation/model notes and license/provenance information

## Current implementation plan
1. Establish project memory, roadmap, testing/diagnostics files.
2. Research public GitHub repositories/tools/assets with compatible licenses that can accelerate original 3D character creation.
3. Record selected dependencies/assets and licenses.
4. Create the first original low-poly character assets.
5. Validate that the model files load and contain expected mesh/material data.
6. Save a candidate checkpoint; do not label VERIFIED until the user tests/approves the models.

## Known bugs/limitations
- No game source or assets exist yet.
- No user-verified baseline exists yet.
- Engine version is not pinned yet.
- Character rigs/animations are not yet implemented.

## Failed approaches
- None.

## Important architecture/design decisions
- Original IP only; gameplay inspiration does not permit copying Nintendo art/assets.
- Character assets are developed before environment assets.
- Diagnostics and guided testing standards will be integrated into the playable application when the application layer begins.
- Asset provenance/license information will be maintained in-repository.

## Test results
- None yet.

## Diagnostic findings
- None yet.

## Files/results already received
- User direction defining the project as an Android game inspired mechanically by NES Zelda and Mario.
- User direction to start with 3D characters.
- User direction to use the master instruction library and public GitHub resources.

## Exact next action
Read ANDROID_GAME_ROADMAP.md and TESTING_DIAGNOSTICS.md after they are created, then research compatible public GitHub character/tool repositories and create the first original 3D character candidate set.

## Checkpoint history
### Checkpoint 0 - Project initialization
- Status: IN PROGRESS
- Verified baseline: NONE
- Candidate: NONE
- Repository was empty at project start.
- Master instruction library was read before project files were created.
