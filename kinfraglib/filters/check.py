"""
Contains function to check which fragments are accepted or rejectes
"""

import pandas as pd
from . import prefilters

def accepted_rejected (fragment_library, value_list, cutoff_value = 0, cutoff_criteria = "<"):
    """
    Go through values list and return a pandas.DataFrame of accepted/rejected fragments 
    and a boolean list if fragment with this cutoff is rejected or accepted.
    
    Parameters
    ----------
    fragment_libray : dict
        fragments organized in subpockets inculding all information
    value_list : list
        list of values calculated for filtering
    cutoff_value : int or float
        value defining the cutoff for accepting or rejecting a fragment
    cutoff_criteria : string of a basic operator
        defining if the rejected fragments values need to be >, <, >=, <=, == or != compared to the cutoff_value
    
    Returns
    -------
    pandas.DataFrames
        accepted/rejected ligands
        
    list of bools
        bool defining if this fragment is accepted or rejected
    """
    accepted = []
    rejected = []
    bools = []
    subpockets = list(fragment_library.keys())
    #go through series indexes
    for i in range (0, len(value_list)):
        pocket = subpockets[i]
        #go through values in array
        for j in range(0, len(value_list[i])):
            val = value_list[i][j]
            #compare value with cutoff
            if cutoff_criteria == "<":
                #when value < cutoff -> add fragment to rejected df
                if val < cutoff_value:
                    rejected.append(fragment_library[pocket].loc[j])
                    bools.append(0)
                else:
                    #when value >= cutoff -> add fragment to accepted df
                    accepted.append(fragment_library[pocket].loc[j])
                    bools.append(1)
            elif cutoff_criteria == ">":
                #when value > cutoff -> add fragment to rejected df
                if val > cutoff_value:
                    rejected.append(fragment_library[pocket].loc[j])
                    bools.append(0)
                else:
                    #when value <= cutoff -> add fragment to accepted df
                    accepted.append(fragment_library[pocket].loc[j])
                    bools.append(1)
            elif cutoff_criteria == "<=":
                #when value <= cutoff -> add fragment to rejected df
                if val <= cutoff_value:
                    rejected.append(fragment_library[pocket].loc[j])
                    bools.append(0)
                else:
                    #when value > cutoff -> add fragment to accepted df
                    accepted.append(fragment_library[pocket].loc[j])
                    bools.append(1)
            elif cutoff_criteria == ">=":
                #when value >= cutoff -> add fragment to rejected df
                if val >= cutoff_value:
                    rejected.append(fragment_library[pocket].loc[j])
                    bools.append(0)
                else:
                #when value < cutoff -> add fragment to accepted df
                    accepted.append(fragment_library[pocket].loc[j])
                    bools.append(1)
            elif cutoff_criteria == "==":
                #when value == cutoff -> add fragment to rejected df
                if val == cutoff_value:
                    rejected.append(fragment_library[pocket].loc[j])
                    bools.append(0)
                else:
                #when value != cutoff -> add fragment to accepted df
                    accepted.append(fragment_library[pocket].loc[j])
                    bools.append(1)
            elif cutoff_criteria == "!=":
                #when value != cutoff -> add fragment to rejected df
                if val != cutoff_value:
                    rejected.append(fragment_library[pocket].loc[j])
                    bools.append(0)
                else:
                #when value == cutoff -> add fragment to accepted df
                    accepted.append(fragment_library[pocket].loc[j])
                    bools.append(1)                 
    return prefilters._make_df_dict(pd.DataFrame(accepted)), prefilters._make_df_dict(pd.DataFrame(rejected)), bools