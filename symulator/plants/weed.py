from symulator.plants.plant import Plant


class Weed(Plant):

    def __init__(self, world):
        super().__init__(world)
        self.set_organizm()

    def set_organizm(self):
        self.name = "weed"
        self.strength = 10
        self.world.weed.append(self)

    def choose_plant(self):
        child = Weed(self.world)
        return child

    def outside_effect(self, org):
        if org.name != "cyber sheep":
            self.world.pygame.current_text.append("Weed intoxicates " + org.name)
            org.alivness = False

    def action(self):
        self.world.pygame.current_text.append("Weed intoxicates its surroundings.")
        self.kill_surrounding_organisms(None, "cyber sheep")
        super().action()
