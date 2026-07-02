import math


class BeamEngine:

    def __init__(self, dxf_engine):
        self.engine = dxf_engine

    def get_beam_entities(self):

        beams = []

        for entity in self.engine.msp:

            try:

                layer = entity.dxf.layer.upper()

                if layer != "BEAM":
                    continue

                # -------- LINE --------
                if entity.dxftype() == "LINE":

                    x1 = entity.dxf.start.x
                    y1 = entity.dxf.start.y

                    x2 = entity.dxf.end.x
                    y2 = entity.dxf.end.y

                    length = math.hypot(x2 - x1, y2 - y1)

                    beams.append({
                        "type": "LINE",
                        "layer": layer,
                        "length": round(length, 3),
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2
                    })

                # -------- LWPOLYLINE --------
                elif entity.dxftype() == "LWPOLYLINE":

                    pts = list(entity.get_points())

                    for i in range(len(pts) - 1):

                        x1, y1 = pts[i][:2]
                        x2, y2 = pts[i + 1][:2]

                        length = math.hypot(x2 - x1, y2 - y1)

                        beams.append({
                            "type": "LWPOLYLINE",
                            "layer": layer,
                            "length": round(length, 3),
                            "x1": x1,
                            "y1": y1,
                            "x2": x2,
                            "y2": y2
                        })

            except Exception:
                pass

        return beams