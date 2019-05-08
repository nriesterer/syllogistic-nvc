Syllogistic NVC
===============

Companion repository for the 2019 article *Modeling Human Syllogistic Reasoning: The Role of "No Valid Conclusion"* published for the 41st Annual Meeting of the Cognitive Science Society (CogSci 2019).

## Overview

- `data/`: Data directory
    - `data/Ragni2016.csv`: Core dataset for the evaluation. Taken from the [CCOBRA repository](https://github.com/CognitiveComputationLab/ccobra/tree/master/benchmarks/syllogistic/data)
    - `data/valid_syllogisms.csv`: Information about which syllogisms have valid conclusions.
- `indiv_table`: Code for generating Figure 4
    - `indiv_table/indiv_table.py`: Generates the Figure 4
    - `indiv_table/individuals.py`: Generates the data for Figure 4
- `nvc_predictions`: Code for generating Figure 2
    - `nvc_predictions/nvc_heatmap.py`: Generates the Figure 2
- `prediction_errors`: Code for generating Figures 1 and 3
    - `prediction_errors/accuracies.py`: Generates the data for Figure 1 and 3
    - `prediction_errors/stackedbar.py`: Generates the Figures 1 and 3

## Dependencies

- Python 3
    - [CCOBRA](https://github.com/CognitiveComputationLab/ccobra)
    - [pandas](https://pandas.pydata.org)
    - [seaborn](https://seaborn.pydata.org)

## Quickstart

Navigate your terminal into the respective analysis directories and run the contained Python scripts:

```
$> cd /path/to/repository/analysis/indiv_table/
$> python3 individuals.py
$> python3 indiv_table.py
```

## Reference

Riesterer, N., Brand, D., Dames, H., & Ragni, M. (2019) Modeling Human Syllogistic Reasoning: The Role of "No Valid Conclusion". In *Proceedings of the 41st Annual Meeting of the Cognitive Science Society*.
