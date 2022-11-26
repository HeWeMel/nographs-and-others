from nographs_and_others.adapt_nographs import AdaptNoGraphsABC

import nographs as nog


class AdaptNoGraphsArray(AdaptNoGraphsABC):
    name = "nog@array"
    gear = nog.GearArraysForIntVertices()
