# Blackwell's Five-Minute Veterinary Consult: Canine and Feline, 6th edition: AI-generated answers vs. book answers

For each question, the "Book answer" is taken directly from the book's own text (see `Blackwells_5min_consult_100_QA.md`). The "AI answer" and "Citation(s)" were produced by running the question through the VetAI PoC's Streamlit app (retrieve -> synthesize -> verify -> generate), which answers only from the two indexed textbooks and drops unsupported claims before writing.

**1. Why are cats more susceptible to acetaminophen toxicosis than dogs?**
_[Acetaminophen (APAP) Toxicosis]_

**Book answer:** Cats cannot effectively glucuronidate acetaminophen because of a genetic deficiency in the glucuronide conjugation pathway. They can be poisoned by as little as 50-60 mg/kg (often half a tablet), and rapidly develop methemoglobinemia.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages mention acetaminophen toxicity treatment but do not state why cats are more susceptible than dogs.)

**Citation(s):** none (no claim cleared the verification gate)

**2. What is the N-acetylcysteine protocol for acetaminophen toxicosis?**
_[Acetaminophen (APAP) Toxicosis]_

**Book answer:** A loading dose of 140 mg/kg diluted in D5W PO or IV, then 70 mg/kg diluted in D5W PO or IV q6h for 5-7 more treatments. Activated charcoal 2 g/kg PO is given right after emesis or gastric lavage, and SAMe can be added as a glutathione donor.

**AI answer:** For acetaminophen toxicosis, the systemic antidote is N-acetylcysteine (Mucomyst). [1] Protocol: loading dose 140 mg/kg [1]; IV, dilute to 5% and give slowly over 15–20 minutes [1]; PO, dilute in 5% dextrose or sterile water [1]; maintenance, after the loading dose give 70 mg/kg PO or IV every 6 hours for seven treatments [1]; large overdoses may require up to 17 doses [1]. The provided evidence does not specify monitoring parameters, criteria for extending therapy, or adjunctive treatments.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.442-443

**3. What is the fomepizole dosing schedule for ethylene glycol toxicosis in dogs?**
_[Ethylene Glycol Toxicosis]_

**Book answer:** 20 mg/kg IV initially, then 15 mg/kg IV at 12 and 24 hours, then 5 mg/kg IV at 36 hours. The book describes fomepizole as an effective, non-toxic liver alcohol dehydrogenase inhibitor that needs less intensive care than ethanol.

**AI answer:** For ethylene glycol toxicosis in dogs, fomepizole is the treatment of choice. [1][2] Dog dosing schedule: 20 mg/kg IV initially [3][4]; 15 mg/kg IV at 12 hours [3][4]; 15 mg/kg IV at 24 hours [3][4]; 5 mg/kg IV at 36 hours [3][4]; repeat every 12 hours if necessary [4]. The provided evidence does not specify criteria for when repeat dosing is necessary.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - p.448; [2] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.447-448; [3] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.445-446; [4] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.464-465

**4. Which methylxanthine makes up the largest fraction in chocolate?**
_[Chocolate (Methylxanthine) Toxicosis]_

**Book answer:** Theobromine. Chocolate toxicosis causes acute gastroenteric, neurologic and cardiac signs from excessive intake of methylxanthine alkaloids.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages state that caffeine and theobromine are methylxanthines and that theobromine is found in chocolate, but do not state which methylxanthine makes up the largest fraction in chocolate.)

**Citation(s):** none (no claim cleared the verification gate)

**5. What are the main effects of xylitol ingestion in dogs, and how fast do signs appear?**
_[Xylitol Toxicosis]_

**Book answer:** Vomiting, weakness, ataxia, seizures, hypoglycemia and hypokalemia, and in some dogs hepatic failure. Signs may develop within 15-30 minutes, but with sugar-free gums hypoglycemia may be delayed up to 12 hours.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages do not mention xylitol ingestion in dogs or the time to onset of signs.)

**Citation(s):** none (no claim cleared the verification gate)

**6. What is the recommended fluid therapy after grape or raisin ingestion in a dog?**
_[Grape, Raisin, and Currant Toxicosis]_

**Book answer:** Fluid diuresis at 2-3 times maintenance for at least 48 hours, longer if renal failure develops, after GI decontamination with emesis and activated charcoal.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages do not mention grape or raisin ingestion or a recommended fluid therapy for it.)

**Citation(s):** none (no claim cleared the verification gate)

**7. Which species is at risk of systemic lily poisoning, and what organ is affected?**
_[Lily Toxicosis]_

**Book answer:** Cats. Ingestion of Lilium or Hemerocallis (daylily) leaves or flowers causes a severe nephrotoxic syndrome, with as little as 2-3 leaves reported to be dangerous. Dogs only get mild GI upset.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages do not mention systemic lily poisoning, the species at risk, or the affected organ.)

**Citation(s):** none (no claim cleared the verification gate)

**8. Why is the coagulopathy from anticoagulant rodenticides delayed?**
_[Rodenticide Toxicosis—Anticoagulants]_

**Book answer:** Because it results from depletion of the vitamin K1-dependent clotting factors II, VII, IX and X, so onset is delayed by 3-5 days.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages state that vitamin K is necessary for production of vitamin K–dependent clotting factors and that vitamin K1 is used for rodenticide toxicity, but do not explicitly explain why coagulopathy from anticoagulant rodenticides is delayed.)

**Citation(s):** none (no claim cleared the verification gate)

**9. How long is vitamin K1 given for first- versus second-generation anticoagulant rodenticides?**
_[Rodenticide Toxicosis—Anticoagulants]_

**Book answer:** 2.5-5.0 mg/kg PO: q12h for 5-7 days for most first-generation products, and q24h for 4-6 weeks for most second-generation products. Feeding a little fat may improve absorption.

**AI answer:** For coumarin-derivative anticoagulants — first-generation/warfarin-type anticoagulants: give vitamin K1 for 7 days. [1] Second-generation anticoagulant rodenticides: give vitamin K1 for 21–30 days. [1]

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - p.445

**10. Which dogs are most susceptible to ivermectin toxicosis?**
_[Ivermectin and Other Macrocyclic Lactones Toxicosis]_

**Book answer:** Collies are most commonly affected, along with dogs homozygous for the ABCB1 gene deletion (found in Shetland sheepdogs, Australian shepherds and others). Heterozygous dogs can react at higher doses.

**AI answer:** Dogs most susceptible to ivermectin toxicosis are collies, Shetland sheepdogs, Australian shepherds, Old English sheepdogs, white German shepherds, long-haired whippets, greyhounds, silken windhounds, other herding breeds, and crosses with these breeds. [1][2] The susceptibility is associated with a deletion mutation of the multidrug-resistant gene ABCB1, resulting in a truncated nonfunctional P-glycoprotein. [1][2] Systemic ivermectin use is contraindicated in these breeds and crosses; the verified evidence provided does not further rank susceptibility among them or quantify relative risk. [3][4]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - p.315; [2] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.314-315; [3] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.651-652; [4] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - p.651

**11. Why is metaldehyde called the 'shake and bake' toxicant?**
_[Metaldehyde Toxicosis]_

**Book answer:** Because of its characteristic tremors, seizures and hyperthermia. Signs usually develop within 4 hours of ingestion, and there is no specific antidote.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages list treatments for metaldehyde and mention diazepam to control tremors, but do not explain the phrase "shake and bake" or provide enough information to answer why it is called that.)

**Citation(s):** none (no claim cleared the verification gate)

**12. How can cats be exposed to permethrin toxicity, and what treats the tremors?**
_[Pyrethrin and Pyrethroid Toxicosis]_

**Book answer:** Through direct contact with dogs treated with permethrin spot-ons. Tremors and seizures are treated with methocarbamol 55-220 mg/kg IV, not exceeding 330 mg/kg/day.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages do not state what treats tremors from permethrin toxicity.)

**Citation(s):** none (no claim cleared the verification gate)

**13. What pathologic findings are associated with NSAID toxicosis?**
_[Nonsteroidal Anti-Inflammatory Drug Toxicosis]_

**Book answer:** GI irritation, ulceration or hemorrhage with possible gastric perforation and peritonitis, plus renal tubular or papillary necrosis or interstitial nephritis. H2 blockers such as ranitidine or famotidine are used for GI ulceration.

**AI answer:** Pathologic findings associated with NSAID toxicosis center on gastrointestinal injury: GI ulceration and bleeding are the most common findings associated with NSAIDs [1]; aspirin adverse effects include gastric irritation that can progress to ulceration and bleeding [2]; COX-1 inhibition is associated with GI ulceration, bleeding, and reduced renal blood flow [3]. Other associated adverse effects that may have pathologic correlates: hepatotoxicity, nephrotoxicity, inhibition of cartilage metabolism, bone marrow suppression, bleeding tendencies [1]. The provided evidence does not describe specific gross necropsy lesions, histopathologic patterns, lesion distribution, or species-specific findings beyond these associated adverse effects.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.287-288; [2] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - p.288; [3] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - p.287

**14. How long can signs be delayed after a pit viper bite, and is local tissue reaction a reliable guide?**
_[Snake Venom Toxicosis—Pit Vipers]_

**Book answer:** Signs may be delayed for up to 8 hours after envenomation, and tissue reaction around the bite is not a reliable indicator of systemic envenomation.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages discuss pit viper antivenin and supportive care, but do not state how long signs can be delayed after a pit viper bite or whether local tissue reaction is a reliable guide.)

**Citation(s):** none (no claim cleared the verification gate)

**15. Which breeds are at increased risk of hypoadrenocorticism?**
_[Hypoadrenocorticism (Addison's Disease)]_

**Book answer:** Great Danes, rottweilers, Portuguese water dogs, standard poodles, bearded collies, Leonbergers, West Highland white terriers, Nova Scotia duck tolling retrievers and Wheaten terriers. Golden retrievers and Chihuahuas have a decreased risk.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages do not state which breeds are at increased risk of hypoadrenocorticism.)

**Citation(s):** none (no claim cleared the verification gate)

**16. What is the long-term treatment for chronic primary hypoadrenocorticism?**
_[Hypoadrenocorticism (Addison's Disease)]_

**Book answer:** Daily glucocorticoid replacement (prednisone 0.1-0.2 mg/kg/day) plus mineralocorticoid replacement with DOCP (Percorten) 2.2 mg/kg IM or SC, usually monthly, adjusted on serial electrolytes.

**AI answer:** Long-term treatment described in the retrieved passage is mineralocorticoid supplementation with DOCP (desoxycorticosterone pivalate) injections, replacing fludrocortisone. [1] DOCP requires an injection every 21–30 days. [1] In the example case, the patient was discharged initially with prednisone and fludrocortisone, with follow-up scheduled in 7 days to monitor electrolytes closely and transition to DOCP for long-term mineralocorticoid supplementation. [1] The provided evidence does not specify further long-term treatment details beyond this.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.186-187

**17. What is the difference between spontaneous and iatrogenic hyperadrenocorticism?**
_[Hyperadrenocorticism (Cushing's Syndrome)—Dogs]_

**Book answer:** Spontaneous HAC is excessive cortisol production by the adrenal cortex. Iatrogenic HAC results from excessive exogenous glucocorticoids given in any form or by any route.

**AI answer:** Spontaneous hyperadrenocorticism (HAC) is caused by excessive production of cortisol by the adrenal cortex. [1] Its two recognised forms are pituitary-dependent HAC (PDH) and adrenal-dependent HAC (ADH). [1] PDH accounts for 85–90% of naturally occurring HAC and results in hypersecretion of ACTH. [2] ADH accounts for 10–15% and is caused by cortisol-secreting adrenocortical neoplasia (adenoma or carcinoma). [2] Iatrogenic HAC results from excessive exogenous administration of glucocorticoids. [1] More specifically, it results from excessive or prolonged exogenous administration of systemic and/or topical glucocorticoids, including otic preparations. [2] It causes bilateral adrenal atrophy and suppressed ACTH levels. [2] Clinically, iatrogenic HAC is indistinguishable from naturally occurring disease. [2] The evidence provided does not cover how to distinguish them diagnostically beyond the stated differences in cause, ACTH status, and adrenal changes.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.404-408; [2] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.408-409

**18. How does mitotane work in canine hyperadrenocorticism?**
_[Hyperadrenocorticism (Cushing's Syndrome)—Dogs]_

**Book answer:** Mitotane (o,p'-DDD, Lysodren) selectively destroys the glucocorticoid-secreting cells of the adrenal cortex. It is one of two main drugs for pituitary-dependent HAC and may be the drug of choice for adrenal tumors because it may destroy tumor cells too.

**AI answer:** Mitotane works by adrenocorticolysis: it is a cytotoxic drug that causes progressive necrosis of the zona fasciculata and zona reticularis of the adrenal gland. [1][2] In practical terms, mitotane destroys adrenocortical cells. [1][2] It inhibits or destroys the cortisol-producing layers of the adrenal gland. [3] Mitotane is used for medical management of both pituitary-dependent and adrenal-dependent hyperadrenocorticism in dogs. [1][2] The provided evidence explains the adrenal cytotoxic mechanism, but does not cover dosing, monitoring, expected response, adverse effects, or patient selection.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.414-415; [2] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.413-414; [3] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.185-186

**19. What is the initial insulin protocol for diabetic ketoacidosis?**
_[Diabetes Mellitus with Ketoacidosis]_

**Book answer:** Regular insulin is the insulin of choice, starting at 0.2 U/kg IM (or SC if hydration is normal), then 0.1-0.2 U/kg 3-6 hours later, which may be given hourly if needed.

**AI answer:** Regular crystalline insulin is used primarily for the treatment of diabetic ketoacidosis. [1] Initial IM protocol by body weight: <3 kg, 1 Unit/animal IM then 1 Unit/animal q1h [2]; 3–10 kg, 2 Units/animal IM then 1 Unit/animal q1h [2]; >10 kg, 0.25 Units/kg IM then 0.1 Unit/kg IM q1h [2]. The provided evidence covers the initial dosing protocol by weight category, but does not cover monitoring, adjustment criteria, duration of hourly dosing, or transition protocol.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.188-189; [2] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - p.467

**20. What is the starting dose of porcine lente insulin (Vetsulin) in cats?**
_[Diabetes Mellitus without Complication—Cats]_

**Book answer:** 2 U per cat SC q12h. Protamine zinc insulin (PZI, U-40) is a long-acting alternative usually given SC q24h.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages identify Vetsulin as Lente porcine insulin zinc suspension and list it as used/approved in cats, but do not provide a starting dose for cats.)

**Citation(s):** none (no claim cleared the verification gate)

**21. What is the starting dose of Vetsulin in diabetic dogs, and what syringe must be used?**
_[Diabetes Mellitus without Complication—Dogs]_

**Book answer:** 0.75 units/kg SC q12h. It is a U-40 insulin, so it must be used with a U-40 insulin syringe.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages state that Vetsulin is U-40 and that U-40 syringes must be used with U-40 insulin, but do not provide a starting dose of Vetsulin in diabetic dogs.)

**Citation(s):** none (no claim cleared the verification gate)

**22. What is the oral methimazole dose for feline hyperthyroidism, and what is the most effective treatment?**
_[Hyperthyroidism]_

**Book answer:** Methimazole 5-15 mg/day divided q8-12h; it can also be given transdermally in PLO gel, though that is slower. Radioiodine therapy is described as arguably the safest and most effective treatment.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages provide an oral methimazole dose for cats, but do not state which treatment is the most effective — likely causing the combined claim to fail verification.)

**Citation(s):** none (no claim cleared the verification gate)

**23. Which dog breeds are predisposed to hypothyroidism?**
_[Hypothyroidism]_

**Book answer:** Larger breeds such as golden retriever, Doberman pinscher, Great Dane and Irish setter, and some smaller breeds including miniature schnauzer, cocker spaniel, poodle and dachshund. It is most common in middle-aged dogs.

**AI answer:** Predisposed breeds are mostly medium and large breed dogs, including golden retriever, Great Dane, doberman pinscher, Irish setter, Airedale terrier, Old English sheepdog, dachshund, miniature schnauzer, Brittany and cocker spaniel, shar-pei, chow chow, poodle, Irish wolfhound, English bulldog, Newfoundland, malamute, and boxer. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.431-432

**24. What is the long-term prednisone dose for insulinoma if diet fails?**
_[Insulinoma]_

**Book answer:** Start at 0.25 mg/kg PO q12h and increase as needed to 2-3 mg/kg PO q12h. Diazoxide is another option.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages mention insulinoma and hyperglycemic agents, and list prednisone/prednisolone doses in other contexts, but do not provide a long-term prednisone dose for insulinoma if diet fails.)

**Citation(s):** none (no claim cleared the verification gate)

**25. How is hypertension controlled before and during pheochromocytoma surgery?**
_[Pheochromocytoma]_

**Book answer:** With phentolamine 0.02-0.1 mg/kg IV to effect. Boxers, miniature poodles and German shepherds are predisposed, with a median age of 11 years.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages mention some antihypertensive drug classes and vasodilators, but do not discuss hypertension control before or during pheochromocytoma surgery.)

**Citation(s):** none (no claim cleared the verification gate)

**26. How is central diabetes insipidus treated?**
_[Diabetes Insipidus]_

**Book answer:** With DDAVP: 1-2 drops of the intranasal preparation in the conjunctival sac q12-24h, or 2-5 µg SC q12-24h. An oral DDAVP tablet is also available.

**AI answer:** Central diabetes insipidus is treated with ADH. [1] Vasopressin (Pitressin) is listed as a dosage form for ADH. [1] Chlorpropamide (Diabinese, Glucamide) potentiates the action of ADH and may be used to treat mild diabetes insipidus. [2] The provided evidence does not specify dosing, route, monitoring, duration of therapy, or criteria for selecting between ADH/vasopressin and chlorpropamide.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.127-128; [2] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.128-129

**27. What blood pressure values define systemic hypertension in dogs and cats?**
_[Hypertension, Systemic]_

**Book answer:** Systolic above 160 mmHg or diastolic above 120 mmHg, measured by any method.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages mention systemic hypertension but do not provide blood pressure values defining it in dogs and cats.)

**Citation(s):** none (no claim cleared the verification gate)

**28. What is the first-line drug for systemic hypertension in cats?**
_[Hypertension, Systemic]_

**Book answer:** Amlodipine, with an ACE inhibitor added if proteinuria (UPC above 0.4) is present. In dogs an ACE inhibitor is used.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages mention several drugs used to treat hypertension, including in cats, but do not state a first-line drug for systemic hypertension in cats.)

**Citation(s):** none (no claim cleared the verification gate)

**29. Which breeds are at increased risk of severe parvovirus enteritis?**
_[Canine Parvovirus Infection]_

**Book answer:** Rottweiler, Doberman pinscher, American pit bull terrier, Labrador retriever, German shepherd and Yorkshire terrier.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages discuss canine parvovirus vaccination protocols and core vaccine status, but do not identify breeds at increased risk of severe parvovirus enteritis.)

**Citation(s):** none (no claim cleared the verification gate)

**30. What causes canine distemper, and is there an effective antiviral?**
_[Canine Distemper]_

**Book answer:** Canine distemper virus, a Morbillivirus in the Paramyxoviridae family. No antiviral drugs are known to be effective, so treatment is supportive, with broad-spectrum antibiotics for secondary infection because CDV is highly immunosuppressive.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages mention canine distemper virus vaccines, but do not explicitly state what causes canine distemper or whether an effective antiviral exists.)

**Citation(s):** none (no claim cleared the verification gate)

**31. What virus causes feline panleukopenia and what cells does it target?**
_[Feline Panleukopenia]_

**Book answer:** Feline parvovirus, which infects only mitotic (rapidly dividing) cells and causes their acute lysis. Clinically it causes sudden depression, vomiting, diarrhea, severe dehydration and high mortality.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages mention feline panleukopenia vaccination protocols but do not state the causative virus or target cells.)

**Citation(s):** none (no claim cleared the verification gate)

**32. What are the hallmark features of FIP?**
_[Feline Infectious Peritonitis (FIP)]_

**Book answer:** Insidious onset, persistent fever that does not respond to treatment, pyogranulomatous tissue reaction, exudative effusions in body cavities and high mortality.

**AI answer:** Hallmark features of feline infectious peritonitis (FIP; feline coronavirus/FCoV) include ascites, pleural effusion, hepatitis, and uveitis. [1] Skin lesions are rare but, when present, are characterized by vasculitis causing nodules or ulcers and focal necrosis, affecting the head and neck. [1] The provided evidence does not further characterize other hallmark clinical signs, diagnostic findings, or disease forms of FIP.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - p.726

**33. Which FeLV subgroup is most transmissible?**
_[Feline Leukemia Virus Infection (FeLV)]_

**Book answer:** FeLV-A. It is present in all isolates. The other subgroups are B, C and T.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages mention FeLV but do not discuss FeLV subgroups or their transmissibility.)

**Citation(s):** none (no claim cleared the verification gate)

**34. What is the dose of zidovudine for FIV and what must be monitored?**
_[Feline Immunodeficiency Virus Infection (FIV)]_

**Book answer:** 5-15 mg/kg PO q12h. It is most effective against acute infection, and bone marrow toxicity must be monitored.

**AI answer:** Zidovudine (Retrovir/Retrovis) is listed as a direct antiviral agent, most effective against acute FIV infections. [1] Dose for FIV: 5–15 mg/kg PO BID. [1] Monitoring: monitor for bone marrow suppression [1]; anemia and leukopenia are reported adverse effects of AZT [2]; monitor packed cell volume in treated cats and perform a complete blood count periodically [2]. (A separate formulary passage lists a different cat dose of 15 mg/kg q12h PO to 20 mg/kg q8h PO, but the FIV-focused passage used here gives 5–15 mg/kg PO BID.)

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.729-733; [2] Blackwell's Five Minute Veterinary Consult Clinical Companion Small Animal Dermatology ( PDFDrive ) - pp.833-834

**35. What is the typical signalment of dogs with heartworm disease?**
_[Heartworm Disease—Dogs]_

**Book answer:** Medium to large breeds more than small dogs, outdoor more than indoor dogs, most aged 3-8 years, and males more often than females.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing." (Synthesis note: the retrieved passages describe affected species, transmission, and clinical signs of heartworm disease, but do not provide a typical dog signalment such as age, breed, or sex.)

**Citation(s):** none (no claim cleared the verification gate)


**36. What antibiotic is used to clear Leptospira from the kidneys?**
_[Leptospirosis]_

**Book answer:** Dihydrostreptomycin 10-15 mg/kg IM q12h for 2 weeks. Procaine penicillin G is used first until kidney function returns to normal.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state what antibiotic is used to clear Leptospira from the kidneys.)

**Citation(s):** none (no claim cleared the verification gate)

**37. What are the antibiotic options for Lyme disease in dogs?**
_[Lyme Borreliosis]_

**Book answer:** Doxycycline 5-10 mg/kg PO q12h with food, amoxicillin 20 mg/kg PO q8-12h, or azithromycin 25 mg/kg PO q24h. Doxycycline is preferred if Anaplasma phagocytophilum co-infection is present.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention doxycycline for Borrelia in small animals, but they do not explicitly state antibiotic options for Lyme disease in dogs.)

**Citation(s):** none (no claim cleared the verification gate)

**38. What is the treatment of choice for canine ehrlichiosis?**
_[Ehrlichiosis (Anaplasma)]_

**Book answer:** Doxycycline 5 mg/kg PO q12h for 4 weeks, given IV for 5 days if the dog is vomiting.

**AI answer:** Doxycycline is ordinarily considered the drug of choice for Ehrlichia infections in dogs, including canine ehrlichiosis. [1][2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.783-784; [2] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.782-783

**39. What drug is FDA-approved for babesiosis and at what dose?**
_[Babesiosis]_

**Book answer:** Imidocarb dipropionate 6.6 mg/kg SC or IM every 1-2 weeks. It may clear B. canis but not B. gibsoni.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages identify Imizol/imidocarb dipropinate for Babesia in dogs and state treatment consists of two injections over a 2-week interval, but they do not state FDA approval or a dose.)

**Citation(s):** none (no claim cleared the verification gate)

**40. What is the fenbendazole regimen for giardiasis in dogs and cats?**
_[Giardiasis]_

**Book answer:** 50 mg/kg PO q24h for 3 days in dogs or 5 days in cats; a second course may be needed. It should be combined with environmental cleaning and bathing the patient.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention fenbendazole as a drug used for Giardia, but they do not provide a fenbendazole regimen for giardiasis in dogs and cats.)

**Citation(s):** none (no claim cleared the verification gate)

**41. What is the recommended treatment once rabies is diagnosed?**
_[Rabies]_

**Book answer:** There is no treatment. Once the diagnosis is certain, euthanasia is indicated, and suspected cases must be securely isolated.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages discuss rabies vaccination schedules and revaccination, but do not state any recommended treatment once rabies is diagnosed.)

**Citation(s):** none (no claim cleared the verification gate)

**42. What is the initial antibiotic choice for uncomplicated canine infectious respiratory disease?**
_[Canine Infectious Respiratory Disease]_

**Book answer:** Amoxicillin/clavulanic acid 12.5-25 mg/kg PO q12h or doxycycline 5 mg/kg PO q12h.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention a Bordetella bronchiseptica case treated with doxycycline, but they do not state an initial antibiotic choice for uncomplicated canine infectious respiratory disease.)

**Citation(s):** none (no claim cleared the verification gate)

**43. What signs characterize feline herpesvirus infection?**
_[Feline Herpesvirus Infection]_

**Book answer:** Sneezing, fever, rhinitis, conjunctivitis and ulcerative keratitis. Kittens are most susceptible, and brachycephalic breeds get more severe corneal disease and corneal sequestra.

**AI answer:** Based on the provided evidence, feline herpesvirus infection is characterized by:

- Vesicles, blisters, and ulcerations of the facial and nasal regions in feline rhinotracheitis caused by alpha-herpesvirus-1. [1]
- Lesions often associated with upper respiratory infection. [1]
- Presentations that may mimic allergic dermatitis, with head and neck pruritus. [1]
- Herpes virus-associated erythema multiforme, in which skin lesions appear 10 days after infection causing respiratory signs and conjunctivitis. [1]
- Generalized erosive and exfoliative dermatosis in herpes virus-associated erythema multiforme, resolving within a few weeks. [1]

The provided evidence focuses on cutaneous lesions and associated respiratory/conjunctival signs; it does not cover the full clinical spectrum of feline herpesvirus infection.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.726-727

**44. What clinical forms can feline calicivirus cause?**
_[Feline Calicivirus Infection]_

**Book answer:** Upper respiratory disease, oral ulceration, pneumonia, occasionally arthritis, or a highly fatal systemic hemorrhagic disease.

**AI answer:** Feline calicivirus can cause several reported clinical forms:

- **Ocular/oral disease:** conjunctivitis and stomatitis. [1]
- **Vesicular/ulcerative disease and respiratory/systemic outcomes:** vesicles that rapidly ulcerate, URI, pneumonia, acute death, or spontaneous resolution. [1]
- **Skin-only syndrome:** fever, swollen feet, and erosive facial lesions, with the nose predominantly affected. [1] This form has spontaneous resolution in 2–3 days. [1]
- **Feline orofacial pain syndrome:** listed as a calicivirus-associated syndrome; Burmese and Siamese cats are predisposed, and it involves trigeminal neuralgia, unilateral intense pruritus, and may be associated with oral disease. [1]

The provided evidence does not define prevalence, diagnostic criteria, transmission, treatment, or prognosis beyond the spontaneous-resolution statements above.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.726-727

**45. What is the clindamycin dose for toxoplasmosis?**
_[Toxoplasmosis]_

**Book answer:** 25-50 mg/kg PO or IM daily divided into two doses, continued for at least 2 weeks after clinical signs clear. Topical 1% prednisone drops q8h are used for uveitis.

**AI answer:** For feline toxoplasmosis, clindamycin is dosed at **12.5–25 mg/kg PO q12h**.[1] A 4-week course is specified for toxoplasmosis.[2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.775-776; [2] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - p.458

**46. Which dog breeds are predisposed to pancreatitis?**
_[Pancreatitis—Dogs]_

**Book answer:** Miniature schnauzer, Yorkshire terrier and cocker spaniel. Acute pancreatitis is most common in middle-aged and older dogs, with a mean age of 6.5 years.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state which dog breeds are predisposed to pancreatitis.)

**Citation(s):** none (no claim cleared the verification gate)

**47. What are the most common signs of pancreatitis in cats?**
_[Pancreatitis—Cats]_

**Book answer:** Vague, nonspecific signs, most often anorexia, lethargy and vomiting. Siamese cats are predisposed, and the mean age for acute pancreatitis is 7.3 years.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The retrieved passages do not state the most common signs of pancreatitis in cats.)

**Citation(s):** none (no claim cleared the verification gate)

**48. Which breeds are predisposed to exocrine pancreatic insufficiency?**
_[Exocrine Pancreatic Insufficiency]_

**Book answer:** German shepherd dogs, rough-coated collies and Eurasians. In young adult dogs it is usually caused by pancreatic acinar atrophy.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state breeds predisposed to exocrine pancreatic insufficiency.)

**Citation(s):** none (no claim cleared the verification gate)

**49. How are pancreatic enzymes dosed for EPI?**
_[Exocrine Pancreatic Insufficiency]_

**Book answer:** Powdered enzymes mixed into food at 1 teaspoon per 10 kg body weight with each meal, with at least two meals a day. Pre-incubating the enzymes with food does not improve their effect.

**AI answer:** For EPI, pancrelipase powder may be dosed as either:

- **2 tsp mixed with food per 20 kg body weight**, or  
- **1–3 tsp per 0.45 kg of food**, mixed **20 minutes before feeding**. [1]

The provided evidence does not cover dose adjustment, monitoring, alternative enzyme formulations, or species-specific recommendations beyond this dosing statement.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.475-476

**50. What is GDV and which dogs are at risk?**
_[Gastric Dilation and Volvulus Syndrome]_

**Book answer:** A condition where the stomach dilates and then rotates around its short axis. Large, deep-chested breeds such as Great Danes and German shepherds are at risk, and risk increases with age.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not define GDV or state which dogs are at risk for GDV.)

**Citation(s):** none (no claim cleared the verification gate)

**51. What is megaesophagus and which cats are predisposed?**
_[Megaesophagus]_

**Book answer:** A focal or generalized dilation of the esophagus with reduced or absent peristalsis. Siamese and Siamese-related cats are predisposed.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not define megaesophagus or identify predisposed cats.)

**Citation(s):** none (no claim cleared the verification gate)

**52. Which dogs are most commonly affected by hemorrhagic gastroenteritis?**
_[Gastroenteritis, Hemorrhagic]_

**Book answer:** Small and toy breeds, especially miniature schnauzer, dachshund, Yorkshire terrier and miniature poodle. It usually affects adults with a mean age of 5 years.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages include a case scenario of hemorrhagic gastroenteritis but do not state which dogs are most commonly affected.)

**Citation(s):** none (no claim cleared the verification gate)

**53. How is IBD categorized?**
_[Inflammatory Bowel Disease]_

**Book answer:** By the predominant mucosal cellular infiltrate, for example lymphocytic-plasmacytic. It is a group of chronic enteropathies with persistent or intermittent GI signs and histologic intestinal inflammation.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not describe how IBD is categorized.)

**Citation(s):** none (no claim cleared the verification gate)

**54. What cytology finding supports hepatic lipidosis in cats?**
_[Hepatic Lipidosis]_

**Book answer:** On fine-needle liver aspiration, more than 80% of hepatocytes show severe cytosolic vacuolation. Vitamin K1 is recommended for all cats with suspected lipidosis.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages mention hepatic lipidosis only as part of feline paraneoplastic syndrome/differentials and do not state a cytology finding that supports hepatic lipidosis in cats.)

**Citation(s):** none (no claim cleared the verification gate)

**55. Where are congenital portosystemic shunts usually located in small dogs and cats?**
_[Portosystemic Vascular Anomaly, Congenital]_

**Book answer:** Extrahepatic shunts are more common in small-breed dogs and cats. Small purebred and mixed 'terrier' dogs are at higher risk.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not discuss congenital portosystemic shunts or their usual locations in small dogs and cats.)

**Citation(s):** none (no claim cleared the verification gate)

**56. How long must kidney disease be present to be called chronic?**
_[Renal Failure, Chronic]_

**Book answer:** More than 3 months. Mean age at diagnosis is about 7 years in dogs and 9 years in cats.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages state that renal failure may be differentiated as acute, chronic, or end-stage, but they do not state how long kidney disease must be present to be called chronic.)

**Citation(s):** none (no claim cleared the verification gate)

**57. How is prerenal azotemia distinguished from acute kidney injury?**
_[Renal Failure, Acute]_

**Book answer:** Prerenal azotemia has concentrated urine (USG at least 1.030 in dogs and 1.035 in cats) and is correctable with fluid repletion.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention that renal damage may be categorized as prerenal, renal, or postrenal, but they do not state how prerenal azotemia is distinguished from acute kidney injury.)

**Citation(s):** none (no claim cleared the verification gate)

**58. Can calcium oxalate uroliths be dissolved medically?**
_[Urolithiasis, Calcium Oxalate]_

**Book answer:** No. No available drugs effectively dissolve them, so they are removed. Steroids and furosemide should be used with care because they promote calciuria.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention management or treatment of calcium oxalate uroliths, but they do not state whether calcium oxalate uroliths can be dissolved medically.)

**Citation(s):** none (no claim cleared the verification gate)

**59. Which six dog breeds make up 60% of calcium oxalate urolith cases?**
_[Urolithiasis, Calcium Oxalate]_

**Book answer:** Miniature schnauzer, Lhasa apso, Yorkshire terrier, bichon frise, shih tzu and miniature poodle.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages mention calcium oxalate urolithiasis and breeds predisposed to urinary bladder stones, but they do not state which six dog breeds make up 60% of calcium oxalate urolith cases.)

**Citation(s):** none (no claim cleared the verification gate)

**60. What are most uroliths in dogs under 12 months old?**
_[Urolithiasis, Struvite—Dogs]_

**Book answer:** Infection-induced struvite (magnesium ammonium phosphate) uroliths.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages discuss urolithiasis management and related drugs but do not state what most uroliths are in dogs under 12 months old.)

**Citation(s):** none (no claim cleared the verification gate)

**61. Which breeds are predisposed to urate uroliths?**
_[Urolithiasis, Urate]_

**Book answer:** Dalmatians, English bulldogs, and breeds at risk of portosystemic shunts such as Yorkshire terriers.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention ammonium acid urate uroliths and separately mention dog breeds predisposed to urinary bladder stones, but they do not state which breeds are predisposed to urate uroliths.)

**Citation(s):** none (no claim cleared the verification gate)

**62. When after estrus do dogs and cats with pyometra usually present?**
_[Pyometra]_

**Book answer:** Dogs within 12 weeks after their last estrus, and cats within 4 weeks of their last estrus. It is life-threatening when the cervix is closed and the bitch is systemically ill.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state when after estrus dogs and cats with pyometra usually present.)

**Citation(s):** none (no claim cleared the verification gate)

**63. When does eclampsia usually occur and which breeds are at risk?**
_[Eclampsia]_

**Book answer:** Usually 1-4 weeks postpartum, most often before day 40. It is most common in toy breeds such as Chihuahua, miniature pinscher, Shih Tzu, miniature poodle and Pomeranian, and in first litters.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not discuss eclampsia, its usual timing, or breeds at risk.)

**Citation(s):** none (no claim cleared the verification gate)

**64. How is eclampsia treated in the bitch?**
_[Eclampsia]_

**Book answer:** 10% calcium gluconate 0.22-0.44 mL/kg IV slowly over 5 minutes to effect, monitoring heart rate or ECG. Hyperthermia and hypoglycemia are corrected, and she is sent home on oral calcium 10-30 mg/kg PO q8h.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The retrieved passages do not state how eclampsia is treated in the bitch.)

**Citation(s):** none (no claim cleared the verification gate)

**65. Why are brachycephalic breeds prone to dystocia?**
_[Dystocia]_

**Book answer:** Because they combine a broad fetal head with a narrow maternal pelvis, as in the Bulldog, Boston terrier and pug.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The retrieved passages do not discuss dystocia or why brachycephalic breeds are prone to it.)

**Citation(s):** none (no claim cleared the verification gate)

**66. Which breeds are at high risk of lymphoma?**
_[Lymphoma—Dogs]_

**Book answer:** Boxer, basset hound, golden retriever, Saint Bernard, Scottish terrier, Airedale terrier and bulldog. Dachshunds and Pomeranians are low-risk.

**AI answer:** Based on the provided evidence, the only breed identified in association with lymphoma is the Airedale terrier. [1]

The evidence does not provide a comprehensive list of breeds at high risk of lymphoma, nor does it quantify risk.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.743-746

**67. What is the typical age of cats with lymphoma by FeLV status?**
_[Lymphoma—Cats]_

**Book answer:** About 3 years in FeLV-positive cats and 7 years in FeLV-negative cats. Lymphoma is also the most common spinal cord tumor in cats.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention FeLV-associated lymphoma and age ranges for some cutaneous lymphoma categories in cats, but they do not give typical cat ages with lymphoma by FeLV status.)

**Citation(s):** none (no claim cleared the verification gate)

**68. What is the standard chemotherapy after amputation for canine osteosarcoma?**
_[Osteosarcoma]_

**Book answer:** A platinum drug (cisplatin or carboplatin) or doxorubicin, with at least four doses recommended.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages list chemotherapeutic drugs with osteosarcoma as an indication, but they do not state the standard chemotherapy after amputation for canine osteosarcoma.)

**Citation(s):** none (no claim cleared the verification gate)

**69. What proportion of canine splenic tumors are hemangiosarcomas, and which breeds are predisposed?**
_[Hemangiosarcoma, Spleen and Liver]_

**Book answer:** Up to 70%. German shepherds, Labrador retrievers and golden retrievers are predisposed.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state the proportion of canine splenic tumors that are hemangiosarcomas or the breeds predisposed.)

**Citation(s):** none (no claim cleared the verification gate)

**70. What is the vinblastine and prednisone protocol for canine mast cell tumors?**
_[Mast Cell Tumors]_

**Book answer:** Vinblastine 2.0 mg/m2 IV every 7 days for 4 doses, then every 14 days for 4 doses, with prednisone 1 mg/kg PO q24h.

**AI answer:** For dogs with mast cell tumors, the provided protocol is vinblastine 2 mg/m² IV every 7 days for four treatments, then every 14 days, with prednisolone 1 mg/kg PO every 24 hours. [1]

The verified evidence provided specifies prednisolone, not prednisone. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.512-513

**71. What proportion of feline mammary tumors are malignant?**
_[Mammary Gland Tumors—Cats]_

**Book answer:** 85-95%, mostly carcinomas. Siamese cats have twice the risk of other breeds.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state the proportion of feline mammary tumors that are malignant.)

**Citation(s):** none (no claim cleared the verification gate)

**72. What is the mean age of dogs with malignant versus benign mammary tumors?**
_[Mammary Gland Tumors—Dogs]_

**Book answer:** 9-11 years for malignant and 7-9 years for benign tumors. They are uncommon in dogs under 5 years.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages discuss mast cell tumors and other skin tumors, but they do not state the mean age of dogs with malignant versus benign mammary tumors.)

**Citation(s):** none (no claim cleared the verification gate)

**73. What is the vincristine protocol for transmissible venereal tumor?**
_[Transmissible Venereal Tumor]_

**Book answer:** 0.5-0.7 mg/m2 IV once weekly, continued for 2 weeks beyond complete resolution of visible disease. Doxorubicin can be tried if remission is partial.

**AI answer:** For dogs and cats with transmissible venereal tumor, the provided evidence supports vincristine at **0.5–0.7 mg/m² IV weekly**, or on a schedule dictated by any concurrent anticancer drugs. [1]

The provided evidence does **not** specify total number of treatments, treatment endpoint, response monitoring, contraindications, adverse-effect management, or protocol modifications.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.348-349

**74. Which breeds are predisposed to dilated cardiomyopathy?**
_[Cardiomyopathy, Dilated—Dogs]_

**Book answer:** Doberman pinscher and boxer, giant breeds (Scottish deerhound, Irish wolfhound, Great Dane, Saint Bernard, Afghan hound, Newfoundland), cocker spaniel and Portuguese water dog.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not mention dilated cardiomyopathy or breeds predisposed to it.)

**Citation(s):** none (no claim cleared the verification gate)

**75. Which cat breeds are predisposed to hypertrophic cardiomyopathy?**
_[Cardiomyopathy, Hypertrophic—Cats]_

**Book answer:** Maine coon, ragdoll, Sphynx, British and American shorthairs, and Persians. Typical age is 5-7 years.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state which cat breeds are predisposed to hypertrophic cardiomyopathy.)

**Citation(s):** none (no claim cleared the verification gate)

**76. What furosemide dose is used for a critically dyspneic cat with HCM?**
_[Cardiomyopathy, Hypertrophic—Cats]_

**Book answer:** 4 mg/kg IV, which can be repeated in 1 hour if the cat is still severely dyspneic. The usual dose is 1-2 mg/kg q8-24h.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages list a general Cat furosemide dosage, but they do not state a furosemide dose specifically for a critically dyspneic cat with HCM.)

**Citation(s):** none (no claim cleared the verification gate)

**77. Which dogs typically develop myxomatous mitral valve disease?**
_[Atrioventricular Valve (Myxomatous) Disease]_

**Book answer:** Small breeds under 20 kg, such as Cavalier King Charles spaniels, Chihuahuas, miniature schnauzers, Maltese, Pomeranians, cocker spaniels, Pekingese and poodles.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not discuss myxomatous mitral valve disease or which dogs typically develop it.)

**Citation(s):** none (no claim cleared the verification gate)

**78. What is a patent ductus arteriosus and when is it usually found?**
_[Patent Ductus Arteriosus]_

**Book answer:** Persistent patency of the fetal ductus connecting the descending aorta to the pulmonary artery. Most are found during the initial vaccination visits, and females are predisposed in many breeds.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not define patent ductus arteriosus or state when it is usually found.)

**Citation(s):** none (no claim cleared the verification gate)

**79. What is the main feature of boxer cardiomyopathy?**
_[Cardiomyopathy—Boxer (Arrhythmogenic Right Ventricular)]_

**Book answer:** Ventricular tachyarrhythmias, which may cause syncope or sudden death. Fewer than 5% of dogs develop congestive heart failure with systolic dysfunction.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention “Boxer” cardiomyopathy as a prevalent cardiovascular disease but do not state its main feature.)

**Citation(s):** none (no claim cleared the verification gate)

**80. When should antiepileptic treatment be started in a dog with genetic epilepsy?**
_[Epilepsy, Genetic (Idiopathic)—Dogs]_

**Book answer:** At the second generalized seizure if the dog is under 2 years old, and in other dogs when the interval between seizures is gradually getting shorter.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages include some antiepileptic drug dosages but do not state when antiepileptic treatment should be started in a dog with genetic epilepsy.)

**Citation(s):** none (no claim cleared the verification gate)

**81. Which breeds get Hansen type I disc disease?**
_[Intervertebral Disc Disease, Thoracolumbar]_

**Book answer:** Dachshund, shih tzu, Lhasa apso, Pekingese, cocker spaniel, Welsh corgi, and toy and miniature poodles. Type II disease affects mainly large breeds.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not mention Hansen type I disc disease or breeds affected by it.)

**Citation(s):** none (no claim cleared the verification gate)

**82. Which breed accounts for about half of wobbler syndrome cases?**
_[Cervical Spondylomyelopathy (Wobbler Syndrome)]_

**Book answer:** The Doberman pinscher. Great Dane, rottweiler, Weimaraner and Dalmatian also have a high incidence.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not mention wobbler syndrome or a breed accounting for about half of its cases.)

**Citation(s):** none (no claim cleared the verification gate)

**83. What gene mutation causes degenerative myelopathy, and is there an effective drug?**
_[Degenerative Myelopathy]_

**Book answer:** A mutation in the superoxide dismutase 1 gene (SOD1). No drug has been proven to slow or halt progression.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state the gene mutation causing degenerative myelopathy or whether an effective drug exists.)

**Citation(s):** none (no claim cleared the verification gate)

**84. What is the pyridostigmine dose for myasthenia gravis?**
_[Myasthenia Gravis]_

**Book answer:** 1-3 mg/kg PO q8-12h, with the syrup diluted half and half in water.

**AI answer:** Pyridostigmine bromide antimyasthenic dosing: **0.02–0.04 mg/kg IV q2h** or **0.5–3 mg/kg PO q8–12h**. [1]

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.479-480

**85. What is geriatric vestibular disease in dogs?**
_[Vestibular Disease, Geriatric—Dogs]_

**Book answer:** An acute, non-progressive disturbance of the peripheral vestibular system in older dogs, usually over 8 years old. The cause is unknown.

**AI answer:** Geriatric vestibular disease in dogs is described in the provided evidence as **idiopathic vestibular disease in older dogs**. [1]

Its diagnosis is made **by exclusion of other causes**. [1]

The provided evidence does not further describe clinical signs, pathophysiology, treatment, prognosis, or specific exclusion criteria.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.559-560

**86. Which breeds have an increased incidence of cranial cruciate ligament disease at a young age?**
_[Cruciate Ligament Disease, Cranial]_

**Book answer:** Rottweilers and Labrador retrievers under 4 years old. The West Highland white terrier is the overrepresented small breed.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state which breeds have an increased incidence of cranial cruciate ligament disease at a young age.)

**Citation(s):** none (no claim cleared the verification gate)

**87. Which dogs are most commonly affected by patellar luxation?**
_[Patellar Luxation]_

**Book answer:** Toy and miniature breeds, such as miniature and toy poodles, Yorkshire terriers, Pomeranians, Pekingese, Chihuahuas and Boston terriers.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state which dogs are most commonly affected by patellar luxation.)

**Citation(s):** none (no claim cleared the verification gate)

**88. What is panosteitis and at what age does it usually occur?**
_[Panosteitis]_

**Book answer:** A self-limiting, painful condition of the long bones of young medium to large-breed dogs, seen radiographically as increased marrow density. It usually occurs at 5-18 months of age, mostly in males.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The retrieved passages discuss panniculitis, not panosteitis.)

**Citation(s):** none (no claim cleared the verification gate)

**89. Which breeds are predisposed to Demodex canis demodicosis?**
_[Demodicosis]_

**Book answer:** American Staffordshire terrier, Shar-Pei, Boston terrier, English bulldog and West Highland white terrier.

**AI answer:** Demodex canis is the most common mite identified in dogs with demodicosis. [1]

Increased incidence of demodicosis is reported in these purebred dogs: American Staffordshire terriers and Staffordshire bull terriers, Chinese shar-peis, Boston terriers, West Highland white terriers, and French and English bulldogs. [1]

The evidence provided reports increased incidence in these breeds but does not further define predisposition beyond this list.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.310-311

**90. Which cats and dogs are predisposed to dermatophytosis?**
_[Dermatophytosis]_

**Book answer:** Longhaired cats such as Persians and Himalayans, and Yorkshire and Manchester terriers. M. canis is more common in younger animals.

**AI answer:** Predisposed cats and dogs include:

- **Cats in long-haired breeds**, in which dermatophytosis is more common and persistent subclinical infection is increased. [1]
- **Young and older animals**, in which clinical signs are more common. [1]
- **Animals with prior confirmed infection, or exposure to an infected animal or contaminated environment**, such as a cattery. [1][2]
- **Animals in catteries, shelters, or other high-population-density settings**, which are risk environments for dermatophytosis. [1][2]
- **Animals in hot, humid regions**, where both asymptomatic carriage and clinical infection are more common. [1]
- **Immunocompromised animals**, including those immunocompromised by disease or medications such as corticosteroids. [1][2]
- **FIV-positive cats**, which have a threefold higher prevalence of dermatophytosis. [1][2]
- **Animals affected by poor nutrition, poor management practices, lack of adequate quarantine, or excessive bathing and grooming.** [2]

The provided evidence gives specific breed predisposition only for **cats**—long-haired breeds. [1] It does not provide dog-specific breed predispositions.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.333-335; [2] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.335-336

**91. How is selamectin used for scabies in dogs?**
_[Sarcoptic Mange]_

**Book answer:** It is labeled every 30 days, but application every 2 weeks for at least three treatments may be more effective.

**AI answer:** For canine scabies due to *Sarcoptes scabiei*, selamectin is used at 6–12 mg/kg applied topically every 2 weeks for 3–4 treatments in dogs. [1]

All in-contact dogs should also be treated, even if they have no clinical signs, because asymptomatic carriers are possible. [2]

The provided evidence does not cover contraindications, safety precautions, monitoring, or comparative efficacy.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.651-652; [2] Blackwell's Five Minute Veterinary Consult Clinical Companion   Small Animal Dermatology ( PDFDrive ) - pp.650-651

**92. What intraocular pressure is diagnostic of glaucoma in dogs and cats?**
_[Glaucoma]_

**Book answer:** Above 25-30 mmHg in dogs and above 31 mmHg in cats.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages discuss drugs that reduce IOP and glaucoma treatment, but they do not state an intraocular pressure diagnostic for glaucoma in dogs or cats.)

**Citation(s):** none (no claim cleared the verification gate)

**93. What Schirmer tear test values indicate KCS in dogs?**
_[Keratoconjunctivitis Sicca]_

**Book answer:** Normal is at least 15 mm/min of wetting; symptomatic dogs usually have less than 10 mm/min. Treatment uses lacrimostimulants such as cyclosporine 0.2% ointment or tacrolimus q12h.

**AI answer:** The provided evidence does **not** give a general diagnostic cutoff for KCS in dogs.

It states that a normal Schirmer tear test value is **15–20 mm/min**.[1] In the cited KCS case, the Schirmer tear test was **8 mm/min in the right eye** and **15 mm/min in the left eye**.[1] The case diagnosis was **keratoconjunctivitis sicca (KCS), also known as “dry eye.”**[1]

So, from the supplied evidence, **8 mm/min was associated with KCS in that case**, while **15–20 mm/min is given as normal**.[1] A broader threshold for diagnosing KCS is not covered by the provided evidence.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - p.352

**94. Why should the prolapsed third eyelid gland be replaced rather than removed?**
_[Prolapsed Gland of the Third Eyelid (Cherry Eye)]_

**Book answer:** Because the gland produces up to 50% of the aqueous tear film, and excising it predisposes to KCS. Surgical replacement (imbrication technique) is recommended.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages discuss KCS and tear production but do not state why a prolapsed third eyelid gland should be replaced rather than removed.)

**Citation(s):** none (no claim cleared the verification gate)

**95. What cough suppressants are used for tracheal collapse?**
_[Tracheal and Airway Collapse]_

**Book answer:** Butorphanol 0.5-1 mg/kg PO q4-8h or hydrocodone 0.22 mg/kg PO q4-8h, reduced to the least frequent dosing that controls the cough.

**AI answer:** For tracheal collapse, the provided evidence specifically identifies **butorphanol** as an antitussive used in a presumptive diagnosis of tracheal collapse to help reduce irritation in the trachea.[1]

More generally, **butorphanol tartrate** is used for relief of chronic nonproductive coughs in dogs.[2][3]

The provided evidence does not cover other cough suppressants used for tracheal collapse.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.424-425; [2] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.114-115; [3] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - p.115

**96. What components make up brachycephalic airway syndrome?**
_[Brachycephalic Airway Syndrome]_

**Book answer:** Stenotic nares, overlong soft palate, everted laryngeal saccules and laryngeal collapse; a hypoplastic trachea may also be present. English bulldogs are most commonly affected (up to 55% of the breed).

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The retrieved passages do not state the components of brachycephalic airway syndrome.)

**Citation(s):** none (no claim cleared the verification gate)

**97. What is the emergency treatment for a cat in an asthma crisis?**
_[Asthma, Bronchitis—Cats]_

**Book answer:** Oxygen and a parenteral bronchodilator such as terbutaline 0.01 mg/kg IV or SC, repeated if there is no improvement in 20-30 minutes.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention feline asthma, respiratory distress, oxygen, bronchodilation drug classes, and corticosteroids, but they do not state an emergency treatment protocol for a cat in an asthma crisis.)

**Citation(s):** none (no claim cleared the verification gate)

**98. What is the starting corticosteroid dose for IMHA and when is it reduced?**
_[Anemia, Immune-Mediated]_

**Book answer:** Prednisone 1-2 mg/kg/day divided q12h for 2-4 weeks (prednisolone in cats). Once the PCV is above 30%, the dose drops to 1 mg/kg q12h and is then tapered by no more than 25-50% per month over 3-6 months.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state a corticosteroid starting dose specifically for IMHA or when it is reduced.)

**Citation(s):** none (no claim cleared the verification gate)

**99. How is desmopressin used before surgery in dogs with von Willebrand disease?**
_[Von Willebrand Disease]_

**Book answer:** 1 µg/kg SC given 30 minutes before surgery in dogs with mild to moderate Type 1 vWD. The response is variable.

**AI answer:** For dogs with von Willebrand disease, desmopressin acetate is listed at **1 mcg/kg SC or IV**; if given IV, it is **diluted in 20 mL saline and administered over 10 min**.[1]

The provided evidence does **not** specify the timing of administration relative to surgery, repeat dosing, monitoring, or case selection.

**Citation(s):** [1] Applied Pharmacology for Veterinary Technicians, 6th Edition (1) - pp.459-460

**100. Which animals are predisposed to heat stroke?**
_[Heat Stroke and Hyperthermia]_

**Book answer:** Longhaired and brachycephalic animals, very young or old animals, young dogs that overexert, and old dogs with preexisting disease. Cats are uncommonly affected.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages do not state which animals are predisposed to heat stroke.)

**Citation(s):** none (no claim cleared the verification gate)
