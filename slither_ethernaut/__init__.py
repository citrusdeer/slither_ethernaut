from slither_ethernaut.detectors.OwnershipClaimable import OwnershipClaimable
from slither_ethernaut.detectors.PrivateVariableNotSecret import PrivateVariableNotSecret


def make_plugin():
    plugin_detectors = [OwnershipClaimable, PrivateVariableNotSecret]
    plugin_printers = []

    return plugin_detectors, plugin_printers
