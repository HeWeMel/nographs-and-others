from nographs_and_others.adapt_nographs import AdaptNoGraphsABC

import nographs as nog


class AdaptNoGraphsIntIDsBitsPreferArrays(AdaptNoGraphsABC):
    name = "nog@IntId"  # Neither "prefer lists" nor "no bits", default
    gear = nog.GearForIntVertexIDsAndIntsMaybeFloats[int, None](False, False)


class AdaptNoGraphsIntIDsBitsPreferLists(AdaptNoGraphsABC):
    name = "@IntIdL"
    gear = nog.GearForIntVertexIDsAndIntsMaybeFloats[int, None](True, False)
    # This combination makes no sense: going from lists to arrays is at
    # least as helpful, but needs only 10% additional runtime, while
    # bit packing needs 30%.


class AdaptNoGraphsIntIDsNoBitsPreferArrays(AdaptNoGraphsABC):
    name = "@IntIdA0B"
    gear = nog.GearForIntVertexIDsAndIntsMaybeFloats[int, None](False, True)


class AdaptNoGraphsIntIDsNoBitsPreferLists(AdaptNoGraphsABC):
    name = "@IntIdL0B"
    gear = nog.GearForIntVertexIDsAndIntsMaybeFloats[int, None](True, True)


class AdaptNoGraphsIntIDsFloatsBits(AdaptNoGraphsABC):
    name = "@IntIdF"
    gear = nog.GearForIntVertexIDsAndCFloats[int, None](False)


class AdaptNoGraphsIntIDsFloatsNoBits(AdaptNoGraphsABC):
    name = "@IntIdF0B"
    gear = nog.GearForIntVertexIDsAndCFloats[int, None](True)
