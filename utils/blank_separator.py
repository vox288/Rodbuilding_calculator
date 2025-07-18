
# This module is used to calculate measurements
# for building fishing rods.
#
# By passing a rodlenght, number of rings and
# an optional modifier it can calculate :
#   - position for the reel_seat
#   - position for the start_ring from bottom up
#   - length of the ringed section
#   - gaps between the rings from tip to bottom
#     and scale those to fit the blank
#
# The modifier will change the relation of gaps
# between the rings. A higher modifier (up to 0.16)
# will shift the rings more to the tip. 
# A lower modifier (down to 0.04) will spread the
# ring gaps more even around the blank


class BlankSeparator:
    """
    Calculates the ideal position of fishingrod components.
    
    Based on rodlenght, number of rings and optional modifier
        length (int)     -- the length of the blank in cm
        rings (int)      -- number of rings, at least 2
        modifier (float) -- default 0.1, changes gap relations
    """
    def __init__(self, length:int, rings:int, modifier:float=0.1):
        self.length = length
        self.rings = rings
        self.modifier = modifier

    def _validate_input(self):
        if not isinstance(self.length, (int, float)):
            raise TypeError("Rodlenght must be a number > 0")
        if self.length <= 0:
            raise ValueError("Rodlenght must be a positive number")
        if not isinstance(self.rings, int):
            raise TypeError("Rings must be a natural number")
        if self.rings <= 1:
            raise ValueError("At least 2 rings are required")
        if not isinstance(self.modifier, float):
            raise TypeError("Modifier has to be a float")
        if self.modifier < 0.04 or self.modifier > 0.16:
            raise ValueError("Modifier is beyond boundary 0.04 - 0.16")

    def calc_reel_seat(self) -> float:
        """Based on rodlenght returns ideal position for reel_seat"""
        self._validate_input()
        multiplicator = 17 - (self.length/100)
        reel_seat = (self.length / 100) * multiplicator
        return round(reel_seat, 2)
      

    def calc_start_ring(self) -> float:
        """Based on rodlenght returns position for the start_ring."""
        self._validate_input()
        start_ring = (self.length / 100) * 24
        return round(start_ring, 2)



    def calc_ringed_section(self) -> float:
        """
        Subtracts reel_seat and start_ring from length
        to calculate ringed section.
        """
        self._validate_input()
        ringed_section = self.length - (
            self.calc_reel_seat() + self.calc_start_ring()
        )
        return round(ringed_section, 2)



    def calc_ring_positions(self) -> dict:
        """
        Calculates the gaps and the increase of their size,
        based on the modifier.
        
        Divides the ringed section into even pieces and multiplies
        them to the power of an increasing modifier

            Returns a dict with increasing gaps
        """
        self._validate_input()
        ring_positions = {}
        sections = self.calc_ringed_section() / (self.rings - 1)
        increase = 0.8
        for ring in range(self.rings - 1):
            position = sections**increase
            ring_positions[ring + 2] = round(position, 2)
            increase += self.modifier
        return ring_positions



    def scale_ring_positions(self):
        """
        Scales gaps to fit actual ringed section and assigns positions to rings.
        Returns:
            dict: (label, ring_number) → scaled position
        """
        self._validate_input()
        scaled_ring_position = {
            ("Ring 1"): 0.00,
        }
        ring_positions = self.calc_ring_positions()
        total_ringed_section = sum(ring_positions.values())
        ring_number = 2
        for ring in ring_positions.values():
            scale_down = ring / total_ringed_section
            scale_up = scale_down * self.calc_ringed_section()
            scaled_ring_position[f"Ring {ring_number}"] = round(scale_up, 2)
            ring_number += 1
        return scaled_ring_position



#For testing purpose
#
#if __name__ == "__main__":
#    run = BlankSeparator(210, 7, 0.1)
#    print("reel_seat at", run.calc_reel_seat())
#    print("start_ring at", run.calc_start_ring())
#    print("ringed section", run.calc_ringed_section())
#    print("ring gaps", run._calc_ring_positions())
#    print("ring positions at", run.scale_ring_positions())
