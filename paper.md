---
numbering:
  heading_2: false
  figure:
    template: Fig. %s
---

<p>
<center>
<b>
<h3>
Parkinson’s disease in the spinal cord: an exploratory study to establish T2*w, MTR and diffusion-weighted imaging metric values
</h3>

<p style="text-align:center;">
Samuelle St-Onge<sup>1,2</sup>, Camille Coustaury<sup>1</sup>, Caroline Landelle<sup>3</sup>, Linda Solstrand Dahlberg<sup>3</sup>, Ovidiu Lungu<sup>3</sup>, Julien Doyon<sup>3</sup>, Benjamin De Leener<sup>1,2,4</sup>
</p>
</b>

<ul style="list-style-type: none">
<li><sup>1</sup>NeuroPoly Lab, Institute of Biomedical Engineering, Polytechnique Montreal, Montreal, QC, Canada</li>
<li><sup>2</sup>CHU Sainte-Justine Research Centre, Montreal, QC, Canada</li>
<li><sup>3</sup>McConnell Brain Imaging Centre, Department of Neurology and Neurosurgery, Montreal Neurological Institute, McGill University, Montreal, QC, Canada</li>
<li><sup>4</sup>Computer Engineering and Software Engineering, Polytechnique Montréal, Montreal, QC, Canada</li>
</ul>
</center>
</p>

## Abstract

Parkinson's disease (PD) is primarily defined by brain pathology, including dopamine neuron degeneration and 𝛼-synuclein aggregation. Emerging evidence suggests that the spinal cord is also affected, with ex-vivo studies reporting abnormal 𝛼-synuclein protein aggregation within spinal cord axons of PD patients. While advanced imaging techniques such as DTI, NODDI, T2*w, and MTR have demonstrated potential for detecting PD-related changes in the brain, their application to spinal cord alterations remains unexplored. This study is the first to investigate MRI-derived metrics in the spinal cord of PD patients, comparing them to healthy controls, to assess potential microstructural changes. Despite significant findings in functional MRI studies using the same cohort, this study found little to no significant microstructural or structural differences in the spinal cord between PD patients and healthy controls, aligning with recent findings in PD mouse models. These results highlight the need for further research to better understand how PD-related alterations in the spinal cord compare to normal aging processes and relate to functional changes.

## 1. Introduction

Parkinson's disease (PD) is a neurodegenerative disease that is defined by both the degeneration of dopamine-producing neurons inside the substantia nigra (Nyatega et al., 2022) and the abnormal accumulation of 𝛼-synuclein inside neurons, forming abnormal protein aggregates commonly referred to as Lewy bodies (Bianco et al., 2002; Muller et al., 2005). While PD has traditionally been linked to brain pathology, indications of the disease have been identified in the spinal cord, notably the presence of abnormal aggregation of 𝛼-synuclein proteins inside spinal cord axons (Nardone et al., 2020). 

Post-mortem studies have reported a higher number of 𝛼-synuclein aggregates in the spinal cord of PD patients compared to their healthy counterparts (Braak et al., 2007; Del Tredici & Braak, 2012). While cases of 𝛼-synuclein aggregates found exclusively in the spinal cord were rare, the presence of 𝛼-synucleinopathy was found common in the spinal cord when it was also present in the brain, which suggests that PD may affect the midbrain before descending in the spinal cord (Del Tredici et al., 2012). There is also extensive evidence indicating that PD may start in the enteric nervous system (ENS) before progressing to the midbrain (Del Tredici & Braak, 2012, 2016). Additionally, it has been hypothesized that there may be two types of PD: one that starts in the ENS and propagates to the brain, and another that begins in the brain before spreading to the ENS (Horsager et al., 2020; Leclair-Visonneau et al., 2020). Nonetheless, the origin of PD within the body remains under debate, along with the mechanisms through which the disease spreads to the spinal cord.

The work of Bloch et al., (2006) has shown a higher concentration of 𝛼-synuclein in the lower brainstem than in the spinal cord, which is consistent with the findings of Del Tredici et al. (2012). Furthermore, Del Tredici & Braak (2012) identified globules filled with 𝛼-synuclein in individuals with advanced PD, as opposed to small varicosities in earlier stages. These findings align with those of Sekigawa et al. (2015), who observed axonal swelling associated to 𝛼-synuclein in the spinal cord of transgenic mice. These results collectively suggest that the spinal cord is indeed affected by PD, hence the relevance of studying its microstructure in PD patients. Nevertheless, in-vivo spinal cord studies for PD are currently limited, and various aspects related to how PD affects the spinal cord microstructure are yet to be understood. 

The impact of PD in the human spinal cord has been explored by Landelle et al. (2023) using functional magnetic resonance imaging (fMRI), where a decrease of functional connectivity has been observed with disease progression in the cervical spinal cord. Recently, Combes et al. (2024) have studied structural MRI in the spinal cord of transgenic PD mice. Their results revealed no structural changes in the spinal cord of the PD mouse compared with their non-transgenic counterparts. However, no studies have investigated MRI-derived metrics to assess the microstructural impact of PD on the human spinal cord. 

Diffusion-weighted imaging (DWI) is a promising modality to quantify spinal cord microstructure, providing information regarding the diffusion of the water molecules that can indicate tissue abnormalities and damage. The diffusion tensor imaging (DTI) model is amongst the most widely used diffusion MRI models, allowing to measure fractional anisotropy (FA), mean diffusivity (MD), radial diffusivity (RD) and axial diffusivity (AD) (O’Donnell & Westin, 2011). Although a few studies have investigated DTI to quantify gray matter integrity such as in healthy aging (Pfefferbaum et al., 2010), DTI is predominantly used to study the white matter, given its strong anisotropy (Assaf & Pasternak, 2008). Recent work has demonstrated the usefulness of DTI to unveil microstructural tissue damage in PD patients for several regions of the brain, such as the substantia nigra and corpus callosum (Atkinson-Clement et al., 2017; Kotian et al., 2020). Notably, a decrease in FA has been recorded with PD progression in the brain (Kotian et al., 2020). Although DTI metrics demonstrated potential for identifying PD-related microstructural changes in the brain, to our knowledge, these metrics have not yet been studied in the spinal cord of PD patients. Another DWI model that shows promise is the Neurite Orientation Dispersion and Density Index (NODDI) (Zhang et al., 2012), which allows the tissue voxel to be compartmentalized into intracellular, extracellular and cerebrospinal fluid compartments. NODDI metrics include the orientation dispersion index (ODI), the isotropic volume fraction (FISO) and neurite density (FICVF). Brain-focused studies reported reduced values for FICVF and ODI in the substantia nigra pars compacta among individuals with PD (Kamagata, Hatano, & Aoki, 2016; Kamagata, Hatano, Okuzumi, et al., 2016). This phenomenon is suspected to be linked to the loss of dopaminergic neurons associated with PD in the brain (Kamagata, Hatano, & Aoki, 2016). However, to our knowledge, no in vivo studies have demonstrated neuronal loss related to PD in the spinal cord. 

Others have explored T2\*-weighted (T2\*w), or its reciprocal R2* (1/T2\*), as a promising method for identifying PD-related changes in the brain. In their study, Schwarz et al. (2018) noticed a decrease in T2\*w signal inside the substantia nigra and nigrosomes in subjects with PD compared to healthy individuals. Since T2\*w is sensitive to changes in susceptibility, this decrease is thought to be attributed to iron accumulation, which is well documented to be associated with PD in the brain (Schwarz et al., 2018; Tambasco et al., 2019; Zeng et al., 2024). Studies suggest that iron deposition is responsible for triggering the activation of immune cells in the brain, which in turn release substances that cause inflammation and cause oxidative stress. This process may aggravate the loss of dopaminergic neurons and contribute to disease progression in PD patients (Zeng et al., 2024). Iron accumulation related to PD in the spinal cord has not been reported to date. However, given that the involvement of the spinal cord in PD is still not fully understood, exploring T2\*w in the spinal cord of PD patients may reveal subtle changes in tissue susceptibility that were not identified in previous post-mortem studies.  Similarly, the magnetization transfer ratio (MTR) has demonstrated relevance in the context of PD in the brain, where studies have noted a decrease in MTR in several brain regions such as the substantia nigra in early PD stages, which is thought to also be linked to iron deposition in the brain (Anik et al., 2007; Tambasco et al., 2003, 2011). However, despite the interest in studying T2\*w and MTR metrics in the PD brain, their investigation for PD in the spinal cord remains unexplored.

The present study aims to explore the potential of quantitative MRI to detect microstructural changes in the spinal cord due to Parkinson’s disease. We aim at establishing relationships between PD and T2\*w, MTR, DTI and NODDI values in the cervical spinal cord. Disease progression will be assessed using the motor component of the Unified Parkinson’s Disease Rating Scale (UPDRS) (Movement Disorder Society Task Force on Rating Scales for Parkinson’s Disease, 2003) to correlate these metrics with motor symptom severity. The study also seeks to evaluate whether DTI, NODDI, T2\*w and MTR metrics can be used to differentiate PD patients from their healthy counterparts, which could lead to identifying potential biomarkers for PD in the spinal cord. 

## 2. Methods

### 2.1 Data acquisition


The study involved the same participants as Landelle et al. (2023), which have been scanned at the Montreal Neurological Institute-Hospital through the Clinical, Biospecimen, Imaging, and Genetic (C-BIG) repository, with a 3 Tesla MRI scanner (Magnetom Prisma, Siemens, Erlangen, Germany). All participants gave their written consent in accordance with the Helsinki Declaration, and the experiment was approved by the local ethics committee (MUCH REB 2019-4626). The acquisition protocol included T1w, T2\*w, magnetization transfer (MT) and a multi-shell diffusion MRI sequence. The detailed acquisition parameters for T2\*w, MTR and DWI are presented in Figure 1. Figure 2 shows examples of raw data acquisitions for a single subject. Because of the limited field-of-view of the acquisitions, only the cervical spinal cord from spinal levels C2 to C5 was considered for this study. 

Participants included both subjects with PD and healthy controls (HC). Individuals with PD underwent clinical interviews and neurological examinations, including an assessment of disease severity with the UPDRS. Using Part III of the UPDRS, which corresponds to the assessment of motor symptoms, participants were further categorized into three groups: Low PD (UPDRSIII 0-20), Med PD (UPDRSIII 20-30), Adv PD (UPDRSIII 30-60). Figure 1B shows the number of subjects per category, for each sequence. The age, sex and UPDRSIII score distribution of the subjects are shown in Figure 1.  

:::{figure} #fig1cell
:label: fig1

(A) Acquisition parameters for T2*w, MTR and DWI; (B) Number of participants per category (controls, low_PD, med_PD and adv_PD) for each sequence according to their UPDRSIII score (C) Age and UPDRSIII distributions.
:::

:::{figure} #fig2cell
:label: fig2

Representative raw data of T2*w, MT0/MT1, and DWI from a single subject.
:::

### 2.2 Data pre-processing and metric extraction

FA, MD, RD and AD metrics were computed from the DWI images using DTI from DIPY via the Spinal Cord Toolbox (SCT) (De Leener et al., 2017). ODI, FISO and FICVF metrics were computed using the NODDI Matlab Toolbox (UCL Microstructure Imaging Group, 2021). The individual MTR, T2\*w and DWI images underwent initial preprocessing using SCT, which first included spinal cord segmentation using the sct_propseg algorithm and manual corrections when necessary. Because of the thick slices of T2\*w (2 mm), MTR and DWI (5 mm) acquisitions, it was difficult to label the vertebrae on these images directly. For this reason, vertebral labeling was performed on T1w acquisitions (slice thickness = 1.3 mm) and were coregistered to the PAM50 template (De Leener et al., 2018). Then, the generated warping fields were used to initialize the coregistration of T2\*w, MTR, DTI and NODDI images to the PAM50 template. Thus we generated average group-level metric maps (i.e., average pixel wise intensity) for both HC and PD subjects, at spinal levels C2 to C5 in the PAM50 space. 

Using the atlas from the co-registered PAM50 template, we extracted DTI metrics from the white matter and its subregions (dorsal columns, ventral funiculi, and lateral funiculi) to quantify axonal damage which may be linked to the presence of α-synuclein aggregates in white matter axons, leading to reduced diffusion anisotropy. Similarly, NODDI metrics were extracted from the white matter and its subregions for their sensitivity to axonal integrity and changes in diffusion orientation. Additionally, NODDI metrics were analyzed in the gray matter to detect potential alterations in dendrite orientation and integrity. MTR values were extracted from the white matter and its subregions due to their sensitivity to demyelination, often linked to axonal loss. Finally, the WM/GM ratio was calculated from T2\*w images using white and gray matter values extracted using the PAM50 atlas. This approach provides a quantitative measure as opposed to using only gray matter values, as the T2\*w signal can vary between acquisitions. The ratio was chosen because gray matter naturally contains higher iron levels than white matter, and T2\*w is particularly sensitive to iron content. 

Importantly, all metrics were extracted using the spinal levels (Frostell et al. (2016), SCT v6.1) instead of the vertebral levels to offer a representation that reflects more accurately the functional organization of the spinal cord into different rootlets, thereby enabling more robust comparisons with the findings of Landelle et al. (2023) in functional MRI. The cross-sectional area of the spinal cord was also computed on all individual T2\*w images via sct_process_segmentation from SCT. 

### 2.3 Effect of groups and UPDRSIII score on MRI metrics

We investigated the relationships between PD and MRI-derived metrics in the cervical spinal cord by examining how these metrics varied across different groups (controls, low PD, medium PD, and advanced PD). To assess the impact of group on DTI, NODDI, T2\*w, and MTR metrics, we performed an analysis of variance (ANOVA), combining spinal levels C2 to C5. Age was included as a covariate to control for its potential confounding effects. Post-hoc t-tests were performed on metrics that showed significant results (p < 0.05) to further explore group differences. 

To investigate how disease severity may affect our metrics, we also used an ordinary least-squares (OLS) regression model, to investigate the relationships between DTI, NODDI, T2\*w, MTR metrics and the UPDRSIII scores, while controlling for age as a potential confounder. For each metric, the OLS analysis was performed for spinal levels C2 to C5 separately. DTI, NODDI and MTR metrics were studied in the white matter and its subregions (dorsal columns, ventral funiculi, lateral funiculi), to identify potential changes which may be attributed to the accumulation of α-synuclein inside white matter axons. Due to its ability to identify changes in gray matter dendrites, the NODDI was also studied in the gray matter, to investigate whether differences in these metrics could be identified with an increasing UPDRSIII score. Finally, the white matter to gray matter ratio (WM/GM) was studied on the T2\*w images. To control for the risk of type I errors due to multiple comparisons, the Bonferroni correction was applied by dividing the significance threshold (α = 0.05) by the number of comparisons, which corresponded to the number of spinal cord regions assessed for each metric. Cross-sectional area (CSA) was also studied using the above-mentioned ANOVA and OLS models to detect potential structural changes in the cervical spinal cord associated with PD. 

## 3. Results
### 3.1 Average metric maps

Figure 3 shows the average metric maps for DTI, NODDI and MTR, obtained by registering the metrics to the PAM50 template and computing the pixel-by-pixel average intensity for each subject category (HC, Low PD, Med PD and Adv PD).  

:::{figure} #fig3cell
:label: fig3

Average spinal cord maps for DTI, NODDI and MTR metrics for C2, C3, C4, and C5 spinal levels for healthy controls (HC), low PD, med PD, adv PD and all PD participants combined.
:::

According to the average metric maps in Figure 3, we notice an increase in ODI and a decrease in FA within the white matter among PD participants compared to their healthy counterparts. Additionally, a decrease in global intensity is observed as we progress through the more caudal spinal levels, which is particularly apparent in MTR and FA maps. 

## 3.2 Comparisons across groups (healthy controls, low PD, medium PD and advanced PD)

Figure 4 presents the results of ANOVA comparing DTI, NODDI, MTR, and T2\*w metrics across the different groups (HC, low PD, med PD, and adv PD). In the white matter, our results showed a significant effect of the group on FA and RD metrics, for the combined spinal levels C2 to C5 (FA : p-Group = 0.0412; RD : p-Group = 0.0138). Our analysis also revealed  a significant effect of the group on the WM/GM in T2\*w (p-Group = 0.0358). Pairwise t-tests with false discovery rate (FDR) correction were applied to compare low PD, med PD and adv PD subjects with the HC group (Table 1), where results showed a significant difference between HC and adv PD groups for the WM/GM in T2\*w, and between HC and med PD for RD in the WM. 

:::{figure} #fig4cell
:label: fig4

ANOVA for NODDI, DTI, T2*w and MTR for HC in comparison with PD subjects categorized by their UPDRSIII score (Low PD, Med PD and Adv PD), for spinal levels C2 to C5 combined.
:::


:::{figure} content/Table1.png

Table 1. FDR-corrected p-values following post-hoc pairwise t-tests between HC – low PD, HC – medium PD and HC – advanced PD. The significant p-values (<0.05) are shown in red with an asterisk (*).
:::

## 3.3 Correlation of metrics with UPDRSIII score

To examine the impact of disease severity on our metrics, we employed an ordinary least-squares (OLS) regression model to explore the associations between DTI, NODDI, T2\*w, and MTR metrics and UPDRS-III scores, with age included as a covariate to account for its potential confounding effects. Prior to conducting the OLS regression analysis, we assessed the potential collinearity between age and UPDRSIII scores. The Variance Inflation Factor (VIF) found was 1.1, which is well below the commonly-used threshold of 10, indicating that collinearity is unlikely to affect our model. Furthermore, the Pearson coefficient between these two variables was 0.31 (p-value = 0.0099), suggesting that age and UPDRSIII are likely to be related, although the effect of one on the other is weak (r=0.31). 

Table 2 presents the p-values from the OLS model for the UPDRS-III and age variables, examining DTI, NODDI, and MTR metrics in relation to UPDRS-III score progression across each studied region. P-values in bold text marked with an asterisk (\*) indicate statistical significance after applying the Bonferroni correction for multiple comparisons, adjusting the significance threshold to 𝛼 = 0.05/N, where N represents the number of regions assessed in the spinal cord for each metric. Figures illustrating the results for each test can be found in the supplementary material. 

According to table 1, some trends were observed in specific regions, for individual spinal levels for some of our metrics. Some p-values for the UPDRSIII score were below 𝛼 = 0.05, but none remained significant after correcting for N comparisons (𝛼 = 0.05/N). For instance, an increase in ODI, FICVF, and FISO was observed in relation to UPDRSIII across all studied spinal cord subregions, along with a decrease in FA, which was prominent at the C4 and C5 levels. The OLS regression model revealed an effect of the UPDRSIII on FA for the entire white matter at spinal levels C3 (p-UPDRSIII = 0.021) and C5 (p-UPDRSIII = 0.029), as well as in some sub-regions of the white matter (Figure 15). Effects of the UPDRSIII score were also observed on other metrics and regions such as RD at spinal level C2 (p-UPDRSIII = 0.043), FISO in the ventral funiculi at spinal level C2 (p-UPDRSIII = 0.013) and FICVF in the dorsal columns at spinal level C5 (p-UPDRSIII = 0.027). In the gray matter, the UPDRSIII revealed an effect on the FICVF at C5. Our findings also suggest an increase in the WM/GM ratio in T2*, particularly at the C4 spinal level. However, when correcting for multiple comparisons, no results were found significant for the UPDRSIII on any of the studied metrics and regions. 

Notably, the OLS model revealed a significant effect of age on MTR for the entire white matter (p-Age = 0.0017) and in the dorsal columns (p-Age = 0.0011) at spinal level C5, even when accounting for N comparisons. The UPDRSIII also demonstrated a significant correlation with the WM/GM ratio in T2\*w at C2, C4 and C5 (p-Age = 0.0005 at C2; p-Age = 0.004 at C4; p-Age = 0.0054 at C5) after correcting the significance threshold for multiple comparisons. 

:::{figure} content/Table2.png

Table 2. FDR-corrected p-values for UPDRSIII and age predictors for the OLS regression model (metric = UPDRSIII + Age) 
:::

In order to compare the findings above with HC, the relationship between age and the metrics was also studied on our healthy subjects. The progression of metric values with age for PD subjects and HC is compared in the supplementary material. In these figures, we notice how the progression of values with age is similar between HC and PD subjects, across all metrics and regions. This lack of distinction makes it challenging to differentiate between the two groups based solely on age-related changes. However, the observed trends, such as an increase in ODI and a decrease in FA, align with findings from previous studies investigating age-related changes in these metrics in healthy individuals (Agosta et al., 2007; Mamata et al., 2005; Vedantam et al., 2013; Wang et al., 2014). 

## 3.4 Cross-sectional area (CSA) of PD subjects versus healthy controls

Figure 5 presents the results of ANOVA comparing spinal cord cross-sectional area (CSA) across HC, low PD, med PD, and adv PD. The results revealed no significant differences in spinal cord cross-sectional area (CSA) between groups. Additionally, an OLS analysis revealed no significant effect of the UPDRSIII score on the CSA (Table 3), but rather a significant effect of age at C3 and C4 spinal levels (p-Age = 0.002). These results suggest that the cervical spinal cord CSA is not affected by PD. 

:::{figure} #fig5cell
:label: fig5

:::{figure} content/Table3.png

Table 3. P-values for UPDRSIII and Age variables for the cross-sectional area (CSA) following ordinary least squares (OLS) analysis. The significance level was corrected for each metric, by dividing 𝛼=0.05 by the number of spinal levels studied. 
:::

# 4. Discussion 

Following our ANOVA analysis, significant differences between HC and some PD groups have been identified. Post-hoc t-tests revealed a significant difference between HC and the advanced PD group for the WM/GM in T2\*w, as well as between HC and medium PD in the white matter for RD. Our results also suggest an increase in ODI, FISO and FICVF as well as a decrease in FA with an increasing UPDRSIII score, which may be attributed to the accumulation of α-synuclein, which can cause axonal swelling, leading to greater neurite orientation dispersion and reduced diffusion anisotropy. However, since the trends observed in relation to the UPDRSIII score were not significant for any of the studied metrics after correcting for multiple comparisons, conclusive interpretations cannot be made based on the current study.

Although several post-mortem studies have reported a higher number of 𝛼-synuclein aggregates in the spinal cord of PD patients (Braak et al., 2007; Del Tredici & Braak, 2012), spinal cord 𝛼-synucleinopathy has also been linked to healthy spinal cord aging (Bloch et al., 2006; Buchman et al., 2017; Oinas et al., 2010; Sumikura et al., 2015). This makes the interpretation of our results difficult, since both aging and PD progression may have similar effects on the spinal cord microstructure. In our work, we have also observed an effect of age on the metrics, such as an increase in ODI and decrease in FA in the cervical spinal cord in both HC and PD subjects. These results are consistent with other work that have explored the effect of age on these DWI metrics in healthy subjects (Agosta et al., 2007). Agosta et al. (2007) have also reported no significant correlation between MD and age, which is also consistent with our findings. Other work with PD in the brain have also reported a negative correlation of FA with age in the substantia nigra (de Oliveira & Pereira, 2021). 

Our current study revealed similar effects of age on our metrics as those observed with the UPDRSIII. In some regions and metrics, such as in the WM/GM in T2\*w, our analysis revealed a stronger effect of age than the UPDRSIII on our metrics. This makes it difficult to differentiate between the effects of Parkinson’s disease progression and normal aging. Additionally, while age was included in the analysis, other potential confounding variables that could impact the progression of the disease, such as medication, should be considered in future work. 

Our results also show an increase in WM/GM in T2\*w with an increasing UPDRSIII in the cervical spinal cord, from C2 to C4, although not significant when correcting for multiple comparisons. Previous work have demonstrated relevance for the WM/GM in T2\*w as a potential biomarker for other neurodegenerative disorders in the spinal cord (Martin et al., 2017); however, to our knowledge, this study is the first to have explored its potential for PD in the spinal cord. Further research will be necessary to establish definitive conclusions regarding its applicability in PD. 

Finally, in the current study, it was difficult to relate our findings for structural MRI in the spinal cord microstructure with those observed with functional MRI in the work of Landelle et al. (2023) using the same subjects. In their work, Landelle et al. (2023) found a decrease in functional connectivity that correlated with upper limb motor symptoms in between PD patients between C4 and C6 spinal levels. However, our analysis did not reveal any significant findings that could be associated with the functional changes described in their work. 

Our analysis of spinal cord cross-sectional area (CSA) aligns with the findings of Combes et al. (2024), as we observed no structural changes due to PD. Indeed, our study revealed no significant differences in CSA between Parkinson’s disease (PD) subjects and healthy controls (HC). Additionally, no significant relationship between the UPDRSIII score and CSA was found. This absence of structural changes could explain the lack of significant correlations between PD and the examined MRI-derived metrics at the microstructural level. Furthermore, the evidence of no structural and microstructural changes within the gray matter may reinforce the findings of Landelle et al. (2023) observed through functional MRI, by suggesting that the effects of PD progression reported in their study were primarily driven by functional changes in the spinal cord rather than anatomical alterations. Nevertheless, subsequent work will be needed to confirm this. 

# 5. Conclusion

In summary, this work is the first to have studied DTI, NODDI, MTR and T2\*w metrics in the cervical spinal cord of a population with PD. Although some significant differences were identified between HC and PD subjects in isolated regions of the spinal cord—notably for FA, RD and the T2\*w WM/GM — no significant changes in microstructural metrics were found in relation to the UPDRSIII score. Our results also suggest that age may have a greater effect on DTI, NODDI, MTR and T2\*w metrics than PD in some regions of the cervical spinal cord. Our lack of significant findings in this current study limits our ability to relate our results to the functional changes observed in the same subjects in Landelle et al. (2023). 

Nonetheless, this exploratory study provides insights into how the cervical spinal cord microstructure is affected by PD, and how it compares to normal aging processes in the spinal cord. The results are also in line with those of Combes et al. (2024), who did not find any structural changes between PD mice and non-transgenic mice. 

# Supplementary material 

TODO : Add supplementary figures

# Acknowledgements

This work is supported by the TransMedTech Institute, thanks to the financial support of the Canada First Research Excellence Fund and the Fonds de recherche du Québec, the Fondation Courtois, the Natural Sciences and Engineering Research Council of Canada (NSERC), and Polytechnique Montreal. We thank the Clinical, Biospecimen, Imaging & Genetic (C-BIG) repository for help in participant recruitment and the brain imaging centre of The Neuro for help in data acquisition. We thank all participants involved in this study.


