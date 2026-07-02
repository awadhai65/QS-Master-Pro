import ezdxf
from collections import Counter
import re


class DXFReader:

    def __init__(self):
        self.doc = None
        self.msp = None

    def open(self, filename):

        self.doc = ezdxf.readfile(filename)

        self.msp = self.doc.modelspace()

    def get_entity_summary(self):

        counter = Counter()

        for e in self.msp:

            counter[e.dxftype()] += 1

        return counter

    def get_layers(self):

        layers = []

        for layer in self.doc.layers:

            layers.append(layer.dxf.name)

        return sorted(layers)

    def get_beam_labels(self):

        beams = set()

        pattern = re.compile(r"^(B|CB|HB|KB)\d*$")

        for entity in self.msp.query("TEXT MTEXT"):

            try:

                if entity.dxftype() == "TEXT":

                    txt = entity.dxf.text.strip()

                else:

                    txt = entity.plain_text().strip()

                if pattern.match(txt):

                    beams.add(txt)

            except:

                pass

        return sorted(beams)