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