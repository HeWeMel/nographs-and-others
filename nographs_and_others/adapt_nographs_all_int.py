from nographs_and_others.adapt_nographs import AdaptNoGraphsABC

import nographs as nog


class AdaptNoGraphsAllIntBits(AdaptNoGraphsABC):
    name = "nog@Int"  # Without option "no bits", default, with bit packing
    gear = nog.GearForIntVerticesAndIDsAndIntsMaybeFloats[None](False)


class AdaptNoGraphsAllIntFloatsBits(AdaptNoGraphsABC):
    name = "@IntF"  # Float, without option "no bits", default, with bit packing
    gear = nog.GearForIntVerticesAndIDsAndCFloats[None](False)


class AdaptNoGraphsAllIntFloatsNoBits(AdaptNoGraphsABC):
    name = "@IntF0B"
    gear = nog.GearForIntVerticesAndIDsAndCFloats[None](True)
