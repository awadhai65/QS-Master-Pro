from line_detector import LineDetector
from reader import DXFReader
from parser import DrawingParser
from beam_locator import BeamLocator

# Create reader
reader = DXFReader()

# Ask for DXF file
filename = input("Enter DXF Path : ")

# Load DXF
reader.open(filename)

print("\nDXF Loaded Successfully\n")

# Entity Summary
print("========== ENTITY SUMMARY ==========\n")

entities = reader.entity_summary()

for key, value in entities.items():
    print(f"{key:20} {value}")

# Read all texts
texts = reader.get_all_text()

# Parse labels
parser = DrawingParser(texts)

print("\n========== BEAMS ==========\n")

for beam in parser.beam_ids():
    print(beam)

print("\n========== SLABS ==========\n")

for slab in parser.slab_ids():
    print(slab)

print("\n========== LAYERS ==========\n")

for layer in reader.get_layers():
    print(layer)

# Beam Coordinates
locator = BeamLocator(reader.msp)

beams = locator.beam_labels()

print("\n========== BEAM COORDINATES ==========\n")

for beam in beams:
    print(
        beam["beam"],
        beam["x"],
        beam["y"]
    )

print("\n========== LINE COUNT ==========\n")

detector = LineDetector(reader.msp)

lines = detector.get_lines()

print(f"Total LINE entities : {len(lines)}")

print("\nFirst 10 Lines:\n")

for line in lines[:10]:
    print(line)