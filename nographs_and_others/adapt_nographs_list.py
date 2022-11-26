from nographs_and_others.adapt_nographs import AdaptNoGraphsABC

import nographs as nog


class AdaptNoGraphsList(AdaptNoGraphsABC):
    name = "nog@list"
    gear = nog.GearListsForIntVertexIDs[int, float](float("infinity"))
