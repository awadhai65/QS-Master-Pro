class LineDetector:

    def __init__(self, modelspace):
        self.msp = modelspace

    def get_lines(self):

        lines = []

        for entity in self.msp.query("LINE"):

            try:

                lines.append({
                    "x1": entity.dxf.start.x,
                    "y1": entity.dxf.start.y,
                    "x2": entity.dxf.end.x,
                    "y2": entity.dxf.end.y
                })

            except Exception:
                pass

        return lines