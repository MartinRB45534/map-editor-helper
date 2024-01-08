"""
main.py
"""

from __future__ import annotations

import sys

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from copy import copy

from Carte.Affichage import affiche
from enums import Tribes, Resources, Improvements, Terrains, tribes_dict, climates_dict

class View:
    """The view shows the network and allows the user to interact with it."""
    def __init__(self, carte=None) -> None:
        self.root = tk.Tk()
        self.figsize = (16, 8)

        # Buttons
        self.bq = tk.Button(master=self.root, text="Quit", command=self.root.quit)
        self.bq.grid(row=4, column=1, columnspan=2)
        self.bq.configure(bg="red")
        self.bs = tk.Button(master=self.root, text="Save", command=self.save)
        self.bs.grid(row=4, column=3, columnspan=2)
        self.bs.configure(bg="green")

        self.bNW = tk.Button(master=self.root, text="Go NW", command=self.goNW)
        self.bNW.grid(row=2, column=0, sticky=tk.E)
        self.bSW = tk.Button(master=self.root, text="Go SW", command=self.goSW)
        self.bSW.grid(row=3, column=0, sticky=tk.E)

        self.bNE = tk.Button(master=self.root, text="Go NE", command=self.goNE)
        self.bNE.grid(row=2, column=1, sticky=tk.W)
        self.bSE = tk.Button(master=self.root, text="Go SE", command=self.goSE)
        self.bSE.grid(row=3, column=1, sticky=tk.W)

        self.be = tk.Button(master=self.root, text="Extend", command=self.extend)
        self.be.grid(row=2, column=2, sticky=tk.E)
        self.bc = tk.Button(master=self.root, text="Contract", command=self.contract)
        self.bc.grid(row=2, column=3, sticky=tk.W)
        self.bcap = tk.Button(master=self.root, text="Make Capital", command=self.make_capital)
        self.bcap.grid(row=3, column=2, columnspan=2)

        # Menus
        self.tribe_var = tk.StringVar(value=list(Tribes)[0])
        self.tribe_menu = tk.OptionMenu(self.root, self.tribe_var,
                                        *list(Tribes),
                                        command=self.change_tribe,
                                        )
        self.tribe_menu.grid(row=2, column=4, sticky=tk.E)
        self.resource_var = tk.StringVar(value=list(Resources)[0])
        self.resource_menu = tk.OptionMenu(self.root, self.resource_var,
                                           *list(Resources),
                                           command=self.change_resource,
                                           )
        self.resource_menu.grid(row=3, column=4, sticky=tk.E)

        self.improvement_var = tk.StringVar(value=list(Improvements)[0])
        self.improvement_menu = tk.OptionMenu(self.root, self.improvement_var,
                                               *list(Improvements),
                                               command=self.change_improvement,
                                               )
        self.improvement_menu.grid(row=3, column=5, sticky=tk.W)

        self.terrain_var = tk.StringVar(value=list(Terrains)[0])
        self.terrain_menu = tk.OptionMenu(self.root, self.terrain_var,
                                           *list(Terrains),
                                           command=self.change_terrain,
                                           )
        self.terrain_menu.grid(row=2, column=5, sticky=tk.W)

        # Map
        if carte is not None:
            cases = carte["map"]
            nb_cases = len(cases)
            # Is it a square?
            if nb_cases ** 0.5 == int(nb_cases ** 0.5):
                self.carte = [[cases[i * int(nb_cases ** 0.5) + j] for j in range(int(nb_cases ** 0.5))] for i in range(int(nb_cases ** 0.5))]
                self.capitals = [(i, j) for i in range(int(nb_cases ** 0.5)) for j in range(int(nb_cases ** 0.5)) if i * int(nb_cases ** 0.5) + j in carte["capitals"]]
                self.carte = [[{"tribu": climates_dict[case["climate"]], "terrain": case["terrain"], "ressource": case["resource"] if "resource" in case else "", "batiment": case["improvement"] if "improvement" in case else ""} for case in row] for row in self.carte]
            else:
                carte = None
        if carte is None:
            self.carte = [[{"tribu": "aimo", "terrain": "ocean", "ressource": "", "batiment": ""}]]
            self.capitals = []
        self.pos = (0, 0)
        self.draw()
        self.root.mainloop()
        exit()

    def change_tribe(self, tribe: tk.StringVar) -> None:
        """Change the tribe of the current tile."""
        self.carte[self.pos[0]][self.pos[1]]["tribu"] = tribe
        self.redraw()

    def change_resource(self, resource: tk.StringVar) -> None:
        """Change the resource of the current tile."""
        self.carte[self.pos[0]][self.pos[1]]["ressource"] = resource
        self.redraw()

    def change_improvement(self, improvement: tk.StringVar) -> None:
        """Change the improvement of the current tile."""
        self.carte[self.pos[0]][self.pos[1]]["batiment"] = improvement
        self.redraw()

    def change_terrain(self, terrain: tk.StringVar) -> None:
        """Change the terrain of the current tile."""
        self.carte[self.pos[0]][self.pos[1]]["terrain"] = terrain
        self.redraw()

    def save(self) -> None:
        """Save the map."""
        with open("map.json", "w") as f:
            f.write(str(self))
    
    def __str__(self) -> str:
        """String representation of the map."""
        capitals = []
        json = '{"map": ['
        i= 0
        for j, row in enumerate(self.carte):
            for k, tile in enumerate(row):
                json += '    {'
                json += f'"climate": {tribes_dict[Tribes(tile["tribu"])]}'
                if tile["ressource"] != "":
                    json += f', "resource": "{tile["ressource"]}"'
                if tile["batiment"] != "":
                    json += f', "improvement": "{tile["batiment"]}"'
                json += f', "terrain": "{tile["terrain"]}"'
                json += '},\n'
                if (j, k) in self.capitals:
                    capitals.append(i)
                i += 1
        json = json[:-2] + '],\n'
        json += f'"capitals": {capitals}\n'
        return json + '}'

    def move(self, new_pos: tuple[int, int]) -> None:
        """Move to a new position."""
        if new_pos[0] < 0:
            return
        if new_pos[1] < 0:
            return
        if new_pos[0] >= len(self.carte):
            return
        if new_pos[1] >= len(self.carte[0]):
            return
        self.pos = new_pos
        self.tribe_var.set(self.carte[self.pos[0]][self.pos[1]]["tribu"])
        self.resource_var.set(self.carte[self.pos[0]][self.pos[1]]["ressource"])
        self.improvement_var.set(self.carte[self.pos[0]][self.pos[1]]["batiment"])
        self.terrain_var.set(self.carte[self.pos[0]][self.pos[1]]["terrain"])
        self.redraw()

    def goNW(self) -> None:
        """Go NW."""
        self.move((self.pos[0], self.pos[1] - 1))

    def goSE(self) -> None:
        """Go SE."""
        self.move((self.pos[0], self.pos[1] + 1))

    def goNE(self) -> None:
        """Go NE."""
        self.move((self.pos[0] - 1, self.pos[1]))

    def goSW(self) -> None:
        """Go SW."""
        self.move((self.pos[0] + 1, self.pos[1]))

    def extend(self) -> None:
        """Extend the map."""
        for i, row in enumerate(self.carte):
            self.carte[i] = row + [{"tribu": "aimo", "terrain": "ocean", "ressource": "", "batiment": ""}]
        self.carte = self.carte + [[{"tribu": "aimo", "terrain": "ocean", "ressource": "", "batiment": ""} for _ in range(len(self.carte[0]))]]
        print("Extending map")
        self.redraw()

    def contract(self) -> None:
        """Contract the map."""
        if len(self.carte) == 1:
            return
        self.carte = self.carte[:-1]
        for i, row in enumerate(self.carte):
            self.carte[i] = row[:-1]
        if 0 > self.pos[0] >= len(self.carte):
            self.pos = (len(self.carte) - 1, self.pos[1])
        if 0 > self.pos[1] >= len(self.carte[0]):
            self.pos = (self.pos[0], len(self.carte[0]) - 1)
        self.redraw()

    def make_capital(self) -> None:
        """Make the current tile a capital."""
        self.capitals.append(copy(self.pos))
        self.redraw()

    def redraw(self) -> None:
        """Redraw the map."""
        self.root.wm_title(f"Map {self.pos}" + ("capital" if self.pos in self.capitals else ""))
        plt.clf()
        b, centers = affiche(self.carte)
        plt.gca().imshow(b)
        # Add a point where we are
        plt.gca().scatter(centers[self.pos[0]][self.pos[1]][0], centers[self.pos[0]][self.pos[1]][1], c="red")
        plt.gca().set_axis_off()
        self.canvas.draw()

    def draw(self) -> None:
        """Draw the network."""
        fig = plt.figure(figsize=self.figsize)
        if self.carte == []:
            return
        ax1 = plt.axes()
        b, centers = affiche(self.carte)
        ax1.imshow(b)
        # Add a point where we are
        ax1.scatter(centers[self.pos[0]][self.pos[1]][0], centers[self.pos[0]][self.pos[1]][1], c="red")
        ax1.set_axis_off()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=2, columnspan=6)

if __name__ == "__main__":
    # did we get a file as an argument?

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            carte = eval(f.read())
    else:
        carte = None

    view = View(carte)
