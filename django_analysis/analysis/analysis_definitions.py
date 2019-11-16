import nipype

from django_analysis.analysis.specifications.fsl.bet import (
    BET_INPUT_SPECIFICATION,
    BET_OUTPUT_SPECIFICATION,
)
from django_analysis.analysis.specifications.fsl.flirt import (
    FLIRT_INPUT_SPECIFICATION,
    FLIRT_OUTPUT_SPECIFICATION,
)
from nipype.interfaces.fsl import BET, FLIRT

analysis_definitions = [
    {
        "title": "BET",
        "description": "FSL brain extraction (BET).",
        "versions": [
            {
                "title": BET().version,
                "description": f"Default BET version for nipype {nipype.__version__}.",
                "input": BET_INPUT_SPECIFICATION,
                "output": BET_OUTPUT_SPECIFICATION,
                "nested_results_attribute": "outputs.get_traitsfree",
            }
        ],
    },
    {
        "title": "FLIRT",
        "description": "FLIRT (FMRIB's Linear Image Registration Tool) is a fully automated robust and accurate tool for linear (affine) intra- and inter-modal brain image registration.",
        "versions": [
            {
                "title": FLIRT().version,
                "description": f"Default FLIRT version for nipype {nipype.__version__}.",
                "input": FLIRT_INPUT_SPECIFICATION,
                "output": FLIRT_OUTPUT_SPECIFICATION,
                "nested_results_attribute": "outputs.get_traitsfree",
            }
        ],
    },
]