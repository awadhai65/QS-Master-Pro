import math


class SnapEngine:

    def __init__(self, tolerance=0.05):
        self.tolerance = tolerance

    def distance(self, p1, p2):

        return math.hypot(
            p1[0]-p2[0],
            p1[1]-p2[1]
        )

    def snap_points(self, points):

        snapped = []

        for p in points:

            found = False

            for i, sp in enumerate(snapped):

                if self.distance(p, sp) <= self.tolerance:

                    snapped[i] = (
                        (p[0]+sp[0])/2,
                        (p[1]+sp[1])/2
                    )

                    found = True

                    break

            if not found:
                snapped.append(p)

        return snapped