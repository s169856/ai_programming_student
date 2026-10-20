from collections import deque

class WaterJugState:
    def __init__(self, jug8, jug5, jug3):
        self.jug8 = jug8
        self.jug5 = jug5
        self.jug3 = jug3
        self.parent = None

    def __eq__(self, other):
        #deze krijg je cadeau, zodat python kan checken of twee states hetzelfde zijn
        return self.jug8 == other.jug8 and self.jug5 == other.jug5 and self.jug3 == other.jug3

    def __hash__(self):
        return hash((self.jug8, self.jug5, self.jug3))
    
    def is_valid_state(self):
        pass
    
    def get_next_states(self):
        next_states = []

        # Mogelijke acties: vul jug8, vul jug5, vul jug3,  leeg jug8, leeg jug5, leeg jug3, elke mogelijk combinatie van giet van pot x naar pot y
        jugs = [self.jug8, self.jug5, self.jug3]

        # HINT: als je overgiet van de bijvoorbeeld jug5 naar jug8, dan heb je in jug8 (8 - self.jug8) liter plaats, 
        # en in jug5 heb je (self.jug5) liter water zitten. Het kleinste getal van die 2, kan je effectief overgieten zonder morsen.
        for jug1 in jugs:
            for jug2 in jugs:
                if jug1 == self.jug8 and self.jug8 < 8 :
                    new_state = WaterJugState()
                    plaats = 8 - jug1

                    if jug2 > plaats:
                        new_state.jug8 = self.jug8 + plaats
                    else:
                        new_state.jug8 = self.jug8 + jug2

                    next_states.append(new_state)

                if jug1 == self.jug5 and self.jug5 < 5:
                    new_state = WaterJugState()
                    plaats = 5 - jug1

                    if jug2 > plaats:
                        new_state.jug5 = self.jug5 + plaats
                    else:
                        new_state.jug5 = self.jug5 + jug2

                    next_states.append(new_state)

                if jug1 == self.jug3 and self.jug3 < 3:
                    new_state = WaterJugState()
                    plaats = 3 - jug1

                    if jug2 > plaats:
                        new_state.jug3 = self.jug3 + plaats
                    else:
                        new_state.jug3 = self.jug3 + jug2

                    next_states.append(new_state)

        return next_states

# De bedoeling is om een nieuw WaterJugState object te maken en dat dan te appenden aan de next_states list maar ik heb geen idee hoe ik ervoor kan zorgen dat ik de juiste waarden bekom en ze aan de juist parameter van het object toeken. Hierboven probeer ik de logica uit te werken voor het over gieten van 1 jug in een andere jug en die states toe te voegen aan de lijst

    def find_solution(self):
        frontier = [initial_state]
        explored_states = []
        goal_state = WaterJugState(4, 4, 0)

        while frontier:
            state = frontier.pop()

            if goal_state.__eq__(state):
                return state 

            for new_state in state.get_next_states():
                for explored_state in explored_states:
                    if new_state.__eq__(explored_state):
                        continue
                    new_state.parent = state
                    frontier.append(new_state)
                    explored_states.append(new_state)




if __name__ == '__main__':
    initial_state = WaterJugState(8, 5, 0)
    solution = initial_state.find_solution()
    if solution:
        print("Oplossing gevonden:")
        # print opeenvolgende stappen van de oplossing
    else:
        print("Geen oplossing gevonden.")
