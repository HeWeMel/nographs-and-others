from nographs_and_others.adapt_nographs import AdaptNoGraphsABC

import nographs as nog

from intbitset import intbitset  # type: ignore


class GearBitsetAndArrayForIntVertices(nog.GearArraysForIntVertices):
    def vertex_id_set(self, vertices):
        return intbitset(vertices)


class AdaptNoGraphsBitsetAndArray(AdaptNoGraphsABC):
    name = "nog+intset"
    gear = GearBitsetAndArrayForIntVertices()
