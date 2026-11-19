# Multi-book test set — review sheet

Written by Claude from the cleaned book pages. Please check each question and its key facts.
Every fact gives the book, the **PDF page** (open the PDF at this page) and the printed page.
Mark anything wrong in the `Reviewer` line; the test only runs after this sheet is approved.

**Leakage rules:** this folder is never indexed or shown to the answering model; questions are
paraphrased (checked: no 8-word overlap with any book page); `test` questions are run once only.

| Type | Count |
| --- | ---: |
| two_book | 14 |
| three_book | 10 |
| conflict | 5 |
| unanswerable | 6 |
| single_book | 5 |

Split: 9 dev / 31 test

## mb-01 · two_book · dev

**Q:** A dog has drunk antifreeze. What antidote regimen is given, and what urine crystal finding supports the diagnosis?

Required books: The Merck Veterinary Manual, Plumb's Veterinary Drug Handbook

- Fomepizole for ethylene glycol in dogs: 20 mg/kg IV load, 15 mg/kg IV at 12 h, 15 mg/kg at 24 h, 5 mg/kg at 36 h.  
  _Plumb's Veterinary Drug Handbook, p. 1596 (PDF p. 1596)_ — “Initially load at 20 mg/kg IV”
- Calcium oxalate (monohydrate, dumb-bell shaped) crystals are associated with ethylene glycol toxicity.  
  _The Merck Veterinary Manual, p. 1618 (PDF p. 1659)_ — “typically seen in association with ethylene glycol toxicity”

Also valid (keyword match [['ethylene glycol', 'fomepizole'], ['ethylene glycol', 'oxalate']]): BSAVA Small Animal Formulary (PDF p. 163); Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 70, 410, 411, 537, 538); Applied Pharmacology for Veterinary Technicians (PDF p. 431, 433, 434, 446, 448); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 1427, 2502, 2703, 2706, 2716); Saunders Comprehensive Veterinary Dictionary (PDF p. 302, 469, 510, 822); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 329)

Reviewer: ☐ OK ☐ Change: ……

## mb-02 · two_book · test

**Q:** When ivermectin is used for canine demodicosis, how should it be given to work, and which breeds need special caution?

Required books: Muller and Kirk's Small Animal Dermatology, Plumb's Veterinary Drug Handbook

- Weekly protocols used for other ectoparasites were not effective for Demodex; daily oral ivermectin can be effective.  
  _Muller and Kirk's Small Animal Dermatology, p. 429 (PDF p. 433)_ — “it can be effective when it is administered orally daily”
- Caution in ABCB1 (MDR1) mutation breeds: Collies, Australian Shepherds, Shelties, Long-haired Whippets - higher CNS toxicity risk.  
  _Plumb's Veterinary Drug Handbook, p. 1977 (PDF p. 1977)_ — “Caution in breeds susceptible to ABCB1”

Also valid (keyword match [['ivermectin', 'demodicosis'], ['ivermectin', 'abcb1'], ['ivermectin', 'mdr1']]): BSAVA Small Animal Formulary (PDF p. 194, 195); Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 84, 132, 256, 323, 426); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 315, 316, 565, 651); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 2772, 4469); Saunders Solutions in Veterinary Practice: Small Animal Dermatology (PDF p. 166, 167, 168, 169, 192); Saunders Comprehensive Veterinary Dictionary (PDF p. 21, 626, 864); Slatter's Fundamentals of Veterinary Ophthalmology (PDF p. 83, 400); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 118, 122, 125, 128, 129); The Merck Veterinary Manual (PDF p. 948, 959, 963, 964, 2617)

Reviewer: ☐ OK ☐ Change: ……

## mb-03 · two_book · test

**Q:** At what ages is a puppy vaccinated against parvovirus in the suggested schedule, and which drugs support a puppy already sick with parvo?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Veterinary Vaccination Schedule

- Parvovirus: live attenuated vaccine at 6 weeks, then 10 and 14 weeks, subcutaneous.  
  _Veterinary Vaccination Schedule, PDF p. 7_ — “Canine Parvo virus Live attenuated 6 weeks”
- Supportive drugs: parenteral ampicillin + gentamicin, antiemetics such as ondansetron or maropitant; gentamicin can harm the kidneys of dehydrated puppies.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 217 (PDF p. 287)_ — “ampicillin and gentamicin”

Also valid (keyword match [['parvovirus', 'vaccin', 'weeks'], ['parvovirus', 'maropitant'], ['parvovirus', 'ondansetron']]): Applied Pharmacology for Veterinary Technicians (PDF p. 364, 365, 384); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 1091, 3658, 3662, 3673, 3677); Plumb's Veterinary Drug Handbook (PDF p. 2638); Saunders Comprehensive Veterinary Dictionary (PDF p. 161, 413, 598); The Merck Veterinary Manual (PDF p. 428, 696, 1383, 1914)

Reviewer: ☐ OK ☐ Change: ……

## mb-04 · two_book · dev

**Q:** For suspected free air in the chest, which radiographic view makes it easier to see and what does auscultation typically reveal?

Required books: Small Animal Surgery (Fossum), Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs

- Pleural gas rises dorsally in ventral recumbency, so it is easier to detect on a DV view than a VD view.  
  _Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, p. 161 (PDF p. 173)_ — “making detection easier in a DV view”
- Pneumothorax: lung sounds are absent over the dorsal lateral chest wall.  
  _Small Animal Surgery (Fossum), p. 739 (PDF p. 799)_ — “absence of pulmonary sounds in the dorsal lateral chest wall”

Also valid (keyword match [['pneumothorax', 'dv view'], ['pneumothorax', 'lung sounds'], ['pneumothorax', 'radiograph']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 94, 96, 300, 309, 464); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 899, 901, 1506, 1514, 1515); Saunders Comprehensive Veterinary Dictionary (PDF p. 891, 933, 1047, 1059, 1121); The Merck Veterinary Manual (PDF p. 1491, 1703, 1705, 1709, 1710)

Reviewer: ☐ OK ☐ Change: ……

## mb-05 · two_book · test

**Q:** In glaucoma management, what pressure value guides whether to keep going with medical treatment or move to surgery, and which oral agent can lower pressure quickly in an emergency?

Required books: Plumb's Veterinary Drug Handbook, Slatter's Fundamentals of Veterinary Ophthalmology

- If IOP stays below 20 mm Hg continue medical treatment; above 20 mm Hg consider surgery.  
  _Slatter's Fundamentals of Veterinary Ophthalmology, p. 298 (PDF p. 314)_ — “IOP < 20 Continue medical Rx”
- Oral glycerin is used for short-term IOP reduction in acute glaucoma; its effect is more variable than mannitol.  
  _Plumb's Veterinary Drug Handbook, p. 1688 (PDF p. 1688)_ — “short-term reduction of IOP in small animals with acute glaucoma”

Also valid (keyword match [['glaucoma', 'glycerin'], ['glaucoma', 'mannitol'], ['intraocular pressure', '20 mm hg']]): BSAVA Small Animal Formulary (PDF p. 171, 172, 201, 215, 352); Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 622, 867, 1555, 1569); Applied Pharmacology for Veterinary Technicians (PDF p. 470); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 4195); Saunders Comprehensive Veterinary Dictionary (PDF p. 355, 584, 698); The Merck Veterinary Manual (PDF p. 1739, 1740, 2611); WSAVA List of Essential Medicines for Cats and Dogs (PDF p. 7, 22)

Reviewer: ☐ OK ☐ Change: ……

## mb-06 · two_book · test

**Q:** How is dry eye confirmed with a tear test, and what kind of drug is commonly used to treat immune-mediated eye disease such as this?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Slatter's Fundamentals of Veterinary Ophthalmology

- Schirmer tear test: normal >= 15 mm/min; < 15 mm/min suggests KCS (interpret with breed).  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 775 (PDF p. 845)_ — “values < 15 mm/min suggest KCS”
- Cyclosporine is a potent immunosuppressive used often for immune-mediated ocular disease.  
  _Slatter's Fundamentals of Veterinary Ophthalmology, p. 72 (PDF p. 88)_ — “Cyclosporine is a potent immunosuppressive drug”

Also valid (keyword match [['schirmer', 'keratoconjunctivitis sicca'], ['keratoconjunctivitis sicca', 'cyclosporine']]): BSAVA Small Animal Formulary (PDF p. 263, 337); Applied Pharmacology for Veterinary Technicians (PDF p. 195, 198, 204, 351, 352); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 716, 778); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 6347); Muller and Kirk's Small Animal Dermatology (PDF p. 678, 920); Plumb's Veterinary Drug Handbook (PDF p. 3699, 3707, 3783, 3784, 3785); Saunders Comprehensive Veterinary Dictionary (PDF p. 1006, 1104); The Merck Veterinary Manual (PDF p. 533); WSAVA List of Essential Medicines for Cats and Dogs (PDF p. 18, 21)

Reviewer: ☐ OK ☐ Change: ……

## mb-07 · two_book · test

**Q:** In a dog in anaphylactic shock, what epinephrine dose is suggested and why does epinephrine help?

Required books: Applied Pharmacology for Veterinary Technicians, Blackwell's Five-Minute Veterinary Consult: Canine and Feline

- Epinephrine 1:1,000 at 0.01 mL/kg parenterally for anaphylactic shock.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 76 (PDF p. 146)_ — “1:1,000; 0.01 mL/kg”
- Epinephrine reverses the hypotension and bronchoconstriction of anaphylactic shock.  
  _Applied Pharmacology for Veterinary Technicians, p. 77 (PDF p. 89)_ — “hypotension and bronchoconstriction of anaphylactic shock”

Also valid (keyword match [['anaphyla', 'epinephrine'], ['anaphyla', 'adrenaline']]): BSAVA Small Animal Formulary (PDF p. 23, 24, 132, 139, 342); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 261); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 2603, 2608, 2609, 2610, 2614); Muller and Kirk's Small Animal Dermatology (PDF p. 509); Plumb's Veterinary Drug Handbook (PDF p. 191, 1062, 1208, 1209, 1350); Saunders Comprehensive Veterinary Dictionary (PDF p. 664); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 173); The Merck Veterinary Manual (PDF p. 1482, 2583, 2651, 2765, 3205); WSAVA List of Essential Medicines for Cats and Dogs (PDF p. 5)

Reviewer: ☐ OK ☐ Change: ……

## mb-08 · two_book · dev

**Q:** How common is pancreatitis among pancreatic diseases of dogs and cats, and which specific blood test is listed for it?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, The Merck Veterinary Manual

- Pancreatitis is the most common exocrine pancreatic disease in dogs and cats; it may be acute or chronic.  
  _The Merck Veterinary Manual, p. 407 (PDF p. 448)_ — “most conm1on exoc1ine pancreatic disease”
- Spec cPL is the test listed for pancreatitis.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 395 (PDF p. 465)_ — “Spec cPL (pancreatitis)”

Also valid (keyword match [['pancreatitis', 'cpl'], ['pancreatitis', 'exocrine pancreatic disease']]): Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 687, 1350, 1353, 1354, 1355); Plumb's Veterinary Drug Handbook (PDF p. 1715); Saunders Comprehensive Veterinary Dictionary (PDF p. 669); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 201, 202); Small Animal Surgery (Fossum) (PDF p. 709)

Reviewer: ☐ OK ☐ Change: ……

## mb-09 · two_book · test

**Q:** How is chronic kidney disease staged in dogs and cats, and what urine protein:creatinine range counts as borderline proteinuria in each species?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, The Merck Veterinary Manual

- IRIS stages 1-4 use two or more fasting, well-hydrated serum creatinine values over several weeks; CKD = present > 3 months.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 1164 (PDF p. 1234)_ — “IRIS CKD stages 1”
- IRIS proteinuria substage 'borderline': UPC 0.2-0.5 in dogs, 0.2-0.4 in cats.  
  _The Merck Veterinary Manual, p. 1513 (PDF p. 1554)_ — “Borderline 0.2-0.5 0.2-0.4”

Also valid (keyword match [['iris', 'stage', 'creatinine'], ['proteinuria', 'borderline']]): Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 7129, 7150, 7471, 7498, 7504); Saunders Comprehensive Veterinary Dictionary (PDF p. 621, 965); Small Animal Surgery (Fossum) (PDF p. 765, 766)

Reviewer: ☐ OK ☐ Change: ……

## mb-10 · two_book · test

**Q:** How is primidone related to phenobarbital, and what organ toxicity is a concern with both drugs?

Required books: Applied Pharmacology for Veterinary Technicians, BSAVA Small Animal Formulary

- Primidone (Mysoline) is converted to phenobarbitone (phenobarbital).  
  _BSAVA Small Animal Formulary, p. 286 (PDF p. 304)_ — “conversion of mysoline to phenobarbitone”
- Hepatotoxicity is an adverse effect of phenobarbital and primidone.  
  _Applied Pharmacology for Veterinary Technicians, p. 86 (PDF p. 98)_ — “hepatotoxicity (phenobarbital and primidone)”

Also valid (keyword match [['primidone', 'phenobarb']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 670, 678, 696, 1596); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 969, 988, 2694, 3465, 3470); Muller and Kirk's Small Animal Dermatology (PDF p. 724, 787, 1065, 1070); Plumb's Veterinary Drug Handbook (PDF p. 64, 449, 450, 545, 721); Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs (PDF p. 528); Saunders Comprehensive Veterinary Dictionary (PDF p. 914); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 59, 207, 291, 310); The Merck Veterinary Manual (PDF p. 475, 493, 2639, 3076)

Reviewer: ☐ OK ☐ Change: ……

## mb-11 · two_book · test

**Q:** Which skin changes point to Cushing's syndrome, including the ones typical in cats, and which dexamethasone dose is used for the suppression test in cats?

Required books: Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, Plumb's Veterinary Drug Handbook

- Cushing's: truncal alopecia, comedones, rat tail, thin skin, phlebectasia, potbelly; in cats curled pinnal tips and skin fragility.  
  _Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, p. 60 (PDF p. 74)_ — “curling of tips of pinnae and skin fragility”
- LDDS is the test of choice for feline HAC and uses 0.1 mg/kg IV dexamethasone, higher than in dogs.  
  _Plumb's Veterinary Drug Handbook, p. 1062 (PDF p. 1062)_ — “uses a higher dose of dexamethasone (0.1 mg/kg IV) than in dogs”

Also valid (keyword match [['hyperadrenocorticism', 'skin fragility'], ['hyperadrenocorticism', 'cats', 'dexamethasone suppression']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 56, 87, 129, 258, 580); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 521, 673, 7357, 7361, 7362); Muller and Kirk's Small Animal Dermatology (PDF p. 142, 789, 793, 794, 795); Saunders Solutions in Veterinary Practice: Small Animal Dermatology (PDF p. 115); Saunders Comprehensive Veterinary Dictionary (PDF p. 42); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 251, 253, 293); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 120, 306); Small Animal Surgery (Fossum) (PDF p. 698); The Merck Veterinary Manual (PDF p. 585, 1015)

Reviewer: ☐ OK ☐ Change: ……

## mb-12 · two_book · dev

**Q:** Against which parasites is selamectin indicated in dogs and cats, and how often is it applied for prevention?

Required books: BSAVA Small Animal Formulary, The Merck Veterinary Manual

- Selamectin is applied topically monthly at ~6 mg/kg; kills fleas and treats Otodectes and sarcoptic mange.  
  _The Merck Veterinary Manual, p. 137 (PDF p. 178)_ — “monthly dosage of -6 mg/kg”
- Selamectin is used for fleas, ear mites (Otodectes), sarcoptic mange, lice, roundworms and heartworm prevention in dogs.  
  _BSAVA Small Animal Formulary, p. 305 (PDF p. 323)_ — “prevention of heartworm disease”

Also valid (keyword match [['selamectin', 'otodectes'], ['selamectin', 'heartworm']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 498, 594, 643, 645, 841); Applied Pharmacology for Veterinary Technicians (PDF p. 222, 257, 265, 271, 273); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 651, 823); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 229, 5350, 5358, 5366); Muller and Kirk's Small Animal Dermatology (PDF p. 428, 432, 434, 456, 502); Plumb's Veterinary Drug Handbook (PDF p. 3187, 3191, 3192, 3908); Saunders Solutions in Veterinary Practice: Small Animal Dermatology (PDF p. 35, 363); Saunders Comprehensive Veterinary Dictionary (PDF p. 1016); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 131, 151); WSAVA List of Essential Medicines for Cats and Dogs (PDF p. 12)

Reviewer: ☐ OK ☐ Change: ……

## mb-13 · two_book · test

**Q:** How should a kennel be disinfected after a parvovirus case, and which antiemetic drugs can be used for the affected puppies?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, The Merck Veterinary Manual

- Clean organic matter, then disinfect with dilute bleach (1:30) or peroxygen / accelerated hydrogen peroxide products.  
  _The Merck Veterinary Manual, p. 376 (PDF p. 417)_ — “dilute bleach”
- Antiemetics for parvovirus: ondansetron, maropitant.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 217 (PDF p. 287)_ — “ondansetron, maropitant”

Also valid (keyword match [['parvovirus', 'bleach'], ['parvovirus', 'disinfect'], ['parvovirus', 'maropitant']]): Applied Pharmacology for Veterinary Technicians (PDF p. 252, 253, 254); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 4031, 4041, 4044, 4046); Saunders Comprehensive Veterinary Dictionary (PDF p. 907, 1198); Small Animal Surgery (Fossum) (PDF p. 42, 48, 185)

Reviewer: ☐ OK ☐ Change: ……

## mb-14 · two_book · test

**Q:** Why can a single injection of meloxicam be risky in an anaesthetised animal or one with liver disease, and how is the drug handled by the body?

Required books: BSAVA Small Animal Formulary, Plumb's Veterinary Drug Handbook

- Delay meloxicam if anaesthetic hypotension is expected (renal perfusion); liver disease prolongs metabolism and risks accumulation.  
  _BSAVA Small Animal Formulary, p. 206 (PDF p. 224)_ — “Liver disease will prolong the metabolism of meloxicam”
- In dogs meloxicam is well absorbed, peaks at 7-8 h, ~97% protein bound and extensively metabolised in the liver.  
  _Plumb's Veterinary Drug Handbook, p. 2259 (PDF p. 2259)_ — “about 97% is bound to plasma proteins”

Also valid (keyword match [['meloxicam', 'liver'], ['meloxicam', 'protein bound'], ['meloxicam', 'hypotension']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 184, 405, 583, 843, 1017); Applied Pharmacology for Veterinary Technicians (PDF p. 78, 288); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 2429, 2655, 2822, 3457, 4723); Saunders Comprehensive Veterinary Dictionary (PDF p. 823); Slatter's Fundamentals of Veterinary Ophthalmology (PDF p. 102); Small Animal Surgery (Fossum) (PDF p. 175, 176, 308, 354, 385); The Merck Veterinary Manual (PDF p. 1002, 2757, 2761, 3078)

Reviewer: ☐ OK ☐ Change: ……

## mb-15 · three_book · dev

**Q:** What are the main mechanisms behind increased thirst and urination in dogs, and which diseases cause the kidneys to stop responding to ADH?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Small Animal Medical Differential Diagnosis: A Book of Lists, Ettinger's Textbook of Veterinary Internal Medicine

- PU results from excess water intake (primary polydipsia) or reduced urine concentrating ability (primary polyuria).  
  _Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 1149_ — “primary polydipsia”
- Secondary nephrogenic DI causes: renal failure, hyperadrenocorticism, hypoadrenocorticism, hepatic insufficiency, pyometra, hypercalcemia, hypokalemia ...  
  _Small Animal Medical Differential Diagnosis: A Book of Lists, p. 118 (PDF p. 122)_ — “Polyuria caused by nonresponsiveness to antidiuretic hormone”
- Primary PU from impaired renal response to ADH: renal failure, HAC (dogs), hyperthyroidism (cats).  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 1094 (PDF p. 1164)_ — “impaired renal response to ADH”

Also valid (keyword match [['polyuria', 'primary polydipsia'], ['nephrogenic diabetes insipidus']]): BSAVA Small Animal Formulary (PDF p. 179); Applied Pharmacology for Veterinary Technicians (PDF p. 125); Plumb's Veterinary Drug Handbook (PDF p. 735, 739, 1765, 1769, 1773); Saunders Comprehensive Veterinary Dictionary (PDF p. 339, 965); The Merck Veterinary Manual (PDF p. 582, 592, 691)

Reviewer: ☐ OK ☐ Change: ……

## mb-16 · three_book · test

**Q:** A cat has inflammation inside the front of the eye. Which systemic infections should be ruled out, and what anti-inflammatory regimen can be given by mouth or injection?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Ettinger's Textbook of Veterinary Internal Medicine, Slatter's Fundamentals of Veterinary Ophthalmology

- Feline uveitis causes: FeLV, FIV, FIP, Toxoplasma gondii, systemic fungi, neoplasia; Bartonella role debated.  
  _Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 549_ — “Toxoplasma gondii”
- Meloxicam 0.2 mg/kg once, then 0.05 mg/kg q24h for 2 days, then 0.025 mg/kg; limit to 4 days (renal risk).  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 97 (PDF p. 167)_ — “limit duration of use to 4 days”
- Infectious causes listed include FIV, FIP (feline coronavirus), FeLV.  
  _Slatter's Fundamentals of Veterinary Ophthalmology, p. 379 (PDF p. 395)_ — “Feline infectious peritonitis”

Also valid (keyword match [['uveitis', 'toxoplasm', 'cat'], ['uveitis', 'meloxicam', 'cat']]): Plumb's Veterinary Drug Handbook (PDF p. 838); Saunders Comprehensive Veterinary Dictionary (PDF p. 390, 925); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 17, 183, 184, 195, 248); The Merck Veterinary Manual (PDF p. 537, 544, 546, 824, 871)

Reviewer: ☐ OK ☐ Change: ……

## mb-17 · three_book · test

**Q:** Which laboratory tests are used to diagnose hyperadrenocorticism, and how does the suppression test differ in cats?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, The Merck Veterinary Manual, Plumb's Veterinary Drug Handbook

- UCCR with oral dexamethasone: if UCCR does not fall into normal range HAC is confirmed; ACTH stimulation is also used.  
  _The Merck Veterinary Manual, p. 545 (PDF p. 586)_ — “the diagnosis of hyperadrenocorticism can be confim1ed”
- ACTH-response test, LDDST and HDDST diagnose HAC; abdominal ultrasound assesses the adrenals.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 60 (PDF p. 130)_ — “ACTH-response test, LDDST, and HDDST”
- Feline LDDS uses 0.1 mg/kg IV dexamethasone, higher than in dogs.  
  _Plumb's Veterinary Drug Handbook, p. 1062 (PDF p. 1062)_ — “Test of choice for diagnosis of feline hyperadrenocorticism”

Also valid (keyword match [['hyperadrenocorticism', 'acth stimulation'], ['hyperadrenocorticism', 'dexamethasone suppression']]): BSAVA Small Animal Formulary (PDF p. 108, 181, 198, 243, 343); Applied Pharmacology for Veterinary Technicians (PDF p. 186); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 354, 424, 425, 780, 811); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 673, 7281, 7286, 7309, 7334); Muller and Kirk's Small Animal Dermatology (PDF p. 789, 790, 793, 794, 795); Saunders Solutions in Veterinary Practice: Small Animal Dermatology (PDF p. 154); Saunders Comprehensive Veterinary Dictionary (PDF p. 34, 42, 290); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 245, 246, 251, 260); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 120, 121, 289, 306, 346); Small Animal Surgery (Fossum) (PDF p. 698)

Reviewer: ☐ OK ☐ Change: ……

## mb-18 · three_book · test

**Q:** What drugs control an overactive thyroid in cats, how do they relate to each other, and can they be given through the skin?

Required books: BSAVA Small Animal Formulary, Plumb's Veterinary Drug Handbook, WSAVA List of Essential Medicines for Cats and Dogs

- Carbimazole is converted to the active drug methimazole, which blocks thyroid hormone synthesis.  
  _BSAVA Small Animal Formulary, p. 49 (PDF p. 67)_ — “Carbimazole is metabolized to the active drug methimazole”
- Methimazole (thiamazole) is given orally but can be compounded as a transdermal preparation.  
  _WSAVA List of Essential Medicines for Cats and Dogs, p. 15 (PDF p. 16)_ — “compounded as transdermal preparations”
- Methimazole is the agent of choice in North America; transdermal PLO gel 2.5 mg twice daily; propylthiouracil has more adverse effects.  
  _Plumb's Veterinary Drug Handbook, p. 2317 (PDF p. 2317)_ — “Transdermal methimazole (in PLO gel; 2.5 mg twice daily)”

Also valid (keyword match [['methimazole', 'transdermal'], ['carbimazole', 'methimazole']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 763, 1372, 1526, 1574); Applied Pharmacology for Veterinary Technicians (PDF p. 183, 490); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 6646, 7139, 7140, 7141, 7142); Muller and Kirk's Small Animal Dermatology (PDF p. 870); Saunders Comprehensive Veterinary Dictionary (PDF p. 95, 202, 722, 1120, 1141); Small Animal Surgery (Fossum) (PDF p. 732, 733, 738); The Merck Veterinary Manual (PDF p. 601, 602, 1653)

Reviewer: ☐ OK ☐ Change: ……

## mb-19 · three_book · dev

**Q:** In a dog with a twisted, bloated stomach, where should IV catheters be placed during stabilisation, and how is recurrence prevented?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Ettinger's Textbook of Veterinary Internal Medicine, The Merck Veterinary Manual

- Place large-gauge catheters in veins cranial to the volvulus (jugular/cephalic), then intensive fluid resuscitation.  
  _Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 6167_ — “large-gauge catheters in veins cranial to the gastric volvulus”
- Recurrence is prevented by permanent gastropexy.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 532 (PDF p. 602)_ — “Prevention of recurrence is achieved through a permanent gastropexy”
- Prophylactic gastropexy is recommended for at-risk breeds or dogs whose relatives had GDV.  
  _The Merck Veterinary Manual, p. 386 (PDF p. 427)_ — “Prophylactic gastropexy”

Also valid (keyword match [['gastric dilat', 'gastropexy'], ['volvulus', 'catheter']]): Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs (PDF p. 381); Saunders Comprehensive Veterinary Dictionary (PDF p. 494); Small Animal Surgery (Fossum) (PDF p. 115, 383, 485, 498, 501)

Reviewer: ☐ OK ☐ Change: ……

## mb-20 · three_book · test

**Q:** Which drug is preferred for treating an underactive thyroid in dogs, what starting dose is used, and when would a T3 product be considered?

Required books: Applied Pharmacology for Veterinary Technicians, Plumb's Veterinary Drug Handbook, WSAVA List of Essential Medicines for Cats and Dogs

- Synthetic T4 (levothyroxine) is the compound of choice; T3 only if response to T4 is poor.  
  _Applied Pharmacology for Veterinary Technicians, p. 170 (PDF p. 182)_ — “T3 products are recommended only when a poor response to T4 occurs”
- Start 0.02 mg/kg PO twice daily; 0.5 mg/m2 may avoid hyperthyroid effects in large breeds.  
  _Plumb's Veterinary Drug Handbook, p. 2100 (PDF p. 2100)_ — “0.02 mg/kg PO twice daily to start”
- Synthetic thyroxine (levothyroxine) treats canine hypothyroidism.  
  _WSAVA List of Essential Medicines for Cats and Dogs, p. 15 (PDF p. 16)_ — “Levothyroxine is the most common form”

Also valid (keyword match [['levothyroxine', 'hypothyroidism', 'mg/kg'], ['levothyroxine', 'liothyronine']]): BSAVA Small Animal Formulary (PDF p. 204, 207, 338); Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 641, 794, 801, 996, 1566); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 436, 799, 800, 827); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 6076, 6950); Muller and Kirk's Small Animal Dermatology (PDF p. 784, 823, 865, 866, 867); Saunders Solutions in Veterinary Practice: Small Animal Dermatology (PDF p. 147, 266, 267, 268); Saunders Comprehensive Veterinary Dictionary (PDF p. 670, 1126); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 254, 255); Small Animal Surgery (Fossum) (PDF p. 727); The Merck Veterinary Manual (PDF p. 2620)

Reviewer: ☐ OK ☐ Change: ……

## mb-21 · three_book · test

**Q:** How common is outer ear inflammation, what role do ear mites play in cats, and how are the contributing causes grouped?

Required books: Small Animal Surgery (Fossum), The Merck Veterinary Manual, Muller and Kirk's Small Animal Dermatology

- Otitis externa: up to 20% of dog admissions (7% cats); 50-89% of affected dogs have otitis media; O. cynotis causes > 50% of feline otitis externa.  
  _Small Animal Surgery (Fossum), p. 338 (PDF p. 365)_ — “up to 20% of hospital admissions”
- Predisposing factors act with primary causes, secondary causes and perpetuating factors.  
  _Muller and Kirk's Small Animal Dermatology, p. 1204 (PDF p. 1203)_ — “primary causes, secondary causes, or perpetuating factors”
- Selamectin is indicated for Otodectes cynotis in dogs and cats.  
  _The Merck Veterinary Manual, p. 137 (PDF p. 178)_ — “Otodectes”

Also valid (keyword match [['otitis externa', 'otodectes'], ['otitis externa', 'perpetuating']]): BSAVA Small Animal Formulary (PDF p. 347); Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 203, 498, 640, 1057, 1058); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 556, 558, 559, 648, 650); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 1666, 3095); Saunders Solutions in Veterinary Practice: Small Animal Dermatology (PDF p. 78, 232, 334, 335); Saunders Comprehensive Veterinary Dictionary (PDF p. 371, 817, 818); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 29, 131, 151, 309, 389); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 113, 354)

Reviewer: ☐ OK ☐ Change: ……

## mb-22 · three_book · test

**Q:** Why might a dog's meloxicam overdose need several days of monitoring, and which patient factors raise the risk of accumulation?

Required books: BSAVA Small Animal Formulary, Ettinger's Textbook of Veterinary Internal Medicine, Plumb's Veterinary Drug Handbook

- Meloxicam terminal half-life ~24 h in dogs; after 5 days concentration falls ~97%.  
  _Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 2765_ — “terminal half-life”
- Liver disease prolongs metabolism and risks accumulation with repeated dosing.  
  _BSAVA Small Animal Formulary, p. 206 (PDF p. 224)_ — “Liver disease will prolong the metabolism of meloxicam”
- Meloxicam is extensively biotransformed in the liver; ~97% protein bound.  
  _Plumb's Veterinary Drug Handbook, p. 2259 (PDF p. 2259)_ — “extensively biotransformed”

Also valid (keyword match [['meloxicam', 'half-life'], ['meloxicam', 'liver']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 184, 405, 583, 843, 1024); Applied Pharmacology for Veterinary Technicians (PDF p. 78, 288); Saunders Comprehensive Veterinary Dictionary (PDF p. 823, 867); Slatter's Fundamentals of Veterinary Ophthalmology (PDF p. 102); Small Animal Surgery (Fossum) (PDF p. 176, 308, 354, 385, 531); The Merck Veterinary Manual (PDF p. 1002, 2757, 2761, 3078)

Reviewer: ☐ OK ☐ Change: ……

## mb-23 · three_book · test

**Q:** How reliable are skin scrapings for finding scabies mites in dogs, and what topical treatment regimens are recommended?

Required books: Small Animal Dermatology: A Color Atlas and Therapeutic Guide, The Merck Veterinary Manual, Saunders Solutions in Veterinary Practice: Small Animal Dermatology

- Superficial scrapings find Sarcoptes in only ~20% of cases.  
  _Small Animal Dermatology: A Color Atlas and Therapeutic Guide, p. 13 (PDF p. 26)_ — “Low (only 20%)”
- Selamectin 6-12 mg/kg twice, 30 days apart (some use three times at 14-day intervals).  
  _Saunders Solutions in Veterinary Practice: Small Animal Dermatology, p. 26 (PDF p. 35)_ — “6–12 mg/kg twice 30 days apart”
- Selamectin (monthly ~6 mg/kg) is indicated for sarcoptic mange.  
  _The Merck Veterinary Manual, p. 137 (PDF p. 178)_ — “sarcoptic mange”

Also valid (keyword match [['sarcoptes', 'scraping'], ['sarcoptic', 'selamectin']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 323, 498, 1026, 1057, 1269); Applied Pharmacology for Veterinary Technicians (PDF p. 211, 222, 271, 273); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 57, 63, 650, 651, 653); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 229, 1665, 1666, 5366); Muller and Kirk's Small Animal Dermatology (PDF p. 112, 480, 484, 488, 1418); Plumb's Veterinary Drug Handbook (PDF p. 3187); Saunders Comprehensive Veterinary Dictionary (PDF p. 1003); Slatter's Fundamentals of Veterinary Ophthalmology (PDF p. 169, 493, 502, 505); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 304, 305)

Reviewer: ☐ OK ☐ Change: ……

## mb-24 · three_book · test

**Q:** How is the mite that causes feline scabies managed in a household, and how widespread is it?

Required books: Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, The Merck Veterinary Manual, Muller and Kirk's Small Animal Dermatology

- Treat all cats on the premises; ivermectin SC two or three times, or one doramectin dose 0.2-0.3 mg/kg.  
  _Muller and Kirk's Small Animal Dermatology, p. 484 (PDF p. 488)_ — “All cats on the premises must be treated”
- Notoedres cati causes notoedric mange in cats.  
  _Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, p. 634 (PDF p. 648)_ — “Notoedres cati”
- Notoedres cati is common in cats throughout the world.  
  _The Merck Veterinary Manual, p. 521 (PDF p. 562)_ — “Notoedres cati is conunon in cats”

Also valid (keyword match [['notoedres', 'cat']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 255, 256, 323, 425, 567); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 1666, 1682); Plumb's Veterinary Drug Handbook (PDF p. 1986, 3187, 3190); Saunders Solutions in Veterinary Practice: Small Animal Dermatology (PDF p. 16, 233, 362); Saunders Comprehensive Veterinary Dictionary (PDF p. 735, 789, 790); Slatter's Fundamentals of Veterinary Ophthalmology (PDF p. 169); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 25, 26, 37, 122, 128); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 113, 115, 304); Small Animal Surgery (Fossum) (PDF p. 365)

Reviewer: ☐ OK ☐ Change: ……

## mb-25 · conflict · dev

**Q:** What meloxicam dose do the books give for cats?

Required books: Applied Pharmacology for Veterinary Technicians, Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Small Animal Surgery (Fossum), The Merck Veterinary Manual

- Applied Pharmacology: 0.3 mg/kg SC one-time; 0.05 mg/kg q24-48h PO chronic.  
  _Applied Pharmacology for Veterinary Technicians, p. 459 (PDF p. 471)_ — “0.3 mg/kg SC one-time injection”
- Merck: 0.1 mg/kg/day for 1-3 days.  
  _The Merck Veterinary Manual, p. 1193 (PDF p. 1234)_ — “cats: 0.1 mg/kg/day”
- Blackwell: 0.2 mg/kg once, 0.05 mg/kg q24h x2 days, then 0.025 mg/kg q24-48h; max 4 days.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 97 (PDF p. 167)_ — “then 0.025 mg/kg q24–48h”
- Fossum: preoperative 0.05-0.1 mg/kg SC.  
  _Small Animal Surgery (Fossum), p. 152 (PDF p. 176)_ — “Cat: 0.05-0.1 mg/kg SC”

Also valid (keyword match [['meloxicam', 'cats', 'mg/kg']]): BSAVA Small Animal Formulary (PDF p. 223, 224, 225); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 804); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 2713, 2765, 2816, 8423); Plumb's Veterinary Drug Handbook (PDF p. 168, 2259, 2262, 2263)

**Conflict:** Initial cat doses range from 0.05 to 0.3 mg/kg and durations from a single dose to chronic use; a good answer shows the different regimens with their books instead of picking one.

Reviewer: ☐ OK ☐ Change: ……

## mb-26 · conflict · test

**Q:** What is a normal Schirmer tear test result?

Required books: Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Ettinger's Textbook of Veterinary Internal Medicine

- Blackwell: normal >= 15 mm/min.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 775 (PDF p. 845)_ — “normal values are ≥15 mm/min”
- Ettinger: dogs 21 +/- 4 mm/min; cats 9-34 mm/min (median 18).  
  _Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 5933_ — “21 +/− 4 mm/min”

Also valid (keyword match [['schirmer', 'mm/min']]): Applied Pharmacology for Veterinary Technicians (PDF p. 352); Slatter's Fundamentals of Veterinary Ophthalmology (PDF p. 52, 53, 88, 426, 459)

**Conflict:** One book gives a single >= 15 mm/min cut-off, the other species-specific ranges (dogs 21 +/- 4; cats 9-34).

Reviewer: ☐ OK ☐ Change: ……

## mb-27 · conflict · test

**Q:** After the puppy series, how often should dogs be revaccinated against parvovirus?

Required books: The Merck Veterinary Manual, Veterinary Vaccination Schedule

- Vaccination Schedule: 6, 10, 14 weeks then yearly.  
  _Veterinary Vaccination Schedule, PDF p. 7_ — “then yearly”
- Merck: 6-8, 10-12, 14-16 wk, booster 1 yr later, then every 3 years.  
  _The Merck Veterinary Manual, p. 376 (PDF p. 417)_ — “and then every 3 yr”

Also valid (keyword match [['parvovirus', 'vaccin', 'every 3'], ['parvo', 'booster', 'yearly'], ['parvovirus', 'revaccinat']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 149, 563, 577, 579); Applied Pharmacology for Veterinary Technicians (PDF p. 364, 365, 384); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 3662, 3976, 4041, 9014, 9015)

**Conflict:** Yearly boosters vs. every 3 years after the 1-year booster.

Reviewer: ☐ OK ☐ Change: ……

## mb-28 · conflict · test

**Q:** How often and how many times should selamectin be applied to treat sarcoptic mange?

Required books: The Merck Veterinary Manual, Saunders Solutions in Veterinary Practice: Small Animal Dermatology

- Saunders: 6-12 mg/kg twice 30 days apart; some apply three times at 14-day intervals.  
  _Saunders Solutions in Veterinary Practice: Small Animal Dermatology, p. 26 (PDF p. 35)_ — “three times at 14-day intervals”
- Merck: monthly ~6 mg/kg topical.  
  _The Merck Veterinary Manual, p. 137 (PDF p. 178)_ — “monthly dosage of -6 mg/kg”

Also valid (keyword match [['selamectin', 'sarcoptic'], ['selamectin', 'scabies']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 323, 498, 1026, 1269); Applied Pharmacology for Veterinary Technicians (PDF p. 222, 265, 271, 273); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 229, 5366); Muller and Kirk's Small Animal Dermatology (PDF p. 428, 432, 434, 487, 518); Plumb's Veterinary Drug Handbook (PDF p. 3187); Slatter's Fundamentals of Veterinary Ophthalmology (PDF p. 169); Small Animal Dermatology: A Color Atlas and Therapeutic Guide (PDF p. 37, 129, 136, 139, 151)

**Conflict:** Two applications 30 days apart (or three at 14 days) vs. monthly application.

Reviewer: ☐ OK ☐ Change: ……

## mb-29 · conflict · test

**Q:** What daily oral meloxicam dose is used in dogs?

Required books: Applied Pharmacology for Veterinary Technicians, Blackwell's Five-Minute Veterinary Consult: Canine and Feline, The Merck Veterinary Manual

- Applied Pharmacology: 0.2 mg/kg initially then 0.1 mg/kg q24h.  
  _Applied Pharmacology for Veterinary Technicians, p. 459 (PDF p. 471)_ — “Dog: 0.2 mg/kg initially PO, then 0.1 mg/kg q24h PO”
- Blackwell (uveitis, dogs): 0.2 mg/kg PO q24h.  
  _Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 99 (PDF p. 169)_ — “Meloxicam 0.2 mg/kg PO q24h”
- Merck: 0.1 mg/kg/day.  
  _The Merck Veterinary Manual, p. 1193 (PDF p. 1234)_ — “dogs: 0.1 mg/kg/day”

Also valid (keyword match [['meloxicam', 'dogs', 'mg/kg']]): BSAVA Small Animal Formulary (PDF p. 223, 224, 225); Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology (PDF p. 804); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 2713, 2765, 2816, 3501, 8423); Plumb's Veterinary Drug Handbook (PDF p. 168, 2259, 2261); Slatter's Fundamentals of Veterinary Ophthalmology (PDF p. 113); Small Animal Surgery (Fossum) (PDF p. 176, 318, 354, 385, 386)

**Conflict:** 0.2 mg/kg q24h ongoing vs 0.2 then 0.1 mg/kg vs 0.1 mg/kg/day.

Reviewer: ☐ OK ☐ Change: ……

## mb-30 · unanswerable · dev

**Q:** What is the dose of bedinvetmab (Librela) for osteoarthritis pain in dogs?

Expected: say the books do not cover it. Absent terms checked across all books: bedinvetmab, librela.

Reviewer: ☐ OK ☐ Change: ……

## mb-31 · unanswerable · test

**Q:** What dose of ilunocitinib (Zenrelia) is recommended for atopic dermatitis in dogs?

Expected: say the books do not cover it. Absent terms checked across all books: ilunocitinib, zenrelia.

Reviewer: ☐ OK ☐ Change: ……

## mb-32 · unanswerable · test

**Q:** How is molidustat (Varenzin) used for anaemia in cats with chronic kidney disease?

Expected: say the books do not cover it. Absent terms checked across all books: molidustat, varenzin.

Reviewer: ☐ OK ☐ Change: ……

## mb-33 · unanswerable · test

**Q:** What tirzepatide dose helps obese cats lose weight?

Expected: say the books do not cover it. Absent terms checked across all books: tirzepatide.

Reviewer: ☐ OK ☐ Change: ……

## mb-34 · unanswerable · test

**Q:** How long does one injection of the 12-month injectable fluralaner protect a dog against fleas and ticks?

Expected: say the books do not cover it. Absent terms checked across all books: fluralaner injectable, bravecto 12, 12-month fluralaner.

Reviewer: ☐ OK ☐ Change: ……

## mb-35 · unanswerable · test

**Q:** What is the dose of the NexGard COMBO (esafoxolaner, eprinomectin, praziquantel) spot-on for cats?

Expected: say the books do not cover it. Absent terms checked across all books: esafoxolaner, nexgard combo.

Reviewer: ☐ OK ☐ Change: ……

## mb-36 · single_book · dev

**Q:** What happens to the darkness of a radiograph when the kVp is raised, and why?

Required books: Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs

- Higher kVp = more penetrating, more transmitted x-rays, darker radiograph.  
  _Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, p. 20 (PDF p. 32)_ — “the higher the kVp, the more transmitted x”

Also valid (keyword match [['kvp', 'darker'], ['kvp', 'density']]): Saunders Comprehensive Veterinary Dictionary (PDF p. 612, 1218)

Reviewer: ☐ OK ☐ Change: ……

## mb-37 · single_book · test

**Q:** What does the term azotemia mean?

Required books: Saunders Comprehensive Veterinary Dictionary

- Azotemia: excess nitrogen-containing compounds in the blood.  
  _Saunders Comprehensive Veterinary Dictionary, p. 105 (PDF p. 125)_ — “an excess of nitrogen-containing compounds in the blood”

Also valid (keyword match [['azotemia', 'nitrogen']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 101, 192, 231, 232, 345); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 1110, 1316, 1321, 1323, 1403); Muller and Kirk's Small Animal Dermatology (PDF p. 404); Small Animal Medical Differential Diagnosis: A Book of Lists (PDF p. 129, 295); Small Animal Surgery (Fossum) (PDF p. 50, 765, 788, 813); The Merck Veterinary Manual (PDF p. 485, 606, 1553, 1557)

Reviewer: ☐ OK ☐ Change: ……

## mb-38 · single_book · test

**Q:** When and how is a breeder chicken flock first vaccinated against Marek's disease?

Required books: Veterinary Vaccination Schedule

- Marek's disease vaccine on day 1 in the hatchery, subcutaneous, 0.2 ml.  
  _Veterinary Vaccination Schedule, PDF p. 1_ — “Day old (1st day) in hatchery Marek”

Also valid (keyword match [['marek', 'day old'], ['marek', 'vaccin']]): Saunders Comprehensive Veterinary Dictionary (PDF p. 476, 699, 1159); The Merck Veterinary Manual (PDF p. 1860, 1863, 2435, 2827, 2890)

Reviewer: ☐ OK ☐ Change: ……

## mb-39 · single_book · test

**Q:** What is nephrogenic diabetes insipidus, and which dog breed has a familial primary form?

Required books: Small Animal Medical Differential Diagnosis: A Book of Lists

- Nephrogenic DI = polyuria from nonresponsiveness to ADH; primary familial form in Huskies.  
  _Small Animal Medical Differential Diagnosis: A Book of Lists, p. 118 (PDF p. 122)_ — “Primary familial (Husky)”

Also valid (keyword match [['nephrogenic diabetes insipidus']]): BSAVA Small Animal Formulary (PDF p. 179); Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 371, 453, 728, 744, 796); Applied Pharmacology for Veterinary Technicians (PDF p. 125); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 1148, 1150, 1160, 1163, 6959); Plumb's Veterinary Drug Handbook (PDF p. 735, 739, 1765, 1769, 1773); Saunders Comprehensive Veterinary Dictionary (PDF p. 965); The Merck Veterinary Manual (PDF p. 582, 592, 691)

Reviewer: ☐ OK ☐ Change: ……

## mb-40 · single_book · test

**Q:** What is a gastropexy and what is it mainly done for?

Required books: Saunders Comprehensive Veterinary Dictionary

- Gastropexy: surgical fixation of the stomach, usually to the abdominal wall, to prevent recurrence of gastric volvulus.  
  _Saunders Comprehensive Veterinary Dictionary, p. 474 (PDF p. 494)_ — “surgical ﬁxation of the stomach”

Also valid (keyword match [['gastropexy', 'volvulus']]): Blackwell's Five-Minute Veterinary Consult: Canine and Feline (PDF p. 602, 603, 604, 618, 1322); Ettinger's Textbook of Veterinary Internal Medicine (PDF p. 6167, 6168, 6179, 6334); Small Animal Surgery (Fossum) (PDF p. 498, 501, 517, 521, 525); The Merck Veterinary Manual (PDF p. 2425)

Reviewer: ☐ OK ☐ Change: ……

