from collections import deque

class Jug:
    def __init__(self, capacity, content):
        self.capacity = capacity
        self.content = content

    def __eq__(self, other):
        return self.capacity == other.capacity and self.content == other.content

class WaterJugState:
    def __init__(self, jugs):
        self.jugs = jugs
        self.parent = None

    def __eq__(self, other):
        result = True
        
        for index in range(len(self.jugs)):
            result = result and self.jugs[index] == other.jugs[index]

        return result

    def __hash__(self):
        return hash((self.jug8, self.jug5, self.jug3))
    
    def is_valid_state(self):
        pass

    def __str__(self):
        return "; ".join([f"Jug {jug.capacity}: {jug.content}" for jug in self.jugs])
    
    def get_next_states(self):
        next_states = []
        number_of_pours = len(self.jugs) - 1
        actions = ["fill", "empty"]
        actions += ["pour" for i in range(number_of_pours)]

        for index in range(len(self.jugs)):
            current_pour = 1

            for action in actions:
                new_state = WaterJugState([Jug(jug.capacity, jug.content) for jug in self.jugs])
                new_state.parent = self

                match action:
                    case "fill":
                        new_state.jugs[index].content = self.jugs[index].capacity
                    case "empty":
                        new_state.jugs[index].content = 0
                    case "pour":
                        target_index = (index + current_pour) % len(self.jugs)
                        current_pour += 1

                        space_in_target = new_state.jugs[target_index].capacity - new_state.jugs[target_index].content

                        if space_in_target > 0:
                            if new_state.jugs[index].content >= space_in_target:
                                new_state.jugs[target_index].content += space_in_target
                                new_state.jugs[index].content -= space_in_target
                            else:
                                new_state.jugs[target_index].content += new_state.jugs[index].content
                                new_state.jugs[index].content = 0

                if new_state != self:
                    next_states.append(new_state) 

        return next_states

        # Mogelijke acties: vul jug8, vul jug5, vul jug3,  leeg jug8, leeg jug5, leeg jug3, elke mogelijk combinatie van giet van pot x naar pot y
        
        # HINT: als je overgiet van de bijvoorbeeld jug5 naar jug8, dan heb je in jug8 (8 - self.jug8) liter plaats, 
        # en in jug5 heb je (self.jug5) liter water zitten. Het kleinste getal van die 2, kan je effectief overgieten zonder morsen.

    def find_solution(self, goal_state):
        frontier = deque([self])
        visited_states = []

        while frontier:
            current_state = frontier.popleft()

            if current_state == goal_state:
                return current_state

            visited_states.append(current_state)

            for new_state in current_state.get_next_states():
                if new_state not in visited_states:
                    frontier.append(new_state)

        return None

if __name__ == '__main__':
    initial_state = WaterJugState([Jug(8, 8), Jug(5, 5), Jug(3, 0)])
    solution = initial_state.find_solution(WaterJugState([Jug(8, 4), Jug(5, 4), Jug(3, 0)]))
    if solution:
        print("Oplossing gevonden:")
        # print opeenvolgende stappen van de oplossing
        state = solution
        states = [solution]

        while state:
            states.append(state.parent)
            state = state.parent

        states.reverse()

        for state in states:
            print(state)
    else:
        print("Geen oplossing gevonden.")
