import math


class SkeletonEngine:

    def __init__(self, graph):

        self.graph = graph

    def component_bbox(self, component):

        xs = []
        ys = []

        for x, y in component:

            xs.append(x)
            ys.append(y)

        return {
            "xmin": min(xs),
            "xmax": max(xs),
            "ymin": min(ys),
            "ymax": max(ys)
        }

    def create_skeleton(self):

        beams = []

        components = self.graph.connected_components()

        for comp in components:

            if len(comp) < 4:
                continue

            box = self.component_bbox(comp)

            width = box["xmax"] - box["xmin"]
            height = box["ymax"] - box["ymin"]

            if width > height:

                orientation = "H"

                length = width

                beam_width = height

                start = (
                    box["xmin"],
                    (box["ymin"] + box["ymax"]) / 2
                )

                end = (
                    box["xmax"],
                    (box["ymin"] + box["ymax"]) / 2
                )

            else:

                orientation = "V"

                length = height

                beam_width = width

                start = (
                    (box["xmin"] + box["xmax"]) / 2,
                    box["ymin"]
                )

                end = (
                    (box["xmin"] + box["xmax"]) / 2,
                    box["ymax"]
                )

            beams.append({

                "orientation": orientation,

                "length": round(length,3),

                "width": round(beam_width,3),

                "start": start,

                "end": end,

                "center": (
                    round((start[0]+end[0])/2,3),
                    round((start[1]+end[1])/2,3)
                )

            })

        return beams