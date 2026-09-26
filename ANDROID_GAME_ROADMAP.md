# ANDROID_GAME_ROADMAP.md

## Project goal
Build an original 3D Android adventure/platform game combining NES-era exploration/action-adventure structure with readable platforming mechanics, while using original IP and mobile-friendly 3D assets.

## Status legend
PLANNED | IN PROGRESS | CANDIDATE | PARTIAL | VERIFIED | FAILED | BLOCKED | SUPERSEDED | DEFERRED | DONE

## Phase 0 - Project foundation
- [DONE] Select canonical repository: auxz2jz/Slot-13
- [DONE] Read master instruction library
- [DONE] Establish project memory
- [DONE] Establish roadmap
- [DONE] Establish testing/diagnostic policy
- [PLANNED] Pin engine/tool versions
- [PLANNED] Add dependency/license manifest
- [PLANNED] Add Android/Godot project skeleton

## Phase 1 - 3D characters
### 1A. Character design language
- [IN PROGRESS] Define original visual language: chunky low-poly forms, clear silhouettes, mobile readability
- [IN PROGRESS] Research reusable public GitHub tools/assets with compatible licenses
- [PLANNED] Record license/provenance for anything reused

### 1B. First character pack
- [PLANNED] Player hero model
- [PLANNED] Ground enemy model
- [PLANNED] Flying enemy model
- [PLANNED] Neutral NPC base model
- [PLANNED] Materials/palette
- [PLANNED] GLB exports
- [PLANNED] Source-generation/model files
- [PLANNED] Automated mesh/file validation
- [PLANNED] User visual approval

### 1C. Character rigging and animation
- [PLANNED] Humanoid skeleton
- [PLANNED] Idle
- [PLANNED] Walk/run
- [PLANNED] Jump/fall/land
- [PLANNED] Attack
- [PLANNED] Hurt/defeat
- [PLANNED] Enemy motion cycles
- [PLANNED] Animation compatibility validation

## Phase 2 - Environment kit
- [PLANNED] Grass/forest biome kit
- [PLANNED] Stone/dungeon biome kit
- [PLANNED] Platforms/ramps/bridges
- [PLANNED] Doors/gates
- [PLANNED] Trees/rocks/bushes
- [PLANNED] Breakable/interactive props
- [PLANNED] Hazards
- [PLANNED] Mobile LOD/culling strategy

## Phase 3 - Player controller
- [PLANNED] Touch controls
- [PLANNED] Gamepad support
- [PLANNED] Run
- [PLANNED] Jump
- [PLANNED] Context/interact
- [PLANNED] Basic melee/ranged action
- [PLANNED] Camera
- [PLANNED] Lock-on/aim assistance only if needed for mobile usability

## Phase 4 - Core gameplay loop
- [PLANNED] Health/damage
- [PLANNED] Collectibles
- [PLANNED] Keys/gates
- [PLANNED] Item-gated traversal
- [PLANNED] Secrets
- [PLANNED] Checkpoints/save
- [PLANNED] Basic enemy AI
- [PLANNED] Simple NPC interaction

## Phase 5 - World structure
- [PLANNED] Small overworld
- [PLANNED] Platforming routes
- [PLANNED] First dungeon/interior
- [PLANNED] Hidden areas
- [PLANNED] Mini-boss/boss prototype
- [PLANNED] Progression loop

## Phase 6 - Android optimization
- [PLANNED] Geometry/material budgets
- [PLANNED] Texture atlas strategy
- [PLANNED] Frame-time telemetry
- [PLANNED] Thermal/battery testing
- [PLANNED] Device quality presets
- [PLANNED] APK/AAB build pipeline

## Phase 7 - Diagnostics and guided testing
- [PLANNED] Persistent structured event logger
- [PLANNED] Crash preservation
- [PLANNED] Player-action correlation IDs
- [PLANNED] Performance/stall monitoring
- [PLANNED] Export Diagnostics
- [PLANNED] Test This Version workflow
- [PLANNED] Character visual test
- [PLANNED] Movement/control test
- [PLANNED] Combat test
- [PLANNED] Save/load test
- [PLANNED] Android performance test

## Phase 8 - Content expansion
- [PLANNED] Additional enemies
- [PLANNED] Additional NPCs
- [PLANNED] More environments
- [PLANNED] Items/upgrades
- [PLANNED] Additional dungeons
- [PLANNED] Audio/music
- [PLANNED] Story/dialogue

## Current next milestone
Character Pack v0.1.0 CANDIDATE:
- 4 original low-poly characters
- GLB files
- source-generation/model notes
- provenance/license manifest
- validation report
- user-facing preview method where practical
