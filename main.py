"""
main.py
"""

from __future__ import annotations

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from copy import copy

from Carte.Affichage import affiche
from enums import Tribes, Resources, Improvements, Terrains, tribes_dict

class View:
    """The view shows the network and allows the user to interact with it."""
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.wm_title("Network")
        self.figsize = (16, 8)

        # Buttons
        bq = tk.Button(master=self.root, text="Quit", command=self.root.quit)
        bq.pack(side=tk.BOTTOM)
        self.run = False
        self.bs = tk.Button(master=self.root, text="Save", command=self.save)
        self.bs.pack(side=tk.BOTTOM)
        self.bNW = tk.Button(master=self.root, text="Go NW", command=self.goNW)
        self.bNW.pack(side=tk.BOTTOM)
        self.bSE = tk.Button(master=self.root, text="Go SE", command=self.goSE)
        self.bSE.pack(side=tk.BOTTOM)
        self.bNE = tk.Button(master=self.root, text="Go NE", command=self.goNE)
        self.bNE.pack(side=tk.BOTTOM)
        self.bSW = tk.Button(master=self.root, text="Go SW", command=self.goSW)
        self.bSW.pack(side=tk.BOTTOM)
        self.be = tk.Button(master=self.root, text="Extend", command=self.extend)
        self.be.pack(side=tk.BOTTOM)
        self.bc = tk.Button(master=self.root, text="Contract", command=self.contract)
        self.bc.pack(side=tk.BOTTOM)
        self.bcap = tk.Button(master=self.root, text="Make Capital", command=self.make_capital)
        self.bcap.pack(side=tk.BOTTOM)

        # Menus
        tribe_var = tk.StringVar(value=list(Tribes)[0])
        self.tribe_menu = tk.OptionMenu(self.root, tribe_var,
                                                *list(Tribes),
                                                )
        self.tribe_menu.pack(side=tk.BOTTOM)
        resource_var = tk.StringVar(value=list(Resources)[0])
        self.resource_menu = tk.OptionMenu(self.root, resource_var,
                                                *list(Resources),
                                                )
        self.resource_menu.pack(side=tk.BOTTOM)
        improvement_var = tk.StringVar(value=list(Improvements)[0])
        self.improvement_menu = tk.OptionMenu(self.root, improvement_var,
                                                *list(Improvements),
                                                )
        self.improvement_menu.pack(side=tk.BOTTOM)
        terrain_var = tk.StringVar(value=list(Terrains)[0])
        self.terrain_menu = tk.OptionMenu(self.root, terrain_var,
                                                *list(Terrains),
                                                )
        self.terrain_menu.pack(side=tk.BOTTOM)

        self.carte = [[{"tribu": "imperius", "terrain": "water", "ressource": "", "batiment": ""}]]
        self.pos = (0, 0)
        self.capitals = []
        self.draw()
        self.root.mainloop()

    def save(self) -> None:
        """Save the map."""
        with open("map.json", "w") as f:
            f.write(str(self))
    
    def __str__(self) -> str:
        """String representation of the map."""
        capitals = []
        json = "{'map': ["
        i= 0
        for row in self.carte:
            for tile in row:
                json += "    {"
                json += f"'climate': {tribes_dict[Tribes(tile['tribu'])]}"
                if tile["ressource"] != "":
                    json += f", 'resource': '{tile['ressource']}'"
                if tile["batiment"] != "":
                    json += f", 'improvement': '{tile['batiment']}'"
                json += f", 'terrain': '{tile['terrain']}'"
                json += "},\n"
                if (i, 0) in self.capitals:
                    capitals.append(i)
                i += 1
        json = json[:-2] + "],\n"
        json += f"'capitals': {capitals},\n"
        return json + "}"

    def goNW(self) -> None:
        """Go NW."""
        self.pos = (self.pos[0], self.pos[1] - 1)
        self.draw()

    def goSE(self) -> None:
        """Go SE."""
        self.pos = (self.pos[0], self.pos[1] + 1)
        self.draw()

    def goNE(self) -> None:
        """Go NE."""
        self.pos = (self.pos[0] - 1, self.pos[1])
        self.draw()

    def goSW(self) -> None:
        """Go SW."""
        self.pos = (self.pos[0] + 1, self.pos[1])
        self.draw()

    def extend(self) -> None:
        """Extend the map."""
        for i, row in enumerate(self.carte):
            self.carte[i] = row + [{"tribu": "imperius", "terrain": "water", "ressource": "", "batiment": ""}]
        self.carte = self.carte + [[{"tribu": "imperius", "terrain": "water", "ressource": "", "batiment": ""}] * len(self.carte[0])]
        self.draw()

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
        self.draw()

    def make_capital(self) -> None:
        """Make the current tile a capital."""
        self.capitals.append(copy(self.pos))
        self.draw()

    def draw(self) -> None:
        """Draw the network."""
        fig = plt.figure(f"Map {self.pos}" + ("capital" if self.pos in self.capitals else ""),
                         figsize=self.figsize) # type: ignore
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
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    view = View()
