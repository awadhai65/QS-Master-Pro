from collections import defaultdict


class PolygonDetector:

    def __init__(self, graph):
        self.graph = graph

    def find_components(self):
        """
        Return connected components having
        at least 4 nodes.
        """

        components = []

        for comp in self.graph.connected_components():

            if len(comp) >= 4:
                components.append(comp)

        return components

    def summary(self):

        comps = self.find_components()

        print("\n========== POLYGON DETECTOR ==========\n")

        print("Candidate Components :", len(comps))

        for i, comp in enumerate(comps[:10], start=1):
            print(
                f"Component {i} : {len(comp)} Nodes"
            )