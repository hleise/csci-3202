# Hunter Leise
# CSCI-3202 Problem Set 2
# Problem 2.1 (SIM Game)

import sys
import copy


class SimGraph:
    def __init__(self, graph=None):
        if graph is None:
            self.graph = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": []}
        else:
            self.graph = graph
        self.red_counter = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
        self.blue_counter = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

    def add_edge(self, node1, node2, color):
        self.graph[node1].append((node2, color))
        self.graph[node2].append((node1, color))
        if color == "red":
            self.red_counter[node1] += 1
            self.red_counter[node2] += 1
        elif color == "blue":
            self.blue_counter[node1] += 1
            self.blue_counter[node2] += 1

    def is_edge_taken(self, node1, node2):
        for edge in self.graph[node1]:
            if edge[0] == node2:
                return True

        return False

    def triangle_exists(self):
        visited = []
        for node in self.graph:
            visited.append(node)
            for edge1 in self.graph[node]:
                if edge1[0] not in visited:
                    for edge2 in self.graph[edge1[0]]:
                        if edge2 in self.graph[node] and edge2[1] == edge1[1]:
                            return True
        return False


class SimGame:
    def __init__(self):
        self.graph = SimGraph()

    def run_game(self):
        player_move = self.set_player()
        move_color = "blue"
        while not self.graph.triangle_exists():
            move_color = "red" if move_color == "blue" else "blue"
            if player_move:
                self.move(move_color)
            else:
                self.ai_move(move_color)

            player_move = not player_move

        print(move_color + " loses :(")

    def ai_move(self, color):
        if color == "red":
            cumulative_list = {key: self.graph.red_counter[key] +
                               len(self.graph.graph[key])
                               for key in self.graph.graph.keys()}
        else:
            cumulative_list = {key: self.graph.blue_counter[key] +
                               len(self.graph.graph[key])
                               for key in self.graph.graph.keys()}

        min_list = sorted(cumulative_list, key=cumulative_list.get)
        failing_move = ""

        for node1 in min_list:
            for node2 in min_list:
                if self.is_valid_move(node1, node2):
                    new_graph = SimGraph(copy.deepcopy(self.graph.graph))
                    new_graph.add_edge(node1, node2, color)
                    if not new_graph.triangle_exists():
                        self.graph.add_edge(node1, node2, color)
                        print("AI went from %s to %s" % (node1, node2))
                        return
                    else:
                        failing_move = node1 + node2

        # Only make a losing move if you absolutely have to
        self.graph.add_edge(failing_move[0], failing_move[1], color)
        print("AI went from %s to %s" % (failing_move[0], failing_move[1]))

    def move(self, color):
        move = input(color + " move: ").lower()
        if len(move) >= 2 and self.is_valid_move(move[0], move[1]):
            self.graph.add_edge(move[0], move[1], color)
        elif move == "graph":
            print(self.graph.graph)
            self.move(color)
        else:
            print("Invalid move")
            self.move(color)

    # Returns whether a move is valid
    def is_valid_move(self, node1, node2):
        if node1 in self.graph.graph.keys()\
           and node2 in self.graph.graph.keys()\
           and node1 != node2\
           and not self.graph.is_edge_taken(node1, node2)\
           and not self.graph.is_edge_taken(node2, node1):
            return True
        return False

    def set_player(self):
        user_input = input("Are you playing as Red? (Y/N): ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            return False
        print("Invalid input, enter 'y' or 'n'")
        return self.set_player()


if __name__ == "__main__":
    new_game = SimGame()
    new_game.run_game()
