# All 17 books (multi-book test set): AI-generated answers vs. book answers — gpt-5-mini

40 questions written from the 17 indexed books (paraphrased, never shown to the answering model). The "Book answer" lists the key facts from the answer key, each with the book and page it comes from (see `eval/multibook/questions_review.md`). The "AI answer" and "Citation(s)" were produced by the VetAI pipeline (retrieve -> synthesize -> verify -> generate) with `openai:gpt-5-mini`, over the full 17-book index (exact retrieval, top-6 passages, max 2 per book). "Score" is from two blind judges (gpt-5-mini and gpt-5.5); note gpt-5-mini is also the answering model here.

Question types: needs 2 books (14), needs 3 books (10), books disagree (5), not in the books (6), single book (5). Split: dev = used to choose settings, test = held out.

**1. A dog has drunk antifreeze. What antidote regimen is given, and what urine crystal finding supports the diagnosis?**
_[needs 2 books · dev · mb-01]_

**Book answer:** Fomepizole for ethylene glycol in dogs: 20 mg/kg IV load, 15 mg/kg IV at 12 h, 15 mg/kg at 24 h, 5 mg/kg at 36 h. (Plumb's Veterinary Drug Handbook, p. 1596) Calcium oxalate (monohydrate, dumb-bell shaped) crystals are associated with ethylene glycol toxicity. (The Merck Veterinary Manual, p. 1618)

**AI answer:** Antidote regimen
- Primary antidote: 4‑methylpyrazole (fomepizole) — it prevents metabolism of ethylene glycol by effectively inactivating alcohol dehydrogenase in dogs, preventing formation of oxalic acid and its renal toxicity. [1]
- Alternative antidote: IV ethanol is given to competitively inhibit alcohol dehydrogenase. [1]
- Triage/setting: dogs are usually managed as outpatients if presentation is < 5 hours post‑ingestion and treated with fomepizole; dogs presenting > 5 hours are usually managed as inpatients for intravenous fluids to correct dehydration, increase tissue perfusion, and promote diuresis. [2]

Urine/kidney findings that support the diagnosis
- Cytologic examination of kidney imprints is often diagnostic; numerous calcium oxalate crystals are found. [2]
- Calcium oxalate crystalluria may be observed in dogs as early as 6 hours after ingestion, and calcium oxalate monohydrate crystals are more common than dihydrate. [3]
- An unusual form associated with ethylene glycol toxicity is small, flat, colorless crystals shaped like “picket fence posts,” found in neutral to acidic urine. [4]

What is not covered by the provided evidence
- Specific dosing, administration schedules, duration of treatment, and monitoring parameters for fomepizole or ethanol are not provided in the cited claims.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 300. Acute Kidney Injury, PDF pp. 7515–7516; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Ethylene Glycol Toxicosis, pp. 468–469; [3] The Merck Veterinary Manual, Toxicology, pp. 3047–3048; [4] The Merck Veterinary Manual, Clinical Pathology and Procedures, pp. 1618–1619

**Score:** gpt-5-mini judge 3/5, facts 50% · gpt-5.5 judge 2/5, facts 50% — The answer identifies fomepizole as the antidote and mentions calcium oxalate/monohydrate crystalluria, but it omits the required fomepizole dosing regimen and does not give the expected dumb-bell crystal morphology.

**2. When ivermectin is used for canine demodicosis, how should it be given to work, and which breeds need special caution?**
_[needs 2 books · test · mb-02]_

**Book answer:** Weekly protocols used for other ectoparasites were not effective for Demodex; daily oral ivermectin can be effective. (Muller and Kirk's Small Animal Dermatology, p. 429) Caution in ABCB1 (MDR1) mutation breeds: Collies, Australian Shepherds, Shelties, Long-haired Whippets - higher CNS toxicity risk. (Plumb's Veterinary Drug Handbook, p. 1977)

**AI answer:** How to give ivermectin for canine generalized demodicosis
- Ivermectin 0.2–0.6 mg/kg PO every 24 hours is often effective for generalized demodicosis. [1]
- An initial ramp‑up can be used: ivermectin 0.1 mg/kg PO on day 1, then 0.2 mg/kg PO on day 2, with oral daily increments of 0.1 mg/kg until 0.2–0.6 mg/kg/day is being administered. [1]
- To identify ivermectin‑sensitive individuals, one option is to administer 120 μg/kg q24h for the first 3 days. [2] An alternative gradual increase schedule is 0.05 mg/kg day 1, 0.1 mg/kg day 2, 0.15 mg/kg day 3, 0.2 mg/kg day 4, 0.3 mg/kg day 5, with continued 0.1 mg/kg daily increases as needed to a maximum of 0.6 mg/kg q24h. [2][3]

Breeds requiring special caution
- Breeds contraindicated or requiring special caution include collies, Shetland sheepdogs, Australian shepherds, Old English sheepdogs, white German shepherds, long‑haired whippets, greyhounds, silken windhounds, other herding breeds, and crosses with these breeds. [2]
- Breeds widely reported to be sensitive to high‑dose ivermectin include the collie, Old English sheepdog, Australian shepherd, Shetland sheepdog, and crosses thereof. [4]

Limitations of the provided evidence
- The cited claims do not provide information on treatment duration, monitoring protocols, adverse effects, safety in individual animals, or alternative treatments.

**Citation(s):** [1] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 5 Parasitic Skin Disorders, p. 105; [2] Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, 19 Demodicosis (Canine and Feline) › Drugs of Choice: Dogs, p. 301; [3] Muller and Kirk's Small Animal Dermatology, Chapter 6 - Parasitic Skin Disease, pp. 428–429; [4] Muller and Kirk's Small Animal Dermatology, Chapter 6 - Parasitic Skin Disease, pp. 428–429

**Score:** gpt-5-mini judge 3/5, facts 75% · gpt-5.5 judge 4/5, facts 50% — The answer correctly states that ivermectin must be given orally once daily and lists the key caution breeds, including collies, Australian shepherds, Shelties, and long-haired whippets. It omits the specific point that weekly ectoparasite protocols are ineffective for Demodex and does not explicitly tie the breed caution to ABCB1/MDR1-related CNS toxicity.

**3. At what ages is a puppy vaccinated against parvovirus in the suggested schedule, and which drugs support a puppy already sick with parvo?**
_[needs 2 books · test · mb-03]_

**Book answer:** Parvovirus: live attenuated vaccine at 6 weeks, then 10 and 14 weeks, subcutaneous. (Veterinary Vaccination Schedule, PDF p. 7) Supportive drugs: parenteral ampicillin + gentamicin, antiemetics such as ondansetron or maropitant; gentamicin can harm the kidneys of dehydrated puppies. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 217)

**AI answer:** Vaccination schedule (parvovirus)

- Start a puppy series at about 4–6 weeks of age, given as 3 injections about a month apart. [1]  
- A commonly used schedule is 6, 9, and 12 weeks of age. [2]  
- If using a modified-live parvovirus vaccine, give 1 dose every 2–4 weeks starting at ≥6 weeks until at least 16 weeks of age. [3]  
- Puppies should be vaccinated every 2–4 weeks with CDV, CAV-2 and CPV-2 vaccines up to 16 weeks of age. [4]  
- The final vaccine (usually given at about 14–18 weeks) is most likely to be protective; the most important dose is at ≥16 weeks when maternal antibody interference is usually lost. [1][4]

Supportive drugs and therapies for a puppy with parvovirus

- Core supportive therapies: intravenous fluids, antibiotics, antiemetics and analgesics. [2]  
- IV fluid supplements commonly used: potassium chloride and 5% dextrose; sodium bicarbonate may be added if there is severe metabolic acidosis. [2]  
- Parenteral antibiotics recommended (examples): ampicillin and gentamicin. [5]  
- Antiemetics recommended (examples): ondansetron and maropitant. [5]  
- Note: gentamicin can cause renal toxicity in dehydrated puppies. [5]  
- Early enteral nutrition via a nasoesophageal tube (compared with nil per os until vomiting ceases) is associated with earlier clinical improvement, significant weight gain, and improved gut barrier function. [2]

Limits of the provided evidence

- These claims name vaccines, timing ranges, supportive drug classes and examples, and some adjunctive measures, but they do not provide specific drug doses, detailed administration protocols, fluid rates, or full treatment algorithms.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 201. Canine and Feline Parvovirus Infection, PDF pp. 4044–4046; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Canine Parvovirus Infection, pp. 216–217; [3] Applied Pharmacology for Veterinary Technicians, 17 - Immunologic Drugs › VACCINE FAILURE, pp. 351–353; [4] Ettinger's Textbook of Veterinary Internal Medicine, 185. Companion Animal Vaccinations, PDF pp. 3658–3659; [5] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Canine Parvovirus Infection, p. 217

**Score:** gpt-5-mini judge 4/5, facts 75% · gpt-5.5 judge 4/5, facts 75% — The treatment/supportive drug portion matches the key, including ampicillin plus gentamicin, ondansetron or maropitant, and the renal risk of gentamicin in dehydrated puppies. The vaccination answer is only partial because it does not clearly give the required suggested schedule of live attenuated vaccine at 6, 10, and 14 weeks subcutaneously, and instead gives several alternative schedules.

**4. For suspected free air in the chest, which radiographic view makes it easier to see and what does auscultation typically reveal?**
_[needs 2 books · dev · mb-04]_

**Book answer:** Pleural gas rises dorsally in ventral recumbency, so it is easier to detect on a DV view than a VD view. (Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, p. 161) Pneumothorax: lung sounds are absent over the dorsal lateral chest wall. (Small Animal Surgery (Fossum), p. 739)

**AI answer:** - Radiography: a right lateral horizontal‑beam radiographic view yields the highest rate of detection and severity gradation for pneumothorax; VD/DV views have the lowest rate of detection. [1]  
- Small volumes of intrathoracic gas can be detected using horizontal‑beam radiography. [2]  
- Auscultation: typically decreased to absent breath/lung sounds dorsally, i.e. muffled lung sounds over the affected regions. [1][3][4]

The provided evidence does not give numerical sensitivity/specificity, detailed positioning or technique beyond “horizontal‑beam,” nor management recommendations.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Pneumothorax, p. 1075; [2] Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, Chapter 3 Thorax › Radiographic views of the thorax, pp. 140–141; [3] The Merck Veterinary Manual, Emergency Medicine and Critical Care, pp. 1663–1664; [4] Ettinger's Textbook of Veterinary Internal Medicine, 37. Tachypnea, Dyspnea and Respiratory Distress, PDF pp. 898–899

**Score:** gpt-5-mini judge 3/5, facts 50% · gpt-5.5 judge 2/5, facts 25% — The answer gives a different radiographic recommendation than the required DV-over-VD point and even groups VD/DV as low detection, so it fails the key radiographic fact. It is partly correct on auscultation by noting decreased to absent dorsal lung sounds, but it is less specific than absent sounds over the dorsolateral chest wall.

**5. In glaucoma management, what pressure value guides whether to keep going with medical treatment or move to surgery, and which oral agent can lower pressure quickly in an emergency?**
_[needs 2 books · test · mb-05]_

**Book answer:** If IOP stays below 20 mm Hg continue medical treatment; above 20 mm Hg consider surgery. (Slatter's Fundamentals of Veterinary Ophthalmology, p. 298) Oral glycerin is used for short-term IOP reduction in acute glaucoma; its effect is more variable than mannitol. (Plumb's Veterinary Drug Handbook, p. 1688)

**AI answer:** Target IOP threshold: continue medical treatment if IOP is < 20 mm Hg; proceed to surgery if IOP is > 20 mm Hg. [1]

Emergency oral agent: oral glycerin, 1–2 mL/kg, is cited as an alternative to mannitol and is occasionally dispensed for the owner to administer to treat a sudden attack of glaucoma. [1][2]

What is not covered by these statements: timing and speed of pressure reduction, contraindications, administration technique or monitoring, comparative efficacy versus other agents, and surgical details are not provided in the cited evidence.

**Citation(s):** [1] Slatter's Fundamentals of Veterinary Ophthalmology, 12 The Glaucomas › Emergency Treatment of Acute Glaucoma, pp. 297–298; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Glaucoma, pp. 551–552

**Score:** gpt-5-mini judge 3/5, facts 75% · gpt-5.5 judge 4/5, facts 75% — The answer correctly gives the 20 mm Hg threshold for continuing medical therapy versus surgery and identifies oral glycerin for acute/emergency glaucoma. It omits the key comparative point that glycerin's effect is more variable than mannitol.

**6. How is dry eye confirmed with a tear test, and what kind of drug is commonly used to treat immune-mediated eye disease such as this?**
_[needs 2 books · test · mb-06]_

**Book answer:** Schirmer tear test: normal >= 15 mm/min; < 15 mm/min suggests KCS (interpret with breed). (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 775) Cyclosporine is a potent immunosuppressive used often for immune-mediated ocular disease. (Slatter's Fundamentals of Veterinary Ophthalmology, p. 72)

**AI answer:** Diagnosis
- Dry eye is confirmed by a Schirmer tear test: decreased results are diagnostic; normal value (dogs): at least 15 mm/min of wetting; symptomatic patients: usually < 10 mm/min of wetting. [1]

Etiology and treatment class
- Immune-mediated causes are the most common cause of KCS. [3]
- A commonly used drug class for immune‑mediated dry eye is topical cyclosporine ophthalmic ointment (e.g., Optimmune®), which acts as a lacrimostimulant and an immunomodulating agent for management of dry eye (KCS). [1][2]

Limitations of the provided evidence
- The supplied claims do not provide dosing, frequency, treatment protocols, monitoring, alternative therapies, or other diagnostic tests.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Keratoconjunctivitis Sicca, p. 779; [2] Plumb's Veterinary Drug Handbook, Appendix › Cyclosporine, pp. 3784–3785; [3] Applied Pharmacology for Veterinary Technicians, 16 - Blood-Modifying, Antineoplastic, and Immunosuppressant Drugs › Cyclophosphamide, pp. 340–341

**Score:** gpt-5-mini judge 5/5, facts 100% · gpt-5.5 judge 4/5, facts 75% — The answer gives the Schirmer tear test and the normal value of at least 15 mm/min, but it does not explicitly state that values below 15 mm/min suggest KCS or mention breed interpretation. It correctly identifies cyclosporine as a commonly used immunomodulating/immunosuppressive ocular treatment.

**7. In a dog in anaphylactic shock, what epinephrine dose is suggested and why does epinephrine help?**
_[needs 2 books · test · mb-07]_

**Book answer:** Epinephrine 1:1,000 at 0.01 mL/kg parenterally for anaphylactic shock. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 76) Epinephrine reverses the hypotension and bronchoconstriction of anaphylactic shock. (Applied Pharmacology for Veterinary Technicians, p. 77)

**AI answer:** Suggested dose
- For anaphylaxis: 0.01–0.02 mg/kg IV; or the dosage may be doubled and given via the endotracheal tube if IV line is not yet established; in less severe cases, may be given IM or SC. [1]  
- For life‑threatening bronchoconstriction the same effective bronchospasm dose is 20 micrograms/kg (0.02 mg/kg) IV, IM, SC, or IT. [1]

Why epinephrine helps
- Epinephrine decreases mediator release from mast cells and basophils, helping to interrupt the allergic cascade. [2]  
- It produces vasoconstriction, which supports blood pressure in shock. [2]  
- It provides positive inotropy and chronotropy, supporting cardiac output. [2]  
- It causes bronchodilation and decreases mucosal edema, which assists with upper airway obstruction. [2]  
- Epinephrine is therefore reserved for emergency treatment of life‑threatening bronchoconstriction (eg, anaphylaxis). [3]

Limitations of the provided evidence
- The provided claims do not address dosing intervals or repeat doses, preparation/dilution, maximum cumulative dose, monitoring, contraindications, species‑specific adjustments beyond the stated doses, or adjunctive/supportive therapies.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Epinephrine, pp. 1354–1355; [2] Ettinger's Textbook of Veterinary Internal Medicine, 129. Anaphylaxis, PDF pp. 2608–2609; [3] The Merck Veterinary Manual, Pharmacology, p. 2610

**Score:** gpt-5-mini judge 5/5, facts 100% · gpt-5.5 judge 4/5, facts 75% — The answer includes the equivalent 0.01 mg/kg dose but does not give the requested 1:1,000 concentration as 0.01 mL/kg and adds a higher dose range. It correctly explains that epinephrine supports blood pressure and causes bronchodilation, matching reversal of hypotension and bronchoconstriction.

**8. How common is pancreatitis among pancreatic diseases of dogs and cats, and which specific blood test is listed for it?**
_[needs 2 books · dev · mb-08]_

**Book answer:** Pancreatitis is the most common exocrine pancreatic disease in dogs and cats; it may be acute or chronic. (The Merck Veterinary Manual, p. 407) Spec cPL is the test listed for pancreatitis. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 395)

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source."

**Citation(s):** none (no claim cleared the verification gate)

**Score:** gpt-5-mini judge 1/5, facts 0% · gpt-5.5 judge 1/5, facts 0% — The candidate declined to answer and provided none of the required book facts. It did not state that pancreatitis is the most common exocrine pancreatic disease in dogs and cats or identify Spec cPL as the listed test.

**9. How is chronic kidney disease staged in dogs and cats, and what urine protein:creatinine range counts as borderline proteinuria in each species?**
_[needs 2 books · test · mb-09]_

**Book answer:** IRIS stages 1-4 use two or more fasting, well-hydrated serum creatinine values over several weeks; CKD = present > 3 months. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 1164) IRIS proteinuria substage 'borderline': UPC 0.2-0.5 in dogs, 0.2-0.4 in cats. (The Merck Veterinary Manual, p. 1513)

**AI answer:** Summary
- IRIS staging for chronic kidney disease in dogs and cats is a four‑tier system based on renal function (serum creatinine). [1]

Staging by serum creatinine
- Stage I: Creatinine <1.4 mg/dL (dogs) and <1.6 mg/dL (cats). [1]  
- Stage II: Creatinine 1.4–2.8 mg/dL (dogs) and 1.6–2.8 mg/dL (cats). [1]  
- Stage III: Creatinine 2.9–5.0 mg/dL (dogs and cats). [1]  
- Stage IV (Severe renal azotemia): Creatinine >5.0 mg/dL (dogs and cats). [2]  
- Staging should be based on a minimum of two results obtained several weeks apart when the patient is fasted and well hydrated. [1]

Urine protein:creatinine (UP:C)
- Borderline proteinuria: UP:C 0.2–0.4 in cats and 0.2–0.5 in dogs. [3]  
- Proteinuria is defined as UP:C ≥0.4 in cats or ≥0.5 in dogs. [3]

Notes on scope of evidence
- The provided evidence specifies staging by serum creatinine, the requirement for repeated measurements, and the UP:C ranges for borderline proteinuria and proteinuria; it does not provide additional staging details (e.g., substaging criteria) or management recommendations.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 301. Chronic Kidney Disease, PDF pp. 7564–7565; [2] The Merck Veterinary Manual, Urinary System, pp. 1512–1513; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Proteinuria, p. 1116

**Score:** gpt-5-mini judge 3/5, facts 75% · gpt-5.5 judge 4/5, facts 75% — The answer correctly gives the IRIS borderline UPC ranges for dogs and cats and states staging requires at least two fasting, well-hydrated creatinine measurements several weeks apart. It omits the requirement that CKD be present for more than 3 months and includes a minor erroneous threshold statement for proteinuria.

**10. How is primidone related to phenobarbital, and what organ toxicity is a concern with both drugs?**
_[needs 2 books · test · mb-10]_

**Book answer:** Primidone (Mysoline) is converted to phenobarbitone (phenobarbital). (BSAVA Small Animal Formulary, p. 286) Hepatotoxicity is an adverse effect of phenobarbital and primidone. (Applied Pharmacology for Veterinary Technicians, p. 86)

**AI answer:** Relationship
- Primidone is rapidly metabolized to phenobarbital and phenylethylmalonamide (PEMA). [1][2]
- In dogs, about 85% of primidone’s antiseizure activity is attributed to the phenobarbital metabolite. [1][2]
- The conversion rate in dogs is approximately 4:1; for example, a 250 mg dose of primidone is approximately equivalent to 60 mg of phenobarbital. [3]

Organ toxicity concern
- Hepatic injury/toxicity is a concern with both primidone and phenobarbital. [1][2][3][4]
- Chronic therapy can cause increases in liver enzymes and decreased serum albumin. [1][2][3][4]
- Pathologic changes reported after ~6 months include hepatic lipidosis, hepatocellular hypertrophy and necrosis. [1][2][3][4]
- Serious hepatic injury probably occurs in approximately 6–14% of dogs treated. [1][2][3][4]

**Citation(s):** [1] BSAVA Small Animal Formulary, DRUG LISTINGS, p. 285; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Appendices › Appendix IX, p. 1526; [3] Plumb's Veterinary Drug Handbook, Systemic Monographs › Primidone, pp. 2997–2998; [4] Plumb's Veterinary Drug Handbook, Systemic Monographs › Primidone, pp. 2998–2999

**Score:** gpt-5-mini judge 5/5, facts 100% · gpt-5.5 judge 5/5, facts 100% — The answer directly states that primidone is metabolized/converted to phenobarbital and identifies hepatic toxicity/injury as a concern with both primidone and phenobarbital. Extra details do not contradict the required facts.

**11. Which skin changes point to Cushing's syndrome, including the ones typical in cats, and which dexamethasone dose is used for the suppression test in cats?**
_[needs 2 books · test · mb-11]_

**Book answer:** Cushing's: truncal alopecia, comedones, rat tail, thin skin, phlebectasia, potbelly; in cats curled pinnal tips and skin fragility. (Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, p. 60) LDDS is the test of choice for feline HAC and uses 0.1 mg/kg IV dexamethasone, higher than in dogs. (Plumb's Veterinary Drug Handbook, p. 1062)

**AI answer:** Skin changes that point to Cushing’s syndrome in cats

- Fragile (bruising, tearing, thin) skin is a sign of feline hyperadrenocorticism. [1][2]  
- Bruising and ulceration (torn skin) can occur in cats with iatrogenic hyperglucocorticoidism. [2]  
- Hair loss (alopecia), hyperpigmentation, and absence of primary hairs are seen in cats with hyperadrenocorticism. [1][2]  
- Profound hair loss and hyperpigmentation occur in affected cats. [2]  
- Perineal hair loss and vulvar enlargement have been reported. [2]  
- The most consistent histologic abnormality is a decreased quantity of dermal collagen; bundles in the superficial and deep dermis are thinner than normal, widely separated, and without normal organization. [2]  
- On electron microscopy, collagen fibril diameters vary in size. [2]  
- Cats with hyperadrenocorticism often have hyperfragility of the skin and are often presented late in the course of disease. [3]

Low‑dose dexamethasone suppression testing in cats

- A low‑dose dexamethasone suppression test (LDDST) protocol used in cats is 0.1 mg/kg dexamethasone IV or IM with serum/plasma samples obtained before and at 4 and 8 hours after injection for cortisol assay. [4][5]  
- Suggested dexamethasone dosages for suppression testing in cats vary from 0.01 to 0.1 mg/kg; because upward of 20% of normal cats do not show adrenal suppression when 0.01 mg/kg is given, some authors suggest using 0.1 mg/kg for low‑dose testing. [3]

Limitations of the provided evidence
- The supplied claims do not provide guidance on interpretation thresholds, diagnostic sensitivity or specificity, alternative diagnostic tests, or treatment/management.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hyperadrenocorticism (Cushing’s Syndrome)—Cats, p. 649; [2] Muller and Kirk's Small Animal Dermatology, Chapter 10 - Endocrine and Metabolic Diseases, pp. 816–818; [3] Muller and Kirk's Small Animal Dermatology, Chapter 10 - Endocrine and Metabolic Diseases, p. 818; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Appendices › Appendix I, pp. 1418–1419; [5] Ettinger's Textbook of Veterinary Internal Medicine, 294. Feline Hyperadrenocorticism, PDF pp. 7355–7356

**Score:** gpt-5-mini judge 3/5, facts 75% · gpt-5.5 judge 3/5, facts 50% — The answer includes feline skin fragility/thin skin and alopecia, but omits several key Cushingoid skin changes such as comedones, rat tail, phlebectasia, potbelly, and curled pinnal tips. It gives the 0.1 mg/kg dexamethasone dose but does not clearly state LDDS is the feline test of choice, that the route is IV, or that this is higher than the dog dose.

**12. Against which parasites is selamectin indicated in dogs and cats, and how often is it applied for prevention?**
_[needs 2 books · dev · mb-12]_

**Book answer:** Selamectin is applied topically monthly at ~6 mg/kg; kills fleas and treats Otodectes and sarcoptic mange. (The Merck Veterinary Manual, p. 137) Selamectin is used for fleas, ear mites (Otodectes), sarcoptic mange, lice, roundworms and heartworm prevention in dogs. (BSAVA Small Animal Formulary, p. 305)

**AI answer:** Indications

- Prevention of heartworm disease — dogs and cats. [1][2][3]  
- Flea control (kills adult fleas and prevents flea eggs from hatching) — dogs and cats. [2][3]  
- Treatment and control of ear mites (Otodectes cynotis) — dogs and cats. [1][2]  
- Treatment and control of sarcoptic mange (Sarcoptes) — dogs. [2][4]  
- Treatment and control of Dermacentor variabilis infestations (ticks) — dogs. [2][3]  
- Treatment of feline intestinal nematodes: hookworm (Ancylostoma tubaeforme) and roundworm (Toxocara cati) — cats. [1][2]

Application frequency for prevention

- For ticks, dosing is monthly; if heavy infestations, a repeat dose may be given 2 weeks after the first dose. [4]

What is not covered by the provided evidence

- The claims supplied do not state a routine application interval for prevention of heartworm, for routine flea control, for ear‑mite treatment, for sarcoptic mange, or for treatment/prevention of the feline intestinal worms.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 13 - Antiparasitic Drugs › Insecticides, p. 264; [2] The Merck Veterinary Manual, Circulatory System, pp. 136–137; [3] Muller and Kirk's Small Animal Dermatology, Chapter 6 - Parasitic Skin Disease, pp. 429–430; [4] Plumb's Veterinary Drug Handbook, Systemic Monographs › Selamectin, pp. 3189–3190

**Score:** gpt-5-mini judge 3/5, facts 50% · gpt-5.5 judge 3/5, facts 50% — The candidate lists several correct indications, including fleas, ear mites, sarcoptic mange, and heartworm prevention, but omits topical monthly dosing at about 6 mg/kg and misses lice and dog roundworms. It also gives the monthly interval only for ticks rather than for selamectin prevention generally.

**13. How should a kennel be disinfected after a parvovirus case, and which antiemetic drugs can be used for the affected puppies?**
_[needs 2 books · test · mb-13]_

**Book answer:** Clean organic matter, then disinfect with dilute bleach (1:30) or peroxygen / accelerated hydrogen peroxide products. (The Merck Veterinary Manual, p. 376) Antiemetics for parvovirus: ondansetron, maropitant. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 217)

**AI answer:** Kennel disinfection — practical points from the evidence
- Proper, strict isolation procedures and strict sanitation are essential after CPV-2 cases. [1]
- A 1:30 dilution of bleach (5% sodium hypochlorite) destroys CPV-2 in a few minutes. [1]
- Household bleach diluted 1:30 and left on a surface for 30 minutes is an effective decontaminating agent. [2]
- Steam cleaning is also effective for decontamination. [2]
- Maintain good hygiene and limit contact with other animals until after the vaccination program is complete. [2]

Antiemetic options for affected puppies (evidence-based)
- Metoclopramide, ondansetron and maropitant appear to be equally effective antiemetics. [3]
- Ondansetron and maropitant are specifically recommended as additional antiemetics. [4]
- In CPV enteritis, maropitant 1 mg/kg/day IV and ondansetron 0.5 mg/kg IV tid appear equally effective at controlling vomiting; maropitant may be associated with improved ability to maintain body weight during illness. [5]
- Metoclopramide dosing reported: 0.3 mg/kg PO or SC tid, or 1–2 mg/kg/day as a constant-rate infusion; metoclopramide may increase the risk of intussusception and should be restricted to dogs that are rehydrated and being appropriately monitored. [5]
- Adrenergic antagonists (e.g., prochlorperazine 0.1–0.5 mg/kg SC tid) can worsen hypotension in hypovolemic animals. [5]
- Note: vomiting may persist despite antiemetic administration. [5]

Limitations of the provided evidence
- The claims address bleach dilution/contact time, steam cleaning, isolation/hygiene, and the antiemetics listed above, but do not provide step‑by‑step cleaning protocols for different materials, PPE recommendations, waste/bedding handling, exact duration of isolation, or other supportive therapies (fluid therapy, nutrition, vaccination schedules). These items are not covered by the supplied evidence.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Canine Parvovirus Infection, pp. 216–217; [2] Ettinger's Textbook of Veterinary Internal Medicine, 201. Canine and Feline Parvovirus Infection, PDF pp. 4046–4047; [3] Ettinger's Textbook of Veterinary Internal Medicine, 201. Canine and Feline Parvovirus Infection, PDF pp. 4038–4039; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Canine Parvovirus Infection, p. 217; [5] The Merck Veterinary Manual, Circulatory System, pp. 375–376

**Score:** gpt-5-mini judge 4/5, facts 75% · gpt-5.5 judge 4/5, facts 75% — The answer correctly identifies 1:30 bleach disinfection and the key antiemetics ondansetron and maropitant. It is incomplete on kennel disinfection because it does not state that organic matter should be cleaned first or mention peroxygen/accelerated hydrogen peroxide products.

**14. Why can a single injection of meloxicam be risky in an anaesthetised animal or one with liver disease, and how is the drug handled by the body?**
_[needs 2 books · test · mb-14]_

**Book answer:** Delay meloxicam if anaesthetic hypotension is expected (renal perfusion); liver disease prolongs metabolism and risks accumulation. (BSAVA Small Animal Formulary, p. 206) In dogs meloxicam is well absorbed, peaks at 7-8 h, ~97% protein bound and extensively metabolised in the liver. (Plumb's Veterinary Drug Handbook, p. 2259)

**AI answer:** Summary answer

Risk in anaesthetised animals
- All NSAIDs can adversely affect renal perfusion during periods of hypotension, so they should be administered cautiously in the peri‑operative period. [1]
- If hypotension during anaesthesia is anticipated, meloxicam should be delayed until the animal is fully recovered from anaesthesia and normotensive. [1]
- Do not give meloxicam to dehydrated, hypovolaemic or hypotensive patients, or to animals with GI disease or blood clotting problems. [2]
- Administration to animals with renal disease requires careful evaluation and is not advisable in the peri‑operative period. [2]

Risk in animals with liver disease
- Liver disease will prolong the metabolism of meloxicam, which can lead to potential drug accumulation and overdose with repeated dosing. [1]
- The provided evidence does not specify the magnitude of risk from a single injection in animals with liver disease. (Not covered by the supplied claims.)

How the drug is handled (pharmacokinetic points supported by the evidence)
- Meloxicam has a duration of action of approximately 24–48 hours in most species. [3]
- Most NSAIDs are excreted in milk; use cautiously in lactating animals. [4]

What is not covered by the supplied evidence
- The claims do not provide specific pharmacokinetic parameters (e.g., clearance values or half‑life in particular species), quantitative risk estimates for a single injection, or management steps beyond the stated cautions.

**Citation(s):** [1] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 205–206; [2] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 206–207; [3] Plumb's Veterinary Drug Handbook, Systemic Monographs › Meloxicam, pp. 2264–2265; [4] Plumb's Veterinary Drug Handbook, Systemic Monographs › Meloxicam, pp. 2260–2261

**Score:** gpt-5-mini judge 3/5, facts 75% · gpt-5.5 judge 3/5, facts 75% — The answer correctly explains the anaesthetic hypotension/renal perfusion concern and the liver disease accumulation concern. However, it omits most of the required pharmacokinetic handling details in dogs, including good absorption, 7-8 h peak, and ~97% protein binding, despite suggesting such parameters were not available.

**15. What are the main mechanisms behind increased thirst and urination in dogs, and which diseases cause the kidneys to stop responding to ADH?**
_[needs 3 books · dev · mb-15]_

**Book answer:** PU results from excess water intake (primary polydipsia) or reduced urine concentrating ability (primary polyuria). (Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 1149) Secondary nephrogenic DI causes: renal failure, hyperadrenocorticism, hypoadrenocorticism, hepatic insufficiency, pyometra, hypercalcemia, hypokalemia ... (Small Animal Medical Differential Diagnosis: A Book of Lists, p. 118) Primary PU from impaired renal response to ADH: renal failure, HAC (dogs), hyperthyroidism (cats). (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 1094)

**AI answer:** Summary — mechanisms
- Antidiuretic (vasoactive) peptide (AVP, antidiuretic hormone) is the main hormone responsible for water homeostasis, acting in renal collecting ducts to increase cell permeability to water. [1]
- Volumes of urine produced and water consumed are controlled by interactions between the kidneys, pituitary gland, and hypothalamus, with plasma osmolality as the primary monitored parameter. [3]
- Polyuria (PU) results either from excessive water intake (primary polydipsia) or from decreased urinary‑concentrating ability (primary polyuria). [2]
- PU may occur when the quantity of functional AVP synthesized in the hypothalamus or released from the posterior pituitary is limited, or when the kidneys fail to respond normally to AVP. [3]
- Polydipsia (PD) results when the thirst center in the anterior hypothalamus is stimulated; in most patients PD is a compensatory response to PU and serves to maintain hydration. [3]

Mechanistic categories relevant in dogs
- Central diabetes insipidus (AVP deficiency): complete or partial deficiencies of AVP (central DI) produce PU/PD and can result from neoplasia, inflammation, trauma, or developmental defects. [1]
- Nephrogenic diabetes insipidus (renal resistance): a complete or partial inability of the kidneys to respond to AVP (NDI); primary NDI is a rare hereditary disorder, while secondary NDI is caused by several diseases or drugs. [1]

Diseases and conditions reported to cause impaired renal response to ADH (secondary NDI)
- Listed causes include renal failure, hyperadrenocorticism (dogs), hyperthyroidism (cats), pyelonephritis, leptospirosis, pyometra, hepatic failure, hypercalcemia, hypokalemia, renal medullary solute washout, dietary protein restriction, and drugs. [4]
- Additional causes compiled in Ettinger’s Box 53.1 include secondary NDI, hyperadrenocorticism, hypercalcemia, liver disease, hyperthyroidism, pyometra/Escherichia coli endotoxemia, pyelonephritis, hypokalemia, hypersomatotropism, leptospirosis, drug administration (e.g., glucocorticoids, phenobarbital), osmotic diuresis, diabetes mellitus, post‑obstructive diuresis, chronic kidney disease and renal medullary washout. [2]

What is not covered here
- The verified claims do not provide diagnostic testing protocols, relative frequencies/prognosis, or treatment recommendations.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 53. Polyuria and Polydipsia, PDF pp. 1150–1152; [2] Ettinger's Textbook of Veterinary Internal Medicine, 53. Polyuria and Polydipsia, PDF pp. 1148–1150; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Polyuria and Polydipsia, p. 1094; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Polyuria and Polydipsia, p. 1095

**Score:** gpt-5-mini judge 3/5, facts 83% · gpt-5.5 judge 4/5, facts 83% — The answer correctly states the two main mechanisms for PU/PD and identifies key diseases causing impaired renal response to ADH, including renal failure, HAC in dogs, and hyperthyroidism in cats. It omits hypoadrenocorticism from the secondary nephrogenic DI causes and has a minor terminology error for AVP.

**16. A cat has inflammation inside the front of the eye. Which systemic infections should be ruled out, and what anti-inflammatory regimen can be given by mouth or injection?**
_[needs 3 books · test · mb-16]_

**Book answer:** Feline uveitis causes: FeLV, FIV, FIP, Toxoplasma gondii, systemic fungi, neoplasia; Bartonella role debated. (Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 549) Meloxicam 0.2 mg/kg once, then 0.05 mg/kg q24h for 2 days, then 0.025 mg/kg; limit to 4 days (renal risk). (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 97) Infectious causes listed include FIV, FIP (feline coronavirus), FeLV. (Slatter's Fundamentals of Veterinary Ophthalmology, p. 379)

**AI answer:** Infectious causes to rule out
- Consider systemic Coronavirus (feline infectious peritonitis) as a cause of uveitis in cats. [1]
- Consider systemic Feline leukemia virus as a cause of uveitis in cats. [1]
- Consider systemic Feline immunodeficiency virus as a cause of uveitis in cats. [1]
- Consider systemic Feline herpesvirus 1 as a cause of uveitis in cats. [1]
- Consider systemic fungal infections such as Histoplasma capsulatum as a cause of uveitis in cats. [1]
- Consider systemic Encephalitozoon cuniculi as a cause of uveitis in cats. [1]
- Consider parasitic causes (e.g., Toxocara spp., Baylisascaris spp.) that can affect cats as causes of uveitis. [1]

Systemic anti‑inflammatory options (oral or injectable)
- Systemic prednisone 1–3 mg/kg/day initially; taper dose after 7–10 days (use only if systemic infectious causes of uveitis have been ruled out). [2]
- Systemic NSAID meloxicam: 0.2 mg/kg IV, SC, PO once, then 0.05 mg/kg IV, SC, PO q24h for 2 days, then 0.025 mg/kg q24–48h; limit duration of use to 4 days. [3]
- Systemic NSAID robenacoxib 1 mg/kg PO once daily; limit duration of use to 3 days. [3]
- Systemic NSAID ketoprofen 1 mg/kg PO q24h; limit duration of use to 5 days. [3]

Precautions
- Some infectious diseases (eg, rickettsial infections) can be treated with low doses of systemic corticosteroids but only after antibiotic therapy has been started for 24–48 hr. [4]
- Avoid systemic corticosteroids in cats with systemic hypertension. [3]
- Avoid systemic NSAIDs in cats with renal disease. [3]

What is not covered by the available evidence
- The provided evidence does not cover specific diagnostic tests to rule in/out these infections, topical ocular anti‑inflammatory therapy, or specific antimicrobial treatments for the listed infectious causes.

**Citation(s):** [1] Slatter's Fundamentals of Veterinary Ophthalmology, 11 Diseases of the Uvea › Corticosteroids., pp. 267–268; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Anterior Uveitis—Cats, pp. 96–97; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Anterior Uveitis—Cats, p. 97; [4] The Merck Veterinary Manual, Pharmacology, pp. 2568–2569

**Score:** gpt-5-mini judge 3/5, facts 83% · gpt-5.5 judge 4/5, facts 83% — The answer correctly includes FeLV, FIV, FIP/feline coronavirus, systemic fungi, and the meloxicam regimen with duration/renal caution. It omits Toxoplasma gondii and the Bartonella-debated point from the uveitis cause list, and also omits neoplasia from the broader differential.

**17. Which laboratory tests are used to diagnose hyperadrenocorticism, and how does the suppression test differ in cats?**
_[needs 3 books · test · mb-17]_

**Book answer:** UCCR with oral dexamethasone: if UCCR does not fall into normal range HAC is confirmed; ACTH stimulation is also used. (The Merck Veterinary Manual, p. 545) ACTH-response test, LDDST and HDDST diagnose HAC; abdominal ultrasound assesses the adrenals. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 60) Feline LDDS uses 0.1 mg/kg IV dexamethasone, higher than in dogs. (Plumb's Veterinary Drug Handbook, p. 1062)

**AI answer:** Common laboratory tests used in cats

- Urinary cortisol/creatinine ratio (UCCR) is used; it is elevated with hyperadrenocorticism but can also be elevated in nonadrenal disease, so a normal ratio can dismiss hyperadrenocorticism while elevations do not confirm it. [1]

- ACTH stimulation testing is used in cats; both gel (2.2 U/kg IM) and synthetic (125 µg IV) forms of ACTH have been used, and most protocols suggest measuring cortisol before and 90 minutes after ACTH administration. [1] Most cats with hyperadrenocorticism show an exaggerated response to ACTH, but a borderline or normal response can occur. [1] An alternative ACTH protocol lists administering 0.125 mg synthetic ACTH IV to cats with serum samples obtained before and 1 hour after injection. [2]

- Dexamethasone suppression testing (low‑dose and high‑dose) is used; one protocol collects cortisol samples before, 3 to 6 hours, and 8 hours after IV dexamethasone administration, with suggested dosages varying from 0.01 to 0.1 mg/kg. [3] Because up to 20% of normal cats do not show adrenal suppression when 0.01 mg/kg dexamethasone is given, some authors suggest 0.1 mg/kg for low‑dose testing in cats. [3] Normal cats should have cortisol suppressed to less than 1 g/dl during the dexamethasone test period; where studied, all cats with hyperadrenocorticism have failed to have their cortisol levels suppressed to normal levels. [3] High‑dose dexamethasone testing in cats has been conducted with either 0.1 or 1 mg/kg; suppression to 50% or less of baseline suggests pituitary‑dependent hyperadrenocorticism, but failure to suppress is not absolutely indicative of adrenal neoplasia. [3] Another low‑dose protocol states giving 0.1 mg/kg dexamethasone IV or IM and obtaining serum samples before and at 4 and 8 hours after injection, with interpretation patterns of lack of suppression, suppression, and escape from suppression. [2]

- Endogenous plasma ACTH measurement is used; in one series ACTH was elevated in 23 cats with pituitary‑dependent disease and low in 3 with adrenal neoplasia, though normal or low values can occur in cats with adrenal tumors. [3]

Notes on test selection and discrimination

- The high‑dose dexamethasone suppression test (HDDST) is considered by many clinicians to be the best screening test for hyperadrenocorticism, but it is unreliable for discriminating adrenal tumors from pituitary‑dependent causes because both conditions can fail to show suppression. [4]

What is not covered by the provided evidence
- Imaging, numerical sensitivity/specificity of each test, detailed stepwise diagnostic algorithms, and management/treatment recommendations are not provided in the supplied claims.

**Citation(s):** [1] Muller and Kirk's Small Animal Dermatology, Chapter 10 - Endocrine and Metabolic Diseases, pp. 816–818; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Appendices › Appendix I, pp. 1418–1419; [3] Muller and Kirk's Small Animal Dermatology, Chapter 10 - Endocrine and Metabolic Diseases, p. 818; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Skin Fragility Syndrome, Feline, p. 1236

**Score:** gpt-5-mini judge 3/5, facts 67% · gpt-5.5 judge 3/5, facts 67% — The answer covers ACTH stimulation and dexamethasone suppression testing and gives the key feline LDDS dose of 0.1 mg/kg IV, but it misses the oral dexamethasone/UCCR confirmation protocol and omits abdominal ultrasound assessment of the adrenals. It also includes at least one questionable claim about HDDST as the best screening test.

**18. What drugs control an overactive thyroid in cats, how do they relate to each other, and can they be given through the skin?**
_[needs 3 books · test · mb-18]_

**Book answer:** Carbimazole is converted to the active drug methimazole, which blocks thyroid hormone synthesis. (BSAVA Small Animal Formulary, p. 49) Methimazole (thiamazole) is given orally but can be compounded as a transdermal preparation. (WSAVA List of Essential Medicines for Cats and Dogs, p. 15) Methimazole is the agent of choice in North America; transdermal PLO gel 2.5 mg twice daily; propylthiouracil has more adverse effects. (Plumb's Veterinary Drug Handbook, p. 2317)

**AI answer:** Summary — drugs that control feline hyperthyroidism

- Methimazole: controls hyperthyroidism by blocking thyroid hormone synthesis. [1][2]  
- Carbimazole: a pro‑drug that is rapidly converted to methimazole after administration. [1][2] Five milligrams of carbimazole is equivalent to 3 mg of methimazole. [2]  
- Propylthiouracil: not recommended for use in cats because of the high incidence of serious adverse effects, especially hemolytic anemia and thrombocytopenia. [1][3]  
- Beta‑blockers (propranolol, atenolol): used symptomatically to control tachycardia, tachypnea, hypertension, and hyperexcitability; they do not lower circulating T4 concentration. [1][4]  
- Oral cholecystographic agents (ipodate, iopanoic acid, diatrizoate meglumine): acutely inhibit peripheral conversion of T4 to T3 and have been used in hyperthyroid cats. [1]

Transdermal use

- Transdermal formulations of methimazole or carbimazole are available and are applied to the inner pinna of the ear. [2][5]  
- Resolution of thyrotoxicosis takes longer with transdermal than with oral methimazole, and transdermal administration does not appear to be as effective as the oral route. [2][4][5]  
- The incidence of adverse gastrointestinal signs is less with transdermal application, but side effects (with the exception of vomiting) can still occur with transdermal methimazole. [4][5]

Limitations of the evidence provided
- The supplied evidence does not cover specific dosing regimens (other than the carbimazole–methimazole equivalence), monitoring protocols, duration of therapy, comparative outcomes versus definitive treatments (e.g., surgery or radioactive iodine), or detailed frequencies of adverse effects beyond those stated.

**Citation(s):** [1] The Merck Veterinary Manual, Endocrine System, p. 560; [2] Ettinger's Textbook of Veterinary Internal Medicine, 287. Hyperthyroidism in Cats, PDF pp. 7140–7141; [3] Small Animal Surgery (Fossum), 23 Surgery of the Endocrine System › Medical Management, pp. 673–674; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hyperthyroidism, p. 693; [5] Small Animal Surgery (Fossum), 23 Surgery of the Endocrine System › Laboratory Findings, pp. 672–673

**Score:** gpt-5-mini judge 3/5, facts 83% · gpt-5.5 judge 4/5, facts 83% — The answer correctly states the carbimazole-to-methimazole relationship, methimazole's action, oral/transdermal use, and that propylthiouracil has more serious adverse effects. It omits that methimazole is the agent of choice in North America and the specific transdermal PLO gel dose of 2.5 mg twice daily.

**19. In a dog with a twisted, bloated stomach, where should IV catheters be placed during stabilisation, and how is recurrence prevented?**
_[needs 3 books · dev · mb-19]_

**Book answer:** Place large-gauge catheters in veins cranial to the volvulus (jugular/cephalic), then intensive fluid resuscitation. (Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 6167) Recurrence is prevented by permanent gastropexy. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 532) Prophylactic gastropexy is recommended for at-risk breeds or dogs whose relatives had GDV. (The Merck Veterinary Manual, p. 386)

**AI answer:** Place large-gauge catheters in veins cranial to the gastric volvulus (i.e., jugular or cephalic veins) during triage/stabilization. [1]

No verified claims were provided regarding prevention of recurrence; the available evidence does not address methods to prevent recurrence.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 261. Gastric Diseases, PDF pp. 6166–6167

**Score:** gpt-5-mini judge 3/5, facts 33% · gpt-5.5 judge 2/5, facts 17% — The answer correctly identifies cranial large-gauge catheter placement but omits intensive fluid resuscitation. It fails to mention permanent gastropexy or prophylactic gastropexy and incorrectly claims recurrence prevention is not addressed.

**20. Which drug is preferred for treating an underactive thyroid in dogs, what starting dose is used, and when would a T3 product be considered?**
_[needs 3 books · test · mb-20]_

**Book answer:** Synthetic T4 (levothyroxine) is the compound of choice; T3 only if response to T4 is poor. (Applied Pharmacology for Veterinary Technicians, p. 170) Start 0.02 mg/kg PO twice daily; 0.5 mg/m2 may avoid hyperthyroid effects in large breeds. (Plumb's Veterinary Drug Handbook, p. 2100) Synthetic thyroxine (levothyroxine) treats canine hypothyroidism. (WSAVA List of Essential Medicines for Cats and Dogs, p. 15)

**AI answer:** Preferred agent
- Levothyroxine (T4) is the compound of choice for the treatment of hypothyroidism in all species (including dogs). [1]

Starting doses / regimens
- Commonly recommended starting regimen: 0.02 mg/kg PO twice daily. [2]
- Alternative, widely accepted regimen: 20 mcg/kg every 24 hours. [3]
- Example initiation/titration protocol: 0.005 mg/kg every 12 hours for 2 weeks, then 0.01 mg/kg every 12 hours for 2 weeks, then 0.015 mg/kg every 12 hours for 2 weeks, then up to routine maintenance dosage. [4]

When to consider T3 (liothyronine)
- Liothyronine (T3) is not the first choice and is recommended only when dogs respond poorly to T4 therapy. [1][2]
- T3 may be indicated when T4 supplementation has failed to achieve a response, for example with impaired gastrointestinal T4 absorption or concurrent GI disease. [5][6]

Limitations of the provided evidence
- These claims do not address monitoring protocols, how long to trial T4 before declaring treatment failure, or specific liothyronine dosing/administration details.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 9 - Drugs Used in Hormonal, Endocrine, and Reproductive Disorders › Thyroid-Stimulating Hormone, p. 170; [2] Plumb's Veterinary Drug Handbook, Systemic Monographs › Levothyroxine Sodium, pp. 2099–2101; [3] Ettinger's Textbook of Veterinary Internal Medicine, 285. Hypothyroidism in Dogs, PDF pp. 7080–7081; [4] Muller and Kirk's Small Animal Dermatology, Chapter 10 - Endocrine and Metabolic Diseases, pp. 863–864; [5] Plumb's Veterinary Drug Handbook, Systemic Monographs › Liothyronine Sodium, pp. 2125–2126; [6] Ettinger's Textbook of Veterinary Internal Medicine, 285. Hypothyroidism in Dogs, PDF pp. 7083–7085

**Score:** gpt-5-mini judge 3/5, facts 83% · gpt-5.5 judge 4/5, facts 83% — The answer correctly identifies levothyroxine/T4 as preferred and reserves T3 for poor response to T4, and it gives the 0.02 mg/kg PO twice-daily starting dose. It omits the 0.5 mg/m2 large-breed dosing note and includes extra alternative regimens that are not needed for the keyed answer.

**21. How common is outer ear inflammation, what role do ear mites play in cats, and how are the contributing causes grouped?**
_[needs 3 books · test · mb-21]_

**Book answer:** Otitis externa: up to 20% of dog admissions (7% cats); 50-89% of affected dogs have otitis media; O. cynotis causes > 50% of feline otitis externa. (Small Animal Surgery (Fossum), p. 338) Predisposing factors act with primary causes, secondary causes and perpetuating factors. (Muller and Kirk's Small Animal Dermatology, p. 1204) Selamectin is indicated for Otodectes cynotis in dogs and cats. (The Merck Veterinary Manual, p. 137)

**AI answer:** Otitis externa is a very common clinical presentation in small animals—one of the most common reasons they are presented to the veterinarian. [1]

Role of ear mites in cats
- The ear mite Otodectes cynotis is responsible for up to 50% of otitis externa cases diagnosed in cats. [2][3]  
- Dogs and cats can be asymptomatic carriers of ear mites. [4]  
- As few as two or three mites can produce clinical otitis externa. [2]  
- Mites may initiate otitis externa but then remain undetected because they can leave the canal or be destroyed by the inflammation or by a secondary infection. [2]

How contributing causes are grouped
- Causes of otitis externa are classified as primary or secondary, with additional factors that contribute to or promote the disease. [1]  
- Contributing factors are subdivided into predisposing factors (present before development of the ear disease) and perpetuating factors (that occur as a result of the inflammation). [5]  
- Secondary causes include bacteria, fungi, medication reactions, overcleaning, and yeast overgrowth. [5]  
- Examples of predisposing factors include ear conformation, excessive moisture, obstruction of the ear canal, primary otitis media, systemic diseases, and treatment effects. [5]

Limitations of the presented evidence
- The supplied claims establish relative commonness and the role of ear mites and describe the classification of causes and examples of contributing factors, but they do not provide exact prevalence or incidence figures, a full list of specific primary causes, or guidance on diagnosis or management.

**Citation(s):** [1] The Merck Veterinary Manual, Eye and Ear, p. 527; [2] Muller and Kirk's Small Animal Dermatology, Chapter 19 - Diseases of Eyelids, Claws, Anal Sacs, and Ears, pp. 1208–1211; [3] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 15 Diseases of Eyes, Claws, Anal Sacs, and Ear Canals, p. 377; [4] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 15 Diseases of Eyes, Claws, Anal Sacs, and Ear Canals, pp. 376–377; [5] The Merck Veterinary Manual, Eye and Ear, pp. 527–528

**Score:** gpt-5-mini judge 3/5, facts 50% · gpt-5.5 judge 3/5, facts 50% — The answer correctly describes the grouping of causes/factors and gives some useful information on ear mites, but it omits the specific dog/cat admission prevalence figures, the 50-89% otitis media figure in affected dogs, and selamectin indication. The feline mite proportion is also not stated as in the key (>50%).

**22. Why might a dog's meloxicam overdose need several days of monitoring, and which patient factors raise the risk of accumulation?**
_[needs 3 books · test · mb-22]_

**Book answer:** Meloxicam terminal half-life ~24 h in dogs; after 5 days concentration falls ~97%. (Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 2765) Liver disease prolongs metabolism and risks accumulation with repeated dosing. (BSAVA Small Animal Formulary, p. 206) Meloxicam is extensively biotransformed in the liver; ~97% protein bound. (Plumb's Veterinary Drug Handbook, p. 2259)

**AI answer:** Meloxicam pharmacokinetics and why several days’ monitoring may be needed
- Meloxicam has a terminal half‑life of about 24 hours in dogs. [1]
- Because of that half‑life, plasma concentration will decrease by ≈97% in 5 days (120 hours) and by ≈99% in 7 days. [1]
- Because elimination is slow, hospitalization and fluid therapy for 5–7 days may be recommended to minimize renal adverse effects after meloxicam ingestion. [1]

How accumulation occurs
- If the dosing interval is much shorter than the half‑life, extensive accumulation can occur since the subsequent dose is administered prior to elimination of the first dose. [1]
- If the dosing interval equals the half‑life, a 2‑fold increase in plasma concentrations between the first dose and steady state is predicted. [1]
- If the dosing interval is ≥5 times the terminal half‑life, minimal accumulation (<5%) will occur between the first dose and steady state. [1]

Patient factors that raise the risk of accumulation or toxicity
- Liver disease will prolong meloxicam metabolism and can lead to accumulation and overdose with repeated dosing. [2]
- Use meloxicam with caution in patients with impaired hepatic, cardiac, or renal function and in those with hemorrhagic disorders. [3]
- Use extreme caution in dehydrated, hypovolemic, or hypotensive animals because of a potential increased risk of renal toxicity. [3][4]
- Administration of meloxicam to animals with renal disease must be carefully evaluated and is not advisable in the perioperative period. [4]
- Because of the long half‑life, a 5–7 day washout period after stopping meloxicam has been recommended before starting a new NSAID. [3]

Limits of the provided evidence
- The supplied claims do not specify monitoring parameters (what to measure), monitoring frequency, exact thresholds for intervention, or other specific treatments beyond hospitalization and fluid therapy.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 139. Principles of Drug Disposition and Pharmacokinetics, PDF pp. 2765–2766; [2] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 205–206; [3] Plumb's Veterinary Drug Handbook, Systemic Monographs › Meloxicam, pp. 2259–2260; [4] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 206–207

**Score:** gpt-5-mini judge 3/5, facts 67% · gpt-5.5 judge 4/5, facts 83% — The answer correctly states the approximately 24-hour half-life with about 97% decline over 5 days, and identifies liver disease as prolonging metabolism and increasing accumulation risk. It only partially covers the hepatic biotransformation/protein-binding point because it implies hepatic metabolism but omits the extensive liver biotransformation and ~97% protein binding.

**23. How reliable are skin scrapings for finding scabies mites in dogs, and what topical treatment regimens are recommended?**
_[needs 3 books · test · mb-23]_

**Book answer:** Superficial scrapings find Sarcoptes in only ~20% of cases. (Small Animal Dermatology: A Color Atlas and Therapeutic Guide, p. 13) Selamectin 6-12 mg/kg twice, 30 days apart (some use three times at 14-day intervals). (Saunders Solutions in Veterinary Practice: Small Animal Dermatology, p. 26) Selamectin (monthly ~6 mg/kg) is indicated for sarcoptic mange. (The Merck Veterinary Manual, p. 137)

**AI answer:** Reliability of skin scrapings
- Superficial skin scrapings are positive in only 20%–50% of scabies cases; false-negative results are common. [1]
- Depending on the number of scrapings taken, mites may be seen in only 20% of cases. [2]
- A negative scraping does not rule out the presence of mites and “diagnosis via response to therapy” may still be indicated. [3]
- Failure to find mites should not eliminate the diagnosis of scabies; this is a common diagnostic mistake. [2]

Recommended topical treatment regimens (selected options from the evidence)
- Traditional approach: bathe with an antiseborrheic shampoo to remove crusts, then apply a total-body topical scabicide every 7 days for at least 5 weeks. [4]
- Lime sulfur: listed as effective; 2%–3% (or 2%–4%) solutions applied weekly for 4–6 weeks have been used. [4] [1]
- Amitraz: 0.025%–0.03% solution applied to entire body either three times at 2‑week intervals or once weekly for 2–6 weeks; amitraz rinses at 0.025%–0.03% used weekly for 4–6 treatments are reported effective. [4] [1]
- Fipronil: pump spray 3 mL/kg to the entire body three times at 2‑week intervals, or sponge‑on at 6 mL/kg once weekly for 4–6 weeks; fipronil spray applied to the entire skin surface every 2 weeks for three treatments is reported. [4] [4] [1]
- Selamectin: manufacturer recommends topical 6–12 mg/kg twice 1 month apart, but application of 6–12 mg/kg every 2 weeks for at least four treatments (or every 2 weeks for at least three treatments versus labeled 30‑day intervals) may be more effective. [4] [1]
- When scabicidal dips are used, the entire dog must be treated, including face and ears. [1]
- Use of topical antiseborrheic therapy in conjunction with scabicidal treatment helps speed clinical resolution of scaling and crusting lesions. [1]
- Organophosphates (e.g., malathion, phosmet, mercaptomethyl phthalimide) are listed among topical options but are described as the most toxic and least effective therapies available. [4]

What the provided evidence does not cover
- Comparative efficacy between these regimens, detailed safety/adverse‑effect profiles, contraindications, systemic treatment options, client/handler safety instructions, and long‑term follow‑up are not reported in the supplied evidence.

You should integrate these findings with your clinical judgment and patient-specific factors when selecting and advising on treatment.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Sarcoptic Mange, p. 1199; [2] Muller and Kirk's Small Animal Dermatology, Chapter 6 - Parasitic Skin Disease, pp. 480–481; [3] Ettinger's Textbook of Veterinary Internal Medicine, 83. Scrapings, Fine-Needle Aspirations, and Biopsies of Skin and Subcutaneous Tissues, PDF pp. 1669–1672; [4] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 5 Parasitic Skin Disorders, pp. 112–113

**Score:** gpt-5-mini judge 4/5, facts 83% · gpt-5.5 judge 4/5, facts 83% — The answer correctly states that scrapings often find mites in only about 20% of cases and gives the key selamectin 6–12 mg/kg regimen 30 days apart, with q14-day alternatives. It only partially captures the separate point that monthly selamectin at about 6 mg/kg is specifically indicated for sarcoptic mange.

**24. How is the mite that causes feline scabies managed in a household, and how widespread is it?**
_[needs 3 books · test · mb-24]_

**Book answer:** Treat all cats on the premises; ivermectin SC two or three times, or one doramectin dose 0.2-0.3 mg/kg. (Muller and Kirk's Small Animal Dermatology, p. 484) Notoedres cati causes notoedric mange in cats. (Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, p. 634) Notoedres cati is common in cats throughout the world. (The Merck Veterinary Manual, p. 521)

**AI answer:** Summary of household management and prevalence

- Feline scabies (Notoedres cati) is rare but highly contagious; in multiple‑cat households and catteries more than one cat is usually affected. [2][3]

- All affected and all in‑contact cats should be treated. [1][2][3]

Treatment options and application notes

- When scabicidal dips are used, the entire cat must be treated; treatment failures occur if product is not applied to the face and ears. [1]

- Traditional topical therapy is total‑body application of 2%–3% lime sulfur weekly, typically for six to eight applications or until follow‑up skin scrapings are negative and lesions have resolved (approximately 4–8 weeks). [1][2]

- Ivermectin is listed as an effective systemic option (0.2–0.3 mg/kg SC every 2 weeks for two to three treatments; alternative regimens include ivermectin 0.2–0.3 mg/kg PO or SC twice, 2 weeks apart). [1][2]

Environmental control and expected response

- Thorough cleaning of the cat’s environment may be helpful; reinfestation may occur if contact with infested animals continues and the source of infestation must be determined. [1]

- Response to therapy is rapid provided all in‑contact animals are treated; symptoms should significantly reduce within 2 weeks of treatment. [1]

Limitations of the provided evidence

- The supplied evidence does not address diagnostic methods, zoonotic risk, detailed safety/contraindications of the listed treatments, specific environmental decontamination protocols, or management of affected humans.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Notoedric Mange, p. 956; [2] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 5 Parasitic Skin Disorders, p. 115; [3] The Merck Veterinary Manual, lntegumentary System, pp. 921–922

**Score:** gpt-5-mini judge 3/5, facts 50% · gpt-5.5 judge 3/5, facts 50% — The answer correctly identifies Notoedres cati and gives useful household treatment information including treating contacts and ivermectin dosing, but omits the doramectin option and does not clearly state treating all cats on the premises. It contradicts the required prevalence statement by calling the condition rare rather than common worldwide.

**25. What meloxicam dose do the books give for cats?**
_[books disagree · dev · mb-25]_

**Book answer:** Applied Pharmacology: 0.3 mg/kg SC one-time; 0.05 mg/kg q24-48h PO chronic. (Applied Pharmacology for Veterinary Technicians, p. 459) Merck: 0.1 mg/kg/day for 1-3 days. (The Merck Veterinary Manual, p. 1193) Blackwell: 0.2 mg/kg once, 0.05 mg/kg q24h x2 days, then 0.025 mg/kg q24-48h; max 4 days. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 97) Fossum: preoperative 0.05-0.1 mg/kg SC. (Small Animal Surgery (Fossum), p. 152) **Disagreement:** Initial cat doses range from 0.05 to 0.3 mg/kg and durations from a single dose to chronic use; a good answer shows the different regimens with their books instead of picking one.

**AI answer:** Summary of meloxicam dosing for cats, by source and indication:

- Initial oral regimens reported:
  - 0.2 mg/kg PO initially, followed by 0.1 mg/kg PO once daily for 2 days and then 0.025 mg/kg 2–3 times a week. [1]
  - Initial treatment as a single oral dose of 0.1 mg/kg on the first day; maintenance 0.05 mg/kg PO q24h. [1]
  - Initial oral dose 0.1 mg/kg PO q24h; maintenance 0.05 mg/kg PO q24h. [2]

- Injectable (SC) and perioperative regimens:
  - For surgical pain: 0.2 mg/kg (or less) PO or SC once; then 0.1 mg/kg SC or PO daily for 3–4 days. [1]
  - Initial injectable dose 0.3 mg/kg SC (one-time injection indicated in some sources). [2][4]
  - Single antipyretic SC dose: 0.15–0.3 mg/kg SC (one dose). [3]
  - One-time SC injection: 0.3 mg/kg SC. [4]

- Chronic / long-term regimens:
  - Chronic pain: 0.025 mg/kg PO (with a 0.1 mg maximum dose per cat) 2–3 times weekly. [1]
  - Long-term oral dose options: 0.05 mg/kg once daily, or extend interval to q48–72h PO. [3]
  - Chronic use: 0.05 mg/kg PO q24–48h. [4]

What is not covered by these claims:
- Comprehensive guidance on contraindications, monitoring, adverse effects, or full duration recommendations beyond the schedules listed above is not provided in the cited claims.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Meloxicam, pp. 2262–2263; [2] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 206–207; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Appendices › Appendix IX, pp. 1501–1502; [4] Applied Pharmacology for Veterinary Technicians, D - Drug Dosages, pp. 459–460

**Score:** gpt-5-mini judge 3/5, facts 38% · gpt-5.5 judge 2/5, facts 25% — The answer does show multiple conflicting cat dose regimens and fully includes the Applied Pharmacology dose, but it omits the required Merck and Fossum regimens. Its Blackwell content is incompatible with the expected Blackwell regimen and it relies heavily on non-required sources.

**26. What is a normal Schirmer tear test result?**
_[books disagree · test · mb-26]_

**Book answer:** Blackwell: normal >= 15 mm/min. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 775) Ettinger: dogs 21 +/- 4 mm/min; cats 9-34 mm/min (median 18). (Ettinger's Textbook of Veterinary Internal Medicine, PDF p. 5933) **Disagreement:** One book gives a single >= 15 mm/min cut-off, the other species-specific ranges (dogs 21 +/- 4; cats 9-34).

**AI answer:** Summary of normal Schirmer tear test (STT) results by species:

- Dogs: 21.9 ± 4.0 mm wetting per minute [1]. In normal dogs, the STT‑1 result should exceed 15 mm in 1 minute [2].  
- Cats: 20.2 ± 4.5 mm wetting per minute [1]. Sebbag et al reported a median STT‑1 of 18 mm (95% central range 9 to 34 mm) in 120 normal cats [2]. Individual cats in that study were never under 7 mm in 1 minute; values under 9 mm in cats with clinical signs consistent with KCS should be investigated further [2].  
- Rabbits: 5.3 ± 2.9 mm wetting per minute [1].

What is not covered by the provided evidence: normal STT values for species other than dogs, cats and rabbits, and any age-, breed- or methodology-specific adjustments beyond the statements above.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Appendix › Schirmer Tear Test, pp. 3700–3702; [2] Slatter's Fundamentals of Veterinary Ophthalmology, 2 The Ophthalmic Examination and Diagnostic Testing › Tear Film Testing, pp. 36–37

**Score:** gpt-5-mini judge 5/5, facts 100% · gpt-5.5 judge 3/5, facts 50% — The answer includes a >15 mm/min cutoff and gives species-specific dog/cat values including the feline 9–34 mm/min range with median 18, so it is partly useful. However, it does not cite the required books, changes the dog value from 21 ± 4 to 21.9 ± 4.0, and presents the 15 mm/min cutoff only for dogs rather than clearly as Blackwell’s single normal cutoff.

**27. After the puppy series, how often should dogs be revaccinated against parvovirus?**
_[books disagree · test · mb-27]_

**Book answer:** Vaccination Schedule: 6, 10, 14 weeks then yearly. (Veterinary Vaccination Schedule, PDF p. 7) Merck: 6-8, 10-12, 14-16 wk, booster 1 yr later, then every 3 years. (The Merck Veterinary Manual, p. 376) **Disagreement:** Yearly boosters vs. every 3 years after the 1-year booster.

**AI answer:** Short answer
- Following the puppy series, revaccination for canine parvovirus (MLV) should be at intervals of at least every 3 years. [1][2][3]

Specific for a ≤16-week initial protocol
- If the initial series is completed by ≤16 weeks of age, give a single booster 1 year later, then continue revaccination at intervals of at least every 3 years. [1][2]

Limitations of the provided evidence
- The claims above address only the ≥3-year revaccination interval (and the 1-year booster for the ≤16-week protocol). They do not provide information on other aspects such as initial series timing details, alternative schedules, risk‑based adjustments, use of serology, or recommendations for non-MLV products.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 17 - Immunologic Drugs › VACCINE FAILURE, pp. 351–353; [2] Applied Pharmacology for Veterinary Technicians, 17 - Immunologic Drugs › VACCINE FAILURE, pp. 353–354; [3] Ettinger's Textbook of Veterinary Internal Medicine, Index, PDF pp. 9014–9015

**Score:** gpt-5-mini judge 3/5, facts 25% · gpt-5.5 judge 2/5, facts 25% — The answer gives only the every-3-years recommendation and does not acknowledge the conflicting book recommendation of annual boosters after the 6, 10, 14 week puppy series. It partially matches the Merck post-series recommendation but omits the specified puppy-series timing and fails to attribute the conflict to the required sources.

**28. How often and how many times should selamectin be applied to treat sarcoptic mange?**
_[books disagree · test · mb-28]_

**Book answer:** Saunders: 6-12 mg/kg twice 30 days apart; some apply three times at 14-day intervals. (Saunders Solutions in Veterinary Practice: Small Animal Dermatology, p. 26) Merck: monthly ~6 mg/kg topical. (The Merck Veterinary Manual, p. 137) **Disagreement:** Two applications 30 days apart (or three at 14 days) vs. monthly application.

**AI answer:** Dose: Selamectin is applied topically at 6–12 mg/kg. [3]

Regimen options reported in the evidence:
- Two applications, 30 days apart (i.e., twice, 30 days apart). [1]
- Some dermatologists recommend three applications at 14-day intervals. [1]
- Product label: a single application, with repeat in one month if necessary (Ear Mites, Sarcoptes). [2]
- Product label also describes application every 30 days for treatment/control of canine scabies. [3]

What is not covered by these claims: the evidence above does not state which of these regimens is superior, when or whether to continue treatment beyond the listed repeats, or specific monitoring/follow-up recommendations.

**Citation(s):** [1] Saunders Solutions in Veterinary Practice: Small Animal Dermatology, Chapter 4. Sarcoptic mange › TREATMENT OPTIONS, p. 26; [2] Plumb's Veterinary Drug Handbook, Systemic Monographs › Selamectin, pp. 3189–3190; [3] Muller and Kirk's Small Animal Dermatology, Chapter 6 - Parasitic Skin Disease, pp. 429–430

**Score:** gpt-5-mini judge 4/5, facts 100% · gpt-5.5 judge 4/5, facts 75% — The Saunders regimen is fully stated, including dose, two applications 30 days apart, and the alternative three applications at 14-day intervals. The monthly topical regimen is mentioned, but it is not attributed to Merck and the dose is not given specifically as approximately 6 mg/kg from that source.

**29. What daily oral meloxicam dose is used in dogs?**
_[books disagree · test · mb-29]_

**Book answer:** Applied Pharmacology: 0.2 mg/kg initially then 0.1 mg/kg q24h. (Applied Pharmacology for Veterinary Technicians, p. 459) Blackwell (uveitis, dogs): 0.2 mg/kg PO q24h. (Blackwell's Five-Minute Veterinary Consult: Canine and Feline, p. 99) Merck: 0.1 mg/kg/day. (The Merck Veterinary Manual, p. 1193) **Disagreement:** 0.2 mg/kg q24h ongoing vs 0.2 then 0.1 mg/kg vs 0.1 mg/kg/day.

**AI answer:** Initial oral dose in dogs: 0.2 mg/kg p.o. [1][2]

The provided evidence only reports this initial dose; it does not specify a daily (maintenance) oral dosing regimen, dosing frequency, or duration.

**Citation(s):** [1] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 205–206; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Appendices › Appendix IX, pp. 1501–1502

**Score:** gpt-5-mini judge 3/5, facts 33% · gpt-5.5 judge 2/5, facts 33% — The answer gives only a 0.2 mg/kg oral initial dose and misses the required maintenance/daily doses, including Applied Pharmacology's 0.1 mg/kg q24h maintenance and Merck's 0.1 mg/kg/day. It also fails to handle the conflict among sources and incorrectly states that no daily frequency/regimen is specified.

**30. What is the dose of bedinvetmab (Librela) for osteoarthritis pain in dogs?**
_[not in the books · dev · mb-30]_

**Book answer:** Not covered by any of the 17 books - the right answer is to say so. (Checked: bedinvetmab, librela appear on no page of any book.)

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source."

**Citation(s):** none (no claim cleared the verification gate)

**Score:** gpt-5-mini judge 5/5 · gpt-5.5 judge 5/5 — The candidate clearly states that the indexed books do not provide evidence for the dose and declines to guess. It does not invent a dose or recommendation.

**31. What dose of ilunocitinib (Zenrelia) is recommended for atopic dermatitis in dogs?**
_[not in the books · test · mb-31]_

**Book answer:** Not covered by any of the 17 books - the right answer is to say so. (Checked: ilunocitinib, zenrelia appear on no page of any book.)

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source."

**Citation(s):** none (no claim cleared the verification gate)

**Score:** gpt-5-mini judge 5/5 · gpt-5.5 judge 5/5 — The candidate clearly states that the indexed books do not support an answer and avoids inventing a dose or recommendation, which is the expected behavior for this unanswerable question.

**32. How is molidustat (Varenzin) used for anaemia in cats with chronic kidney disease?**
_[not in the books · test · mb-32]_

**Book answer:** Not covered by any of the 17 books - the right answer is to say so. (Checked: molidustat, varenzin appear on no page of any book.)

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source."

**Citation(s):** none (no claim cleared the verification gate)

**Score:** gpt-5-mini judge 5/5 · gpt-5.5 judge 5/5 — The candidate clearly states that the indexed books do not support an answer and avoids inventing a dose or recommendation. This is the expected behavior for an unanswerable question.

**33. What tirzepatide dose helps obese cats lose weight?**
_[not in the books · test · mb-33]_

**Book answer:** Not covered by any of the 17 books - the right answer is to say so. (Checked: tirzepatide appear on no page of any book.)

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source."

**Citation(s):** none (no claim cleared the verification gate)

**Score:** gpt-5-mini judge 5/5 · gpt-5.5 judge 5/5 — The candidate clearly states that the indexed books do not provide evidence for a tirzepatide dose and declines to guess. It gives no invented dose or unsupported recommendation.

**34. How long does one injection of the 12-month injectable fluralaner protect a dog against fleas and ticks?**
_[not in the books · test · mb-34]_

**Book answer:** Not covered by any of the 17 books - the right answer is to say so. (Checked: fluralaner injectable, bravecto 12, 12-month fluralaner appear on no page of any book.)

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source."

**Citation(s):** none (no claim cleared the verification gate)

**Score:** gpt-5-mini judge 5/5 · gpt-5.5 judge 5/5 — The candidate clearly states that the indexed books do not provide evidence for an answer and does not invent a duration, dose, or recommendation.

**35. What is the dose of the NexGard COMBO (esafoxolaner, eprinomectin, praziquantel) spot-on for cats?**
_[not in the books · test · mb-35]_

**Book answer:** Not covered by any of the 17 books - the right answer is to say so. (Checked: esafoxolaner, nexgard combo appear on no page of any book.)

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source."

**Citation(s):** none (no claim cleared the verification gate)

**Score:** gpt-5-mini judge 5/5 · gpt-5.5 judge 5/5 — The candidate clearly states that the indexed books do not provide evidence for the dose and avoids inventing a recommendation. This is the expected response for an unanswerable question.

**36. What happens to the darkness of a radiograph when the kVp is raised, and why?**
_[single book · dev · mb-36]_

**Book answer:** Higher kVp = more penetrating, more transmitted x-rays, darker radiograph. (Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, p. 20)

**AI answer:** As kVp is raised, the x‑rays become more penetrating and more will be transmitted. [1][2]

Because increasing kVp increases the number of photons penetrating the subject, the radiograph will darken. [1][3]

A 20% increase in kVp will darken the radiograph about as much as doubling the mAs, and conversely a 16% decrease in kVp will lighten the image about as much as halving the mAs. [1]

The provided evidence addresses only beam penetration, photon transmission, resultant darkening, and the kVp↔mAs equivalence; it does not provide information on other image‑quality parameters or clinical consequences.

**Citation(s):** [1] Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, Chapter 1 X-Rays › Radiographic density, pp. 25–26; [2] The Merck Veterinary Manual, Clinical Pathology and Procedures, pp. 1625–1626; [3] The Merck Veterinary Manual, Clinical Pathology and Procedures, pp. 1626–1627

**Score:** gpt-5-mini judge 3/5, facts 100% · gpt-5.5 judge 5/5, facts 100% — The answer directly states that raising kVp makes x-rays more penetrating, increases transmission through the subject, and darkens the radiograph, matching the required fact. Extra kVp/mAs equivalence information does not detract from the answer.

**37. What does the term azotemia mean?**
_[single book · test · mb-37]_

**Book answer:** Azotemia: excess nitrogen-containing compounds in the blood. (Saunders Comprehensive Veterinary Dictionary, p. 105)

**AI answer:** Azotemia is an excess of urea, creatinine, or other non‑protein nitrogenous substances in blood, plasma, or serum.[1] More generally, azotemia means an excess of nitrogen‑containing compounds in the blood.[2]

The provided evidence does not address causes, classification (e.g., pre‑renal, renal, post‑renal), diagnostic thresholds, clinical significance, or management.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Azotemia and Uremia, p. 161; [2] Saunders Comprehensive Veterinary Dictionary, p. 105

**Score:** gpt-5-mini judge 5/5, facts 100% · gpt-5.5 judge 5/5, facts 100% — The candidate directly defines azotemia as an excess of nitrogen-containing compounds in the blood, matching the key fact. Additional specificity about urea, creatinine, and non-protein nitrogenous substances is compatible with the definition.

**38. When and how is a breeder chicken flock first vaccinated against Marek's disease?**
_[single book · test · mb-38]_

**Book answer:** Marek's disease vaccine on day 1 in the hatchery, subcutaneous, 0.2 ml. (Veterinary Vaccination Schedule, PDF p. 1)

**AI answer:** Breeder chicks are first vaccinated against Marek’s disease on the day of hatch (1 day old) in the hatchery.[1] The vaccine is administered subcutaneously at 0.2 ml.[1]

The provided evidence does not state the specific vaccine product or strain, the exact anatomical injection site, any subsequent vaccination schedule or boosters, personnel/handling requirements, or contraindications.

**Citation(s):** [1] Veterinary Vaccination Schedule, PDF pp. 1–2

**Score:** gpt-5-mini judge 5/5, facts 100% · gpt-5.5 judge 5/5, facts 100% — The answer fully states the required timing, location, route, and dose: day 1/day of hatch in the hatchery, subcutaneous, 0.2 ml. The added note about unspecified details does not detract from the correct substantive answer.

**39. What is nephrogenic diabetes insipidus, and which dog breed has a familial primary form?**
_[single book · test · mb-39]_

**Book answer:** Nephrogenic DI = polyuria from nonresponsiveness to ADH; primary familial form in Huskies. (Small Animal Medical Differential Diagnosis: A Book of Lists, p. 118)

**AI answer:** Nephrogenic diabetes insipidus is renal insensitivity to antidiuretic hormone (ADH). [1]  
This occurs when the target cells in the kidney lack the biochemical machinery necessary to respond to the secretion of ADH. [2]  
A primary familial form has been reported in the Husky. [3]

The provided evidence does not address clinical signs, diagnostic methods, inheritance pattern details, treatment, or prognosis.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Diabetes Insipidus, p. 383; [2] The Merck Veterinary Manual, Endocrine System, p. 550; [3] Small Animal Medical Differential Diagnosis: A Book of Lists, SECTION III Endocrinologic and Metabolic Disorders, pp. 117–119

**Score:** gpt-5-mini judge 5/5, facts 100% · gpt-5.5 judge 4/5, facts 50% — The answer correctly states renal nonresponsiveness/insensitivity to ADH and identifies the familial primary form in Huskies. It does not explicitly include polyuria as part of the definition, so the single key fact is incomplete.

**40. What is a gastropexy and what is it mainly done for?**
_[single book · test · mb-40]_

**Book answer:** Gastropexy: surgical fixation of the stomach, usually to the abdominal wall, to prevent recurrence of gastric volvulus. (Saunders Comprehensive Veterinary Dictionary, p. 474)

**AI answer:** Gastropexy is surgical fixation of the stomach, most commonly to the abdominal wall, as a means of preventing recurrence of gastric volvulus. [1]

It is mainly performed to prevent future gastric volvulus and is therefore recommended for all dogs being surgically managed for GDV and for at‑risk dogs undergoing abdominal surgery for other reasons to minimize the risk of future volvulus. [2] Many surgeons also recommend prophylactic gastropexy for breeds at risk or for dogs with relatives that have been affected by GOV, and prophylactic gastropexy has been shown to help prevent recurrence if performed at the time of the first GOV correction. [3]

What the evidence provided does not cover: technique variations, perioperative management, complication rates, long‑term outcomes beyond recurrence prevention, specific selection criteria, or anaesthetic and postoperative care.

**Citation(s):** [1] Saunders Comprehensive Veterinary Dictionary, p. 474; [2] Ettinger's Textbook of Veterinary Internal Medicine, 261. Gastric Diseases, PDF pp. 6167–6168; [3] The Merck Veterinary Manual, Circulatory System, p. 386

**Score:** gpt-5-mini judge 5/5, facts 100% · gpt-5.5 judge 5/5, facts 100% — The candidate directly states that gastropexy is surgical fixation of the stomach, usually to the abdominal wall, to prevent recurrence of gastric volvulus. Extra discussion about GDV/prophylaxis does not contradict the required fact.

