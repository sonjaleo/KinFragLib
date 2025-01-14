# WIP: Custom filtered fragment library

The (full) fragment library resulting from the KinFragLib fragmentation procedure comprises 7486 fragments, which are the basis for exploring the subpocket-based chemical space of ligands co-crystallized with kinases (see `data/fragment_library/`).

To reduce the fragment library size and enable the recombination avoiding combinatorial explosion and to increase the chance of synthesizability of the newly created molecules, the fragment library can now be filtered by customizable filtering steps, namely:

1. Pre-filtering (Remove pool X, deduplicate, remove unfragmented fragments, remove fragments only connecting to pool X and fragments in pool X) \[mandatory\]
2. Filter for unwanted substructures (PAINS and Brenk et al.) \[optional\]
3. Filter for drug likeness (Ro3 and QED) \[optional\]
4. Filter for synthesizability (Buyable building blocks and SYBA) \[optional\]
5. Filter for pairwise retrosynthesizability (using ASKCOS) \[optional\]

- `custom_filter_results.csv`: File containing the filtering results, including per fragment, from the pre-filtered library, the SMILES and subpocket as indices, the calculated scores and boolean columns, if a fragment passes a specific filter, generated by the filtering steps.

Please refer to the notebook `notebooks/custom_kinfraglib/2_1_custom_filters_pipeline.ipynb` to check how the data was generated and/or to generate your own custom fragment library (de-)activating filters and modifying the filtering parameters.