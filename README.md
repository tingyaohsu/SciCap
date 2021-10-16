# SciCap: Scientific Figures Dataset

#### This is the Github repo of [SCICAP: Generating Captions for Scientific Figures](https://github.com/tingyaohsu/SciCap).

SCICAP a large-scale figure-caption dataset based on computer science arXiv papers published between 2010 and 2020. SCICAP contained more than two million figures extracted from over 290,000 papers and focused on one of the dominent figure type - graphplot . 

## Folder Structure
```
├── SciCap-Caption-All.zip (caption JSON files for BOTH sub(280k) + non-sub(130k) images)                       	
│   ├── SciCap-Caption-All-train.json                                       
│   │   └── [{figure-1}, {figure-2}, …, {figure-n}]                                 
│   ├── SciCap-Caption-All-val.json                   
│   │   └── [{figure-1}, {figure-2}, …, {figure-n}]             
│   └── SciCap-Caption-All-test.json           		
│       └── [{figure-1}, {figure-2}, …, {figure-n}]                                           
│
├── SciCap-No-Subfig-Img                         	
│   ├── SciCap-No-Subfig-Img-Train.zip (image files)                                   
│   │                                   
│   ├── SciCap-No-Subfig-Img-Val-No-Subfig.zip (image files)                   
│   │            
│   └── SciCap-No-Subfig-Img-Test-No-Subfig.zip (image files)           		 
│                                      
├── SciCap-Yes-Subfig-Img                         	
│   ├── SciCap-Yes-Subfig-Img-Train.zip (image files)                                   
│   │                                    # expert labels folder
│   ├── SciCap-Yes-Subfig-Img-Val.zip (image files)                   
│   │            
│   └── SciCap-Yes-Subfig-Img-Test.zip (image files)           		
│
├── arxiv-metadata-oai-snapshot.json (from arXiv dataset’s summary)
│
└── List-of-Files-for-Each-Experiments (json)
```

## JSON Format Structure
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
