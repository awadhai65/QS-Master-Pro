"""
QS Master Pro
DXF Reader Engine v0.1
"""

import ezdxf
from collections import Counter


class DXFReader:

    def __init__(self):
        self.doc = None
        self.msp = None
        self.filename = ""

    def open(self, filename):
        self.filename = filename
        self.doc = ezdxf.readfile(filename)
        self.msp = self.doc.modelspace()

    def entity_summary(self):

        counter = Counter()

        for entity in self.msp:
            counter[entity.dxftype()] += 1

        return dict(counter)

    def get_layers(self):

        layers = []

        for layer in self.doc.layers:
            layers.append(layer.dxf.name)

        return sorted(layers)

    def get_all_text(self):

        texts = []

        for entity in self.msp.query("TEXT MTEXT"):

            try:

                if entity.dxftype() == "TEXT":
                    txt = entity.dxf.text.strip()

                else:
                    txt = entity.plain_text().strip()

                if txt:
                    texts.append(txt)

            except Exception:
                pass

        return texts