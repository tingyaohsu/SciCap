# SciCap: Scientific Figures Dataset

#### This is the Github repo of [SCICAP: Generating Captions for Scientific Figures](https://github.com/tingyaohsu/SciCap).

SCICAP a large-scale figure-caption dataset based on computer science arXiv papers published between 2010 and 2020. SCICAP contained more than two million figures extracted from over 290,000 papers and focused on one of the dominent figure type - graphplot . 

## Folder Structure
```
├── SciCap-Caption-All.zip (caption JSON files for BOTH sub(280k) + non-sub(130k) images)                       	
│   ├── SciCap-Caption-All-train.json                                        # test set, containing 1,000 abstracts
│   │   └── [{figure-1}, {figure-2}, …, {figure-n}]                                  # expert labels folder
│   ├── SciCap-Caption-All-val.json                   # expert labels from Bio expert
│   │   └── [{figure-1}, {figure-2}, …, {figure-n}]             # expert labels from CS expert
│   └── SciCap-Caption-All-test.json           		# crowd labels evaluated against Bio expert's labels
│       └── [{figure-1}, {figure-2}, …, {figure-n}]    # crowd labels evaluated against CS expert's labels                                        
│
├── SciCap-No-Subfig-Img                         	# human labels folder
│   ├── SciCap-No-Subfig-Img-Train.zip (image files)                                   # test set, containing 1,000 abstracts
│   │                                    # expert labels folder
│   ├── SciCap-No-Subfig-Img-Val-No-Subfig.zip (image files)                   # expert labels from Bio expert
│   │            # expert labels from CS expert
│   ├── SciCap-No-Subfig-Img-Test-No-Subfig.zip (image files)           		# crowd labels evaluated against Bio 
│   │                                    # empty folder (desgined for future 
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
