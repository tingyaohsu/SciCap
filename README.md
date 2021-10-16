# SciCap: Scientific Figures Dataset

#### This is the Github repo of [SCICAP: Generating Captions for Scientific Figures](https://github.com/tingyaohsu/SciCap).

SCICAP a large-scale figure-caption dataset based on computer science arXiv papers published between 2010 and 2020. SCICAP contained more than two million figures extracted from over 290,000 papers and focused on one of the dominent figure type - graphplot . 

## Folder Structure
```
├── human_label                                     # human labels folder
│   ├── test                                        # test set, containing 1,000 abstracts
│   │   └── expert                                  # expert labels folder
│   │       ├── biomedical_expert                   # expert labels from Bio expert
│   │       ├── computer_science_expert             # expert labels from CS expert
│   │       ├── biomedical_expert-eval.csv          # crowd labels evaluated against Bio expert's labels
│   │       └── computer_science_expert-eval.csv    # crowd labels evaluated against CS expert's labels
│   ├── dev                                         # dev set, containing 1,000 abstracts
│   ├── train                                       # training set, containing 8,965 abstracts
│   └── coda_metadata.csv                           # metadata for CODA-19
└── machine_label                                   # empty folder (desgined for future automatic labels)
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
