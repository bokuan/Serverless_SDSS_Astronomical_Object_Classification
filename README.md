
# Serverless SDSS Astronomical Object Classification


<!-- PROJECT SHIELDS -->
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://huggingface.co/spaces/bokuan/SDSS_star_classificiation">
    <img src="https://github.com/bokuan/Serverless_SDSS_Astronomical_Object_Classification/blob/main/res/logo.jpg" alt="Logo" width="900" height="200">
  </a>

  
  <p align="center">
    Serverless ML System
    <br />
    <a href="https://huggingface.co/spaces/bokuan/SDSS_star_classificiation"><strong>feel free to try »</strong></a>
    <br />
    <br />
    <a href="https://huggingface.co/spaces/bokuan/SDSS_star_classificiation">Prediction app</a>
    ·
    <a href="https://huggingface.co/spaces/bokuan/SDSS_star_classificiation_monitor">Monitor app</a>
    
  </p>

</p>

This README.md is for developers who want to try to quickly develop machine learning model user interfaces online instead of just using ipynb for classification or regression.
<span style="color:red">**Just click the link below the picture to see our demo.**</span>
 
## Table of contents

- [Background](#Background)
  - [Requirements](#Requirements)
  - [install](#install)
- [Data](#Data)
- [Structure](#Structure)
- [Authors](#Authors)

## Background

In astronomy, the classification of astronomical observations is a topic of major concern. In the past, the classification of astronomical objects could be judged by astronomical morphology, but with the scaling up of astronomy, the image resolution is not enough to support the classification of celestial objects based on morphology. 

Classification by the photometric characteristics of celestial objects is considered a good alternative. Spectra reveal the temperature, radiation and other physics characteristics of different types of stars through the specific wavelengths of light they emit or absorb. Redshift also provides important information about the motion characteristics of different types of objects. Therefore, by analyzing photometric characteristics machine learning algorithms can efficiently classify celestial objects in large-scaling astronomy.

Astronomical observations have two basic characteristics: <br>
<b>Large scale:</b> the number of catalog objects in SDSS17 released data has reached billion level; <br><b>Continuity: </b>astronomical observation is a continuous process, and the addition of new data must be considered when building an ML model. 

Due to these two characteristics, local-based celestial objects classification model could be expensive and hard to scale. In this project, we used the following frameworks: hopsworks.ai, modal.com and huggingface.com, to build up a scalable serverless machine learning system on the astronomical object classification task.


### Requirements
1. If you have windows, install twofish
2. hopsworks
3. joblib
4. scikit-learn==1.1.1
5. seaborn
6. dataframe-image
7. modal
8. gradio==4.2.0
9. pandas<2.2.0

### **install**
Clone the repo

```sh
git clone https://github.com/bokuan/Serverless_SDSS_Astronomical_Object_Classification.git
```

## Data 
The data sources include a data lake and a data warehosue:

The data lake is SDSS Data Release 17 (DR17), which is the final data release of the fourth phase of the Sloan Digital Sky Survey (SDSS-IV). DR17 contains SDSS observations through January 2021: https://www.sdss4.org/dr17/

The data warehouse is a pre-processed fragment from SDSS-IV DR17, which contains 100,000 celestial objects: https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17

### Structure

[![structure](https://github.com/bokuan/Serverless_SDSS_Astronomical_Object_Classification/blob/main/res/structure.png)](https://github.com/bokuan/Serverless_SDSS_Astronomical_Object_Classification/blob/main/res/structure.png)


### Authors
- [Tong Mo](https://github.com/Tongm56)
- Bokuan Li [Github](https://github.com/bokuan) / [Personal page](https://bokuan.li/)


### License

 [LICENSE.txt](https://github.com/bokuan/Serverless_SDSS_Astronomical_Object_Classification/blob/main/LICENSE)

### Reference

- [Bai Y, Liu J F, Wang S, et al. Machine learning applied to Star–Galaxy–QSO classification and stellar effective temperature regression[J]. The Astronomical Journal, 2018, 157(1): 9.](https://iopscience.iop.org/article/10.3847/1538-3881/aaf009/meta)
- [Hopsworks documentation](https://docs.hopsworks.ai/3.5/)




