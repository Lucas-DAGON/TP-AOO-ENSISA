import logging
import random

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""
    print("CharacterError: Invalid character operation.")


class Character:
    """A class representing a character with a name, _life, _attack, and _defense.""" 
    

    def __init__(self, _name: str, _attack:float = 20.0, _life:float = 100.0, _defense:float = 0.1) -> None:
        """Initialize the character with a name, life, attack, and defense."""
        self._name = _name
        self._attack:float = _attack
        self._life:float = _life
        self._defense:float = _defense

    def take_damage(self, damage_value: float) -> None:
        """Apply damage to the character."""
        if damage_value < 0:
            raise CharacterError("Damage cannot be negative.")
        self._life -= damage_value * self._defense

    def attack(self, target: "Character") -> None:
        """Attack another character."""
        if not isinstance(target, Character):
            raise CharacterError()
        damage_value = self._attack
        if damage_value > 0:
            target.take_damage(damage_value)
        else:
            log.warning(f"{self._name} attacked {target._name}, but the attack was ineffective.")

    @property
    def name(self) -> str:
        """Return the name of the character."""
        return self._name
    
    @property
    def is_dead(self) -> bool:
        """Check if the character is dead."""
        return self._life <= 0

    def __repr__(self) -> str:
        """Return a string representation of the character."""
        return f"{self._name} <{self._life}>"

class Weapon:
    """A class representing a weapon with a name and attack."""
    def __init__(self, _name: str, attack: float) -> None:
        """Initialize the weapon with a name and attack."""
        self._name = _name
        self.attack = attack

    @classmethod
    def default(cls) -> None:
        """Return a default weapon."""
        return cls("Wood stick", 1.0)
    
    @property
    def name(self) -> str:
        """Return the name of the weapon."""
        return self._name

class Warrior(Character):
    """A class representing a warrior character with a weapon."""
    def __init__(self, _name: str, weapon: Weapon = "Wood stick") -> None:
        """Initialize the warrior with a name and weapon."""
        super().__init__(_name, _attack = 20.0, _life = 100.0, _defense = 0.1)
        self._weapon = weapon
        self._attack = self._attack + weapon.attack
        self._life = self._life * 1.5
        self._defense = self._defense * 1.2

    def attack(self, target: Character) -> None:
        """Attack another character with the weapon."""
        if not isinstance(target, Character):
            raise CharacterError()
        damage_value = self._weapon.attack + self._attack
        if in_rage := self.is_raging:
            damage_value *= 0.2
        if damage_value > 0:
            target.take_damage(damage_value)
        else:
            log.warning(f"{self._name} attacked {target._name}, but the attack was ineffective.")

    @property
    def is_raging(self) -> bool:
        """Check if the warrior is raging."""
        return True


class Magician(Character):
    """A class representing a magician character."""
    def __init__(self, _name: str) -> None:
        """Initialize the magician with a name."""
        super().__init__(_name, _attack = 10.0 * 2, _life = 100.0 * 0.8, _defense = 0.1)

    def attack(self, target: Character) -> None:
        """Attack another character."""
        if not isinstance(target, Character):
            raise CharacterError()
        damage_value = self._attack + 10.0
        if damage_value > 0:
            target.take_damage(damage_value)
        else:
            log.warning(f"{self._name} attacked {target._name}, but the attack was ineffective.")

    def _activate_magical_shield(self) -> bool:
        """Activate the magical shield."""
        if random.random() <= 0.33:
            log.info(f"{self._name} activated the magical shield.")
            return True
        else:
            log.info(f"{self._name} failed to activate the magical shield.")
            return False
        
    def take_damage(self, damage_value):
        """Apply damage to the magician."""
        if self._activate_magical_shield():
            log.info(f"{self._name} is protected by the magical shield.")
            return
        else:
            return super().take_damage(damage_value)
        