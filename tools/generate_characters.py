import hashlib
import json
import math
from pathlib import Path

import numpy as np
import trimesh

OUT = Path(__file__).resolve().parents[1] / "assets" / "characters" / "v0.1.0"
OUT.mkdir(parents=True, exist_ok=True)

PALETTE = {
    "skin": [214, 165, 118, 255],
    "skin_dark": [171, 121, 83, 255],
    "navy": [45, 63, 87, 255],
    "navy_dark": [27, 37, 53, 255],
    "orange": [214, 104, 45, 255],
    "tan": [163, 126, 82, 255],
    "brown": [93, 62, 45, 255],
    "dark_brown": [52, 36, 31, 255],
    "teal": [52, 135, 134, 255],
    "cream": [222, 213, 190, 255],
    "stone": [102, 111, 105, 255],
    "moss": [83, 122, 75, 255],
    "moss_dark": [55, 83, 51, 255],
    "amber": [239, 176, 67, 255],
    "violet": [110, 83, 145, 255],
    "violet_dark": [67, 47, 91, 255],
    "cyan": [77, 182, 196, 255],
    "charcoal": [38, 42, 46, 255],
    "grayblue": [100, 125, 139, 255],
}


def colorize(mesh, rgba):
    result = mesh.copy()
    result.visual.face_colors = np.tile(
        np.asarray(rgba, dtype=np.uint8), (len(result.faces), 1)
    )
    return result


def ellipsoid(scale, center, color, subdivisions=1):
    mesh = trimesh.creation.icosphere(subdivisions=subdivisions, radius=1.0)
    mesh.apply_scale(scale)
    mesh.apply_translation(center)
    return colorize(mesh, color)


def box(extents, center, color, rot_xyz=(0.0, 0.0, 0.0)):
    mesh = trimesh.creation.box(extents=extents)
    for angle, axis in zip(rot_xyz, ([1, 0, 0], [0, 1, 0], [0, 0, 1])):
        if abs(angle) > 1e-8:
            mesh.apply_transform(trimesh.transformations.rotation_matrix(angle, axis))
    mesh.apply_translation(center)
    return colorize(mesh, color)


def cylinder_between(a, b, radius, color, sections=8):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    vector = b - a
    height = float(np.linalg.norm(vector))
    if height <= 1e-6:
        raise ValueError("Cylinder endpoints must be different")
    mesh = trimesh.creation.cylinder(radius=radius, height=height, sections=sections)
    mesh.apply_transform(trimesh.geometry.align_vectors([0, 0, 1], vector / height))
    mesh.apply_translation((a + b) / 2.0)
    return colorize(mesh, color)


def cone(radius, height, center, color, sections=8, direction=(0, 0, 1)):
    mesh = trimesh.creation.cone(radius=radius, height=height, sections=sections)
    mesh.apply_transform(
        trimesh.geometry.align_vectors([0, 0, 1], np.asarray(direction, dtype=float))
    )
    mesh.apply_translation(center)
    return colorize(mesh, color)


def prism(points_xz, thickness, center, color):
    points = np.asarray(points_xz, dtype=float)
    count = len(points)
    vertices = []
    for y in (-thickness / 2.0, thickness / 2.0):
        vertices.extend([[x, y, z] for x, z in points])

    faces = []
    for i in range(1, count - 1):
        faces.append([0, i, i + 1])
        faces.append([count, count + i + 1, count + i])
    for i in range(count):
        j = (i + 1) % count
        faces.append([i, j, count + j])
        faces.append([i, count + j, count + i])

    mesh = trimesh.Trimesh(
        vertices=np.asarray(vertices),
        faces=np.asarray(faces),
        process=True,
    )
    mesh.apply_translation(center)
    return colorize(mesh, color)


def add(scene, name, mesh):
    scene.add_geometry(mesh, node_name=name, geom_name=name)


def hero_aster():
    scene = trimesh.Scene()
    add(scene, "hero_torso", ellipsoid((0.34, 0.22, 0.44), (0, 0, 1.12), PALETTE["navy"]))
    add(scene, "hero_belt", box((0.68, 0.30, 0.10), (0, 0, 0.88), PALETTE["tan"]))
    add(scene, "hero_head", ellipsoid((0.27, 0.24, 0.30), (0, -0.01, 1.66), PALETTE["skin"]))
    add(scene, "hero_hair_cap", ellipsoid((0.28, 0.25, 0.15), (0, 0.02, 1.84), PALETTE["dark_brown"]))
    add(scene, "hero_hair_back", box((0.30, 0.14, 0.20), (0, 0.18, 1.67), PALETTE["dark_brown"], (math.radians(-12), 0, 0)))
    add(scene, "hero_scarf", box((0.46, 0.30, 0.10), (0, -0.01, 1.40), PALETTE["orange"]))
    add(scene, "hero_scarf_tail_long", box((0.11, 0.08, 0.46), (0.15, 0.20, 1.18), PALETTE["orange"], (math.radians(12), 0, math.radians(-8))))
    add(scene, "hero_scarf_tail_short", box((0.10, 0.07, 0.30), (-0.06, 0.21, 1.23), PALETTE["orange"], (math.radians(-8), 0, math.radians(5))))
    add(scene, "hero_arm_L", cylinder_between((-0.28, 0, 1.28), (-0.48, 0.01, 0.98), 0.105, PALETTE["navy"]))
    add(scene, "hero_arm_R", cylinder_between((0.28, 0, 1.28), (0.48, 0.01, 0.98), 0.105, PALETTE["navy"]))
    add(scene, "hero_hand_L", ellipsoid((0.11, 0.09, 0.12), (-0.50, 0.01, 0.91), PALETTE["skin"]))
    add(scene, "hero_hand_R", ellipsoid((0.11, 0.09, 0.12), (0.50, 0.01, 0.91), PALETTE["skin"]))
    add(scene, "hero_shoulder_guard_R", ellipsoid((0.20, 0.20, 0.12), (0.34, 0.00, 1.33), PALETTE["grayblue"]))
    add(scene, "hero_leg_L", cylinder_between((-0.16, 0, 0.85), (-0.17, 0, 0.38), 0.13, PALETTE["navy_dark"]))
    add(scene, "hero_leg_R", cylinder_between((0.16, 0, 0.85), (0.17, 0, 0.38), 0.13, PALETTE["navy_dark"]))
    add(scene, "hero_boot_L", box((0.27, 0.38, 0.22), (-0.17, -0.08, 0.18), PALETTE["brown"]))
    add(scene, "hero_boot_R", box((0.27, 0.38, 0.22), (0.17, -0.08, 0.18), PALETTE["brown"]))
    add(scene, "hero_pack", box((0.48, 0.22, 0.50), (0, 0.28, 1.13), PALETTE["brown"]))
    add(scene, "hero_pack_roll", cylinder_between((-0.18, 0.41, 1.39), (0.18, 0.41, 1.39), 0.075, PALETTE["cream"]))
    add(scene, "hero_side_pouch", box((0.20, 0.16, 0.25), (-0.35, 0.10, 0.80), PALETTE["tan"]))
    add(scene, "hero_eye_L", ellipsoid((0.035, 0.020, 0.050), (-0.09, -0.235, 1.69), PALETTE["charcoal"]))
    add(scene, "hero_eye_R", ellipsoid((0.035, 0.020, 0.050), (0.09, -0.235, 1.69), PALETTE["charcoal"]))
    return scene


def enemy_moss_mite():
    scene = trimesh.Scene()
    add(scene, "mite_body", ellipsoid((0.45, 0.55, 0.30), (0, 0, 0.36), PALETTE["moss_dark"]))
    add(scene, "mite_shell", ellipsoid((0.50, 0.48, 0.24), (0, 0.06, 0.56), PALETTE["stone"]))
    add(scene, "mite_moss_patch", ellipsoid((0.31, 0.28, 0.10), (-0.08, 0.06, 0.75), PALETTE["moss"]))
    add(scene, "mite_head", ellipsoid((0.34, 0.30, 0.23), (0, -0.42, 0.42), PALETTE["moss"]))
    add(scene, "mite_eye_L", ellipsoid((0.055, 0.030, 0.065), (-0.12, -0.69, 0.46), PALETTE["amber"]))
    add(scene, "mite_eye_R", ellipsoid((0.055, 0.030, 0.065), (0.12, -0.69, 0.46), PALETTE["amber"]))
    legs = [
        (-0.32, -0.22, 0.32, -0.58, -0.33, 0.16),
        (0.32, -0.22, 0.32, 0.58, -0.33, 0.16),
        (-0.40, 0.02, 0.32, -0.66, 0.04, 0.14),
        (0.40, 0.02, 0.32, 0.66, 0.04, 0.14),
        (-0.32, 0.25, 0.32, -0.56, 0.40, 0.15),
        (0.32, 0.25, 0.32, 0.56, 0.40, 0.15),
    ]
    for index, values in enumerate(legs, 1):
        x1, y1, z1, x2, y2, z2 = values
        add(scene, f"mite_leg_{index}", cylinder_between((x1, y1, z1), (x2, y2, z2), 0.055, PALETTE["charcoal"], 6))
    add(scene, "mite_feeler_L", cylinder_between((-0.14, -0.55, 0.55), (-0.25, -0.86, 0.67), 0.025, PALETTE["stone"], 6))
    add(scene, "mite_feeler_R", cylinder_between((0.14, -0.55, 0.55), (0.25, -0.86, 0.67), 0.025, PALETTE["stone"], 6))
    return scene


def enemy_prismwing():
    scene = trimesh.Scene()
    add(scene, "wing_body", ellipsoid((0.24, 0.32, 0.30), (0, 0, 0.84), PALETTE["violet_dark"]))
    add(scene, "wing_chest", ellipsoid((0.28, 0.25, 0.25), (0, -0.10, 1.02), PALETTE["violet"]))
    add(scene, "wing_head", ellipsoid((0.22, 0.21, 0.20), (0, -0.28, 1.22), PALETTE["violet"]))
    add(scene, "wing_eye_L", ellipsoid((0.05, 0.025, 0.055), (-0.08, -0.475, 1.25), PALETTE["cyan"]))
    add(scene, "wing_eye_R", ellipsoid((0.05, 0.025, 0.055), (0.08, -0.475, 1.25), PALETTE["cyan"]))
    add(scene, "wing_tail", cone(0.14, 0.48, (0, 0.12, 0.52), PALETTE["violet_dark"], 7, (0, 0, -1)))

    shape = [(0.00, 0.00), (0.46, 0.20), (0.62, 0.00), (0.40, -0.22)]
    left = prism([(-x, z) for x, z in shape], 0.07, (-0.18, 0.02, 1.03), PALETTE["cyan"])
    right = prism([(x, z) for x, z in shape], 0.07, (0.18, 0.02, 1.03), PALETTE["cyan"])
    left.apply_transform(trimesh.transformations.rotation_matrix(math.radians(-12), [0, 0, 1], point=(-0.18, 0.02, 1.03)))
    right.apply_transform(trimesh.transformations.rotation_matrix(math.radians(12), [0, 0, 1], point=(0.18, 0.02, 1.03)))
    add(scene, "wing_L", left)
    add(scene, "wing_R", right)
    add(scene, "wing_antenna_L", cylinder_between((-0.09, -0.40, 1.34), (-0.20, -0.62, 1.52), 0.02, PALETTE["charcoal"], 6))
    add(scene, "wing_antenna_R", cylinder_between((0.09, -0.40, 1.34), (0.20, -0.62, 1.52), 0.02, PALETTE["charcoal"], 6))
    return scene


def npc_waykeeper():
    scene = trimesh.Scene()
    add(scene, "npc_torso", ellipsoid((0.38, 0.25, 0.48), (0, 0, 1.08), PALETTE["teal"]))
    add(scene, "npc_undershirt", box((0.30, 0.27, 0.36), (0, -0.03, 1.10), PALETTE["cream"]))
    add(scene, "npc_head", ellipsoid((0.27, 0.24, 0.30), (0, -0.01, 1.67), PALETTE["skin_dark"]))
    add(scene, "npc_cowl", ellipsoid((0.34, 0.29, 0.20), (0, 0.03, 1.84), PALETTE["grayblue"]))
    add(scene, "npc_cowl_back", box((0.45, 0.18, 0.36), (0, 0.20, 1.56), PALETTE["grayblue"], (math.radians(8), 0, 0)))
    add(scene, "npc_arm_L", cylinder_between((-0.31, 0, 1.25), (-0.47, -0.02, 0.94), 0.105, PALETTE["teal"]))
    add(scene, "npc_arm_R", cylinder_between((0.31, 0, 1.25), (0.47, -0.02, 0.94), 0.105, PALETTE["teal"]))
    add(scene, "npc_hand_L", ellipsoid((0.10, 0.09, 0.11), (-0.49, -0.02, 0.88), PALETTE["skin_dark"]))
    add(scene, "npc_hand_R", ellipsoid((0.10, 0.09, 0.11), (0.49, -0.02, 0.88), PALETTE["skin_dark"]))
    add(scene, "npc_leg_L", cylinder_between((-0.15, 0, 0.78), (-0.15, 0, 0.34), 0.13, PALETTE["brown"]))
    add(scene, "npc_leg_R", cylinder_between((0.15, 0, 0.78), (0.15, 0, 0.34), 0.13, PALETTE["brown"]))
    add(scene, "npc_boot_L", box((0.26, 0.36, 0.20), (-0.15, -0.07, 0.16), PALETTE["dark_brown"]))
    add(scene, "npc_boot_R", box((0.26, 0.36, 0.20), (0.15, -0.07, 0.16), PALETTE["dark_brown"]))
    add(scene, "npc_satchel_strap", box((0.08, 0.32, 0.98), (0.04, 0.02, 1.10), PALETTE["tan"], (0, math.radians(-24), 0)))
    add(scene, "npc_satchel", box((0.34, 0.18, 0.31), (0.33, 0.18, 0.78), PALETTE["tan"]))
    add(scene, "npc_eye_L", ellipsoid((0.035, 0.020, 0.050), (-0.09, -0.235, 1.70), PALETTE["charcoal"]))
    add(scene, "npc_eye_R", ellipsoid((0.035, 0.020, 0.050), (0.09, -0.235, 1.70), PALETTE["charcoal"]))
    return scene


MODELS = {
    "hero_aster": ("Player adventurer", hero_aster),
    "enemy_moss_mite": ("Ground enemy", enemy_moss_mite),
    "enemy_prismwing": ("Flying enemy", enemy_prismwing),
    "npc_waykeeper": ("Neutral NPC base", npc_waykeeper),
}


def has_uv(mesh):
    uv = getattr(mesh.visual, "uv", None)
    return uv is not None and len(uv) == len(mesh.vertices)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_model(name, role, scene, path):
    raw = scene.export(file_type="glb")
    path.write_bytes(raw)

    loaded = trimesh.load(path, force="scene")
    geometries = list(loaded.geometry.values())
    bounds = loaded.bounds
    vertex_count = sum(len(g.vertices) for g in geometries)
    triangle_count = sum(len(g.faces) for g in geometries)

    return {
        "role": role,
        "file": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "mesh_count": len(geometries),
        "vertex_count": vertex_count,
        "triangle_count": triangle_count,
        "bounds": bounds.tolist() if bounds is not None else None,
        "extents_xyz": (bounds[1] - bounds[0]).tolist() if bounds is not None else None,
        "normals_present": all(len(g.vertex_normals) == len(g.vertices) for g in geometries),
        "uvs_present": all(has_uv(g) for g in geometries),
        "uses_vertex_colors": all(hasattr(g.visual, "face_colors") for g in geometries),
        "skeleton_skin_present": False,
        "animation_count": 0,
        "reload_parse": "PASS",
        "status": "CANDIDATE",
        "notes": "Separate named body-part meshes retained for later rigging/animation.",
    }


def main():
    report = {
        "pack_version": "0.1.0",
        "status": "CANDIDATE",
        "format": "glTF 2.0 binary (GLB)",
        "units": "meters",
        "generator": "trimesh 4.11.1",
        "models": {},
    }

    for name, (role, builder) in MODELS.items():
        scene = builder()
        report["models"][name] = validate_model(name, role, scene, OUT / f"{name}.glb")

    (OUT / "validation_report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )

    (OUT / "README.md").write_text(
        """# Character Pack v0.1.0 — CANDIDATE

Original low-poly mobile-friendly character meshes generated by this repository.

## Models
- hero_aster.glb — player adventurer
- enemy_moss_mite.glb — ground enemy
- enemy_prismwing.glb — flying enemy
- npc_waykeeper.glb — neutral NPC base

## Current state
These models use separate named body-part meshes and vertex colors. They are static
mesh candidates prepared for a later rigging/animation pass. They are not user-verified.

See validation_report.json for mesh counts, geometry budgets, hashes, bounds, and load checks.
""",
        encoding="utf-8",
    )

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
