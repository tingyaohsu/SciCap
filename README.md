# SciCap: Scientific Figures Dataset

#### This is the Github repo of [SCICAP: Generating Captions for Scientific Figures](https://github.com/tingyaohsu/SciCap).

SCICAP a large-scale figure-caption dataset based on computer science arXiv papers published between 2010 and 2020. SCICAP contained more than two million figures extracted from over 290,000 papers and focused on one of the dominent figure type - graphplot . 

## Folder Structure
```
├── SciCap-Caption-All.zip (caption JSON files for BOTH sub(280k) + non-sub(130k) images)                       	
│   ├── SciCap-Caption-All-train.json                                       
│   │   └── [{figure-1}, {figure-2}, …, {figure-n}]                                 
│   ├── SciCap-Caption-All-val.json                                
│   └── SciCap-Caption-All-test.json           	                                          
├── SciCap-No-Subfig-Img (image files)                    	
│   ├── SciCap-No-Subfig-Img-Train.zip                                                                       
│   ├── SciCap-No-Subfig-Img-Val-No-Subfig.zip                               
│   └── SciCap-No-Subfig-Img-Test-No-Subfig.zip           		                                     
├── SciCap-Yes-Subfig-Img (image files)                       	
│   ├── SciCap-Yes-Subfig-Img-Train.zip                                                                       
│   ├── SciCap-Yes-Subfig-Img-Val.zip                       
│   └── SciCap-Yes-Subfig-Img-Test.zip            		
├── arxiv-metadata-oai-snapshot.json (from arXiv dataset’s summary)
└── List-of-Files-for-Each-Experiments (json)
    ├── Single-Sentence-Caption-file-index.json
    │	├── No-Subfig
    │   │	├── Train
    │	│ 	├── Val
    │	│   	└── Test
    │   └── Yes-Subfig
    │   	├── Train
    │	 	├── Val
    │	   	└── Test
    ├── First-Sentence-file-index.json
    └── Caption-No-More-Than-100-Tokens-file-index.json
```

- List-of-Files-for-Each-Experiments: 


## JSON Data Format

### JSON Scheme

- contains-subfigure: boolean (check if contain subfigure)
- paper-ID: the unique paper ID in arXiv dataset
- figure-ID: the extracted figure ID of paper (the index is not same as the label in caption)
- figure-type: the figure type
- 0-originally-extracted: original captions of figures
- 1-lowercase-and-token-and-remove-figure-index: Removed figure index and lowercase the captions   
- 2-normalized: 
  - 2-1-basic-num: caption after replace the number
  - 2-2-advanced-euqation-bracket: caption after replace the equations and contents in the bracket
- Img-text: texts in the figure, including labels, lengends ... etc.

Within the caption content, we have three attributes:

- caption: caption after each normalization
- sentence: sentence tokenize
- token: word tokenize

### Example JSON Object

An actual JSON object from SciCap:

```
{
  "contains-subfigure": boolean (check if contain subfigure),
  "paper-ID": the unique paper ID in arXiv dataset,
  "figure-ID": the extracted figure ID of paper (the index is not same as the label in caption),
  "figure-type": the figure type,
  "0-originally-extracted": "Figure 2: Impact of the replay attack, as a function of the spoofing attack duration. (a) Location offset or error: Distance between the attack-induced and the actual victim receiver position. (b) Time offset or error: Time difference between the attack-induced clock value and the actual time.", (original caption)
  "1-lowercase-and-token-and-remove-figure-index": {
    "caption": "impact of the replay attack , as a function of the spoofing attack duration . ( a ) location offset or error : distance between the attack-induced and the actual victim receiver position . ( b ) time offset or error : time difference between the attack-induced clock value and the actual time .", (lowcase & index remove normalization)
    "sentence": [
	  "impact of the replay attack , as a function of the spoofing attack duration .",
	  "( a ) location offset or error : distance between the attack-induced and the actual victim receiver position .",
	  "( b ) time offset or error : time difference between the attack-induced clock value and the actual time ."
    ], (sentenize)
    "token": [
      "impact",
      "of",
      "the",
      "replay",
      "attack",
      ...,
    ] (tokenize)
  },
  "2-normalized": {
    "2-1-basic-num": {
      "caption": "impact of the replay attack , as a function of the spoofing attack duration . ( a ) location offset or error : distance between the attack-induced and the actual victim receiver position . ( b ) time offset or error : time difference between the attack-induced clock value and the actual time .", (number normalization)
      "sentence": [
        "impact of the replay attack , as a function of the spoofing attack duration .",
	"( a ) location offset or error : distance between the attack-induced and the actual victim receiver position .",
	"( b ) time offset or error : time difference between the attack-induced clock value and the actual time ."
  	], (sentenize)
      "token": [
	"impact",
	"of",
	"the",
	"replay",
	"attack",
	...,
      ] (tokenize)
    },
    "2-2-advanced-euqation-bracket": {
      "caption": "impact of the replay attack , as a function of the spoofing attack duration . BRACKET-TK location offset or error : distance between the attack-induced and the actual victim receiver position . BRACKET-TK time offset or error : time difference between the attack-induced clock value and the actual time .", (euqation & bracket normalization)
      "sentence": [
    	"impact of the replay attack , as a function of the spoofing attack duration .",
    	"BRACKET-TK location offset or error : distance between the attack-induced and the actual victim receiver position .",
    	"BRACKET-TK time offset or error : time difference between the attack-induced clock value and the actual time ."
      ], (sentenize)
      "token": [
	"impact",
	"of",
	"the",
	"replay",
	"attack",
	...,
      ] (tokenize)
    }
  }
  "Img-text": [
    "(b)",
    "s]",
    "[m",
    "fs",
    "et",
    "e",
    "of",
    ...,
   ],
}
```

## Normalized Token
- BRACKET-TK: Used regular expressions to identify equations in captions and replaced them with [EQUATION]. 
- NUM-TK: Replaced all the numbers (e.g., 0, -0.2, 3.44%, 1,000,000) with [NUM].
- EQUAT-TK:  Replaced all the text spans enclosed by any types of bracket pairs, including {}, [], and (), with [BRACKET].

## How to Cite?
```
```

## Baseline Performance

<img align="right" src="https://github.com/tingyaohsu/SciCap/blob/main/img/table_with_datasize.png" width="40%">
To examine the feasibility and challenges of creating an image-captioning model for scientific figures, we established several baselines and tested them using SCICAP. The caption quality was measured by BLEU-4, using the test set of the corresponding data collection as a reference. We trained the models on each data collection with varying levels of data filtering and text normalization. Table 2 shows the results. We also designed three variations of the baseline models, Vision-only, Vision+Text, and Text-only. Table 3 shows the results.<br><br>
<img align="left" src="https://github.com/tingyaohsu/SciCap/blob/main/img/table_with_img%2Btxt.png" width="40%">



## Acknowledgements
We thank Chieh-Yang Huang, Hua Shen, and Chacha Chen for helping with the data annotation. We thank Chieh-Yang Huang for the feedback and strong technical support. We also thank the anonymous reviewers for their constructive feedback. This research was partially supported by the Seed Grant (2020) from the College of Information Sciences and Technology (IST), Pennsylvania State University.
