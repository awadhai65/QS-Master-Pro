import networkx as nx


class GeometryGraph:

    def __init__(self):
        self.graph = nx.Graph()

    def _round_point(self, x, y):
        return (round(x, 3), round(y, 3))

    def add_line(self, x1, y1, x2, y2):

        p1 = self._round_point(x1, y1)
        p2 = self._round_point(x2, y2)

        self.graph.add_node(p1)
        self.graph.add_node(p2)

        self.graph.add_edge(
            p1,
            p2,
            length=((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        )

    def build(self, beam_entities):

        self.graph.clear()

        for beam in beam_entities:

            if beam["type"] != "LINE":
                continue

            self.add_line(
                beam["x1"],
                beam["y1"],
                beam["x2"],
                beam["y2"]
            )

    def total_nodes(self):
        return self.graph.number_of_nodes()

    def total_edges(self):
        return self.graph.number_of_edges()

    def connected_components(self):
        return list(nx.connected_components(self.graph))

    def print_summary(self):

        print("\n========== GEOMETRY GRAPH ==========\n")

        print("Nodes      :", self.total_nodes())
        print("Edges      :", self.total_edges())
        print("Components :", len(self.connected_components()))