import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multitest import multipletests

"""
# Post-Hoc Analysis

This scripts performs post-hoc analyses on the data obtained from figure_4.ipynb. 
It includes pairwise t-tests between CTRL-early PD, CTRL-mid PD, and CTRL-adv PD groups.
The p-values are then corrected for multiple comparisons using the Benjamini-Hochberg procedure, also known as the False Discovery Rate (FDR) correction.

The script was run for the following metrics and labels, which had significant differences between groups in the OLS regression analysis:
- Fractional anisotropy (FA) in the white matter (WM)
- Radial diffusivity (RD) in the white matter (WM)
- T2*-weighted (T2*w) in the white matter to gray matter ratio (WM/GM)

Author : Samuelle St-Onge
"""

# Perform pairwise t-tests

def post_hoc_analysis(metric, label, vert_level):
    """
    Perform post-hoc analysis using pairwise t-tests and FDR correction.
    
    Parameters:
    -----------
    metric : str
        The name of the metric (such as 'FA', 'RD', etc.) used to load the corresponding CSV file 
        containing the data for analysis (i.e., the CSV files stored in 'content/data/').
        
    label : str
        The label of interest (e.g., 'white matter', 'gray matter', etc.).
        
    Returns:
    --------
    None
    """
    
    # Load data for the specified metric
    data = pd.read_csv(f'data/parkinsons-spinalcord-mri-metrics/data/{metric}.csv')

    # Filter data based on vertebral level
    data = data[data['VertLevel'] == vert_level]

    # Add WM/GM ratio if applicable
    if label == 'WM/GM':
        # Compute and add the WM/GM ratio to the dataframe
        data_WM = data[data['Label'] == 'white matter']
        data_GM = data[data['Label'] == 'gray matter']
        data_WMGM = data_WM.copy() # Make a copy of data_WM to have the information from the other columns
        data_WMGM['Label'] = 'WM/GM' # Change the label name to 'WM/GM'
        data_WMGM['WA'] = data_WM['WA'].values / data_GM['WA'].values
        data = pd.concat([data, data_WMGM], ignore_index=True) # Add the WM/GM ratio to the dataframe
    
    # Filter data based on label and UPDRS group
    data = data[data['Label'] == label]
    
    CTRL_data = data[data['UPDRS_class_bis'] == 'CTRL']['WA']
    earlyPD_data = data[data['UPDRS_class_bis'] == 'early']['WA']
    midPD_data = data[data['UPDRS_class_bis'] == 'mid']['WA']
    advPD_data = data[data['UPDRS_class_bis'] == 'adv']['WA']

    # Perform pairwise t-tests between CTRL and PD groups
    pval_ctrl_early = stats.ttest_ind(CTRL_data, earlyPD_data, equal_var=False)[1]
    pval_ctrl_mid = stats.ttest_ind(CTRL_data, midPD_data, equal_var=False)[1]
    pval_ctrl_adv = stats.ttest_ind(CTRL_data, advPD_data, equal_var=False)[1]

    # Collect the raw p-values in a list
    raw_pvals = [pval_ctrl_early, pval_ctrl_mid, pval_ctrl_adv]

    # Apply FDR correction using the Benjamini-Hochberg method
    _, pvals_adj, _, _ = multipletests(raw_pvals, method='fdr_bh')

    # Print the original and adjusted p-values for each comparison
    print(f"\n------------ Post-hoc t-tests results with original p-values and FDR-corrected p-values for {metric} in {label} : ------------ \n")
    print(f"CTRL vs early PD: Raw p-value = {pval_ctrl_early:.4f}, Adjusted p-value (FDR) = {pvals_adj[0]:.4f}")
    print(f"CTRL vs mid PD: Raw p-value = {pval_ctrl_mid:.4f}, Adjusted p-value (FDR) = {pvals_adj[1]:.4f}")
    print(f"CTRL vs adv PD: Raw p-value = {pval_ctrl_adv:.4f}, Adjusted p-value (FDR) = {pvals_adj[2]:.4f}")

# Run the function for each combination of metric and label which had significant differences in the OLS regression analysis (see figure_4.ipynb)
post_hoc_analysis('FA', 'white matter', '2:05')
post_hoc_analysis('RD', 'white matter', '2:05')
