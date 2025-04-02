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

:::{figure} #fig2cell
:label: fig2

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

According to the average metric maps in Figure 3, we notice an increase in ODI and a decrease in FA within the white matter among PD participants compared to their healthy counterparts. Additionally, a decrease in global intensity is observed as we progress through the more caudal spinal levels, which is particularly apparent in MTR and FA maps. 

## 3.2 Comparisons across groups (healthy controls, low PD, medium PD and advanced PD)

Figure 4 presents the results of ANOVA comparing DTI, NODDI, MTR, and T2\*w metrics across the different groups (HC, low PD, med PD, and adv PD). In the white matter, our results showed a significant effect of the group on FA and RD metrics, for the combined spinal levels C2 to C5 (FA : p-Group = 0.0412; RD : p-Group = 0.0138). Our analysis also revealed  a significant effect of the group on the WM/GM in T2\*w (p-Group = 0.0358). Pairwise t-tests with false discovery rate (FDR) correction were applied to compare low PD, med PD and adv PD subjects with the HC group (Table 1), where results showed a significant difference between HC and adv PD groups for the WM/GM in T2\*w, and between HC and med PD for RD in the WM. 

:::{figure} #fig4cell
:label: fig4

A funny take on the difference between articles with code and articles from code.
:::

Let's see how directives work with a simple example by rendering a video from an external source:

:::{iframe} https://cdn.curvenote.com/0191bd75-1494-72f5-b48a-a0aaad296e4c/public/links-8237f1bb937ea247c2875ad14e560512.mp4
:label: figvid
:width: 100%

Video reused from [mystmd.org](https://mystmd.org) (CC-BY-4.0, [source](https://mystmd.org/guide)).
:::ell
:label: fig2

An example of a figure generated from a Jupyter Notebook that lives in the `content` folder of this repository.  Check `content/figure_2.md` to see how this figure was generated and where the label `#fig2cell` is defined.
:::

Both interactive, cool right! All your assets are centralized in this one document, which ideally lives in a GitHub repository. You may forget what you did, but your commit history will be there to remind you.

## NeuroLibre and MyST Markdown

NeuroLibre is a reproducible preprint publisher that makes it a seamless experience to publish preprints written in MyST Markdown, and commits to the long term preservation of the content, runtime, data, and the functionality of the code.

:::{seealso}
You can refer to [this blogpost](https://conp.ca/about-neurolibre/#:~:text=NeuroLibre%20is%20a%20platform%20for,articles%2C%20tutorials%2C%20and%20reports) for more information about NeuroLibre.
:::

### Data

Unless your preprint does not include any output that requires computational resources, you typically need to provide a set of inputs to supplement the generation of the assets in your article. The type and size of the data can vary greatly from one article to another, from a `50KB` excel spreadsheet to a `2GB` neuroimaging dataset of brain images.

The only requirement is that the data must be publicly available to be accessed by NeuroLibre. To specify your data dependencies, you can provide a `binder/data_requirement.json` file in the root of your repository, with the following structure:

```json
{
  { "src": "https://drive.google.com/uc?id=1hOohYO0ifFD-sKN_KPPXOgdQpNQaThiJ",
  "dst": "../data",
  "projectName": "neurolibre-demo-dataset"
  }
}
```

:::{note}
The above configuration specifies that the data will be downloaded from Google Drive and placed in and saved in a `data/neurolibre-demo-dataset` at the root of your repository. The `dst` field indicates `../data` as the root of the repository is one directory up from the `binder` directory where the `data_requirement.json` file is located.

Even when the `dst` field is specified differently, NeuroLibre will always mount the data in the `data` folder at the root of your repository. We recommend you to follow the same convention while working locally and to remember to `.gitignore` the `data` folder!
:::

:::{seealso}
You can refer to [this documentation](https://docs.neurolibre.org/en/latest/STRUCTURE.html#the-binder-folder-data) for more information about the `binder/data_requirement.json` file and the available options to specify your data dependencies.
:::

#### How can I get NeuroLibre to cache my data dependencies? 

You can use [this issue template](https://github.com/neurolibre/info/issues/new?assignees=agahkarakuzu&labels=DOWNLOAD&projects=&template=data_cache.md&title=) to request the caching of your data dependencies.

### Code 

NeuroLibre follows the [reproducible runtime environment specification (REES)](https://repo2docker.readthedocs.io/en/latest/specification.html) to define a runtime environment for your preprint. Any programming language supported by Project Jupyter (e.g. python, R, julia, etc.) can be used to create your executable content, where you place necessary [BinderHub configuration files](https://mybinder.readthedocs.io/en/latest/using/config_files.html#config-files) in the `binder` folder.

#### How much computational resources are available and for how long my notebooks can run to generate the outputs?

For each preprint, we guarantee a minimum of 1 CPU core and 4 GB of RAM (8GB maximum), and a maximum of 1 hours of runtime to execute all the notebooks in the `content` folder.

> Do you really want someone to run your code for 1 hour? Probably not.

Even though long-running code cells may be of interest to interactive tutorials, a reader who is interested in reproducing your Figure would be less likely to wait for more than a few minutes for the outputs to be generated. This is why we encourage you to create notebooks that can be run in the "attention span" of a reader.

### Preview your preprint

#### Locally

It is always a good practice to be able to build your MyST article locally before publishing it to NeuroLibre. If you install MyST as described [here](https://mystmd.org/guide/installing), in a virtual environment that has all your code dependencies installed, you can build your myst article:

```bash
cd path/to/your/repo
myst build --execute --html
```

:::{note}
NeuroLibre also supports Jupyter Book for publishing preprints. You can refer to [this documentation](https://jupyterbook.org/en/stable/intro.html) to find out more about it. However, as of late 2024, MyST is our recommended route for writing preprints.
:::

#### Roboneuro preview service

If you have a data dependency and have NeuroLibre cached it for you, you can start using the Roboneuro preview service to build your preprint: https://robo.neurolibre.org

#### Technical screening

Once you submit your preprint to NeuroLibre, our team will perform a technical screening to ensure that your preprint can be built successfully. This is to make sure that your preprint is in line with our guidelines and to avoid any issues that may arise during the build process.

You can visit our technical screening repository [neurolibre/neurolibre-reviews](https://github.com/neurolibre/neurolibre-reviews/issues) to see examples of this process.

### After your preprint is published

We archive all the reproducibility assets of your preprint on Zenodo and link those objects to your reproducible preprint that is assigned a DOI and indexed by [Crossref](https://www.crossref.org/) (also by Google Scholar, Researchgate, and other platforms that use Crossref metadata).

Your preprint can be found, cited, and more importantly, reproduced by any interested reader, and that includes you (probably a few years after you published your preprint)!

### Is the idea of wanting to publish a dashboard with your preprint too crazy?

Absolutely not! We encourage you to publish your dashboard alongside your preprint to showcase your results in the best way possible.

:::: {admonition} An interactive dashboard developed with R Shiny
:class: tip
:::{iframe} https://shinybrain.db.neurolibre.org
:width: 100%
:label: intdashboard
:align: center

MRShiny Brain interactive dashboard at [https://shinybrain.db.neurolibre.org](https://shinybrain.db.neurolibre.org)
:::
::::

:::: {admonition} An award-winning dashboard developed using Plotly Dash
:class: tip
:::{iframe} https://rrsg2020.db.neurolibre.org/
:width: 100%
:label: intdashboard2
:align: center

ISMRM RRSG 2020 interactive dashboard at [https://rrsg2020.db.neurolibre.org/](https://rrsg2020.db.neurolibre.org/)
:::
::::

These dashboards [](#intdashboard) and [](#intdashboard2) are embedded in their respective NeuroLibre preprints! If you are interested in publishing your own dashboard with NeuroLibre, please open an issue using [this template](https://github.com/neurolibre/info/issues/new?assignees=agahkarakuzu&labels=dashboard&projects=&template=new_dashboard.md&title=%5BNEW+DASHBOARD%5D).

If you have any questions or need further assistance, please reach out to us at `info@neurolibre.org`.
