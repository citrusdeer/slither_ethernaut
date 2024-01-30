from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import Binary, BinaryType
from slither.core.variables.state_variable import StateVariable
from slither.analyses.data_dependency.data_dependency import is_tainted


class PrivateVariableNotSecret(AbstractDetector):  # pylint: disable=too-few-public-methods
    """
    Documentation
    """

    ARGUMENT = "PrivateVariableNotSecret"  # slither will launch the detector with slither.py --mydetector
    HELP = "Private Variable used as a secret, vulnerable to lookup"
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.LOW

    WIKI = "Ethernaut #8 -- Vault"

    WIKI_TITLE = "Something else"
    WIKI_DESCRIPTION = " does a thing"
    WIKI_EXPLOIT_SCENARIO = " #haxors"
    WIKI_RECOMMENDATION = "fix it"


    def _detect(self):
        results = []
        for contract in self.contracts:
            for func in contract.functions:
                for instr in func.nodes:
                    for ir in instr.irs:
                        if isinstance(ir, Binary) and BinaryType.return_bool(ir.type):

                            # probably a better way to do this. but it works for now
                            try:
                                if ir.variable_left.visibility == "private" and is_tainted(ir.variable_right, contract) \
                                or ir.variable_right.visibility == "private" and is_tainted(ir.variable_left, contract):
                                    info = [
                                            "Private Variable Compared Against user-controlled variable!",
                                            "Attackers can look up private values by slot number.",
                                            f"{func.full_name} {func.source_mapping}",
                                            f"{instr}",
                                            ""
                                            ]
                                    results.append(self.generate_result("\n".join(str(i) for i in info)))
                            except:
                                pass

        return results
