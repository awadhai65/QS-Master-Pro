import math


class CenterlineEngine:

    def __init__(self, beam_entities):
        self.beam_entities = beam_entities

    def distance_between_parallel(self, a, b):
        """
        Distance between two parallel vertical or horizontal lines.
        """

        # Vertical
        if abs(a["x1"] - a["x2"]) < 0.001 and abs(b["x1"] - b["x2"]) < 0.001:
            return abs(a["x1"] - b["x1"])

        # Horizontal
        if abs(a["y1"] - a["y2"]) < 0.001 and abs(b["y1"] - b["y2"]) < 0.001:
            return abs(a["y1"] - b["y1"])

        return None

    def merge_parallel_lines(self):

        centerlines = []

        used = set()

        tolerance = 0.35

        for i in range(len(self.beam_entities)):

            if i in used:
                continue

            line1 = self.beam_entities[i]

            for j in range(i + 1, len(self.beam_entities)):

                if j in used:
                    continue

                line2 = self.beam_entities[j]

                d = self.distance_between_parallel(line1, line2)

                if d is None:
                    continue

                if d > tolerance:
                    continue

                # Vertical Beam
                if abs(line1["x1"] - line1["x2"]) < 0.001:

                    cx = (line1["x1"] + line2["x1"]) / 2

                    y1 = min(line1["y1"], line1["y2"])
                    y2 = max(line1["y1"], line1["y2"])

                    length = abs(y2 - y1)

                    centerlines.append({
                        "orientation": "V",
                        "beam_width": round(d, 3),
                        "length": round(length, 3),
                        "cx": round(cx, 3),
                        "cy": round((y1 + y2) / 2, 3)
                    })

                # Horizontal Beam
                else:

                    cy = (line1["y1"] + line2["y1"]) / 2

                    x1 = min(line1["x1"], line1["x2"])
                    x2 = max(line1["x1"], line1["x2"])

                    length = abs(x2 - x1)

                    centerlines.append({
                        "orientation": "H",
                        "beam_width": round(d, 3),
                        "length": round(length, 3),
                        "cx": round((x1 + x2) / 2, 3),
                        "cy": round(cy, 3)
                    })

                used.add(i)
                used.add(j)

                break

        return centerlines