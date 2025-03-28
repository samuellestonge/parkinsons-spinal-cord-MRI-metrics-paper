import pandas as pd
from statsmodels.stats.multitest import multipletests
import statsmodels.formula.api as smf

# Initialize an empty dataframe to store results
results_table = pd.DataFrame()

# Define lists of metrics, labels, and vertebral levels of interest for OLS analysis
metrics = ['FA', 'MD', 'AD', 'RD', 'ODI', 'FISO', 'FICVF', 'MTR', 'T2star']
labels = ['spinal cord', 'white matter', 'gray matter', 'dorsal columns', 'ventral funiculi', 'lateral funiculi']  
vert_levels = ['2', '3', '4', '5']

# Method for OLS regression analysis and p-value correction using FDR
def ols_regression_analysis(metric):

    """
    This function performs Ordinary Least Squares (OLS) regression analysis for a given metric, with a focus on 
    each vertebral level and label of interest. The function applies the 'ols' method from the 
    statsmodels library to model the relationship between the outcome variable ('WA') and two 
    predictors: 'UPDRSIII_total' and 'Age'.

    After fitting the regression models, the p-values for the two predictors ('UPDRSIII' and 'Age') are 
    extracted. To account for multiple comparisons, the Benjamini-Hochberg procedure is applied 
    to control the False Discovery Rate (FDR) and adjust the p-values accordingly.

    Parameters:
    -----------
    metric : str
        The name of the metric (such as 'FA', 'MD', etc.) used to load the corresponding CSV file 
        containing the data for analysis (i.e., the CSV files stored in 'content/data/').

    Returns:
    --------
    pd.DataFrame
        A DataFrame containing the original p-values for 'UPDRSIII' and 'Age', as well as the adjusted 
        p-values after FDR correction. The data is organized for each combination of metric, label, 
        and vertebral level.
    """

    # Get data for the specified metric 
    data = pd.read_csv(f'content/data/{metric}.csv')

    # Create an empty list to collect the results
    p_values_list = []

    # Loop through vertebral levels and labels to extract p-values from your model
    for vert_level in vert_levels:
        for label in labels:

            data_for_analysis = data[(data['Label'] == label) & (data['VertLevel'] == vert_level)]
        
            ols_model = smf.ols(formula='WA ~ UPDRSIII_total + Age', data=data_for_analysis)
            ols_results = ols_model.fit()
            
            # Extract p-values for UPDRSIII and Age from the model
            pvalue_UPDRSIII = ols_results.pvalues.loc['UPDRSIII_total']
            pvalue_Age = ols_results.pvalues.loc['Age']
            
            # Create DataFrames for the p-values and add to the list
            p_values_list.append({
                'metric': metric,
                'VertLevel': vert_level,
                'Label': label,
                'p-values': pvalue_UPDRSIII,
                'p-value_type': 'UPDRSIII'
            })
            
            p_values_list.append({
                'metric': metric,
                'VertLevel': vert_level,
                'Label': label,
                'p-values': pvalue_Age,
                'p-value_type': 'Age'
            })

            # Convert the list to a DataFrame
            p_values_df = pd.DataFrame(p_values_list)

            # Separate the p-values for UPDRSIII and Age, ensuring we don't work on views
            p_values_UPDRSIII = p_values_df[p_values_df['p-value_type'] == 'UPDRSIII'].copy()
            p_values_age = p_values_df[p_values_df['p-value_type'] == 'Age'].copy()

            # Apply FDR correction to UPDRSIII p-values
            p_values_UPDRSIII['p-values_FDR_corrected'] = multipletests(p_values_UPDRSIII['p-values'], method='fdr_bh')[1]

            # Apply FDR correction to Age p-values
            p_values_age['p-values_FDR_corrected'] = multipletests(p_values_age['p-values'], method='fdr_bh')[1]

            # Combine the corrected p-values back into the original DataFrame
            p_values_df = pd.concat([p_values_UPDRSIII, p_values_age])

            # Convert the 'Label' column to a categorical type to specify the desired order
            p_values_df['Label'] = pd.Categorical(p_values_df['Label'], categories=labels, ordered=True)

            # Sort the DataFrame based on the custom order of the 'Label' column
            p_values_df_sorted = p_values_df.sort_values(by=['Label', 'VertLevel'], ascending=[True, True])

    return p_values_df_sorted

# Apply the method to each metric and combine the results in a common dataframe
for metric in metrics:
    p_values = ols_regression_analysis(metric)
    results_table = pd.concat([results_table, p_values], ignore_index=True)

# Save the results to a CSV
results_table.to_csv(f'content/results/OLS_results.csv')