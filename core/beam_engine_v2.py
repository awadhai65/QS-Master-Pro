"""
QS Master Pro
Beam Engine V2
Reads Beam Geometry from DXF
"""

import math


class BeamEngineV2:

    def __init__(self, dxf_engine):

        self.engine = dxf_engine

    # ----------------------------------------------------
    # Utility
    # ----------------------------------------------------

    def distance(self, p1, p2):

        return math.hypot(
            p2[0] - p1[0],
            p2[1] - p1[1]
        )

    # ----------------------------------------------------
    # Read Beam Layer
    # ----------------------------------------------------

    def read_entities(self):

        entities = []

        for e in self.engine.msp:

            try:

                if e.dxf.layer.upper() != "BEAM":
                    continue

                # LINE

                if e.dxftype() == "LINE":

                    entities.append({
                        "type": "LINE",
                        "start": (
                            e.dxf.start.x,
                            e.dxf.start.y
                        ),
                        "end": (
                            e.dxf.end.x,
                            e.dxf.end.y
                        )
                    })

                # LWPOLYLINE

                elif e.dxftype() == "LWPOLYLINE":

                    pts = []

                    for p in e.get_points():

                        pts.append((p[0], p[1]))

                    entities.append({
                        "type": "LWPOLYLINE",
                        "points": pts
                    })

            except Exception:

                pass

        return entities

    # ----------------------------------------------------
    # Detect Rectangular Beam Outlines
    # ----------------------------------------------------

    def detect_rectangles(self):

        rectangles = []

        entities = self.read_entities()

        for ent in entities:

            if ent["type"] != "LWPOLYLINE":
                continue

            pts = ent["points"]

            if len(pts) != 4 and len(pts) != 5:
                continue

            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]

            xmin = min(xs)
            xmax = max(xs)

            ymin = min(ys)
            ymax = max(ys)

            width = xmax - xmin
            height = ymax - ymin

            rectangles.append({

                "xmin": xmin,
                "xmax": xmax,

                "ymin": ymin,
                "ymax": ymax,

                "width": round(width,3),
                "height": round(height,3),

                "cx": round((xmin+xmax)/2,3),
                "cy": round((ymin+ymax)/2,3)

            })

        return rectangles

    # ----------------------------------------------------
    # Beam Centerline
    # ----------------------------------------------------

    def beam_centerlines(self):

        beams = []

        rects = self.detect_rectangles()

        for r in rects:

            if r["width"] > r["height"]:

                orientation = "H"

                beam_length = r["width"]

                beam_width = r["height"]

            else:

                orientation = "V"

                beam_length = r["height"]

                beam_width = r["width"]

            beams.append({

                "orientation": orientation,

                "length": round(beam_length,3),

                "width": round(beam_width,3),

                "cx": r["cx"],

                "cy": r["cy"]

            })

        return beams