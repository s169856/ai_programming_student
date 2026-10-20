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
        
        # HINT: als je overgiet van de bijvoorbeeld jug5 naar jug8, dan heb je in jug8 (8 - self.jug8) liter plaats, 
        # en in jug5 heb je (self.jug5) liter water zitten. Het kleinste getal van die 2, kan je effectief overgieten zonder morsen.

    def find_solution(self):
        pass


if __name__ == '__main__':
    initial_state = WaterJugState(8, 5, 0)
    solution = initial_state.find_solution()
    if solution:
        print("Oplossing gevonden:")
        # print opeenvolgende stappen van de oplossing
    else:
        print("Geen oplossing gevonden.")
