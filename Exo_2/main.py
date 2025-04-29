import logging
import sys

from character import Magician, Warrior, Weapon, Character
from character import CharacterError
from simulator import FightSimulator

log = logging.getLogger(__name__)


def main():
    simulator = FightSimulator(
        [
            Warrior("Thor", Weapon("Hammer", 3.0)),
            Magician("Gandalf"),
            Magician("Merlin"),
            Warrior("Gimli", Weapon("Axe", 4.0)),
        ]
    )

    simulator.run()

def debug():
    """Debug function to test the simulator."""
    basic_fighter = Character("Soldier")

if __name__ == "__main__":

    # Switch level to logging.DEBUG to activate debug logs
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    #debug()
    main()
