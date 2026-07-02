from dxf_engine import DXFEngine

engine = DXFEngine()

path = input("DXF Path : ")

engine.load(path)

print("\n========== ENTITY SUMMARY ==========")

for k, v in engine.entity_summary().items():
    print(f"{k:20} {v}")

print("\n========== LAYERS ==========")

for layer in engine.get_layers():
    print(layer)

print("\n========== TOTAL TEXT ==========")
print(len(engine.get_texts()))

print("\n========== TOTAL LINES ==========")
print(len(engine.get_lines()))
from beam_engine import BeamEngine

beam_engine = BeamEngine(engine)

beam_lines = beam_engine.get_beam_entities()

print("\n========== BEAM LINES ==========\n")

print("Total Beam Entities :", len(beam_lines))

if len(beam_lines) == 0:
    print("No beam entities found on BEAM layer")

print()

for beam in beam_lines[:20]:
    print(beam)
    from centerline_engine import CenterlineEngine

center_engine = CenterlineEngine(beam_lines)

centerlines = center_engine.merge_parallel_lines()

print("\n========== CENTERLINES ==========\n")

print("Total Centerlines :", len(centerlines))

print()

for c in centerlines[:20]:
    print(c)
    from beam_engine_v2 import BeamEngineV2

beam2 = BeamEngineV2(engine)

beams = beam2.beam_centerlines()

print("\n========== BEAM ENGINE V2 ==========\n")

print("Detected Rectangular Beams :", len(beams))

print()

for b in beams[:20]:
    print(b)
    from geometry.graph import GeometryGraph

graph = GeometryGraph()

graph.build(beam_lines)

graph.print_summary()
from geometry.polygon import PolygonDetector

poly = PolygonDetector(graph)

poly.summary()
from geometry.skeleton import SkeletonEngine

sk = SkeletonEngine(graph)

beams = sk.create_skeleton()

print("\n========== SKELETON ==========\n")

print("Skeleton Beams :", len(beams))

print()

for beam in beams[:20]:
    print(beam)