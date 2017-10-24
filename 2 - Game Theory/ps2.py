# Hunter Leise
# CSCI-3202 Problem Set 2


# Question 2.1

class SimGraph:
    def __init__(self):
        self.graph = {
            "a": [],
            "b": [],
            "c": [],
            "d": [],
            "e": [],
            "f": [],
            "g": [],
            "h": []
        }

    def add_edge(self, node1, node2, color):
        self.graph[node1].append((node2, color))
        self.graph[node2].append((node1, color))

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
                            print(edge2[1] + " loses :(")
                            return True
        return False


class SimGame:
    def __init__(self):
        self.graph = SimGraph()

    def run_game(self):
        player_move = self.set_player()
        move_color = "red"
        while not self.graph.triangle_exists():
            if player_move:
                self.move(move_color)
            else:
                self.ai_move(move_color)

            player_move = not player_move
            move_color = "blue" if move_color == "red" else "red"

    def ai_move(self, color):
        for node1 in self.graph.graph.keys():
            for node2 in self.graph.graph.keys():
                if self.is_valid_move(node1, node2):
                    self.graph.add_edge(node1, node2, color)
                    print("AI went from %s to %s" % (node1, node2))
                    break
            break

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
