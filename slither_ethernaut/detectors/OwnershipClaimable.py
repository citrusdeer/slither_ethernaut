from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification


class OwnershipClaimable(AbstractDetector):  # pylint: disable=too-few-public-methods
    """
    Documentation
    """

    ARGUMENT = "ownershipClaimable"  # slither will launch the detector with slither.py --mydetector
    HELP = "Help printed by slither"
    IMPACT = DetectorClassification.MEDIUM
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "#writes-to-owner"

    WIKI_TITLE = "Something else"
    WIKI_DESCRIPTION = " does a thing"
    WIKI_EXPLOIT_SCENARIO = " #haxors"
    WIKI_RECOMMENDATION = "fix it"

    def _detect(self):
        #breakpoint()

        info = "This is an example!"
        ret = []
        #breakpoint()
        for contract in self.slither.contracts_derived:
            for f in contract.functions:
                # breakpoint()
                if f.name == "constructor":
                    continue # constructor is expected to write to owner, not a finding
                for var in f.variables_written:
                    if var.name == "owner":
                        json = self.generate_result(f"{f.solidity_signature} writes to {var.name}\n")
                        ret.append(json)

        return ret
