# TESTING_DIAGNOSTICS.md

This project follows:
- auxz2jz/master-instruction-library/DIAGNOSTICS_STANDARD.md
- auxz2jz/master-instruction-library/GUIDED_TESTING_STANDARD.md

## Asset-stage testing
Before the playable application exists, model candidates must be validated without pretending that a file's existence proves it is usable.

For each character asset record:
- source/provenance
- license
- generation/export tool
- vertex/triangle count
- mesh count
- material count
- bounding dimensions
- whether normals exist
- whether UVs exist
- whether skeleton/skin exists
- animation count
- GLB parse/load result
- warnings/errors

A character is CANDIDATE after generation + automated validation.
A character becomes visually VERIFIED only after the user actually views it and confirms it is acceptable.

## Character visual guided test
When a viewer/game preview exists, provide a Test This Version flow:
1. Open character gallery.
2. Rotate player hero.
3. Confirm silhouette and proportions look correct.
4. Inspect ground enemy.
5. Inspect flying enemy.
6. Inspect neutral NPC.
7. Report visual problems per character.
8. Export diagnostics on technical load/render failure.

## Application-stage diagnostics
When gameplay begins, implement:
- USER_ACTION logging for movement, jump, attack, interact, pause, settings, load/save
- operation/result separation
- scene/state transitions
- errors and stack traces
- global crash preservation where supported
- bounded persistent action trace
- correlation IDs for important gameplay operations
- frame-time/performance telemetry where diagnostically valuable
- save/load validation
- asset-load failures
- Export Diagnostics
- Test This Version guided test sessions

## Privacy
Do not log unrestricted text input, secrets, tokens, precise location, or unnecessary private paths.
