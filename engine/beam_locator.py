import re


class BeamLocator:

    def __init__(self, modelspace):
        self.msp = modelspace

    def beam_labels(self):

        beams = []

        pattern = re.compile(r"^(B|CB|HB|KB)\d*$")

        for entity in self.msp.query("TEXT MTEXT"):

            try:

                if entity.dxftype() == "TEXT":
                    txt = entity.dxf.text.strip()
                    x = entity.dxf.insert.x
                    y = entity.dxf.insert.y

                else:
                    txt = entity.plain_text().strip()
                    x = entity.dxf.insert.x
                    y = entity.dxf.insert.y

                if pattern.match(txt):

                    beams.append({
                        "beam": txt,
                        "x": x,
                        "y": y
                    })

            except Exception:
                pass

        return beams