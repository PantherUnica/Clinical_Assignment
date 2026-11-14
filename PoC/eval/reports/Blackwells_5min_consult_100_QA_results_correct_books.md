# Blackwell's Five-Minute Veterinary Consult: Canine and Feline: AI answers vs book answers (correct books indexed)

Each question was run through the VetAI PoC pipeline (retrieve → synthesize → verify → generate) with the index built from only the BSAVA formulary and Blackwell's Canine & Feline. The **book answer** is the answer key; the **AI answer** and **citations** are what the system produced. Citations show the book and page of the passage each claim was verified against.
**Answered with citations: 96 of 100.**


**1. Why are cats more susceptible to acetaminophen toxicosis than dogs?**
_[Acetaminophen (APAP) Toxicosis]_

**Book answer:** Cats cannot effectively glucuronidate acetaminophen because of a genetic deficiency in the glucuronide conjugation pathway. They can be poisoned by as little as 50-60 mg/kg (often half a tablet), and rapidly develop methemoglobinemia.

**AI answer:**

Cats are more susceptible to acetaminophen toxicosis than dogs because they have markedly limited elimination capacity: cats cannot effectively glucuronidate and therefore eliminate acetaminophen less well than dogs. [1]

Mechanistically, cats have a genetic deficiency in the glucuronide conjugation pathway, making them vulnerable. [1] They also saturate both glucuronidation and sulfation biotransformation routes. [1] As a result, cats develop the toxic cytochrome P450 metabolite at much lower doses than dogs. [1]

Following glutathione depletion, feline RBCs are most susceptible to oxidative injury. [1]

The provided evidence explains the comparative susceptibility in terms of impaired conjugation/elimination, earlier formation of the toxic metabolite, and RBC oxidative injury; it does not provide additional comparative clinical signs, dose thresholds, or treatment information.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.80

_Claims: 5 verified / 5 proposed · 8.658s_

**2. What is the N-acetylcysteine protocol for acetaminophen toxicosis?**
_[Acetaminophen (APAP) Toxicosis]_

**Book answer:** A loading dose of 140 mg/kg diluted in D5W PO or IV, then 70 mg/kg diluted in D5W PO or IV q6h for 5-7 more treatments. Activated charcoal 2 g/kg PO is given right after emesis or gastric lavage, and SAMe can be added as a glutathione donor.

**AI answer:**

For dogs and cats with paracetamol (acetaminophen) poisoning, after inducing emesis, use acetylcysteine immediately if ingestion occurred within 24 hours. [1] Acetylcysteine reduces the extent of liver injury in cases of paracetamol poisoning. [1]

**IV protocol option:**  
- 150 mg/kg by IV infusion in 200 mL 5% glucose over 15 min, then [1]  
- 50 mg/kg IV infusion in 500 mL over 4 hours, then [1]  
- 100 mg/kg IV infusion in 1000 mL over 16 hours. [1]

**Oral protocol option:**  
- 140 mg/kg loading dose PO, then [1]  
- 70 mg/kg PO q4h for 17 doses unless initial serum paracetamol levels indicate a non-toxic level. [1]

For oral administration, dilute the oral solution to a 5% solution and give via a stomach tube, as it tastes unpleasant. [1]

The provided evidence does not cover monitoring parameters, adverse effects, contraindications, or protocol modifications.

**Citation(s):** [1] BSAVA formulations document - pp.21-22

_Claims: 5 verified / 5 proposed · 14.064s_

**3. What is the fomepizole dosing schedule for ethylene glycol toxicosis in dogs?**
_[Ethylene Glycol Toxicosis]_

**Book answer:** 20 mg/kg IV initially, then 15 mg/kg IV at 12 and 24 hours, then 5 mg/kg IV at 36 hours. The book describes fomepizole as an effective, non-toxic liver alcohol dehydrogenase inhibitor that needs less intensive care than ethanol.

**AI answer:**

For dogs with ethylene glycol toxicosis, the fomepizole (4-methyl pyrazole; Antizol-Vet) dosing schedule is:

- **Loading dose:** 20 mg/kg IV initially, using the 5% formulation (50 mg/mL). [1][2] This may be administered over **15–20 minutes**. [3]
- **12 hours:** 15 mg/kg IV. [1][2][3]
- **24 hours:** 15 mg/kg IV. [1][2][3]
- **36 hours:** 5 mg/kg IV. [1][2][3]

The verified evidence provided covers the dosing schedule, formulation concentration, route, and loading-dose infusion duration; it does not provide any additional monitoring, adjustment, or patient-specific modification guidance.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.538-539; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.539; [3] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1494-1495

_Claims: 4 verified / 4 proposed · 10.484s_

**4. Which methylxanthine makes up the largest fraction in chocolate?**
_[Chocolate (Methylxanthine) Toxicosis]_

**Book answer:** Theobromine. Chocolate toxicosis causes acute gastroenteric, neurologic and cardiac signs from excessive intake of methylxanthine alkaloids.

**AI answer:**

Theobromine makes up the largest fraction of methylxanthines in chocolate products. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.326

_Claims: 1 verified / 1 proposed · 4.395s_

**5. What are the main effects of xylitol ingestion in dogs, and how fast do signs appear?**
_[Xylitol Toxicosis]_

**Book answer:** Vomiting, weakness, ataxia, seizures, hypoglycemia and hypokalemia, and in some dogs hepatic failure. Signs may develop within 15-30 minutes, but with sugar-free gums hypoglycemia may be delayed up to 12 hours.

**AI answer:**

**Main effects in dogs**

- Xylitol ingestion can cause vomiting, weakness, ataxia, seizures, hypokalemia, hypophosphatemia/hyperphosphatemia, and hypoglycemia due to excess insulin release.[1]
- Progressive lethargy, weakness, ataxia, collapse, and seizures may occur.[1]
- Mild to moderate ALT elevations can be seen within 4 hours of ingestion.[1]
- Hepatic failure with high liver enzymes, hyperbilirubinemia, and coagulopathy may occur at dosages >0.5 g/kg.[1]
- Dosages >0.075–0.1 g/kg may cause hypoglycemia.[1]

**Onset of signs**

- Signs may develop within 15–30 minutes of exposure.[1]
- With sugar-free gums, hypoglycemia may be delayed up to 12 hours.[1]
- The provided evidence does not specify the onset time for hepatic failure.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1483

_Claims: 7 verified / 7 proposed · 17.107s_

**6. What is the recommended fluid therapy after grape or raisin ingestion in a dog?**
_[Grape, Raisin, and Currant Toxicosis]_

**Book answer:** Fluid diuresis at 2-3 times maintenance for at least 48 hours, longer if renal failure develops, after GI decontamination with emesis and activated charcoal.

**AI answer:**

After grape or raisin ingestion in a dog, recommended fluid therapy is fluid diuresis at 2–3 times maintenance for a minimum of 48 hours; continue longer if renal failure develops. [1]

0.9% NaCl is most commonly recommended, although fluid choice may vary with circumstance. [1]

Correct fluid imbalances such as dehydration, and monitor fluid in/out during therapy. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.634

_Claims: 4 verified / 4 proposed · 7.736s_

**7. Which species is at risk of systemic lily poisoning, and what organ is affected?**
_[Lily Toxicosis]_

**Book answer:** Cats. Ingestion of Lilium or Hemerocallis (daylily) leaves or flowers causes a severe nephrotoxic syndrome, with as little as 2-3 leaves reported to be dangerous. Dogs only get mild GI upset.

**AI answer:**

Cats are at risk of systemic lily poisoning.[1]

The affected organ is the kidney: ingestion of leaves or flowers results in a severe nephrotoxic syndrome,[2] and gross pathologic findings include swollen kidneys.[1]

Dogs are reported to develop only mild gastrointestinal upset, even after ingestion of large quantities of plant material.[1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.874; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.873-874

_Claims: 4 verified / 4 proposed · 11.413s_

**8. Why is the coagulopathy from anticoagulant rodenticides delayed?**
_[Rodenticide Toxicosis—Anticoagulants]_

**Book answer:** Because it results from depletion of the vitamin K1-dependent clotting factors II, VII, IX and X, so onset is delayed by 3-5 days.

**AI answer:**

Anticoagulant rodenticides cause a delayed-onset coagulopathy because they interfere with vitamin K1 recycling rather than directly disrupting clot formation immediately. They inhibit vitamin K1 epoxide reductase, DT diaphorase, and possibly other enzymes involved in reducing vitamin K1 epoxide back to vitamin K1. [2]

Vitamin K1 is required for carboxylation of clotting factors II, VI, IX, and X; without adequate carboxylation, these clotting factors do not bind calcium sufficiently to participate in clot formation. [2] Anticoagulant rodenticide intoxication therefore produces a coagulopathy after a delay of about 3–5 days, associated with reduction of vitamin K1–dependent clotting factors II, VII, IX, and X. [1]

The provided evidence establishes the mechanism of impaired vitamin K1 recycling and the observed 3–5 day delay, but it does not further specify why that interval is 3–5 days rather than another duration.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1256-1257; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1257

_Claims: 3 verified / 3 proposed · 14.678s_

**9. How long is vitamin K1 given for first- versus second-generation anticoagulant rodenticides?**
_[Rodenticide Toxicosis—Anticoagulants]_

**Book answer:** 2.5-5.0 mg/kg PO: q12h for 5-7 days for most first-generation products, and q24h for 4-6 weeks for most second-generation products. Feeding a little fat may improve absorption.

**AI answer:**

For **most first-generation anticoagulant rodenticides**, vitamin K1 is given for **5–7 days** at **2.5–5.0 mg/kg PO q12h**. [1]

For **most second-generation anticoagulant rodenticides**, vitamin K1 is given for **4–6 weeks** at **2.5–5.0 mg/kg PO q24h**. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1257-1258

_Claims: 2 verified / 2 proposed · 11.59s_

**10. Which dogs are most susceptible to ivermectin toxicosis?**
_[Ivermectin and Other Macrocyclic Lactones Toxicosis]_

**Book answer:** Collies are most commonly affected, along with dogs homozygous for the ABCB1 gene deletion (found in Shetland sheepdogs, Australian shepherds and others). Heterozygous dogs can react at higher doses.

**AI answer:**

Dogs most susceptible to ivermectin toxicosis are:

- **Collies**, which are most commonly affected by ivermectin and other macrocyclic lactone toxicosis. [1]
- **Dogs homozygous for the ABCB1 gene deletion**; **heterozygous dogs can react at higher doses**. [1]
- Breeds in which the **ABCB1 mutation has been found**, including **Shetland sheepdogs, Australian shepherds, Old English sheepdogs, German shepherds, English shepherds, longhaired whippets, silken windhounds**, and **mixed-breed dogs**. [1]
- **Collies, Shetland sheepdogs, Old English sheepdogs, Australian shepherds, other herding breeds, and crosses with these breeds**, in which ivermectin is contraindicated. [2]

The provided evidence identifies susceptible breeds and ABCB1 genotype risk, but does not quantify relative risk among the non-collie breeds.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.840-841; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.426

_Claims: 4 verified / 4 proposed · 9.979s_

**11. Why is metaldehyde called the 'shake and bake' toxicant?**
_[Metaldehyde Toxicosis]_

**Book answer:** Because of its characteristic tremors, seizures and hyperthermia. Signs usually develop within 4 hours of ingestion, and there is no specific antidote.

**AI answer:**

Metaldehyde is called the “shake and bake” toxicant because it is associated with characteristic tremors and seizures—the “shake”—and hyperthermia—the “bake.” [1][2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.946; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.945-946

_Claims: 1 verified / 1 proposed · 5.82s_

**12. How can cats be exposed to permethrin toxicity, and what treats the tremors?**
_[Pyrethrin and Pyrethroid Toxicosis]_

**Book answer:** Through direct contact with dogs treated with permethrin spot-ons. Tremors and seizures are treated with methocarbamol 55-220 mg/kg IV, not exceeding 330 mg/kg/day.

**AI answer:**

Cats can be exposed to permethrin toxicity by misapplication of permethrin-containing dog-only flea products directly on cats.[1] Reactions may also occur through direct contact with dogs treated with permethrin spot-on products.[2]

Cats inappropriately treated with permethrin-containing dog products often develop muscle tremors, ataxia, seizures, hyperthermia, and death within hours if not treated.[2]

For tremors or seizures in cats exposed to permethrin, methocarbamol is used: injectable methocarbamol 55–220 mg/kg IV, not to exceed 330 mg/kg/day; administer one-half dose slowly IV, wait until the patient begins to relax, then continue to effect; do not exceed 2 mL/min injection rate, and start with a lower dose initially.[1] Methocarbamol remains the agent of choice and can also be used orally for mild tremors at 50–100 mg/kg q8h, with 30-minute onset time.[1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1214; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1214

_Claims: 5 verified / 5 proposed · 10.545s_

**13. What pathologic findings are associated with NSAID toxicosis?**
_[Nonsteroidal Anti-Inflammatory Drug Toxicosis]_

**Book answer:** GI irritation, ulceration or hemorrhage with possible gastric perforation and peritonitis, plus renal tubular or papillary necrosis or interstitial nephritis. H2 blockers such as ranitidine or famotidine are used for GI ulceration.

**AI answer:**

Pathologic findings associated with NSAID toxicosis include:

- **Gastrointestinal:** erosions and ulcers. [1] A perforated gastric ulcer may occur secondary to NSAID toxicosis. [1][2]
- **Hemic/Lymphatic/Immune:** bleeding disorders secondary to decreased platelet aggregation. [1]
- **Hepatobiliary:** idiosyncratic hepatocellular damage. [1]
- **Renal/Urologic:** acute renal failure and acute interstitial nephritis. [1]

The provided evidence does not further characterise lesion distribution, severity, species differences, or gross versus histopathologic appearance.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1024; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1024-1025

_Claims: 5 verified / 5 proposed · 13.12s_

**14. How long can signs be delayed after a pit viper bite, and is local tissue reaction a reliable guide?**
_[Snake Venom Toxicosis—Pit Vipers]_

**Book answer:** Signs may be delayed for up to 8 hours after envenomation, and tissue reaction around the bite is not a reliable indicator of systemic envenomation.

**AI answer:**

Pit viper signs may be delayed for up to 8 hours after envenomation. [1]

Local tissue reaction is not a fully reliable guide on its own: 85% of pit viper bite victims have altered laboratory values and clinically important swelling, but about 20–30% of crotalid bites are “dry bites” with little if any venom deposited and no associated toxicity. [1]

The provided evidence does not further define how accurately the degree of local tissue reaction predicts systemic toxicity or laboratory abnormalities.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1311

_Claims: 3 verified / 3 proposed · 11.618s_

**15. Which breeds are at increased risk of hypoadrenocorticism?**
_[Hypoadrenocorticism (Addison's Disease)]_

**Book answer:** Great Danes, rottweilers, Portuguese water dogs, standard poodles, bearded collies, Leonbergers, West Highland white terriers, Nova Scotia duck tolling retrievers and Wheaten terriers. Golden retrievers and Chihuahuas have a decreased risk.

**AI answer:**

Breeds reported to have increased relative risk of hypoadrenocorticism include Great Danes, rottweilers, Portuguese water dogs, standard poodles, bearded collies, Leonbergers, West Highland white terriers, Nova Scotia duck tolling retrievers, and Wheaten terriers. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.772

_Claims: 1 verified / 1 proposed · 5.857s_

**16. What is the long-term treatment for chronic primary hypoadrenocorticism?**
_[Hypoadrenocorticism (Addison's Disease)]_

**Book answer:** Daily glucocorticoid replacement (prednisone 0.1-0.2 mg/kg/day) plus mineralocorticoid replacement with DOCP (Percorten) 2.2 mg/kg IM or SC, usually monthly, adjusted on serial electrolytes.

**AI answer:**

For chronic primary hypoadrenocorticism, long-term management is lifelong hormonal replacement therapy. [3]

**Glucocorticoid replacement**
- Prednisone is typically given daily at **0.1–0.2 mg/kg/day**. [1]
- Increase the replacement glucocorticoid dose during periods of stress, including travel, boarding, hospitalization, and surgery. [3]
- In cats, though not preferred, **Depo-Medrol 10 mg IM monthly** is an alternative means of glucocorticoid replacement. [1]

**Mineralocorticoid replacement**
- **DOCP / Percorten 2.2 mg/kg IM or SC** is typically given monthly and adjusted as needed based on serial electrolyte determinations. [1]
- For an average-sized cat, the initial monthly DOCP dose is **12.5 mg**. [1]
- Alternatively, **fludrocortisone acetate / Florinef 5–10 µg/kg q12h** can be used orally, adjusted by **0.05- to 0.1-mg increments** based on serial electrolyte determinations. [1][2]
- Fludrocortisone acetate has some glucocorticoid activity, so the maintenance prednisone dose for patients receiving fludrocortisone may be lower than for dogs receiving DOCP. [1][2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.773; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.773; [3] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.774

_Claims: 8 verified / 8 proposed · 18.992s_

**17. What is the difference between spontaneous and iatrogenic hyperadrenocorticism?**
_[Hyperadrenocorticism (Cushing's Syndrome)—Dogs]_

**Book answer:** Spontaneous HAC is excessive cortisol production by the adrenal cortex. Iatrogenic HAC results from excessive exogenous glucocorticoids given in any form or by any route.

**AI answer:**

Spontaneous hyperadrenocorticism (HAC) is caused by excessive production of cortisol by the adrenal cortex. [1]

Iatrogenic HAC results from excessive exogenous administration of glucocorticoids, of any form or by any route. [1][2]

In both forms, the clinical signs are due to the deleterious effects of elevated circulating glucocorticoid concentrations on multiple organ systems. [1][2]

The provided evidence distinguishes the two forms by source of glucocorticoid excess: endogenous adrenal cortical cortisol production in spontaneous HAC versus exogenous glucocorticoid administration in iatrogenic HAC. It does not cover differences in diagnosis, specific clinical signs, treatment, prognosis, or underlying causes of spontaneous HAC beyond excessive adrenal cortical cortisol production.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.719-720; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.720

_Claims: 3 verified / 3 proposed · 7.92s_

**18. How does mitotane work in canine hyperadrenocorticism?**
_[Hyperadrenocorticism (Cushing's Syndrome)—Dogs]_

**Book answer:** Mitotane (o,p'-DDD, Lysodren) selectively destroys the glucocorticoid-secreting cells of the adrenal cortex. It is one of two main drugs for pituitary-dependent HAC and may be the drug of choice for adrenal tumors because it may destroy tumor cells too.

**AI answer:**

Mitotane (o,p′-DDD, Lysodren) is used for medical management of pituitary-dependent hyperadrenocorticism in dogs. [1]

Its mechanism is adrenocorticolytic: mitotane selectively destroys glucocorticoid-secreting cells of the adrenal cortex. [1] This causes necrosis of the adrenal cortex, reducing production of adrenal cortical hormones. [2]

In adrenal tumour–associated hyperadrenocorticism, mitotane may be the drug of choice for medical management because it may destroy tumour cells as well as control cortisol secretion. [1]

The provided evidence describes mitotane’s adrenal cortical cell destruction and consequent reduction in adrenal cortical hormone production, but it does not provide further detail on molecular mechanism, dosing protocols, monitoring, adverse effects, or comparative efficacy.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.721-722; [2] BSAVA formulations document - pp.243-244

_Claims: 4 verified / 4 proposed · 9.496s_

**19. What is the initial insulin protocol for diabetic ketoacidosis?**
_[Diabetes Mellitus with Ketoacidosis]_

**Book answer:** Regular insulin is the insulin of choice, starting at 0.2 U/kg IM (or SC if hydration is normal), then 0.1-0.2 U/kg 3-6 hours later, which may be given hourly if needed.

**AI answer:**

**Initial insulin protocol for diabetic ketoacidosis**

Insulin is necessary to inhibit lipolysis, inhibit hepatic gluconeogenesis, and promote peripheral glucose uptake in diabetes mellitus with ketoacidosis. [1] Insulin must be given, regardless of blood glucose concentration, to correct the ketoacidotic state. [2] Regular insulin is the insulin of choice. [1]

**Intermittent regular insulin protocol**
- Give regular insulin 0.2 U/kg IM initially, or SC if hydration is normal. [1]
- Give 0.1–0.2 U/kg 3–6 hours later. [1]
- Subsequent doses may be given hourly if the patient is closely monitored. [1]
- Consider the response to the previous insulin dose when calculating subsequent doses. [1]
- Ideally, blood glucose should fall by 50–100 mg/dL/h. [1]
- Check blood glucose every 1–3 hours with Chemstrip BG reagent strips and an automated test strip analyzer. [2]

**Continuous-rate infusion option**
Regular insulin can also be administered as a continuous-rate infusion via a designated catheter. [1]

Preparation:
- Dogs: add 2.2 units/kg regular insulin to 250 mL 0.9% NaCl. [1]
- Cats: add 1.1 units/kg regular insulin to 250 mL 0.9% NaCl. [1]
- Allow 50 mL of the dilute insulin solution to flow through the IV tubing and discard. [1]

Rate by blood glucose:
- >250 mg/dL: 10 mL/hour. [1]
- 200–250 mg/dL: 7 mL/hour. [1][2]
- 150–200 mg/dL: 5 mL/hour. [1][2]
- 100–150 mg/dL: 5 mL/hour and add 2.5% dextrose to the IV crystalloid fluids. [1][2]
- <100 mg/dL: discontinue IV insulin infusion and continue 2.5–5% dextrose in IV crystalloid infusion. [1][2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.456; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.456-457

_Claims: 18 verified / 18 proposed · 26.424s_

**20. What is the starting dose of porcine lente insulin (Vetsulin) in cats?**
_[Diabetes Mellitus without Complication—Cats]_

**Book answer:** 2 U per cat SC q12h. Protamine zinc insulin (PZI, U-40) is a long-acting alternative usually given SC q24h.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The retrieved passages do not state a starting dose of porcine lente insulin/Vetsulin in cats.)

**Citation(s):** none (no claim cleared the verification gate)

_Claims: 0 verified / 0 proposed · 4.107s_

**21. What is the starting dose of Vetsulin in diabetic dogs, and what syringe must be used?**
_[Diabetes Mellitus without Complication—Dogs]_

**Book answer:** 0.75 units/kg SC q12h. It is a U-40 insulin, so it must be used with a U-40 insulin syringe.

**AI answer:**

Vetsulin starting dose in diabetic dogs: **0.75 units/kg subcutaneously every 12 hours**. [1]

Vetsulin is a **U-40 insulin**, so it **must be used with a U-40 insulin syringe**. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.460-461

_Claims: 2 verified / 2 proposed · 5.902s_

**22. What is the oral methimazole dose for feline hyperthyroidism, and what is the most effective treatment?**
_[Hyperthyroidism]_

**Book answer:** Methimazole 5-15 mg/day divided q8-12h; it can also be given transdermally in PLO gel, though that is slower. Radioiodine therapy is described as arguably the safest and most effective treatment.

**AI answer:**

For oral methimazole in feline hyperthyroidism:

- A commonly cited dose is 2.5 mg/cat PO q12h.[1]
- Another regimen is 2.5 mg/cat PO q12h for 7–14 days, then 5–10 mg/cat PO q12h, with T4 monitoring.[3]
- More broadly, methimazole is most often recommended at 5–15 mg/day divided q8–12h.[2]

For the most effective treatment:

- Radioiodine therapy is arguably the safest and most effective treatment.[2]

**Citation(s):** [1] BSAVA formulations document - pp.229-230; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.763; [3] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1573-1574

_Claims: 4 verified / 4 proposed · 9.83s_

**23. Which dog breeds are predisposed to hypothyroidism?**
_[Hypothyroidism]_

**Book answer:** Larger breeds such as golden retriever, Doberman pinscher, Great Dane and Irish setter, and some smaller breeds including miniature schnauzer, cocker spaniel, poodle and dachshund. It is most common in middle-aged dogs.

**AI answer:**

Dog breeds reported as predisposed to hypothyroidism include:

- **Larger breeds:** golden retriever, Doberman pinscher, Great Dane, and Irish setter. [1][2]
- **Smaller breeds:** miniature schnauzer, cocker spaniel, poodle, and dachshund. [1][2]

The provided evidence does not cover all possible predisposed breeds beyond those listed above.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.799; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.799

_Claims: 2 verified / 2 proposed · 7.534s_

**24. What is the long-term prednisone dose for insulinoma if diet fails?**
_[Insulinoma]_

**Book answer:** Start at 0.25 mg/kg PO q12h and increase as needed to 2-3 mg/kg PO q12h. Diazoxide is another option.

**AI answer:**

If dietary therapy is ineffective for insulinoma, prednisone may be started at 0.25 mg/kg PO q12h and increased as needed to 2–3 mg/kg PO q12h. [1]

The provided evidence does not specify a distinct “long-term” maintenance dose beyond increasing as needed within that range.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.827

_Claims: 1 verified / 1 proposed · 5.614s_

**25. How is hypertension controlled before and during pheochromocytoma surgery?**
_[Pheochromocytoma]_

**Book answer:** With phentolamine 0.02-0.1 mg/kg IV to effect. Boxers, miniature poodles and German shepherds are predisposed, with a median age of 11 years.

**AI answer:**

Before pheochromocytoma surgery, hypertension is typically controlled medically to stabilize the patient prior to surgery.[1]

**Preoperative control**
- Use **phenoxybenzamine 0.2–1.5 mg/kg PO q12h** for **1–2 weeks prior to surgery**.[1]
- For hypertension associated with phaeochromocytoma in dogs, start phenoxybenzamine at a low dose and increase until hypertension is controlled, typically for **10–14 days prior to surgery**.[2]
- **Propranolol 0.15–0.5 mg/kg PO q8h** may be administered concurrently to prevent a hypertensive crisis.[2]
- Avoid using a nonselective β-blocker such as propranolol without prior alpha-adrenergic blockade, because severe hypertension can develop if it is used without prior alpha blockade such as phentolamine or phenoxybenzamine.[1]

**Intraoperative control**
- Pre- and intraoperative hypertension can be treated with **phentolamine 0.02–0.1 mg/kg IV to effect**.[1]
- Tumor manipulation may cause severe hypertension if the patient is not properly premedicated.[1]

The provided evidence does not cover specific monitoring protocols, anaesthetic choices, or postoperative hypertension management.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1125-1126; [2] BSAVA formulations document - pp.284-285

_Claims: 7 verified / 7 proposed · 18.078s_

**26. How is central diabetes insipidus treated?**
_[Diabetes Insipidus]_

**Book answer:** With DDAVP: 1-2 drops of the intranasal preparation in the conjunctival sac q12-24h, or 2-5 µg SC q12-24h. An oral DDAVP tablet is also available.

**AI answer:**

**Central diabetes insipidus treatment**

- Treat with **desmopressin/DDAVP**: **1–2 drops of the intranasal preparation in the conjunctival sac q12–24h** to control PU/PD.[1][2] Central diabetes insipidus may also be treated with **one to two drops in the subconjunctival sac q12–24h**.[3]
- Alternatively, the intranasal preparation may be given **SC at 2–5 µg q12–24h**.[1][2]
- An oral DDAVP preparation is available as **0.1–0.2 mg tablets**; each **0.1 mg is comparable to 1 large drop of the intranasal preparation**.[2]
- Adjust treatment according to the patient’s signs; the ideal DDAVP dose and frequency are based on water intake.[2]
- Maintain a **normal diet with free access to water**.[1] Water must be available at all times for patients with diabetes insipidus.[3]
- Avoid excessive DDAVP dosing, as overdose can cause water intoxication.[2]

The provided evidence covers DDAVP, diet, and water access; it does not cover other treatments.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.453; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.453-454; [3] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.744

_Claims: 8 verified / 8 proposed · 16.94s_

**27. What blood pressure values define systemic hypertension in dogs and cats?**
_[Hypertension, Systemic]_

**Book answer:** Systolic above 160 mmHg or diastolic above 120 mmHg, measured by any method.

**AI answer:**

Systemic hypertension is defined as a sustained elevation in systolic arterial blood pressure, diastolic arterial blood pressure, or both. [1]

In dogs and cats, a systolic blood pressure >160 mmHg or a diastolic blood pressure >120 mmHg, obtained by any method, is considered abnormal. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.758-759

_Claims: 2 verified / 2 proposed · 6.059s_

**28. What is the first-line drug for systemic hypertension in cats?**
_[Hypertension, Systemic]_

**Book answer:** Amlodipine, with an ACE inhibitor added if proteinuria (UPC above 0.4) is present. In dogs an ACE inhibitor is used.

**AI answer:**

Amlodipine is the first-line oral drug for systemic hypertension in cats. [1][2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.760; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.760

_Claims: 1 verified / 1 proposed · 5.307s_

**29. Which breeds are at increased risk of severe parvovirus enteritis?**
_[Canine Parvovirus Infection]_

**Book answer:** Rottweiler, Doberman pinscher, American pit bull terrier, Labrador retriever, German shepherd and Yorkshire terrier.

**AI answer:**

Breeds shown to be at increased risk for severe CPV enteritis include:

- Rottweiler [1]
- Doberman pinscher [1]
- American pit bull terrier [1]
- Labrador retriever [1]
- German shepherd [1]
- Yorkshire terrier [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.286

_Claims: 1 verified / 1 proposed · 6.719s_

**30. What causes canine distemper, and is there an effective antiviral?**
_[Canine Distemper]_

**Book answer:** Canine distemper virus, a Morbillivirus in the Paramyxoviridae family. No antiviral drugs are known to be effective, so treatment is supportive, with broad-spectrum antibiotics for secondary infection because CDV is highly immunosuppressive.

**AI answer:**

Canine distemper is caused by canine distemper virus (CDV), a Morbillivirus within the Paramyxoviridae family. [1]

Incompletely attenuated vaccines are a rare cause. [1]

No antiviral drugs are known to be effective. [2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.280; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.281

_Claims: 3 verified / 3 proposed · 7.531s_

**31. What virus causes feline panleukopenia and what cells does it target?**
_[Feline Panleukopenia]_

**Book answer:** Feline parvovirus, which infects only mitotic (rapidly dividing) cells and causes their acute lysis. Clinically it causes sudden depression, vomiting, diarrhea, severe dehydration and high mortality.

**AI answer:**

Feline panleukopenia is caused by feline parvovirus. [1]

Feline parvovirus infects only mitotic cells, causing acute cytolysis of rapidly dividing cells. [1] Specifically, it destroys intestinal crypt cells of the jejunum and ileum. [1] In neonatal kittens, it also destroys rapidly dividing granular cells of the cerebellum and retinal cells of the eye. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.577-578

_Claims: 4 verified / 4 proposed · 11.529s_

**32. What are the hallmark features of FIP?**
_[Feline Infectious Peritonitis (FIP)]_

**Book answer:** Insidious onset, persistent fever that does not respond to treatment, pyogranulomatous tissue reaction, exudative effusions in body cavities and high mortality.

**AI answer:**

FIP is a systemic, immune-mediated, viral disease of domestic and exotic cats. [1]

Hallmark features include:

- Insidious onset. [1]
- Persistent non-responsive fever. [1]
- Pyogranulomatous tissue reaction. [1]
- Accumulation of exudative effusions in body cavities. [1]
- High mortality. [1]

The two classic forms are:

- Wet or effusive form, which targets the body cavities. [1]
- Dry or non-effusive form, which targets a variety of organs. [1]

The provided evidence does not cover further clinical signs, diagnostic criteria, pathology distribution, treatment, or prognosis beyond high mortality. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.571-572

_Claims: 7 verified / 7 proposed · 8.244s_

**33. Which FeLV subgroup is most transmissible?**
_[Feline Leukemia Virus Infection (FeLV)]_

**Book answer:** FeLV-A. It is present in all isolates. The other subgroups are B, C and T.

**AI answer:**

FeLV-A is the most transmissible FeLV subgroup. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.575-576

_Claims: 1 verified / 1 proposed · 4.914s_

**34. What is the dose of zidovudine for FIV and what must be monitored?**
_[Feline Immunodeficiency Virus Infection (FIV)]_

**Book answer:** 5-15 mg/kg PO q12h. It is most effective against acute infection, and bone marrow toxicity must be monitored.

**AI answer:**

For FIV, zidovudine dose is 5–15 mg/kg PO q12h. [1]

For cats, reported zidovudine dosing is 5–10 mg/kg PO or SC q12h, [2] or 5–10 mg/kg daily PO or SC in 2–4 divided doses. [3]

Monitoring: monitor for bone marrow toxicity. [1] Monitor packed cell volume in treated cats and perform a complete blood count periodically. [2][4] Haematological monitoring is recommended. [3][5]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.570-571; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1616-1617; [3] BSAVA formulations document - pp.374-376; [4] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1617-1618; [5] BSAVA formulations document - pp.373-374

_Claims: 6 verified / 6 proposed · 15.014s_

**35. What is the typical signalment of dogs with heartworm disease?**
_[Heartworm Disease—Dogs]_

**Book answer:** Medium to large breeds more than small dogs, outdoor more than indoor dogs, most aged 3-8 years, and males more often than females.

**AI answer:**

Typical signalment/risk profile for dogs with heartworm disease:

- Medium- to large-breed dogs are affected more often than small dogs. [1]
- Outdoor dogs are affected more often than indoor dogs. [1]
- Infestation can occur at any age, but most affected dogs are 3–8 years old. [1]
- Males are affected more often than females. [1]

The provided evidence does not further specify breed predispositions beyond size category.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.643-644

_Claims: 4 verified / 4 proposed · 7.168s_

**36. What antibiotic is used to clear Leptospira from the kidneys?**
_[Leptospirosis]_

**Book answer:** Dihydrostreptomycin 10-15 mg/kg IM q12h for 2 weeks. Procaine penicillin G is used first until kidney function returns to normal.

**AI answer:**

Dihydrostreptomycin is used to eliminate the organism from kidney interstitial tissues, at 10–15 mg/kg IM q12h for 2 weeks. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.869

_Claims: 1 verified / 1 proposed · 5.357s_

**37. What are the antibiotic options for Lyme disease in dogs?**
_[Lyme Borreliosis]_

**Book answer:** Doxycycline 5-10 mg/kg PO q12h with food, amoxicillin 20 mg/kg PO q8-12h, or azithromycin 25 mg/kg PO q24h. Doxycycline is preferred if Anaplasma phagocytophilum co-infection is present.

**AI answer:**

Antibiotic options for canine Lyme borreliosis include:

- **Doxycycline**: **5–10 mg/kg PO q12h**, given **with food**; **vomiting and gastritis are possible**. [1]  
- **Amoxicillin**: **20 mg/kg PO q8–12h**. [1]  
- **Azithromycin**: **25 mg/kg PO q24h**. [1]  

If there is co-infection with **Anaplasma phagocytophilum**, **doxycycline is preferred**. [1]

The recommended treatment duration is **4 weeks**. [1]

The provided evidence does not cover comparative efficacy, contraindications, monitoring, or management of treatment failure.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.890

_Claims: 3 verified / 3 proposed · 8.613s_

**38. What is the treatment of choice for canine ehrlichiosis?**
_[Ehrlichiosis (Anaplasma)]_

**Book answer:** Doxycycline 5 mg/kg PO q12h for 4 weeks, given IV for 5 days if the dog is vomiting.

**AI answer:**

The treatment of choice for canine ehrlichiosis is doxycycline at 5 mg/kg PO q12h for 4 weeks. [1]

If the dog is vomiting, give doxycycline IV for 5 days. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.504

_Claims: 1 verified / 1 proposed · 5.193s_

**39. What drug is FDA-approved for babesiosis and at what dose?**
_[Babesiosis]_

**Book answer:** Imidocarb dipropionate 6.6 mg/kg SC or IM every 1-2 weeks. It may clear B. canis but not B. gibsoni.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages mention antibabesial drugs and some babesiosis treatments, but they do not state which drug is FDA-approved for babesiosis or provide an FDA-approved dose.)

**Citation(s):** none (no claim cleared the verification gate)

_Claims: 0 verified / 0 proposed · 4.284s_

**40. What is the fenbendazole regimen for giardiasis in dogs and cats?**
_[Giardiasis]_

**Book answer:** 50 mg/kg PO q24h for 3 days in dogs or 5 days in cats; a second course may be needed. It should be combined with environmental cleaning and bathing the patient.

**AI answer:**

**Dogs — giardiasis:** fenbendazole **50 mg/kg PO q24h for 3 days**.[1][2]

**Cats — giardiasis:** fenbendazole **20 mg/kg p.o. for 5 days**.[2]

**Additional cat dosing claim:** fenbendazole **50 mg/kg PO q24h for 5 days** is provided for cats, but that claim is not specified as giardiasis-specific.[1]

**Repeat treatment:** a second course of treatment may be necessary.[1]

The provided evidence does not reconcile the two cat dosing statements.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.619; [2] BSAVA formulations document - pp.149-150

_Claims: 5 verified / 5 proposed · 17.211s_

**41. What is the recommended treatment once rabies is diagnosed?**
_[Rabies]_

**Book answer:** There is no treatment. Once the diagnosis is certain, euthanasia is indicated, and suspected cases must be securely isolated.

**AI answer:**

No treatment is recommended for rabies. [1] Once the diagnosis is certain, euthanasia is indicated. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1222-1223

_Claims: 2 verified / 2 proposed · 5.622s_

**42. What is the initial antibiotic choice for uncomplicated canine infectious respiratory disease?**
_[Canine Infectious Respiratory Disease]_

**Book answer:** Amoxicillin/clavulanic acid 12.5-25 mg/kg PO q12h or doxycycline 5 mg/kg PO q12h.

**AI answer:**

For initial treatment of uncomplicated canine infectious respiratory disease, the supported antibiotic options are:

- Amoxicillin/clavulanic acid 12.5–25 mg/kg PO q12h [1]
- Doxycycline 5 mg/kg PO q12h [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.283

_Claims: 1 verified / 1 proposed · 4.871s_

**43. What signs characterize feline herpesvirus infection?**
_[Feline Herpesvirus Infection]_

**Book answer:** Sneezing, fever, rhinitis, conjunctivitis and ulcerative keratitis. Kittens are most susceptible, and brachycephalic breeds get more severe corneal disease and corneal sequestra.

**AI answer:**

Feline herpesvirus infection causes acute disease in domestic and many exotic cats characterized by sneezing, fever, rhinitis, conjunctivitis, and ulcerative keratitis. [1]

Typical historical signs include acute onset of paroxysmal sneezing, blepharospasm with ocular discharge, anorexia associated with high fever, general malaise, or inability to smell, and recurrent signs in carriers. [2]

Physical examination findings can include fever up to 106°F (41°C), rhinitis with serous, mucopurulent, or purulent nasal discharge, and conjunctivitis with serous, mucopurulent, or purulent ocular discharge. [2] Ocular involvement can include keratitis with ulceration, descemetocele, or panophthalmitis. [2] Chronic manifestations can include chronic rhinitis/sinusitis with chronic purulent nasal discharge. [2] Herpes dermatitis may occur near the nasal openings. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.564-565; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.565

_Claims: 11 verified / 12 proposed, 1 dropped by the gate · 13.992s_

**44. What clinical forms can feline calicivirus cause?**
_[Feline Calicivirus Infection]_

**Book answer:** Upper respiratory disease, oral ulceration, pneumonia, occasionally arthritis, or a highly fatal systemic hemorrhagic disease.

**AI answer:**

Feline calicivirus infection may cause several clinical forms:

- Upper respiratory infection with eye and nose involvement. [1]
- Ulcerative disease, primarily of the mouth. [1]
- Pneumonia. [1]
- Acute arthritis. [1]
- Systemic hemorrhagic disease. [1]

These forms may occur alone or in any combination. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.561-562

_Claims: 6 verified / 6 proposed · 7.978s_

**45. What is the clindamycin dose for toxoplasmosis?**
_[Toxoplasmosis]_

**Book answer:** 25-50 mg/kg PO or IM daily divided into two doses, continued for at least 2 weeks after clinical signs clear. Topical 1% prednisone drops q8h are used for uveitis.

**AI answer:**

Clindamycin dosing for toxoplasmosis:

- **General:** **10 mg/kg PO q12h for 2–4 weeks** is recommended for toxoplasmosis. [1]
- **Cats:** **12.5–25 mg/kg PO q12h** for toxoplasmosis. [2]
- **Dogs:** **25 mg/kg PO daily in divided doses** for toxoplasmosis. [3]
- **Cats:** **25 mg/kg PO daily in divided doses** for toxoplasmosis. [3]

The provided evidence covers **oral clindamycin dosing for cats and dogs**, but does not provide any additional route, monitoring, contraindication, or adverse-effect information.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.357; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1532-1533; [3] BSAVA formulations document - pp.90-91

_Claims: 4 verified / 4 proposed · 7.151s_

**46. Which dog breeds are predisposed to pancreatitis?**
_[Pancreatitis—Dogs]_

**Book answer:** Miniature schnauzer, Yorkshire terrier and cocker spaniel. Acute pancreatitis is most common in middle-aged and older dogs, with a mean age of 6.5 years.

**AI answer:**

Reported breed predilections for canine pancreatitis include:

- Miniature schnauzer [1]
- Yorkshire terrier [1]
- Cocker spaniel [1]

In Miniature schnauzers, a possible genetic basis has been described, with select mutations in the SPINK 1 gene potentially conferring increased susceptibility. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1071-1072

_Claims: 2 verified / 2 proposed · 5.943s_

**47. What are the most common signs of pancreatitis in cats?**
_[Pancreatitis—Cats]_

**Book answer:** Vague, nonspecific signs, most often anorexia, lethargy and vomiting. Siamese cats are predisposed, and the mean age for acute pancreatitis is 7.3 years.

**AI answer:**

In cats with pancreatitis, the most frequently reported clinical signs are anorexia, lethargy, and vomiting. [1][2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1070; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1070

_Claims: 1 verified / 1 proposed · 6.325s_

**48. Which breeds are predisposed to exocrine pancreatic insufficiency?**
_[Exocrine Pancreatic Insufficiency]_

**Book answer:** German shepherd dogs, rough-coated collies and Eurasians. In young adult dogs it is usually caused by pancreatic acinar atrophy.

**AI answer:**

Breeds predisposed to exocrine pancreatic insufficiency are:

- German shepherd dogs [1]
- Rough-coated collies [1]
- Eurasians [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.544

_Claims: 1 verified / 1 proposed · 6.541s_

**49. How are pancreatic enzymes dosed for EPI?**
_[Exocrine Pancreatic Insufficiency]_

**Book answer:** Powdered enzymes mixed into food at 1 teaspoon per 10 kg body weight with each meal, with at least two meals a day. Pre-incubating the enzymes with food does not improve their effect.

**AI answer:**

Powdered pancreatic enzymes are the treatment of choice for EPI.[1][2]

**Initial dosing**
- Mix enzyme powder thoroughly in food at **1 teaspoon/10 kg body weight with each meal**; feed **at least two meals daily** to promote weight gain.[1][2]
- Preincubation of enzymes with food does **not** improve effectiveness of oral enzyme therapy.[1][2]
- Avoid tablets and capsules because mixing of enzymes and chyme is unpredictable.[1]

**Dose reduction after response**
- After a complete response has been achieved, gradually reduce the pancreatic enzyme supplement to a dose that prevents return of clinical signs.[1]
- Once body weight and conditioning normalize, gradually reduce the daily enzyme dosage to a level that maintains normal body weight.[1]

**Raw pancreas alternatives**
- Each teaspoon of pancreatic enzyme supplement can be replaced with **1–3 oz** of raw chopped pancreas, approximately **30–90 g**.[1]
- Fresh raw or fresh-frozen pig pancreas, approximately **100 g per meal**, is also an effective treatment.[3]

**Dog-specific dosing options**
- Tryplase: give the contents of **2–5 capsules/day** sprinkled on food; **5 capsules** are sufficient to digest **500 g** of dog food.[3]
- Alternatively, give at least **1–1.5 teaspoonfuls** of powdered non-enteric-coated pancreatic extract per **100 g of food** or per **10 kg body weight per meal**.[3]
- Mix thoroughly with food.[3]
- Best results are usually obtained by feeding only **2 or 3 meals/day**.[3]

**Cat-specific dosing options**
- Tryplase: give the contents of **1–2 capsules/day** sprinkled on food; **2 capsules** are sufficient to digest **250 g** of cat food.[3]
- Alternatively, give **1 teaspoonful** of powdered non-enteric-coated pancreatic extract mixed thoroughly with each meal.[3]
- Adjust the dose as necessary.[3]

The provided evidence does not specify a detailed tapering schedule beyond gradual reduction to the lowest dose that maintains body weight and prevents recurrence of clinical signs.[1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.545; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.544-545; [3] BSAVA formulations document - pp.270-271

_Claims: 15 verified / 15 proposed · 26.37s_

**50. What is GDV and which dogs are at risk?**
_[Gastric Dilation and Volvulus Syndrome]_

**Book answer:** A condition where the stomach dilates and then rotates around its short axis. Large, deep-chested breeds such as Great Danes and German shepherds are at risk, and risk increases with age.

**AI answer:**

GDV is a disease in dogs in which the stomach dilates and subsequently rotates around its short axis. [1]

Dogs described as at increased risk or predisposed include:

- Large, deep-chested breeds. [2]
- Great Danes. [2]
- German shepherd dogs. [2]
- Deep-chested dogs, particularly large and giant breeds, due to anatomic predisposition. [2]
- Smaller, deep-chested breeds such as dachshund and Pekingese, although GDV is rarely reported in these breeds. [2]
- Dogs of any age, with risk increasing as age increases. [2]
- Dogs with a first-order relative with a history of GDV. [2]

Reported or suspected associated risk factors include:

- Activity following a meal, which GDV has classically been linked to. [2]
- Recently eating from a raised food bowl. [2]
- Faster speed of eating. [2]
- Possibly gastrointestinal neoplasia, because it can cause motility disturbances and gastric retention of food and/or air. [2]

The supplied evidence does not establish that these are the only dogs or risk factors associated with GDV.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.600-601; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.601

_Claims: 13 verified / 13 proposed · 19.336s_

**51. What is megaesophagus and which cats are predisposed?**
_[Megaesophagus]_

**Book answer:** A focal or generalized dilation of the esophagus with reduced or absent peristalsis. Siamese and Siamese-related cats are predisposed.

**AI answer:**

Megaesophagus is a focal or generalized, diffuse dilation of the esophagus with decreased to absent peristalsis. [1]

Cats predisposed to megaesophagus are Siamese and Siamese-related cats. [2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.928-929; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.929

_Claims: 2 verified / 2 proposed · 9.662s_

**52. Which dogs are most commonly affected by hemorrhagic gastroenteritis?**
_[Gastroenteritis, Hemorrhagic]_

**Book answer:** Small and toy breeds, especially miniature schnauzer, dachshund, Yorkshire terrier and miniature poodle. It usually affects adults with a mean age of 5 years.

**AI answer:**

Hemorrhagic gastroenteritis affects dogs. [1] All breeds can be affected, but incidence is greater in small-breed and toy-breed dogs. [2]

Dogs most commonly represented include:

- Miniature schnauzers [2]
- Dachshunds [2]
- Yorkshire terriers [2]
- Miniature poodles [2]

It is usually reported in adult dogs, with a mean age of 5 years. [2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.611-612; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.612

_Claims: 4 verified / 4 proposed · 9.612s_

**53. How is IBD categorized?**
_[Inflammatory Bowel Disease]_

**Book answer:** By the predominant mucosal cellular infiltrate, for example lymphocytic-plasmacytic. It is a group of chronic enteropathies with persistent or intermittent GI signs and histologic intestinal inflammation.

**AI answer:**

IBD is generally categorized by the predominant mucosal cellular infiltrate, such as lymphocytic-plasmacytic enteritis, eosinophilic enteritis, or granulomatous enteritis. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.823

_Claims: 1 verified / 1 proposed · 5.732s_

**54. What cytology finding supports hepatic lipidosis in cats?**
_[Hepatic Lipidosis]_

**Book answer:** On fine-needle liver aspiration, more than 80% of hepatocytes show severe cytosolic vacuolation. Vitamin K1 is recommended for all cats with suspected lipidosis.

**AI answer:**

Fine-needle liver aspiration cytology showing >80% hepatocytes with severe cytosolic vacuolation supports feline hepatic lipidosis. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.673-674

_Claims: 1 verified / 1 proposed · 5.16s_

**55. Where are congenital portosystemic shunts usually located in small dogs and cats?**
_[Portosystemic Vascular Anomaly, Congenital]_

**Book answer:** Extrahepatic shunts are more common in small-breed dogs and cats. Small purebred and mixed 'terrier' dogs are at higher risk.

**AI answer:**

In small breed dogs and cats, congenital portosystemic vascular anomalies are more commonly extrahepatic. [1]

The provided evidence does not specify a more precise anatomical location beyond “extrahepatic.”

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1169

_Claims: 1 verified / 1 proposed · 6.132s_

**56. How long must kidney disease be present to be called chronic?**
_[Renal Failure, Chronic]_

**Book answer:** More than 3 months. Mean age at diagnosis is about 7 years in dogs and 9 years in cats.

**AI answer:**

Kidney disease is considered chronic when it has been present for more than 3 months. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1233-1234

_Claims: 1 verified / 1 proposed · 4.648s_

**57. How is prerenal azotemia distinguished from acute kidney injury?**
_[Renal Failure, Acute]_

**Book answer:** Prerenal azotemia has concentrated urine (USG at least 1.030 in dogs and 1.035 in cats) and is correctable with fluid repletion.

**AI answer:**

The provided evidence uses “acute renal failure” rather than “acute kidney injury,” and does not provide additional AKI staging or definitions.

**Findings supporting prerenal azotemia**

- A urine specific gravity ≥1.030 in dogs or ≥1.035 in cats supports prerenal azotemia. [1]
- After appropriate therapy to restore renal perfusion, prerenal azotemia typically shows a dramatic reduction in azotemia within 24–48 hours. [1]
- Dehydration, poor peripheral perfusion, low cardiac output, recent fluid loss, high-protein diet, or black, tarry stools are listed as factors supporting assessment for prerenal azotemia. [1]

**Findings supporting renal/acute renal failure rather than prerenal azotemia**

- Azotemic patients that have not received fluids and have urine specific gravity <1.030 in dogs or <1.035 in cats typically have primary renal azotemia. [1][2]
- Acute renal failure is differentiated by normal to large renal size, cylindruria, lack of indications of chronicity, and a history of recent nephrotoxin exposure or hypotensive episode. [3]
- Recent onset of altered urine output, clinical signs consistent with uremia, exposure to possible nephrotoxicants or ischemic renal injury, or normal to enlarged kidney size are listed as factors supporting assessment for acute renal failure. [1]
- In drug-induced nephrotoxicosis, urinalysis may show low urine specific gravity, often <1.025, proteinuria, glucosuria, or cylindruria. [4]

**Practical distinction from the supplied evidence**

Prerenal azotemia is supported by concentrated urine at or above the species thresholds and rapid improvement in azotemia after renal perfusion is restored. [1] Acute renal failure/primary renal azotemia is supported by inadequate urine concentration in an untreated azotemic patient, cylindruria, normal to enlarged kidneys, no evidence of chronicity, and a recent nephrotoxin exposure or hypotensive episode. [1][2][3]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.231-232; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.232; [3] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1234-1235; [4] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1017-1018

_Claims: 7 verified / 7 proposed · 25.233s_

**58. Can calcium oxalate uroliths be dissolved medically?**
_[Urolithiasis, Calcium Oxalate]_

**Book answer:** No. No available drugs effectively dissolve them, so they are removed. Steroids and furosemide should be used with care because they promote calciuria.

**AI answer:**

No. Calcium oxalate uroliths are not amenable to medical dissolution.[1][2] No available drugs effectively dissolve calcium oxalate uroliths.[3] There are also no reports of dissolution of CaOx uroliths with therapeutic foods.[1]

These claims address medical dissolution with drugs and therapeutic foods; they do not cover other management approaches.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1420; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1419-1420; [3] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1420

_Claims: 3 verified / 3 proposed · 7.25s_

**59. Which six dog breeds make up 60% of calcium oxalate urolith cases?**
_[Urolithiasis, Calcium Oxalate]_

**Book answer:** Miniature schnauzer, Lhasa apso, Yorkshire terrier, bichon frise, shih tzu and miniature poodle.

**AI answer:**

The six dog breeds reported to represent 60% of calcium oxalate urolith cases are miniature schnauzer, Lhasa apso, Yorkshire terrier, bichon frise, shih tzu, and miniature poodle. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1419

_Claims: 1 verified / 1 proposed · 6.298s_

**60. What are most uroliths in dogs under 12 months old?**
_[Urolithiasis, Struvite—Dogs]_

**Book answer:** Infection-induced struvite (magnesium ammonium phosphate) uroliths.

**AI answer:**

Most uroliths in immature dogs under 12 months old are infection-induced struvite. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1427

_Claims: 1 verified / 1 proposed · 4.999s_

**61. Which breeds are predisposed to urate uroliths?**
_[Urolithiasis, Urate]_

**Book answer:** Dalmatians, English bulldogs, and breeds at risk of portosystemic shunts such as Yorkshire terriers.

**AI answer:**

Breeds with reported predilection for urate uroliths include:

- Dalmatians. [1]
- English bulldogs. [1]
- Breeds at risk for portosystemic shunts, such as Yorkshire terriers. [1]

The provided evidence does not cover any other predisposed breeds.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1428-1429

_Claims: 2 verified / 2 proposed · 10.794s_

**62. When after estrus do dogs and cats with pyometra usually present?**
_[Pyometra]_

**Book answer:** Dogs within 12 weeks after their last estrus, and cats within 4 weeks of their last estrus. It is life-threatening when the cervix is closed and the bitch is systemically ill.

**AI answer:**

Dogs with pyometra usually present within 12 weeks after their last estrus. [1]

Cats with pyometra usually present within 4 weeks of the last call/estrus. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1209

_Claims: 2 verified / 2 proposed · 5.396s_

**63. When does eclampsia usually occur and which breeds are at risk?**
_[Eclampsia]_

**Book answer:** Usually 1-4 weeks postpartum, most often before day 40. It is most common in toy breeds such as Chihuahua, miniature pinscher, Shih Tzu, miniature poodle and Pomeranian, and in first litters.

**AI answer:**

Eclampsia is post-parturient hypocalcemia. [1]

**Usual timing**
- It usually develops **1–4 weeks postpartum**. [1]
- It is most common **before day 40 postpartum**. [1]
- It may also occur **at term, prepartum, or during late lactation**. [1]
- It only **occasionally occurs prepartum**. [1]

**Patients/breeds at risk**
- In dogs, it occurs in the **postpartum bitch**, is most common in **toy breeds**, and has a higher incidence with the **first litter**. [1]
- Breeds reported at increased risk are **Chihuahua, miniature pinscher, Shih Tzu, miniature poodle, Mexican hairless, and Pomeranian**. [1]
- In cats, eclampsia is **rare**. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.499-500

_Claims: 6 verified / 6 proposed · 10.061s_

**64. How is eclampsia treated in the bitch?**
_[Eclampsia]_

**Book answer:** 10% calcium gluconate 0.22-0.44 mL/kg IV slowly over 5 minutes to effect, monitoring heart rate or ECG. Hyperthermia and hypoglycemia are corrected, and she is sent home on oral calcium 10-30 mg/kg PO q8h.

**AI answer:**

**Immediate treatment**

- Give calcium gluconate 10% solution at 0.22–0.44 mL/kg IV, slowly to effect over 5 minutes; monitor heart rate or ECG during administration. [1]
- Correct hypoglycemia. [1]
- For unresponsive seizures, give diazepam 5 mg IV. [1]
- Treat cerebral edema, if indicated. [1]
- Monitor serum calcium concentration until it is stabilized in the normal range. [1]

**Manage nursing/pups**

- Remove puppies from the dam onto a foster dam or hand-raise. [1]
- If this is not possible or is undesirable because of the behavioral need for contact with the dam, remove pups from the dam for 24 hours, or until serum calcium is stabilized, and provide supplementation for the remainder of lactation. [1]
- Start puppies on solid food at 3–4 weeks of age. [1]

**Ongoing calcium and monitoring**

- Send home on calcium carbonate, or calcium gluconate 10–30 mg/kg PO q8h until lactation ends. [1]
- Calcium carbonate TUMS 500 mg tablets supply 200 mg calcium. [1]
- Continue to monitor serum calcium level. [1]
- Magnesium supplementation may be helpful in hypomagnesemic bitches. [1]

**Avoid**

- Avoid corticosteroids because they cause decreased intestinal absorption and increased renal excretion of calcium. [1]
- Avoid calcium supplementation during gestation. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.500-501

_Claims: 14 verified / 14 proposed · 24.516s_

**65. Why are brachycephalic breeds prone to dystocia?**
_[Dystocia]_

**Book answer:** Because they combine a broad fetal head with a narrow maternal pelvis, as in the Bulldog, Boston terrier and pug.

**AI answer:**

Brachycephalic breeds are prone to dystocia because affected dogs are described as having a broad head and narrow pelvis, creating an anatomic predisposition to difficult birth. [1][2]

The listed brachycephalic breeds predisposed to dystocia are the Bulldog, Boston terrier, and pug. [2]

The provided evidence does not cover any additional mechanisms or risk factors beyond the broad head–narrow pelvis description.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.493-494; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.494

_Claims: 2 verified / 2 proposed · 8.464s_

**66. Which breeds are at high risk of lymphoma?**
_[Lymphoma—Dogs]_

**Book answer:** Boxer, basset hound, golden retriever, Saint Bernard, Scottish terrier, Airedale terrier and bulldog. Dachshunds and Pomeranians are low-risk.

**AI answer:**

Reported high-risk breeds for LSA are:

- Boxer [1]
- Basset hound [1]
- Golden retriever [1]
- Saint Bernard [1]
- Scottish terrier [1]
- Airedale terrier [1]
- Bulldog [1]

The provided evidence does not cover whether other breeds are also high risk.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.900

_Claims: 1 verified / 1 proposed · 5.646s_

**67. What is the typical age of cats with lymphoma by FeLV status?**
_[Lymphoma—Cats]_

**Book answer:** About 3 years in FeLV-positive cats and 7 years in FeLV-negative cats. Lymphoma is also the most common spinal cord tumor in cats.

**AI answer:**

Typical age of cats with lymphoma by FeLV status:

- FeLV-positive cats with lymphoma: 3 years. [1]
- FeLV-negative cats with lymphoma: 7 years. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.897-898

_Claims: 2 verified / 2 proposed · 5.904s_

**68. What is the standard chemotherapy after amputation for canine osteosarcoma?**
_[Osteosarcoma]_

**Book answer:** A platinum drug (cisplatin or carboplatin) or doxorubicin, with at least four doses recommended.

**AI answer:**

After amputation for appendicular canine osteosarcoma, adjuvant chemotherapy is recommended. [1]

Current standard-of-care options are chemotherapy with either platinum-based drugs—cisplatin or carboplatin—or doxorubicin. [2] A minimum of four doses is recommended. [2] Chemotherapy is typically initiated within 2 weeks of surgery. [2]

Standard protocols listed in the provided evidence are:

- Cisplatin 70 mg/m² IV every 3 weeks. [2]
- Carboplatin 300 mg/m² IV every 3 weeks. [2]
- Doxorubicin 30 mg/m² IV every 3 weeks for 5 doses; this is described as a less expensive option and may be used in combination with cisplatin. [2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1055-1056; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1056

_Claims: 7 verified / 7 proposed · 10.927s_

**69. What proportion of canine splenic tumors are hemangiosarcomas, and which breeds are predisposed?**
_[Hemangiosarcoma, Spleen and Liver]_

**Book answer:** Up to 70%. German shepherds, Labrador retrievers and golden retrievers are predisposed.

**AI answer:**

Hemangiosarcoma accounts for up to 70% of all canine splenic tumors. [1]

Predisposed breeds include German shepherds, Labrador retrievers, and golden retrievers. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.653-654

_Claims: 2 verified / 2 proposed · 5.813s_

**70. What is the vinblastine and prednisone protocol for canine mast cell tumors?**
_[Mast Cell Tumors]_

**Book answer:** Vinblastine 2.0 mg/m2 IV every 7 days for 4 doses, then every 14 days for 4 doses, with prednisone 1 mg/kg PO q24h.

**AI answer:**

For dogs with mast cell tumors, the verified protocol is:

- **Vinblastine:** 2.0 mg/m² IV every 7 days for 4 treatments, then every 14 days for 4 treatments. [1]
- **Prednisone:** 1 mg/kg PO every 24 hours. [1]

The provided evidence does not specify prednisone duration or tapering schedule.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.919-920

_Claims: 1 verified / 1 proposed · 8.641s_

**71. What proportion of feline mammary tumors are malignant?**
_[Mammary Gland Tumors—Cats]_

**Book answer:** 85-95%, mostly carcinomas. Siamese cats have twice the risk of other breeds.

**AI answer:**

85–95% of feline mammary tumors are malignant. Most are carcinomas; sarcomas are rare. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.909-910

_Claims: 1 verified / 1 proposed · 4.717s_

**72. What is the mean age of dogs with malignant versus benign mammary tumors?**
_[Mammary Gland Tumors—Dogs]_

**Book answer:** 9-11 years for malignant and 7-9 years for benign tumors. They are uncommon in dogs under 5 years.

**AI answer:**

In dogs with mammary gland tumors, the reported mean age is:

- **Malignant tumors:** **9–11 years** [1]
- **Benign tumors:** **7–9 years** [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.912

_Claims: 1 verified / 1 proposed · 5.189s_

**73. What is the vincristine protocol for transmissible venereal tumor?**
_[Transmissible Venereal Tumor]_

**Book answer:** 0.5-0.7 mg/m2 IV once weekly, continued for 2 weeks beyond complete resolution of visible disease. Doxorubicin can be tried if remission is partial.

**AI answer:**

For transmissible venereal tumor, reported vincristine protocols are:

- Vincristine sulfate 0.5–0.7 mg/m² IV once weekly, continued for 2 weeks beyond complete resolution of gross disease. [1]
- Alternatively, in dogs and cats with transmissible venereal tumours: vincristine 0.025 mg/kg IV every 7 days for 4 weeks. [2]

CBC and platelet count should be performed before each chemotherapy treatment. [1]

The provided evidence does not clarify how to choose between the mg/m² and mg/kg protocols.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1399; [2] BSAVA formulations document - pp.363-364

_Claims: 3 verified / 3 proposed · 11.273s_

**74. Which breeds are predisposed to dilated cardiomyopathy?**
_[Cardiomyopathy, Dilated—Dogs]_

**Book answer:** Doberman pinscher and boxer, giant breeds (Scottish deerhound, Irish wolfhound, Great Dane, Saint Bernard, Afghan hound, Newfoundland), cocker spaniel and Portuguese water dog.

**AI answer:**

Predisposed breeds for dilated cardiomyopathy in dogs include:

- Doberman pinscher and boxer. [1]
- Giant breeds: Scottish deerhound, Irish wolfhound, Great Dane, Saint Bernard, Afghan hound, and Newfoundland. [1]
- Cocker spaniel and Portuguese water dog. [1]

The provided evidence covers these canine breed predilections only; it does not address predisposition in other species or additional dog breeds.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.300

_Claims: 3 verified / 3 proposed · 9.509s_

**75. Which cat breeds are predisposed to hypertrophic cardiomyopathy?**
_[Cardiomyopathy, Hypertrophic—Cats]_

**Book answer:** Maine coon, ragdoll, Sphynx, British and American shorthairs, and Persians. Typical age is 5-7 years.

**AI answer:**

Cat breeds predisposed to hypertrophic cardiomyopathy include Maine coon cats, ragdolls, Sphynx, British and American shorthairs, and Persians. [1][2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.302-303; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.303

_Claims: 1 verified / 1 proposed · 6.053s_

**76. What furosemide dose is used for a critically dyspneic cat with HCM?**
_[Cardiomyopathy, Hypertrophic—Cats]_

**Book answer:** 4 mg/kg IV, which can be repeated in 1 hour if the cat is still severely dyspneic. The usual dose is 1-2 mg/kg q8-24h.

**AI answer:**

For a critically dyspneic cat with HCM, furosemide is often used at a high dose of **4 mg/kg IV**. [1]

This dose can be **repeated in 1 hour** if the cat remains severely dyspneic. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.303-304

_Claims: 2 verified / 2 proposed · 7.316s_

**77. Which dogs typically develop myxomatous mitral valve disease?**
_[Atrioventricular Valve (Myxomatous) Disease]_

**Book answer:** Small breeds under 20 kg, such as Cavalier King Charles spaniels, Chihuahuas, miniature schnauzers, Maltese, Pomeranians, cocker spaniels, Pekingese and poodles.

**AI answer:**

Myxomatous mitral valve disease typically affects small-breed dogs under 20 kg, although it may also be encountered in larger dogs. [1]

Reported breed predilections include Cavalier King Charles spaniels, Chihuahuas, Miniature Schnauzers, Maltese, Pomeranians, Cocker Spaniels, Pekingese, Poodles, and others. [1]

In affected breeds such as Cavalier King Charles spaniels, a murmur may be detected from 2 years of age, with peak incidence at 6–8 years. [1] Onset of CHF is from 8–12 years. [1]

Males develop the disease at a younger age than females, resulting in a higher prevalence at a given age in males. [2]

The provided evidence covers typical size, breed, age-related presentation, CHF onset, and sex association, but does not address other risk factors.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.225; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.225

_Claims: 5 verified / 6 proposed, 1 dropped by the gate · 10.22s_

**78. What is a patent ductus arteriosus and when is it usually found?**
_[Patent Ductus Arteriosus]_

**Book answer:** Persistent patency of the fetal ductus connecting the descending aorta to the pulmonary artery. Most are found during the initial vaccination visits, and females are predisposed in many breeds.

**AI answer:**

Patent ductus arteriosus is persistent patency of the fetal ductus arteriosus connecting the descending aorta to the pulmonary artery. [1] In this condition, the ductus arteriosus fails to close following birth, permitting persistent communication between the aorta and pulmonary artery. [1]

It is usually found in young animals, with a reported median age of presentation of 5 months in dogs. [2] The vast majority are identified during the initial vaccination sequence. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1091; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1093-1094

_Claims: 4 verified / 4 proposed · 7.475s_

**79. What is the main feature of boxer cardiomyopathy?**
_[Cardiomyopathy—Boxer (Arrhythmogenic Right Ventricular)]_

**Book answer:** Ventricular tachyarrhythmias, which may cause syncope or sudden death. Fewer than 5% of dogs develop congestive heart failure with systolic dysfunction.

**AI answer:**

The main feature of boxer cardiomyopathy is ventricular tachyarrhythmias, as it is a myocardial disease commonly characterized by these arrhythmias, which can be accompanied by syncope or sudden death. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.295-296

_Claims: 1 verified / 1 proposed · 6.735s_

**80. When should antiepileptic treatment be started in a dog with genetic epilepsy?**
_[Epilepsy, Genetic (Idiopathic)—Dogs]_

**Book answer:** At the second generalized seizure if the dog is under 2 years old, and in other dogs when the interval between seizures is gradually getting shorter.

**AI answer:**

For a dog with genetic epilepsy:

- If the dog is **< 2 years old**, start antiepileptic treatment at the **second generalized seizure**. [1]
- In other dogs, start antiepileptic treatment when the **interictal period gradually shortens**. [1]

These claims do not cover other possible indications for starting treatment.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.520-521

_Claims: 2 verified / 2 proposed · 4.882s_

**81. Which breeds get Hansen type I disc disease?**
_[Intervertebral Disc Disease, Thoracolumbar]_

**Book answer:** Dachshund, shih tzu, Lhasa apso, Pekingese, cocker spaniel, Welsh corgi, and toy and miniature poodles. Type II disease affects mainly large breeds.

**AI answer:**

Hansen type I disc disease breed predispositions in the provided evidence are:

**Cervical intervertebral disc disease:** dachshund, poodle, beagle, and Cocker spaniel. [1]

**Thoracolumbar disc disease:** dachshund; Shih Tzu; Lhaso Apso; Pekingese; Cocker spaniel; Welsh corgis; and toy and miniature poodles. [2]

The evidence provided only covers cervical and thoracolumbar Hansen type I disc disease breed predispositions; it does not address other spinal regions or broader breed risk beyond these lists.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.830; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.833

_Claims: 2 verified / 2 proposed · 10.756s_

**82. Which breed accounts for about half of wobbler syndrome cases?**
_[Cervical Spondylomyelopathy (Wobbler Syndrome)]_

**Book answer:** The Doberman pinscher. Great Dane, rottweiler, Weimaraner and Dalmatian also have a high incidence.

**AI answer:**

Doberman pinscher dogs account for approximately 50% of wobbler syndrome cases. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.317-318

_Claims: 1 verified / 1 proposed · 4.67s_

**83. What gene mutation causes degenerative myelopathy, and is there an effective drug?**
_[Degenerative Myelopathy]_

**Book answer:** A mutation in the superoxide dismutase 1 gene (SOD1). No drug has been proven to slow or halt progression.

**AI answer:**

Canine degenerative myelopathy in many breeds has been shown to result from mutation in the superoxide dismutase 1 gene, SOD1. [1] The mutation underlying most degenerative myelopathy is a c.118 G > A transition in Exon 2 of SOD1, predicting an E40K missense mutation. [1] A second SOD1 missense mutation, c.52 A > T, has been reported only in Bernese mountain dogs. [1]

No drug has been proven effective in slowing or halting disease progression. [2]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.422-423; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.423-424

_Claims: 4 verified / 4 proposed · 9.822s_

**84. What is the pyridostigmine dose for myasthenia gravis?**
_[Myasthenia Gravis]_

**Book answer:** 1-3 mg/kg PO q8-12h, with the syrup diluted half and half in water.

**AI answer:**

Pyridostigmine is used for treatment of myasthenia gravis. [1]

**Dogs:** 0.2–5 mg/kg PO q8–12h. [2]

**Cats:** 0.25 mg/kg PO q8–12h. [2]

**Additional listed antimyasthenic dosing:** pyridostigmine bromide 0.02–0.04 mg/kg q2h IV, or 0.5–3 mg/kg q8–12h PO. [3]

**Citation(s):** [1] BSAVA formulations document - pp.314-315; [2] BSAVA formulations document - p.315; [3] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1599-1600

_Claims: 4 verified / 4 proposed · 12.678s_

**85. What is geriatric vestibular disease in dogs?**
_[Vestibular Disease, Geriatric—Dogs]_

**Book answer:** An acute, non-progressive disturbance of the peripheral vestibular system in older dogs, usually over 8 years old. The cause is unknown.

**AI answer:**

Geriatric vestibular disease in dogs is an acute-onset, non-progressive disturbance of the peripheral vestibular system in older dogs. [1] It is a common, sporadic, acquired disease of older dogs, with patients usually > 8 years old. [1] Its pathophysiology is unknown. [1]

It is often incorrectly referred to as a stroke, but it is neither central in location nor suspected to be vascular or ischemic in origin. [1]

Typical signs are acute-onset peripheral vestibular dysfunction, usually unilateral but occasionally bilateral. [1] Historical findings include sudden onset of imbalance, disorientation, reluctance to stand, and usually head tilt and irregular eye movements. [1] It may be preceded or accompanied by nausea and vomiting. [1]

It is primarily distinguished from other causes of vestibular deficits by the acute onset and usually rapid improvement without specific treatment. [2] The prognosis for rapid improvement and recovery is excellent. [2]

The provided evidence does not cover diagnostic testing, specific treatment options, or detailed exclusion of other causes of vestibular signs.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1462-1463; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1463

_Claims: 10 verified / 10 proposed · 10.458s_

**86. Which breeds have an increased incidence of cranial cruciate ligament disease at a young age?**
_[Cruciate Ligament Disease, Cranial]_

**Book answer:** Rottweilers and Labrador retrievers under 4 years old. The West Highland white terrier is the overrepresented small breed.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The provided passages discuss cranial cruciate ligament disease definition, pathophysiology, causes, risk factors, diagnosis, and treatment, but they do not list breeds with increased incidence at a young age.)

**Citation(s):** none (no claim cleared the verification gate)

_Claims: 0 verified / 0 proposed · 3.304s_

**87. Which dogs are most commonly affected by patellar luxation?**
_[Patellar Luxation]_

**Book answer:** Toy and miniature breeds, such as miniature and toy poodles, Yorkshire terriers, Pomeranians, Pekingese, Chihuahuas and Boston terriers.

**AI answer:**

Patellar luxation is most common in toy and miniature dog breeds. [1]

Reported breed predilections include miniature and toy poodles, Yorkshire terriers, Pomeranians, Pekingese, Chihuahuas, and Boston terriers. [1]

Females have a higher reported risk than males, with risk in females 1.5 times that in males. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1089

_Claims: 3 verified / 4 proposed, 1 dropped by the gate · 8.023s_

**88. What is panosteitis and at what age does it usually occur?**
_[Panosteitis]_

**Book answer:** A self-limiting, painful condition of the long bones of young medium to large-breed dogs, seen radiographically as increased marrow density. It usually occurs at 5-18 months of age, mostly in males.

**AI answer:**

Panosteitis is a self-limiting, painful condition affecting one or more of the long bones of young, medium- to large-breed dogs. [1] It is characterized clinically by lameness and radiographically by high density of the marrow cavity. [1]

The provided evidence states that it occurs in young dogs, but does not specify a usual age range.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1076-1077

_Claims: 2 verified / 3 proposed, 1 dropped by the gate · 6.356s_

**89. Which breeds are predisposed to Demodex canis demodicosis?**
_[Demodicosis]_

**Book answer:** American Staffordshire terrier, Shar-Pei, Boston terrier, English bulldog and West Highland white terrier.

**AI answer:**

Reported breed predilections for *Demodex canis* demodicosis are:

- American Staffordshire terrier [1]
- Shar-Pei [1]
- Boston terrier [1]
- English bulldog [1]
- West Highland white terrier [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.424-425

_Claims: 1 verified / 1 proposed · 5.245s_

**90. Which cats and dogs are predisposed to dermatophytosis?**
_[Dermatophytosis]_

**Book answer:** Longhaired cats such as Persians and Himalayans, and Yorkshire and Manchester terriers. M. canis is more common in younger animals.

**AI answer:**

Cats predisposed to dermatophytosis include longhaired breeds, particularly Persians and Himalayans. [1] M. canis is more common in younger animals. [1] Cats with immunocompromise due to disease such as FeLV or FIV, or due to medications such as glucocorticoids, are also at increased risk. [1]

Dogs predisposed to dermatophytosis include Yorkshire terriers and Manchester terriers. [1] M. canis is more common in younger animals. [1] Other dermatophyte species associated with rodents or wildlife are seen more often in adults. [1] Generalized dermatophytosis in older dogs is associated with immunosuppression. [1] Immunocompromise due to disease or glucocorticoid medication is also a risk factor. [1]

For both cats and dogs, risk factors include high population density and poor management practices. [1]

The evidence provided does not further specify sex, neuter status, or additional breed predispositions beyond those listed above. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.433

_Claims: 8 verified / 8 proposed · 11.579s_

**91. How is selamectin used for scabies in dogs?**
_[Sarcoptic Mange]_

**Book answer:** It is labeled every 30 days, but application every 2 weeks for at least three treatments may be more effective.

**AI answer:**

For dogs with scabies/sarcoptic mange, selamectin is used as a topical spot-on formulation; available pipettes contain 6% or 12% selamectin. [2]

**Dose:** use a minimum dose of 6 mg/kg. [2]

**Schedule:** selamectin is labeled for treatment of scabies when applied every 30 days. [1] However, for effective treatment of sarcoptic mange, application on three occasions at 2-week intervals is recommended. [2] Application every 2 weeks for at least three treatments may be more effective. [1]

**Age restriction:** selamectin is not for use in dogs less than 6 weeks old. [2]

The provided evidence does not cover additional management measures, follow-up testing, adverse effects, contraindications other than age, or use with other treatments.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1269; [2] BSAVA formulations document - pp.322-323

_Claims: 6 verified / 6 proposed · 11.735s_

**92. What intraocular pressure is diagnostic of glaucoma in dogs and cats?**
_[Glaucoma]_

**Book answer:** Above 25-30 mmHg in dogs and above 31 mmHg in cats.

**AI answer:**

Glaucoma is diagnosed based on elevated IOP **plus compatible changes in vision or the appearance of the globe, optic nerve, and/or retina**. In dogs, the diagnostic IOP threshold is **>25–30 mmHg**, measured by applanation, rebound, or Schiotz tonometry. [1]

In cats, the diagnostic IOP threshold is **>31 mmHg**, measured by applanation, rebound, or Schiotz tonometry, with compatible changes in vision or the appearance of the globe, optic nerve, and/or retina. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.620-621

_Claims: 2 verified / 2 proposed · 7.701s_

**93. What Schirmer tear test values indicate KCS in dogs?**
_[Keratoconjunctivitis Sicca]_

**Book answer:** Normal is at least 15 mm/min of wetting; symptomatic dogs usually have less than 10 mm/min. Treatment uses lacrimostimulants such as cyclosporine 0.2% ointment or tacrolimus q12h.

**AI answer:**

In dogs, decreased Schirmer tear test results are diagnostic for KCS. [1]

Practical interpretation:

- Normal: at least 15 mm/min of wetting. [1]
- Symptomatic patients: usually <10 mm/min of wetting. [1]

The provided evidence does not define an exact single diagnostic cutoff for all dogs beyond stating that decreased results are diagnostic and that symptomatic patients are usually <10 mm/min. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.849

_Claims: 3 verified / 3 proposed · 6.579s_

**94. Why should the prolapsed third eyelid gland be replaced rather than removed?**
_[Prolapsed Gland of the Third Eyelid (Cherry Eye)]_

**Book answer:** Because the gland produces up to 50% of the aqueous tear film, and excising it predisposes to KCS. Surgical replacement (imbrication technique) is recommended.

**AI answer:**

The prolapsed third eyelid gland should be replaced because surgical replacement is the listed treatment for this condition.[1] Preservation of the gland is important because it produces up to 50% of the aqueous tear film.[1] Removal/excision is therefore undesirable, as it puts the patient at substantial risk for developing KCS as the dog ages.[1]

The provided evidence does not further compare specific replacement techniques or quantify the risk of KCS after excision.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1175-1176

_Claims: 3 verified / 4 proposed, 1 dropped by the gate · 8.788s_

**95. What cough suppressants are used for tracheal collapse?**
_[Tracheal and Airway Collapse]_

**Book answer:** Butorphanol 0.5-1 mg/kg PO q4-8h or hydrocodone 0.22 mg/kg PO q4-8h, reduced to the least frequent dosing that controls the cough.

**AI answer:**

For tracheal collapse, narcotic cough suppressants used to break the cough cycle include:

- **Butorphanol**: 0.5–1 mg/kg PO q4–8h. [1]
- **Hydrocodone**: 0.22 mg/kg PO q4–8h. [1]

For **non-productive, paroxysmal, continuous, or debilitating cough associated with airway collapse**, listed antitussives in dogs include:

- **Butorphanol**: 0.55 mg/kg PO q6–12h, or 0.055–0.11 mg/kg SC. [2]
- **Hydrocodone**: 2.5–5 mg/dog PO q6–24h. [2]
- **Codeine**: 0.1–0.3 mg/kg PO q6–8h. [2]

For **severe respiratory distress in tracheal collapse**, sedation and cough suppression can include **butorphanol 50 µg/kg SC**. [1] Addition of **acepromazine 25 µg/kg SC** can enhance sedative effects and further reduce the cough reflex. [1]

Over-the-counter cough suppressants rarely reduce cough. [3]

The provided evidence does not cover patient selection, contraindications, adverse effects, monitoring, or comparative efficacy among these agents.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1395; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.273; [3] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.1395

_Claims: 5 verified / 5 proposed · 15.094s_

**96. What components make up brachycephalic airway syndrome?**
_[Brachycephalic Airway Syndrome]_

**Book answer:** Stenotic nares, overlong soft palate, everted laryngeal saccules and laryngeal collapse; a hypoplastic trachea may also be present. English bulldogs are most commonly affected (up to 55% of the breed).

**AI answer:**

Brachycephalic airway syndrome is partial upper airway obstruction in brachycephalic breeds of dogs and cats. [1]

Components listed for brachycephalic airway syndrome include:

- Stenotic nares [1]
- Overlong soft palate [1]
- Everted laryngeal saccules [1]
- Laryngeal collapse [1]

Hypoplastic trachea can also be present and worsen respiratory distress. [1]

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.262-263

_Claims: 3 verified / 3 proposed · 6.705s_

**97. What is the emergency treatment for a cat in an asthma crisis?**
_[Asthma, Bronchitis—Cats]_

**Book answer:** Oxygen and a parenteral bronchodilator such as terbutaline 0.01 mg/kg IV or SC, repeated if there is no improvement in 20-30 minutes.

**AI answer:**

Emergency treatment for a cat in an asthma crisis is oxygen and a parenteral bronchodilator. [1] In an acute crisis, nursing care includes oxygen therapy, bronchodilators, and sedatives. [1] Manipulation should be minimized to lessen stress and oxygen needs. [1]

**Bronchodilator**
- Injectable terbutaline: **0.01 mg/kg IV or SC**. [1]
- It can be repeated if there is no clinical improvement, defined as decreased respiratory rate or effort, within **20–30 minutes**. [1]

**Sedation/anxiolysis**
A sedative can help decrease anxiety. [1] Listed options are:
- Butorphanol tartrate **0.2–0.4 mg/kg IV or IM**. [1]
- Buprenorphine **0.01 mg/kg IV or IM**. [1]
- Acepromazine **0.01–0.05 mg/kg SC**. [1]

**Corticosteroid**
A short-acting parenteral corticosteroid may also be required. [1]
- Dexamethasone sodium phosphate: **0.1–0.25 mg/kg IV or SC**. [1]
- It can be repeated if no improvement is noted within **20–30 minutes**. [1]

The provided evidence does not cover additional diagnostics, monitoring parameters, or longer-term management after stabilization.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.194-195

_Claims: 10 verified / 10 proposed · 12.495s_

**98. What is the starting corticosteroid dose for IMHA and when is it reduced?**
_[Anemia, Immune-Mediated]_

**Book answer:** Prednisone 1-2 mg/kg/day divided q12h for 2-4 weeks (prednisolone in cats). Once the PCV is above 30%, the dose drops to 1 mg/kg q12h and is then tapered by no more than 25-50% per month over 3-6 months.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages provide corticosteroid doses for uses such as allergy, anti-inflammatory treatment, immunosuppression, hypoadrenocorticism, shock, and lymphoma, but they do not state an IMHA starting corticosteroid dose or when to reduce it.)

**Citation(s):** none (no claim cleared the verification gate)

_Claims: 0 verified / 0 proposed · 3.489s_

**99. How is desmopressin used before surgery in dogs with von Willebrand disease?**
_[Von Willebrand Disease]_

**Book answer:** 1 µg/kg SC given 30 minutes before surgery in dogs with mild to moderate Type 1 vWD. The response is variable.

**AI answer:**

Desmopressin acetate (DDAVP) is a vasopressin analog used preoperatively in dogs with mild to moderate Type 1 von Willebrand disease to enhance surgical hemostasis. [1]

Recommended administration is 1 µg/kg SC, given 30 minutes before surgery. [1]

Response is variable, so transfusion should be available if DDAVP alone does not prevent bleeding. [1]

The provided evidence does not cover use in dogs outside mild to moderate Type 1 vWD, nor alternative dosing schedules.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - pp.1474-1475

_Claims: 3 verified / 3 proposed · 9.395s_

**100. Which animals are predisposed to heat stroke?**
_[Heat Stroke and Hyperthermia]_

**Book answer:** Longhaired and brachycephalic animals, very young or old animals, young dogs that overexert, and old dogs with preexisting disease. Cats are uncommonly affected.

**AI answer:**

Animals predisposed to heat stroke include:

- **Dogs and cats**, although cats are uncommon cases. [1]
- **Any breed**; heat stroke is not limited to specific breeds. [1]
- **Animals of any age**, but especially age extremes. [1]
- **Young dogs** that tend to overexert. [1]
- **Animals with a previous history of heat-related disease.** [2]
- **Animals with heat intolerance due to poor acclimatization.** [2]
- **Animals with underlying disease**, including laryngeal paralysis, brachycephalic obstructive disease, cardiovascular disease, neuromuscular disease, and previous history of heat-related disease. [1]

The provided evidence does not further define breed-specific, environmental, or management-related predispositions beyond the factors listed above.

**Citation(s):** [1] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.646; [2] Blackwell's Five Minute Veterinary Consult   Canine and Feline - p.646

_Claims: 7 verified / 16 proposed, 9 dropped by the gate · 17.319s_
