# SciCap: Scientific Figures Dataset

#### This is the Github repo of the EMNLP 2021 Findings' paper, [SciCap: Generating Captions for Scientific Figures](https://aclanthology.org/2021.findings-emnlp.277/).

SciCap a large-scale figure caption dataset based on Computer Science arXiv papers published between 2010 and 2020. SCICAP contained over **416k** figures that focused on one of the dominent figure type - **graphplot**, extracted from over 290,000 papers. 

This dataset aims to allow researchers to study how to use computational models to analyze and caption scientific figures at scale.

SciCap is only for non-commercial use, and is released under <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>. By using SciCap, you agree to the terms in the license.


## How to Cite?
```
@inproceedings{hsu-etal-2021-scicap-generating,
    title = "{S}ci{C}ap: Generating Captions for Scientific Figures",
    author = "Hsu, Ting-Yao  and
      Giles, C Lee  and
      Huang, Ting-Hao",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.277",
    pages = "3258--3264",
    abstract = "Researchers use figures to communicate rich, complex information in scientific papers. The captions of these figures are critical to conveying effective messages. However, low-quality figure captions commonly occur in scientific articles and may decrease understanding. In this paper, we propose an end-to-end neural framework to automatically generate informative, high-quality captions for scientific figures. To this end, we introduce SCICAP, a large-scale figure-caption dataset based on computer science arXiv papers published between 2010 and 2020. After pre-processing {--} including figure-type classification, sub-figure identification, text normalization, and caption text selection {--} SCICAP contained more than two million figures extracted from over 290,000 papers. We then established baseline models that caption graph plots, the dominant (19.2{\%}) figure type. The experimental results showed both opportunities and steep challenges of generating captions for scientific figures.",
}
```

## Download the Dataset

#### You can dowload the SCICAP dataset here: [Download Link](https://www.dropbox.com/s/t1sjqesl0pynaxo/scicap_data.zip?dl=0) (18.15 GB) ####

## Folder Structure
```
scicap_data.zip
├── SciCap-Caption-All                  #caption text for all figures
│	├── Train
│	├── Val
│	└── Test
├── SciCap-No-Subfig-Img                #image files for the figures without subfigures
│	├── Train
│	├── Val
│	└── Test
├── SciCap-Yes-Subfig-Img               #image files for the figures with subfigures
│	├── Train
│	├── Val
│	└── Test
├── arxiv-metadata-oai-snapshot.json    #arXiv paper's metadata (from arXiv dataset)
└── List-of-Files-for-Each-Experiments  #list of figure names used in each experiment 
    ├── Single-Sentence-Caption
    │   ├── No-Subfig
    │   │   ├── Train
    │	│   ├── Val
    │	│   └── Test
    │	└── Yes-Subfig
    │       ├── Train
    │       ├── Val
    │       └── Test
    ├── First-Sentence                  #Same as in Single-Sentence-Caption
    └── Caption-No-More-Than-100-Tokens #Same as in Single-Sentence-Caption
```

### Number of Figures in Each Subset

| Data Collection        | Does the figure have subfigures? |  Train  | Validate |  Test  |
|------------------------|:------:|:-------:|:--------:|:------:|
| First Sentence         |   Yes  | 226,608 |  28,326  | 28,327 |
| First Sentence                       |   No   | 106,834 |  13,354  | 13,355 |
| Single-Sent Caption    |   Yes  | 123,698 |  15,469  | 15,531 |
| Single-Sent Caption                   |   No   |  75,494 |   9,242  |  9,459 |
| Caption w/ <=100 words |   Yes  | 216,392 |  27,072  | 27,036 |
| Caption w/ <=100 words                       |   No   | 105,687 |  13,215  | 13,226 |

## JSON Data Format

### Example Data Instance (Caption and Figure)

An actual JSON object from SCICAP:

```
{
  "contains-subfigure": true, 
  "Img-text": ["(b)", "s]", "[m", "fs", "et", "e", "of", "T", "im", "Attack", "duration", "[s]", "350", "300", "250", "200", "150", "100", "50", "0", "50", "100", "150", "200", "250", "300", "0", "(a)", "]", "[", "m", "fs", "et", "e", "of", "ta", "nc", "D", "is", "Attack", "duration", "[s]", "10000", "9000", "8000", "7000", "6000", "5000", "4000", "3000", "2000", "1000", "0", "50", "100", "150", "200", "250", "300", "0"], 
  "paper-ID": "1001.0025v1", 
  "figure-ID": "1001.0025v1-Figure2-1.png", 
  "figure-type": "Graph Plot", 
  "0-originally-extracted": "Figure 2: Impact of the replay attack, as a function of the spoofing attack duration. (a) Location offset or error: Distance between the attack-induced and the actual victim receiver position. (b) Time offset or error: Time difference between the attack-induced clock value and the actual time.", 
  "1-lowercase-and-token-and-remove-figure-index": {
    "caption": "impact of the replay attack , as a function of the spoofing attack duration . ( a ) location offset or error : distance between the attack-induced and the actual victim receiver position . ( b ) time offset or error : time difference between the attack-induced clock value and the actual time .", 
    "sentence": ["impact of the replay attack , as a function of the spoofing attack duration .", "( a ) location offset or error : distance between the attack-induced and the actual victim receiver position .", "( b ) time offset or error : time difference between the attack-induced clock value and the actual time ."], 
    "token": ["impact", "of", "the", "replay", "attack", ",", "as", "a", "function", "of", "the", "spoofing", "attack", "duration", ".", "(", "a", ")", "location", "offset", "or", "error", ":", "distance", "between", "the", "attack-induced", "and", "the", "actual", "victim", "receiver", "position", ".", "(", "b", ")", "time", "offset", "or", "error", ":", "time", "difference", "between", "the", "attack-induced", "clock", "value", "and", "the", "actual", "time", "."]
  }, 
  "2-normalized": {
    "2-1-basic-num": {
      "caption": "impact of the replay attack , as a function of the spoofing attack duration . ( a ) location offset or error : distance between the attack-induced and the actual victim receiver position . ( b ) time offset or error : time difference between the attack-induced clock value and the actual time .", 
      "sentence": ["impact of the replay attack , as a function of the spoofing attack duration .", "( a ) location offset or error : distance between the attack-induced and the actual victim receiver position .", "( b ) time offset or error : time difference between the attack-induced clock value and the actual time ."], 
      "token": ["impact", "of", "the", "replay", "attack", ",", "as", "a", "function", "of", "the", "spoofing", "attack", "duration", ".", "(", "a", ")", "location", "offset", "or", "error", ":", "distance", "between", "the", "attack-induced", "and", "the", "actual", "victim", "receiver", "position", ".", "(", "b", ")", "time", "offset", "or", "error", ":", "time", "difference", "between", "the", "attack-induced", "clock", "value", "and", "the", "actual", "time", "."]
      }, 
    "2-2-advanced-euqation-bracket": {
      "caption": "impact of the replay attack , as a function of the spoofing attack duration . BRACKET-TK location offset or error : distance between the attack-induced and the actual victim receiver position . BRACKET-TK time offset or error : time difference between the attack-induced clock value and the actual time .", 
      "sentence": ["impact of the replay attack , as a function of the spoofing attack duration .", "BRACKET-TK location offset or error : distance between the attack-induced and the actual victim receiver position .", "BRACKET-TK time offset or error : time difference between the attack-induced clock value and the actual time ."], 
      "tokens": ["impact", "of", "the", "replay", "attack", ",", "as", "a", "function", "of", "the", "spoofing", "attack", "duration", ".", "BRACKET-TK", "location", "offset", "or", "error", ":", "distance", "between", "the", "attack-induced", "and", "the", "actual", "victim", "receiver", "position", ".", "BRACKET-TK", "time", "offset", "or", "error", ":", "time", "difference", "between", "the", "attack-induced", "clock", "value", "and", "the", "actual", "time", "."]
      }
    }
  }
```


<br>Corresponding Figure: **1001.0025v1-Figure2-1.png**


<img align="center" src="https://github.com/tingyaohsu/SciCap/blob/main/img/figure-example.png">

### JSON Scheme

- **contains-subfigure:** boolean (check if contain subfigure)
- **paper-ID:** the unique paper ID in the arXiv dataset
- **figure-ID:** the extracted figure ID of paper (the index is not the same as the label in the caption)
- **figure-type:** the figure type
- **0-originally-extracted:** original captions of figures
- **1-lowercase-and-token-and-remove-figure-index:** Removed figure index and the captions in lowercase
- **2-normalized:** 
  - **2-1-basic-num:** caption after replacing the number
  - **2-2-advanced-euqation-bracket:** caption after replacing the equations and contents in the bracket
- **Img-text:** texts extracted from the figure, such as the texts for labels, legends ... etc.

Within the caption content, we have three attributes:

- **caption:** caption after each normalization
- **sentence:** a list of segmented sentences
- **token:** a list of tokenized words


### Normalized Token
In the paper, we used *[NUM], [BRACKET], [EQUATION]*, but we decided to use *NUM-TK, BRACKET-TK, EQUAT-TK* in the final data release to avoid the extra problems caused by "[]".

| Token  | Description |
| ------------- | ------------- |
| NUM-TK  | Numbers (e.g., 0, -0.2, 3.44%, 1,000,000). |
| BRACKET-TK  | Text spans enclosed by any types of bracket pairs, including {}, [], and ().  |
| EQUAT-TK  | Math equations identified using regular expressions. |



## Baseline Performance

<img align="right" src="https://github.com/tingyaohsu/SciCap/blob/main/img/table_with_datasize.png" width="40%">
To examine the feasibility and challenges of creating an image-captioning model for scientific figures, we established several baselines and tested them using SCICAP. The caption quality was measured by BLEU-4, using the test set of the corresponding data collection as a reference. We trained the models on each data collection with varying levels of data filtering and text normalization. Table 2 shows the results. We also designed three variations of the baseline models, Vision-only, Vision+Text, and Text-only. Table 3 shows the results.<br><br><br><br>
<img align="left" src="https://github.com/tingyaohsu/SciCap/blob/main/img/table_with_img%2Btxt.png" width="40%">
<p><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><p>

## License
  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
  
SciCap is only for non-commercial use, and is released under <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a>. By using SciCap, you agree to the terms in the license.

This dataset uses data in the [arXiv dataset](https://www.kaggle.com/Cornell-University/arxiv).
The [arXiv dataset](https://www.kaggle.com/Cornell-University/arxiv) uses the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license](https://creativecommons.org/publicdomain/zero/1.0/) for the metadata, which grants permission to remix, remake, annotate, and publish the metadata.
