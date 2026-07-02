import ezdxf
from collections import Counter


class DXFEngine:
    def __init__(self):
        self.doc = None
        self.msp = None
        self.filename = None

    def load(self, filename):
        """Load DXF file"""
        self.filename = filename
        self.doc = ezdxf.readfile(filename)
        self.msp = self.doc.modelspace()

    def entity_summary(self):
        """Return entity count"""
        counter = Counter()

        for entity in self.msp:
            counter[entity.dxftype()] += 1

        return dict(counter)

    def get_layers(self):
        """Return all layer names"""
        return sorted(layer.dxf.name for layer in self.doc.layers)

    def get_texts(self):
        """Return TEXT & MTEXT with coordinates"""
        texts = []

        for entity in self.msp.query("TEXT MTEXT"):
            try:
                if entity.dxftype() == "TEXT":
                    txt = entity.dxf.text
                    x = entity.dxf.insert.x
                    y = entity.dxf.insert.y
                else:
                    txt = entity.plain_text()
                    x = entity.dxf.insert.x
                    y = entity.dxf.insert.y

                texts.append({
                    "text": txt.strip(),
                    "x": x,
                    "y": y
                })
            except Exception:
                pass

        return texts

    def get_lines(self):
        """Return all LINE entities"""
        lines = []

        for entity in self.msp.query("LINE"):
            try:
                lines.append({
                    "x1": entity.dxf.start.x,
                    "y1": entity.dxf.start.y,
                    "x2": entity.dxf.end.x,
                    "y2": entity.dxf.end.y,
                    "layer": entity.dxf.layer
                })
            except Exception:
                pass

        return lines