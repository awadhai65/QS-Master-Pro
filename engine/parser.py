import re


class DrawingParser:

    def __init__(self, texts):

        self.texts = texts

    def beam_ids(self):

        beams = []

        pattern = re.compile(r"^(B|CB|HB|KB)\d*$")

        for text in self.texts:

            if pattern.match(text):
                beams.append(text)

        return sorted(set(beams))

    def slab_ids(self):

        slabs = []

        pattern = re.compile(r"^S\d+$")

        for text in self.texts:

            if pattern.match(text):
                slabs.append(text)

        return sorted(set(slabs))