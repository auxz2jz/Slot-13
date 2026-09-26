# PROJECT_MEMORY.md

## Project identity
- Repository: auxz2jz/Slot-13
- Working title: Android 3D Adventure Platformer
- Platform target: Android
- Project status: IN PROGRESS
- Current phase: Phase 1 - Original 3D characters
- Current version/build: Character Pack v0.1.0 VERIFIED visual baseline; v0.2.0 high-detail CANDIDATE
- Last user-verified working version: Character Pack v0.1.0 visual designs approved by user on 2026-09-25
- Latest unverified candidate: Character Pack v0.2.0 high-detail local package, SHA-256 15f1c0d220b6886bd6b3f902b44d3c4a91637bb71fe7f107e507aa55995c6eec

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
- Character generation: trimesh 4.11.1 + NumPy
- Source-model format: procedural source scripts, with Blender-compatible work possible later
- Mobile-first geometry/material budgets
- GitHub stores source, project documentation, generated models where practical, and license records

## Current task
Create and visually approve the first original 3D character set before building the environment.

Current Character Pack v0.1.0 candidates:
1. Aster - player adventurer
2. Moss Mite - ground enemy
3. Prismwing - flying enemy
4. Waykeeper - neutral NPC base

## Current implementation plan
1. [DONE] Establish project memory, roadmap, testing/diagnostics files.
2. [DONE] Research compatible public GitHub repositories/tools/assets.
3. [DONE] Record selected references and licenses in ASSET_PROVENANCE.md.
4. [DONE] Create four original low-poly character candidates.
5. [DONE] Validate local GLB parsing and geometry budgets.
6. [DONE] Commit deterministic generator and GitHub build workflow.
7. [PENDING] Confirm GitHub-generated binary asset commit; the workflow run has not yet been observable through the available GitHub connector.
8. [DONE] User visually approved all four v0.1.0 character designs on 2026-09-25.
9. [IN PROGRESS] Preserve v0.1.0 exactly and create higher-detail v0.2.0 meshes with larger triangle budgets.
10. [PLANNED] Add LOD tiers so higher-detail close models can fall back to lightweight versions at distance.
11. [PLANNED] After high-detail visual approval, begin rigging/animation.

## Character candidate results
### hero_aster.glb
- Meshes: 22
- Vertices: 498
- Triangles: 908
- Local reload parse: PASS
- SHA-256: bcb8534f88737062a45944a9412261f5f0d865d84d71caa8e9aa0bfb42075442

### enemy_moss_mite.glb
- Meshes: 14
- Vertices: 364
- Triangles: 672
- Local reload parse: PASS
- SHA-256: 8f78d4a61a67b01dfff76e0c818049ba6106a55ce8ead15915e78a114ddc4424

### enemy_prismwing.glb
- Meshes: 10
- Vertices: 263
- Triangles: 486
- Local reload parse: PASS
- SHA-256: dd00bec02fe8601b2268d48e214c6c019b7894bfbe6450173305ef5751de3991

### npc_waykeeper.glb
- Meshes: 17
- Vertices: 414
- Triangles: 760
- Local reload parse: PASS
- SHA-256: 488f3966b288526d8c6f15b3973ab34c5ac13a88e1f70705b9df2dfda5b2bfd1

## Known bugs/limitations
- Character Pack v0.1.0 is static/unrigged and contains no animations.
- Models use vertex colors and no UV texture maps in this candidate.
- Engine version is not pinned yet.
- GitHub Actions binary-generation commit has not yet been confirmed through the available connector; do not claim the GLBs are committed until verified.

## Failed approaches / publication notes
- Direct binary publication through the normal GitHub text-file contents API is unsuitable for GLB files.
- A GitHub-native generator workflow was therefore committed. Its resulting bot commit has not yet been observed.
- This is not considered a development loop; no repeated code changes were made in response.

## Important architecture/design decisions
- Original IP only; gameplay inspiration does not permit copying Nintendo art/assets.
- Character assets are developed before environment assets.
- Character body parts remain separately named to support later rigging/animation.
- Mobile readability and low geometry budgets take priority over high-detail realism.
- Diagnostics and guided testing standards will be integrated into the playable application when the application layer begins.
- Asset provenance/license information is maintained in ASSET_PROVENANCE.md.
- CHARACTER_DESIGN.md records current visual intent.

## Test results
- Four local GLB exports generated successfully.
- All four GLBs reloaded successfully with trimesh.
- Visual contact-sheet sanity check completed.
- User visual verification: PASS — user stated they like the characters on 2026-09-25.

## Diagnostic findings
- No mesh-load failures in the local validation pass.
- GitHub workflow execution is not observable via the currently available push-run connector path, so binary publication status remains unconfirmed.

## Files/results already received
- User direction defining the project as an Android game inspired mechanically by NES Zelda and Mario.
- User direction to start with 3D characters.
- User direction to use the master instruction library and public GitHub resources.
- CC0 license review: KayKit Adventurers and Gobkit Free Assets.
- Local Character Pack v0.1.0 package and preview.

## Exact next action
Preserve Character Pack v0.1.0 as the first user-verified visual baseline. Build Character Pack v0.2.0 as a separate higher-detail candidate with approximately:
- Hero/NPC LOD0: 4,000–8,000 triangles each
- Ground/flying enemy LOD0: 2,000–5,000 triangles each
- LOD1: roughly half LOD0
- LOD2: retain or derive from the verified v0.1.0 low-poly meshes

Do not overwrite v0.1.0. After v0.2.0 visual approval, proceed to rigging and animation.

## Checkpoint history
### Checkpoint 0 - Project initialization
- Status: IN PROGRESS
- Verified baseline: NONE
- Candidate: NONE
- Repository was empty at project start.
- Master instruction library was read before project files were created.

### Checkpoint 1 - Character Pack v0.1.0
- Status: CANDIDATE
- Verified baseline: NONE
- Candidate package SHA-256: 0f82a84b87f05f1b2e4061265c87809596739b6530c2184e746244852e539788
- Four original character GLBs generated locally.
- All four passed local GLB reload parsing.
- Deterministic generator committed at tools/generate_characters.py.
- GitHub generation workflow committed at .github/workflows/build-character-pack.yml.
- ASSET_PROVENANCE.md and CHARACTER_DESIGN.md committed.
- GitHub-generated binary asset commit: NOT YET CONFIRMED.
- User visual verification: PENDING.


### Checkpoint 2 - v0.1.0 visual approval / v0.2.0 detail upgrade
- Date: 2026-09-25
- v0.1.0 status: VERIFIED VISUAL BASELINE
- User explicitly stated they like the four character designs.
- Exact v0.1.0 package SHA-256 remains: 0f82a84b87f05f1b2e4061265c87809596739b6530c2184e746244852e539788
- v0.1.0 must remain preserved and must not be overwritten.
- New requested direction: increase character mesh resolution / triangle counts while preserving the approved designs.
- Planned v0.2.0 strategy: higher-detail LOD0 meshes plus lower LOD tiers for Android performance.


### Checkpoint 3 - Character Pack v0.2.0 high-detail candidate
- Status: CANDIDATE / USER VISUAL REVIEW PENDING
- v0.1.0 remains the VERIFIED visual baseline and was not overwritten.
- Package SHA-256: 15f1c0d220b6886bd6b3f902b44d3c4a91637bb71fe7f107e507aa55995c6eec
- Aster HD: 8,748 triangles; GLB reload PASS.
- Moss Mite HD: 8,144 triangles; GLB reload PASS.
- Prismwing HD: 5,672 triangles; GLB reload PASS.
- Waykeeper HD: 7,640 triangles; GLB reload PASS.
- Local preview contact sheet generated.
- User visual approval: PENDING.
- Exact next action: user inspects v0.2.0 preview/GLBs and either approves or requests targeted changes.
