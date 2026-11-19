# Blackwell's Five-Minute Veterinary Consult: Canine and Feline: AI answers vs book answers (all 17 books indexed, gpt-5-mini)

Each question was run through the VetAI PoC pipeline (retrieve → synthesize → verify → generate) with `openai:gpt-5-mini`, over the index of all 17 reference books (top-6 passages, at most 2 from any one book). The **book answer** is the answer key; the **AI answer** and **citations** are what the system produced. Citations show the book, chapter/section and page of the passage each claim was verified against ("PDF p." where the book prints no page numbers).
**Answered with citations: 99 of 100.**


**1. Why are cats more susceptible to acetaminophen toxicosis than dogs?**
_[Acetaminophen (APAP) Toxicosis]_

**Book answer:** Cats cannot effectively glucuronidate acetaminophen because of a genetic deficiency in the glucuronide conjugation pathway. They can be poisoned by as little as 50-60 mg/kg (often half a tablet), and rapidly develop methemoglobinemia.

**AI answer:**

Cats are more susceptible because they primarily metabolize acetaminophen via sulfation; when this pathway (and glucuronidation) is saturated, toxic metabolites are produced and cats develop the toxic cytochrome P450 metabolite at much lower doses than dogs. [1][2]

In cats, deacetylation of acetaminophen to p-aminophenol (PAP) causes oxidative damage to red blood cells, and glutathione depletion leads to rapid methemoglobinemia and Heinz body formation. [2][3]

In short, greater reliance on sulfation with limited glucuronidation → earlier formation of toxic cytochrome P450 metabolites, plus PAP-mediated oxidative RBC injury and glutathione depletion, explains the increased susceptibility of cats compared with dogs.

The provided evidence does not specify comparative dose thresholds, broader clinical course, or treatment/management details.

**Citation(s):** [1] The Merck Veterinary Manual, Toxicology, p. 3029; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Acetaminophen (apap) Toxicosis, p. 10; [3] Ettinger's Textbook of Veterinary Internal Medicine, 269. Acute Toxic and Other Parenchymal Liver Disease, PDF pp. 6641–6642

**2. What is the N-acetylcysteine protocol for acetaminophen toxicosis?**
_[Acetaminophen (APAP) Toxicosis]_

**Book answer:** A loading dose of 140 mg/kg diluted in D5W PO or IV, then 70 mg/kg diluted in D5W PO or IV q6h for 5-7 more treatments. Activated charcoal 2 g/kg PO is given right after emesis or gastric lavage, and SAMe can be added as a glutathione donor.

**AI answer:**

N-acetylcysteine (NAC) protocols for acetaminophen toxicosis

Protocol options
- Standard loading dose: 140 mg/kg of a 5% solution IV or PO (diluted in 5% dextrose or sterile water). [1][2][3]
- Standard oral maintenance: 70 mg/kg PO q6h for 7 treatments. [1][2][4]
- For cats: initial oral loading dose 140 mg/kg, followed by 70 mg/kg PO q6h for 7 treatments. [2]

IV administration details
- Administer IV doses as slow IV over 15–20 minutes (dilute to 5%). [1][2][3]
- If using a solution not labeled for injectable use, it is preferable to use a 0.2 micron in-line filter (or a 0.2‑micron bacteriostatic filter for IV administration). [1][4]
- Alternative IV infusion regimen (three-step infusion): 150 mg/kg IV in 200 ml 5% glucose over 15 minutes, then 50 mg/kg IV in 500 ml over 4 hours, then 100 mg/kg IV in 1000 ml over 16 hours. [5]

Other considerations
- If activated charcoal was given, wait 2–3 hours before PO administration of NAC (activated charcoal may adsorb NAC). [2][4]
- For massive ingestions some authors suggest a 280 mg/kg loading dose and continuing treatment for 12–17 doses. [2][4]

Monitoring
- Monitor liver enzymes and recheck at 24 and 48 hr; monitor for methemoglobinemia, Heinz body anemia, and hemolysis. [1][2]

Limitations of the provided evidence
- The provided claims give oral and IV dosing options, an alternative IV infusion regimen, monitoring recommendations, and cat-specific oral dosing, but do not specify a standard IV maintenance dosing schedule following the 140 mg/kg IV loading dose, nor do they provide criteria for choosing PO versus IV, timing to start NAC after ingestion, or other supportive care measures.

**Citation(s):** [1] The Merck Veterinary Manual, Toxicology, pp. 3029–3030; [2] Plumb's Veterinary Drug Handbook, Systemic Monographs › Acetylcysteine, pp. 78–79; [3] Applied Pharmacology for Veterinary Technicians, C - Antidotes, p. 431; [4] Plumb's Veterinary Drug Handbook, Systemic Monographs › Acetylcysteine, pp. 76–78; [5] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 3–4

**3. What is the fomepizole dosing schedule for ethylene glycol toxicosis in dogs?**
_[Ethylene Glycol Toxicosis]_

**Book answer:** 20 mg/kg IV initially, then 15 mg/kg IV at 12 and 24 hours, then 5 mg/kg IV at 36 hours. The book describes fomepizole as an effective, non-toxic liver alcohol dehydrogenase inhibitor that needs less intensive care than ethanol.

**AI answer:**

Fomepizole dosing schedule for ethylene glycol toxicosis in dogs:

- Initial loading dose: 20 mg/kg IV. [1][2][3][4]  
- At 12 hours after the initial dose: 15 mg/kg IV. [1][2][3][4]  
- At 24 hours after the initial dose: 15 mg/kg IV. [1][2][3][4]  
- At 36 hours after the initial dose: 5 mg/kg IV; additional 5 mg/kg doses may be given as necessary. [1][2][3][4]

The provided evidence does not specify criteria for when additional 5 mg/kg doses should be given or how long dosing should continue beyond the doses listed.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Fomepizole, pp. 1595–1596; [2] Plumb's Veterinary Drug Handbook, Systemic Monographs › Fomepizole, pp. 1596–1598; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Ethylene Glycol Toxicosis, p. 469; [4] The Merck Veterinary Manual, Toxicology, p. 3048

**4. Which methylxanthine makes up the largest fraction in chocolate?**
_[Chocolate (Methylxanthine) Toxicosis]_

**Book answer:** Theobromine. Chocolate toxicosis causes acute gastroenteric, neurologic and cardiac signs from excessive intake of methylxanthine alkaloids.

**AI answer:**

Theobromine is the largest fraction of methylxanthines in chocolate products [1]. The same is reported for cacao bean mulch [2]. 

The provided evidence does not give quantitative concentrations or the relative amounts of other methylxanthines.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Chocolate (Methylxanthine) Toxicosis, p. 256; [2] The Merck Veterinary Manual, Toxicology, p. 2966

**5. What are the main effects of xylitol ingestion in dogs, and how fast do signs appear?**
_[Xylitol Toxicosis]_

**Book answer:** Vomiting, weakness, ataxia, seizures, hypoglycemia and hypokalemia, and in some dogs hepatic failure. Signs may develop within 15-30 minutes, but with sugar-free gums hypoglycemia may be delayed up to 12 hours.

**AI answer:**

Main effects
- Xylitol produces a rapid, dose‑dependent insulin release in dogs that can cause profound hypoglycemia. [1][2]
- Clinical manifestations of the hypoglycemia include vomiting, weakness, ataxia, depression, hypokalemia, seizures, and coma. [2][3][4]
- Xylitol exposure can also increase serum liver enzyme activities, and a subset of dogs progress to severe hepatic necrosis or hepatic insufficiency/failure with signs such as depression, vomiting, icterus, and coagulopathy. [2][3][4][5]

How fast signs appear
- Clinical effects of hypoglycemia generally occur within 30 minutes of ingestion. [1][2]
- If xylitol is in a substrate that slows absorption (for example, some gum products), hypoglycemia may be delayed (reported up to 12 hours or up to 12–18 hours after exposure). [2][3][4]
- Mild to moderate elevations of ALT can be seen within 4 hours of ingestion. [4]

Dose associations (risk indicators)
- Dosages over ~75–100 mg/kg have been associated with hypoglycemia in dogs. [3]
- Some dogs ingesting >500 mg/kg may develop severe hepatic insufficiency or failure. [1][3]
- Hepatic failure with very high liver enzymes, hyperbilirubinemia, and coagulopathy may occur at dosages >0.5 g/kg. [4]

Limitations of the provided evidence
- The supplied evidence does not include specific treatment recommendations, detailed prognostic probabilities, or exact timelines for progression from enzyme elevations to clinical hepatic failure.

**Citation(s):** [1] The Merck Veterinary Manual, Toxicology, p. 2968; [2] Ettinger's Textbook of Veterinary Internal Medicine, 134. Hepatotoxicoses, PDF pp. 2696–2697; [3] The Merck Veterinary Manual, Toxicology, pp. 2968–2969; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Xylitol Toxicosis, p. 1413; [5] Ettinger's Textbook of Veterinary Internal Medicine, 269. Acute Toxic and Other Parenchymal Liver Disease, PDF pp. 6648–6650

**6. What is the recommended fluid therapy after grape or raisin ingestion in a dog?**
_[Grape, Raisin, and Currant Toxicosis]_

**Book answer:** Fluid diuresis at 2-3 times maintenance for at least 48 hours, longer if renal failure develops, after GI decontamination with emesis and activated charcoal.

**AI answer:**

Recommended approach
- Provide aggressive fluid diuresis at 2–3 times maintenance for a minimum of 48 hours; continue longer if renal failure develops.[1][2]
- Fluid choice may vary with circumstance, but 0.9% NaCl is the most commonly recommended.[1]

Monitoring
- Monitor serum chemistry values, particularly renal values, for a minimum of 72 hours.[1]
- Renal function and fluid balance should be monitored during fluid administration.[2]

Limitations of the evidence
- The provided claims do not specify exact infusion rates in mL/kg/h, detailed criteria for stopping or tapering fluids, or recommendations for adjunctive therapies.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Grape, Raisin, and Currant Toxicosis, p. 564; [2] The Merck Veterinary Manual, Toxicology, p. 2968

**7. Which species is at risk of systemic lily poisoning, and what organ is affected?**
_[Lily Toxicosis]_

**Book answer:** Cats. Ingestion of Lilium or Hemerocallis (daylily) leaves or flowers causes a severe nephrotoxic syndrome, with as little as 2-3 leaves reported to be dangerous. Dogs only get mild GI upset.

**AI answer:**

Cats are the species at risk of systemic lily poisoning. [1][2]

Ingestion of Lilium and Hemerocallis spp. results in a severe nephrotoxic syndrome (renal/acute kidney injury). [1][2]

The provided evidence does not specify other species at risk, nor does it detail clinical signs, timelines, treatments, or prognosis.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Lily Toxicosis, p. 804; [2] Ettinger's Textbook of Veterinary Internal Medicine, 135. Renal Toxicoses, PDF pp. 2709–2710

**8. Why is the coagulopathy from anticoagulant rodenticides delayed?**
_[Rodenticide Toxicosis—Anticoagulants]_

**Book answer:** Because it results from depletion of the vitamin K1-dependent clotting factors II, VII, IX and X, so onset is delayed by 3-5 days.

**AI answer:**

Anticoagulant rodenticides inhibit vitamin K1 epoxide reductase, DT diaphorase, and possibly other enzymes involved in the reduction of vitamin K1 epoxide to vitamin K1. [1]

By antagonizing vitamin K epoxide reductase they block recycling of vitamin K and thereby stop production/activation of clotting factors II, VII, IX, and X. [2][3]

Vitamin K1 is required for carboxylation of clotting factors II, VII, IX, and X; uncarboxylated clotting factors do not bind calcium sufficiently to participate in clot formation. [1][4]

A latent period occurs because clotting factors already present at the time of ingestion continue to function until they are consumed, so clinical signs are typically delayed (reported as 3–5 days or 3–7 days after ingestion). [1][3][5]

The individual factors have different half‑lives (II 42 h, VII 6.2 h, IX 13.9 h, X 16.5 h) and gradually decline over 36–72 hours following intoxication, which underlies the progressive loss of coagulation once vitamin K recycling is inhibited. [4]

What is not covered by the provided evidence: specifics on species variability, dose–response thresholds, diagnostic testing, monitoring, or treatment recommendations.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Rodenticide Toxicosis—Anticoagulants, p. 1187; [2] The Merck Veterinary Manual, Toxicology, pp. 3165–3166; [3] Ettinger's Textbook of Veterinary Internal Medicine, 138. Hematologic Toxicoses, PDF pp. 2742–2743; [4] Ettinger's Textbook of Veterinary Internal Medicine, 171. Hyper- and Hypocoagulable States, PDF pp. 3308–3309; [5] The Merck Veterinary Manual, Toxicology, p. 3166

**9. How long is vitamin K1 given for first- versus second-generation anticoagulant rodenticides?**
_[Rodenticide Toxicosis—Anticoagulants]_

**Book answer:** 2.5-5.0 mg/kg PO: q12h for 5-7 days for most first-generation products, and q24h for 4-6 weeks for most second-generation products. Feeding a little fat may improve absorption.

**AI answer:**

Summary of reported treatment durations

First‑generation anticoagulants
- Several sources report vitamin K1 at 2.5–5.0 mg/kg PO q12h for 5–7 days for most first‑generation anticoagulants. [1][2]
- Another source states treatment with phytonadione for 14 days is usually sufficient for first‑generation agents. [3]
- A documented warfarin/first‑generation protocol: initially 2.5 mg/kg SC in several sites, then 1–2.5 mg/kg in divided PO doses q8–12h for 5–7 days. [5]

Second‑generation anticoagulants
- Several sources report vitamin K1 PO q24h for 4–6 weeks for most second‑generation anticoagulants. [1][2]
- Other guidance states recommended dosages are generally 3–5 mg/kg/day PO for 3–4 weeks (second‑generation agents are the vast majority of exposures). [4]
- If the anticoagulant is a second‑generation agent or is unknown, treatment should be instituted for at least 30 days. [3]
- A documented brodifacoum regimen: initially 5 mg/kg SC in several sites, then 2.5 mg/kg PO q12h for 3 weeks, then re‑evaluate coagulation status. [5]

What is not fully resolved by these sources
- Exact single optimal duration is inconsistent across sources (reports range from ~3 weeks to 6 weeks for second‑generation agents and from 5–7 days to 14 days for first‑generation agents), so choice of duration depends on the specific agent and clinical judgment.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Rodenticide Toxicosis—Anticoagulants, p. 1188; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Rodenticide Toxicosis—Anticoagulants, pp. 1187–1188; [3] Plumb's Veterinary Drug Handbook, Systemic Monographs › Phytonadione, pp. 2896–2897; [4] The Merck Veterinary Manual, Toxicology, pp. 3166–3167; [5] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 352–353

**10. Which dogs are most susceptible to ivermectin toxicosis?**
_[Ivermectin and Other Macrocyclic Lactones Toxicosis]_

**Book answer:** Collies are most commonly affected, along with dogs homozygous for the ABCB1 gene deletion (found in Shetland sheepdogs, Australian shepherds and others). Heterozygous dogs can react at higher doses.

**AI answer:**

Most susceptible: Collies are the single most commonly affected breed. [1]

At-risk breeds and populations: Dogs with the MDR1/ABCB1 mutation (which impairs p‑glycoprotein transport of ivermectin) are at higher risk for CNS toxicity; this includes Collies, Australian Shepherds, Shetland sheepdogs, long‑haired Whippets and similar breeds. [2] The ABCB1 mutation has been identified in Shetland sheepdogs, Australian shepherds, Old English sheepdogs, German shepherds, English shepherds, longhaired whippets, silken windhounds, and a variety of mixed‑breed dogs. [1]

Contraindications and breed groups: Ivermectin is contraindicated in collies, Shetland sheepdogs, Old English sheepdogs, Australian shepherds, other herding breeds, and crosses with these breeds. [3]

Pathophysiology and genetics: Ivermectin‑sensitive collies lack adequate P‑glycoprotein to exclude ivermectin from the brain. [4] Dogs homozygous for the ABCB1 gene deletion are affected; heterozygous dogs can react at higher doses. [1]

Limitations of the evidence provided: These statements identify which breeds and genetic statuses confer increased susceptibility, the underlying P‑glycoprotein mechanism, and contraindicated breeds. The provided evidence does not give dose thresholds, prevalence data, specific clinical signs, diagnostic testing procedures, or treatment recommendations.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Ivermectin and Other Macrocyclic Lactones Toxicosis, p. 771; [2] Plumb's Veterinary Drug Handbook, Systemic Monographs › Ivermectin, pp. 1981–1982; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Demodicosis, p. 356; [4] Muller and Kirk's Small Animal Dermatology, Chapter 6 - Parasitic Skin Disease, pp. 428–429

**11. Why is metaldehyde called the 'shake and bake' toxicant?**
_[Metaldehyde Toxicosis]_

**Book answer:** Because of its characteristic tremors, seizures and hyperthermia. Signs usually develop within 4 hours of ingestion, and there is no specific antidote.

**AI answer:**

Metaldehyde is called the “shake and bake” toxicant because it produces characteristic tremors and seizures (“shake”) together with marked hyperthermia (“bake”). [1]

The hyperthermia is often 106°F (41°C) or greater and, if uncontrolled, can progress to DIC and multi‑organ failure. [1]

Neurologic signs — including severe muscle tremors, anxiety, hyperesthesia, ataxia, tachycardia, and hyperthermia — typically develop within 1–3 hours after ingestion. [2]

These claims explain the nickname but do not provide information on the biochemical mechanism, specific clinical management, or species‑specific prognosis.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Metaldehyde Toxicosis, p. 876; [2] The Merck Veterinary Manual, Toxicology, pp. 3070–3071

**12. How can cats be exposed to permethrin toxicity, and what treats the tremors?**
_[Pyrethrin and Pyrethroid Toxicosis]_

**Book answer:** Through direct contact with dogs treated with permethrin spot-ons. Tremors and seizures are treated with methocarbamol 55-220 mg/kg IV, not exceeding 330 mg/kg/day.

**AI answer:**

How cats are exposed
- Misapplication of permethrin-containing dog-only flea products onto cats can expose them to permethrin. [1][2]
- Direct contact with permethrin spot-on treated dogs (for example during grooming or close contact) can expose cats. [2][3]
- Cats inappropriately treated with permethrin-containing products for use on dogs often develop muscle tremors, ataxia, seizures, hyperthermia, and death within hours if not treated. [2]

What treats the tremors
- Methocarbamol remains the agent of choice to treat tremors, especially for cats exposed to permethrin. [1]
- Methocarbamol injectable (Robaxin-V) dosing: 55–220 mg/kg IV not to exceed 330 mg/kg/day; administer one-half dose slowly IV, wait until the patient begins to relax, then continue administration to effect; do not exceed 2 mL/minute injection rate, and start with a lower dose initially. [1]
- Methocarbamol can be used orally for treating mild tremors at 50–100 mg/kg q8h; onset ~30 minutes. [1]
- Diazepam at low dosages has been used to control minor hyperesthesia. [1]
- Seizure control has been achieved with pentobarbital, propofol (3–6 mg/kg IV or 0.1 mg/kg/min CRI), and inhalant anesthetics. [1]

What is not covered by the provided evidence
- The supplied claims do not include details on decontamination procedures, other supportive care measures (fluid therapy, temperature control), monitoring protocols, or detailed prognostic statistics beyond the statement that untreated cases may die within hours.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Pyrethrin and Pyrethroid Toxicosis, p. 1144; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Pyrethrin and Pyrethroid Toxicosis, p. 1144; [3] Plumb's Veterinary Drug Handbook, Appendix › Imidacloprid, pp. 3889–3890

**13. What pathologic findings are associated with NSAID toxicosis?**
_[Nonsteroidal Anti-Inflammatory Drug Toxicosis]_

**Book answer:** GI irritation, ulceration or hemorrhage with possible gastric perforation and peritonitis, plus renal tubular or papillary necrosis or interstitial nephritis. H2 blockers such as ranitidine or famotidine are used for GI ulceration.

**AI answer:**

Summary of pathologic findings associated with NSAID toxicosis

Gastrointestinal
- Erosions and ulcers of the GI tract. [1]
- Vomiting is the most common clinical adverse effect. [2]
- GI ulceration is the most common life‑threatening adverse effect; hematemesis can occur. [2][6]
- NSAID‑induced GI bleeding may be occult (causing iron‑deficiency anemia) or overt with vomiting, hematemesis, and melena. [2]
- As organic acids, NSAIDs (especially aspirin) may cause direct chemical irritation of the GI mucosa. [2]
- Enterohepatic recirculation of certain NSAIDs can produce high biliary concentrations that increase ulcerogenic potential in the gut. [2]
- Injury can occur anywhere in the GI tract, with the large colon (especially the right dorsal colon) and gastric mucosa most sensitive. [3]
- Ulcerative lesions in the large colon can produce a protein‑losing enteropathy with ventral edema, anorexia, lethargy, weight loss, diarrhea, and colic. [3]
- Scarring of the right dorsal colon can lead to large‑colon impactions; severe cases may require large‑colon resection. [3]
- COX inhibitors cause delayed GI healing. [3]
- Phenylbutazone at high dose or with prolonged administration causes a protein‑losing enterocolopathy in horses. [3]

Renal / Urologic
- Acute renal failure and acute interstitial nephritis have been reported. [1]
- Typical NSAID adverse effects from impaired prostaglandin synthesis include renal necrosis. [4]
- NSAID nephrotoxicity is also listed among other potential side effects. [5]

Hepatobiliary
- Idiosyncratic hepatocellular damage has been reported. [1]
- Hepatotoxicity is listed as a possible adverse effect. [5]

Hematologic / Hemostasis
- Bleeding disorders may occur secondary to decreased platelet aggregation. [1]
- NSAID‑induced GI blood loss may be worsened by impaired platelet function because COX‑1 inhibition prevents platelets from forming TXA2, a potent aggregating agent. [2]
- Reduced platelet aggregation and bleeding tendencies are noted among other adverse effects. [5]
- Typical adverse effects include altered platelet function contributing to bleeding. [4]

Other reported pathologic effects
- Etodolac can cause keratoconjunctivitis sicca (KCS) in some dogs. [4]
- Inhibition of cartilage metabolism and bone marrow suppression are listed among other side effects. [5]

What the provided evidence does not cover
- Detailed histopathologic descriptions of lesions, timelines to lesion development, dose–response relationships, species‑specific incidence, or management/prognosis are not provided in the supplied evidence.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Nonsteroidal Anti-Inflammatory Drug Toxicosis, p. 954; [2] The Merck Veterinary Manual, Pharmacology, p. 2716; [3] The Merck Veterinary Manual, Circulatory System, p. 292; [4] Slatter's Fundamentals of Veterinary Ophthalmology, 3 Ophthalmic Medications and Therapeutics › Cautions and Contraindications With NSAID Use, p. 71; [5] Applied Pharmacology for Veterinary Technicians, 14 - Drugs Used to Relieve Pain and Inflammation › Nonsteroidal Antiinflammatory Drugs, pp. 275–276; [6] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hematemesis, p. 587

**14. How long can signs be delayed after a pit viper bite, and is local tissue reaction a reliable guide?**
_[Snake Venom Toxicosis—Pit Vipers]_

**Book answer:** Signs may be delayed for up to 8 hours after envenomation, and tissue reaction around the bite is not a reliable indicator of systemic envenomation.

**AI answer:**

- Signs after a pit viper (crotalid) bite can be delayed for up to 8 hours after envenomation. [1]

- If erythema, edema, and pain are not seen within 20 minutes of the bite, envenomation has not occurred. [3] Envenomation does not occur in approximately 20% to 25% of bites. [3]

- Despite the above, animals should be monitored for a minimum of 24 hours after being bitten. [3] All snakebite victims should be monitored closely for a minimum of 24 (crotalid) to 48 (elapid) hours for the development of clinical signs. [2]

What is not covered by the provided evidence: how to reconcile the 20‑minute “no local signs” rule with the reported possibility of up to an 8‑hour delay in signs, and any additional diagnostic or treatment guidance.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Snake Venom Toxicosis—Pit Vipers, p. 1241; [2] The Merck Veterinary Manual, Toxicology, pp. 3159–3160; [3] Small Animal Surgery (Fossum), 16 Surgery of the Integumentary System › Treatment, pp. 266–267

**15. Which breeds are at increased risk of hypoadrenocorticism?**
_[Hypoadrenocorticism (Addison's Disease)]_

**Book answer:** Great Danes, rottweilers, Portuguese water dogs, standard poodles, bearded collies, Leonbergers, West Highland white terriers, Nova Scotia duck tolling retrievers and Wheaten terriers. Golden retrievers and Chihuahuas have a decreased risk.

**AI answer:**

Breeds reported to have an increased relative risk of hypoadrenocorticism: Great Danes, rottweilers, Portuguese water dogs, standard poodles, bearded collies, Leonbergers, West Highland white terriers, Nova Scotia duck tolling retrievers, and Wheaten terriers.[1]

Hypoadrenocorticism may be familial in Standard Poodles, West Highland White Terriers, Great Danes, Bearded Collies, Portuguese Water Dogs, and a variety of other breeds.[2]

The provided evidence does not specify the magnitude of increased risk for each breed, overall prevalence, age/sex predilections, the genetic mode of inheritance, or any diagnostic or management details.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hypoadrenocorticism (Addison’s Disease), p. 702; [2] The Merck Veterinary Manual, Endocrine System, p. 574

**16. What is the long-term treatment for chronic primary hypoadrenocorticism?**
_[Hypoadrenocorticism (Addison's Disease)]_

**Book answer:** Daily glucocorticoid replacement (prednisone 0.1-0.2 mg/kg/day) plus mineralocorticoid replacement with DOCP (Percorten) 2.2 mg/kg IM or SC, usually monthly, adjusted on serial electrolytes.

**AI answer:**

- Life‑long glucocorticoid and/or mineralocorticoid replacement therapy is required. [1]

- Typical long‑term regimen for chronic primary hypoadrenocorticism: most patients will need daily glucocorticoid replacement (prednisone, 0.1–0.2 mg/kg/day), plus mineralocorticoid replacement (DOCP, Percorten, 2.2 mg/kg IM or SC, typically given monthly and adjusted as needed on the basis of serial electrolyte determinations). [1]

- If using oral fludrocortisone, adjust the daily dose by 0.05–0.1 mg increments as needed based on serial electrolyte determinations; after starting therapy check electrolytes weekly until they stabilize in the normal range, then monthly for the first 3–6 months and every 3–12 months thereafter. [2]

- Many dogs on fludrocortisone require incremental dose increases during the first 6–24 months; in most dogs the final fludrocortisone dosage needed is 20–30 µg/kg/day, and very few are controlled on 10 µg/kg/day or less. [2]

What is not covered by the provided evidence: comparative choice of DOCP versus fludrocortisone, adverse effects, detailed monitoring for DOCP beyond “adjusted as needed on the basis of serial electrolyte determinations,” and acute/crisis management.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hypoadrenocorticism (Addison’s Disease), p. 703; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hypoadrenocorticism (Addison’s Disease), p. 704

**17. What is the difference between spontaneous and iatrogenic hyperadrenocorticism?**
_[Hyperadrenocorticism (Cushing's Syndrome)—Dogs]_

**Book answer:** Spontaneous HAC is excessive cortisol production by the adrenal cortex. Iatrogenic HAC results from excessive exogenous glucocorticoids given in any form or by any route.

**AI answer:**

Short answer
- Spontaneous hyperadrenocorticism (HAC) is caused by endogenous excessive cortisol production by the adrenal cortex. [1]  
- Iatrogenic HAC is caused by excessive exogenous administration of glucocorticoids (systemic and/or topical, including otic) and results in bilateral adrenal atrophy with suppressed ACTH. [1]

Pathogenesis — spontaneous forms
- Spontaneous HAC comprises pituitary-dependent (PDH) and adrenal-dependent (ADH) forms. [1]  
- PDH: uncontrolled proliferation (tumor) of basophilic or chromophobic cells of the pars intermedia and pars distalis → hypersecretion of ACTH → bilateral adrenocortical hyperplasia. [1]  
- ADH: cortisol-secreting adrenocortical neoplasia (cortical adenoma or carcinoma). [1]

Pathogenesis — iatrogenic form, clinical and practical points
- Iatrogenic HAC results from exogenous glucocorticoids (oral, injectable, or topical—including eyes, ears, skin). [1][2]  
- It causes adrenal atrophy and suppressed endogenous ACTH. [1]  
- Clinically, iatrogenic HAC is indistinguishable from naturally occurring (spontaneous) disease. [1]  
- Long-term steroid use by mouth, injection, or topically can produce adrenocortical suppression and iatrogenic HAC in dogs. [2]  
- A poor cortisol response to an ACTH stimulation test is suggestive of iatrogenic disease. [3]  
- The treatment of choice for iatrogenic HAC is to taper off and stop glucocorticoid therapy. [3]

What the provided evidence does not cover
- The evidence above does not provide detailed diagnostic protocols to differentiate PDH from ADH, nor does it specify management options, prognosis, tapering schedules, monitoring protocols, or therapeutic interventions for spontaneous (endogenous) HAC.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, 26 Hyperadrenocorticism, Canine › Etiology/Pathophysiology, pp. 394–395; [2] Muller and Kirk's Small Animal Dermatology, Chapter 10 - Endocrine and Metabolic Diseases, pp. 799–800; [3] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 9 Hereditary, Congenital, and Acquired Alopecias, p. 238

**18. How does mitotane work in canine hyperadrenocorticism?**
_[Hyperadrenocorticism (Cushing's Syndrome)—Dogs]_

**Book answer:** Mitotane (o,p'-DDD, Lysodren) selectively destroys the glucocorticoid-secreting cells of the adrenal cortex. It is one of two main drugs for pituitary-dependent HAC and may be the drug of choice for adrenal tumors because it may destroy tumor cells too.

**AI answer:**

Mitotane is an adrenal cytotoxic agent used for medical treatment of pituitary‑dependent hyperadrenocorticism (PDH) in dogs. [1]

Its principal effect is destruction of adrenal cortical tissue: it causes severe, progressive necrosis of the zona fasciculata and zona reticularis. [1] It selectively destroys glucocorticoid‑secreting cells of the adrenal cortex and may destroy tumor cells, which is why it is considered a drug of choice for adrenal tumors (AT). [2] The degree of cortical destruction is dose‑dependent. [3]

Mitotane can also inhibit adrenocortical function without producing overt cell destruction. [1] Although it has been stated that the zona glomerulosa is spared (and aldosterone synthesis unaffected), this is only partially true because the zona glomerulosa may also be affected by mitotane therapy. [1]

For adrenal tumors, the therapeutic goal with mitotane is both reduction of cortisol production and destruction of the neoplastic cells. [4]

What is not covered by the provided evidence: specific dosing regimens, monitoring protocols, timing of effect, frequency or predictors of zona glomerulosa involvement, and adverse‑effect profiles are not described in the cited claims.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Mitotane, pp. 2469–2470; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hyperadrenocorticism (Cushing’s Syndrome)—Dogs, pp. 651–652; [3] Small Animal Surgery (Fossum), 23 Surgery of the Endocrine System › Laboratory Findings, pp. 640–641; [4] Ettinger's Textbook of Veterinary Internal Medicine, 293. Hyperadrenocorticism (Cushing's Syndrome) in Dogs, PDF pp. 7325–7326

**19. What is the initial insulin protocol for diabetic ketoacidosis?**
_[Diabetes Mellitus with Ketoacidosis]_

**Book answer:** Regular insulin is the insulin of choice, starting at 0.2 U/kg IM (or SC if hydration is normal), then 0.1-0.2 U/kg 3-6 hours later, which may be given hourly if needed.

**AI answer:**

Concise initial insulin protocol for diabetic ketoacidosis

- Insulin choice: Regular insulin is the insulin of choice. [1]

- Initial dose (bolus): Give 0.2 U/kg IM (or SC if hydration is normal) as the initial dose. [1]

- Subsequent boluses: Give 0.1–0.2 U/kg 3–6 hours after the initial dose; doses may be given hourly if the patient is closely monitored, and the response to the previous insulin dose should be considered when calculating subsequent dosages. [1]

- Continuous-rate infusion (alternative): Regular insulin may be given as a CRI via a designated catheter; for dogs place 2.2 units/kg into 250 mL 0.9% NaCl, for cats place 1.1 units/kg into 250 mL 0.9% NaCl. Allow 50 mL of the dilute insulin to flow through the IV tubing and discard. [1][2]

- CRI rate adjustments by blood glucose (BG):
  - If BG > 250 mg/dL, administer at 10 mL/hour. [1][3]
  - If BG 200–250 mg/dL, administer at 7 mL/hour. [1][3]
  - If BG 150–200 mg/dL, administer at 5 mL/hour. [1][3]
  - If BG 100–150 mg/dL, administer at 5 mL/hour and add 2.5% dextrose to the IV crystalloid fluids. [1][3]
  - If BG < 100 mg/dL, discontinue IV insulin infusion and continue 2.5–5% dextrose in IV crystalloid infusion. [1][3]

- Monitoring blood glucose: Check blood glucose every 1–3 hours with Chemstrip BG reagent strips and an automated test-strip analyzer (Accu-Chek III; AlphaTrak glucometer). [3]

- Treatment priorities and goals:
  - Insulin must be given, regardless of the blood glucose concentration, to correct the ketoacidotic state. [3]
  - The goal is to slowly lower BG to <250 mg/dL over 6–10 hours; hourly decreases of 50–75 mg/dL/h are ideal. [4]

- Potassium and dose modification:
  - Delay insulin for a minimum of 2 hours if serum K+ concentrations are within the normal range, but delay up to 4 hours if hypokalemia persists. [4]
  - Initial doses (first 2–3 injections) may be reduced by 25–50% in animals with severe hypokalemia. [2]

- Transition as BG approaches 250 mg/dL: Switch to IM regular insulin at 0.1–0.3 U/kg every 4–6 hours, or to SC regular insulin every 6–8 hours if hydration status is good; provide 5% dextrose IV during this stage. [2]

Limitations / what is not covered by the provided evidence
- Specific guidance on potassium supplementation dosing and timing, other electrolyte or acid–base management, fluid therapy regimens, criteria for stopping CRI beyond the BG-based rules above, and broader monitoring beyond BG frequency are not provided in the cited claims.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Diabetes Mellitus with Ketoacidosis, p. 386; [2] Plumb's Veterinary Drug Handbook, Systemic Monographs › Insulin, pp. 1874–1875; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Diabetes Mellitus with Ketoacidosis, pp. 386–387; [4] Ettinger's Textbook of Veterinary Internal Medicine, 290. Diabetic Ketoacidosis and the Hyperosmolar Hyperglycemic State, PDF p. 7209

**20. What is the starting dose of porcine lente insulin (Vetsulin) in cats?**
_[Diabetes Mellitus without Complication—Cats]_

**Book answer:** 2 U per cat SC q12h. Protamine zinc insulin (PZI, U-40) is a long-acting alternative usually given SC q24h.

**AI answer:**

Options reported for starting doses of porcine lente insulin (Vetsulin) in cats:

- Vetsulin product insert: 0.5 Units/kg SC once daily. [1]  
- Alternative recommended starting doses (porcine insulin zinc, lente): 1 Unit per cat SC twice daily for cats <4 kg, and 1.5–2 Units per cat SC twice daily for cats >4 kg. [1]  
- Behrend (2007) glucose-based recommendations: 0.25 Units/kg SC twice daily if blood glucose is 216–342 mg/dL; 0.5 Units/kg SC twice daily if blood glucose is >360 mg/dL. [1]

What is not covered by the provided evidence: which of these regimens should be chosen for a given cat, how to monitor and adjust dosing over time, and safety/contraindication details are not provided in the cited claims.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Insulin, pp. 1876–1877

**21. What is the starting dose of Vetsulin in diabetic dogs, and what syringe must be used?**
_[Diabetes Mellitus without Complication—Dogs]_

**Book answer:** 0.75 units/kg SC q12h. It is a U-40 insulin, so it must be used with a U-40 insulin syringe.

**AI answer:**

Starting dose — dose amount:
- One source lists Vetsulin® at 0.5 U/kg SC once daily, given concurrently with or right after a meal. [1]
- Another source lists Vetsulin® at 0.5 U/kg SC twice daily. [2]

The provided evidence is inconsistent about dosing frequency and does not resolve which regimen (once vs twice daily) should be chosen for a starting dose.

Syringe:
- Vetsulin® is an animal-approved U-40 insulin and U-40 syringes must be used with U-40 insulin. [3]

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Insulin, pp. 1874–1875; [2] Plumb's Veterinary Drug Handbook, Systemic Monographs › Insulin, pp. 1875–1876; [3] Applied Pharmacology for Veterinary Technicians, 9 - Drugs Used in Hormonal, Endocrine, and Reproductive Disorders › Insulin, pp. 175–176

**22. What is the oral methimazole dose for feline hyperthyroidism, and what is the most effective treatment?**
_[Hyperthyroidism]_

**Book answer:** Methimazole 5-15 mg/day divided q8-12h; it can also be given transdermally in PLO gel, though that is slower. Radioiodine therapy is described as arguably the safest and most effective treatment.

**AI answer:** No supported answer. "I could not find evidence in the indexed books to support an answer to this question. Rather than guess, I am reporting that the evidence is missing. Nothing here is stated without a verified source." (Synthesis note: The passages contain multiple oral methimazole dosing statements (examples: "The starting dose is 2.5 mg administered every 12 hours." (plumbs-drug-handbook_p02319_02092); "The recommended initial dose of methimazole is 1.25 to 2.5 mg PO q12h." (ettinger-internal-medicine_p07140_05762); "Cats: 2.5 mg/cat p.o. q12h." (bsava-formulary_p00229_00268); "The recommended initial daily dose of methimazole is 2.5-5 mg in two divided doses." (merck-vet-manual_p00601_01168)), but none of the provided passages state which treatment is the "most effective.")

**Citation(s):** none (no claim cleared the verification gate)

**23. Which dog breeds are predisposed to hypothyroidism?**
_[Hypothyroidism]_

**Book answer:** Larger breeds such as golden retriever, Doberman pinscher, Great Dane and Irish setter, and some smaller breeds including miniature schnauzer, cocker spaniel, poodle and dachshund. It is most common in middle-aged dogs.

**AI answer:**

Summary of breeds reported as predisposed to canine hypothyroidism:

- Cornell University (breeds at risk, in decreasing order of relative risk): Chinese Shar pei, Chow Chow, Great Dane, Irish wolfhound, Boxer, English bulldog, Dachshund, Afghan hound, Newfoundland, Malamute, Doberman pinscher, Brittany spaniel, Poodle, Golden retriever, and Miniature schnauzer. [1]

- Additional breeds reported in other studies: Airedale terrier, Cocker spaniel, Irish setter, Shetland sheepdog, Old English sheepdog, and Pomeranian. [2]

- Breeds in which antithyroglobulin antibodies (TgAA) are found more often: Great Danes, Borzois, Irish setters, Old English sheepdogs, and Doberman pinschers. [2]

- Breeds with a high prevalence of TgAA positivity that are at significantly increased risk for developing hypothyroidism include (but are not confined to) English Setter, Gordon Setter, Golden Retriever, Doberman Pinscher, Old English Sheepdog, Rhodesian Ridgeback, Cocker Spaniel and Boxer. [3]

- A summary list of predisposed breeds (mostly medium and large breeds) includes: golden retriever, Great Dane, doberman pinscher, Irish setter, Airedale terrier, Old English sheepdog, dachshund, miniature schnauzer, Brittany and cocker spaniel, shar-pei, chow chow, poodle, Irish wolfhound, English bulldog, Newfoundland, malamute, and boxer. [4]

- Larger-breed dogs are overall more likely to develop hypothyroidism (examples: golden retriever, Doberman pinscher, Great Dane, Irish setter), though several smaller breeds also appear predisposed (miniature schnauzer, cocker spaniel, poodle, dachshund). [5]

What is not covered by these claims: a complete or exhaustive list of all predisposed breeds, quantitative prevalence or absolute risk estimates, age/sex effects, or other risk modifiers are not provided.

**Citation(s):** [1] Muller and Kirk's Small Animal Dermatology, Chapter 10 - Endocrine and Metabolic Diseases, p. 852; [2] Muller and Kirk's Small Animal Dermatology, Chapter 10 - Endocrine and Metabolic Diseases, pp. 852–853; [3] Ettinger's Textbook of Veterinary Internal Medicine, 285. Hypothyroidism in Dogs, PDF pp. 7050–7051; [4] Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, 28 Hypothyroidism › Signalment/History, pp. 417–418; [5] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hypothyroidism, p. 729

**24. What is the long-term prednisone dose for insulinoma if diet fails?**
_[Insulinoma]_

**Book answer:** Start at 0.25 mg/kg PO q12h and increase as needed to 2-3 mg/kg PO q12h. Diazoxide is another option.

**AI answer:**

If dietary therapy is ineffective, prednisone may be started at 0.25 mg/kg PO q12h and can be increased as needed to 2–3 mg/kg PO q12h. [1][2]

The provided evidence does not specify a particular long-term maintenance dose, duration of therapy, tapering schedule, monitoring parameters, or other management details.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Insulinoma, p. 757; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Insulinoma, p. 757

**25. How is hypertension controlled before and during pheochromocytoma surgery?**
_[Pheochromocytoma]_

**Book answer:** With phentolamine 0.02-0.1 mg/kg IV to effect. Boxers, miniature poodles and German shepherds are predisposed, with a median age of 11 years.

**AI answer:**

Summary — preoperative and intraoperative control of hypertension for pheochromocytoma

Preoperative α-blockade
- Treat for several weeks before surgery with an α-adrenergic blocker (e.g., phenoxybenzamine). [1][2][3]
- Initial phenoxybenzamine dosing: 0.25 mg/kg PO q12h, gradually increased every 2–3 days until blood pressure is within the normal range; this titration may take 1–2 weeks; maximum dose 2 mg/kg. [1]
- An alternative protocol is to start phenoxybenzamine 0.25 mg/kg PO q12h and increase every 2–3 days until reaching 1–1.5 mg/kg PO q12h; treatment in both hypertensive and normotensive dogs should continue for 10–14 days before surgery. [4]
- Recommended phenoxybenzamine range is 0.2–1.5 mg/kg PO q12h beginning 1–2 weeks prior to surgery. [3]

Heart-rate control / adjuncts
- Heart rate can be controlled with a β‑adrenergic blocker (e.g., propranolol, metoprolol, esmolol), but β‑blockade should NOT be initiated until adequate α‑blockade has been established (i.e., normal blood pressure). [1]
- If catecholamine‑induced complications persist after several days of phenoxybenzamine, adding a β‑adrenergic blocker, preferably a selective β1 blocker (e.g., atenolol), can help with preoperative stabilization. [3][4]

Intraoperative / acute hypertension management
- Pre‑ and intraoperative hypertension can be treated with phentolamine 0.02–0.1 mg/kg IV to effect. [3]
- If hypertension is present, sodium nitroprusside or nitroglycerin may also be infused. [5]

Drugs to avoid in suspected pheochromocytoma
- Avoid ketamine, xylazine, medetomidine, dexmedetomidine, atropine, glycopyrrolate, and acepromazine. [1][5]

Limitations
- The provided evidence specifies α‑ and β‑blockade strategies, phentolamine dosing, consideration of nitroprusside/nitroglycerin, and drugs to avoid, but does not provide detailed anesthetic induction/maintenance protocols, infusion rates/dosing for nitroprusside or nitroglycerin, monitoring targets, fluid management, or postoperative hypertensive management.

**Citation(s):** [1] Small Animal Surgery (Fossum), 23 Surgery of the Endocrine System › Anesthesia, p. 643; [2] Ettinger's Textbook of Veterinary Internal Medicine, 298. Pheochromocytoma, PDF pp. 7449–7450; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Pheochromocytoma, pp. 1055–1056; [4] Ettinger's Textbook of Veterinary Internal Medicine, 298. Pheochromocytoma, PDF pp. 7450–7451; [5] Small Animal Surgery (Fossum), 23 Surgery of the Endocrine System › Postoperative Care and Assessment, p. 645

**26. How is central diabetes insipidus treated?**
_[Diabetes Insipidus]_

**Book answer:** With DDAVP: 1-2 drops of the intranasal preparation in the conjunctival sac q12-24h, or 2-5 µg SC q12-24h. An oral DDAVP tablet is also available.

**AI answer:**

Primary therapy
- Central DI is treated with synthetic ADH (desmopressin acetate, DDAVP). [2]

Routes and dosing options described
- Subconjunctival: one to two drops q12–24 h. [1]
- Conjunctival (dogs): one drop twice daily in the conjunctival sac controls polyuria in most dogs. [4]
- Intranasal solution placed in conjunctival sac: 1–4 drops once to twice daily. [4]
- Intranasal solution parenterally: may be given 2–5 micrograms SC once to twice daily. [4]
- Oral tablets (100 mcg q12–24 h) have been used but response is variable and often poor. [3]
- In cats, reported regimens include oral 25–50 mcg q8–12 h, SQ 4 mcg q24 h, conjunctival, and nasal (1 drop q12 h) administration. [3]

Therapeutic trial and expected response
- An ADH supplementation (DDAVP) trial is used; a positive response is a ≥50% decrease in water intake within 3–5 days. [2]
- The response to treatment is rapid and polyuria returns rapidly if DDAVP is discontinued. [3]

Supportive care
- Water must be available at all times for patients with diabetes insipidus. [1]

Limitations of the provided evidence
- These claims describe agents, routes and doses, the ADH trial criterion, speed of response, and the need for water access. They do not provide guidance on monitoring, adverse effects, how to choose between routes for an individual patient, long‑term dose adjustment, or other supportive/contraindication considerations.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hypernatremia, pp. 674–675; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Diabetes Insipidus, p. 383; [3] Ettinger's Textbook of Veterinary Internal Medicine, 282. Diabetes Insipidus, PDF pp. 6973–6974; [4] Plumb's Veterinary Drug Handbook, Systemic Monographs › Desmopressin Acetate, pp. 1036–1037

**27. What blood pressure values define systemic hypertension in dogs and cats?**
_[Hypertension, Systemic]_

**Book answer:** Systolic above 160 mmHg or diastolic above 120 mmHg, measured by any method.

**AI answer:**

Short answer
- In dogs and cats, systolic blood pressure > 160 mmHg or diastolic blood pressure > 120 mmHg (obtained by any method) is considered abnormal. [1]
- With certain exceptions, systolic pressures > 180 mmHg in an animal that appears calm are likely to be truly increased, and systolic pressures > 200 mmHg should be strongly considered evidence of systemic hypertension. [2] [2]

What is not covered by the provided evidence
- The claims do not provide details on measurement technique, frequency of measurement, criteria for confirmation over time, staging, associated target‑organ damage, or treatment/management thresholds.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hypertension, Systemic, p. 689; [2] The Merck Veterinary Manual, Circulatory System, p. 125

**28. What is the first-line drug for systemic hypertension in cats?**
_[Hypertension, Systemic]_

**Book answer:** Amlodipine, with an ACE inhibitor added if proteinuria (UPC above 0.4) is present. In dogs an ACE inhibitor is used.

**AI answer:**

Amlodipine is the first-line drug for systemic hypertension in cats.[1][2][3][4][5]

The provided evidence does not include information on dosing, monitoring, contraindications, adverse effects, alternative or adjunctive therapies, or patient-specific treatment selection.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 236. Systemic Hypertension, PDF pp. 5282–5284; [2] Ettinger's Textbook of Veterinary Internal Medicine, 287. Hyperthyroidism in Cats, PDF pp. 7146–7147; [3] Plumb's Veterinary Drug Handbook, Systemic Monographs › Amitriptyline HCl, pp. 215–217; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hypertension, Systemic, p. 690; [5] WSAVA List of Essential Medicines for Cats and Dogs, Cardiorespiratory and renal systems › Complementary list, p. 13

**29. Which breeds are at increased risk of severe parvovirus enteritis?**
_[Canine Parvovirus Infection]_

**Book answer:** Rottweiler, Doberman pinscher, American pit bull terrier, Labrador retriever, German shepherd and Yorkshire terrier.

**AI answer:**

Breeds reported to be at increased risk for severe canine parvovirus (CPV) enteritis include rottweiler, doberman pincher, American pit bull terrier, Labrador retriever, German shepherd, and Yorkshire terrier. [3][4]

Separately, rottweilers, doberman pinschers, American pit bull terriers, English springer spaniels, and German shepherds have been described as being at increased risk of disease (the citation does not specify severe CPV enteritis). [1][2]

What is not covered by the provided evidence: the magnitude of the increased risk, effects of age or vaccination status, case outcomes or case-fatality, and specific management implications.

**Citation(s):** [1] The Merck Veterinary Manual, Circulatory System, p. 374; [2] The Merck Veterinary Manual, Circulatory System, pp. 373–374; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Canine Parvovirus Infection, p. 216; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Canine Parvovirus Infection, p. 216

**30. What causes canine distemper, and is there an effective antiviral?**
_[Canine Distemper]_

**Book answer:** Canine distemper virus, a Morbillivirus in the Paramyxoviridae family. No antiviral drugs are known to be effective, so treatment is supportive, with broad-spectrum antibiotics for secondary infection because CDV is highly immunosuppressive.

**AI answer:**

Canine distemper is caused by canine distemper virus (CDV). [1][2]

There is no single specific or uniformly successful antiviral treatment; experimental in vitro work with antiviral agents shows promise but these agents have not yet been widely used. [3][4]

Current management is therefore symptomatic and supportive (broad‑spectrum antibiotics, balanced electrolyte solutions, parenteral nutrition, antipyretics, analgesics, and anticonvulsants) and good nursing care is essential. [3][4]

The provided evidence does not specify which antiviral agents were studied, their in vivo/clinical efficacy, dosing, safety, or clinical availability.

**Citation(s):** [1] Slatter's Fundamentals of Veterinary Ophthalmology, 7 Diseases of the Conjunctiva › Canine Viral Conjunctivitis, pp. 171–172; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Canine Distemper, p. 211; [3] The Merck Veterinary Manual, Generalized Conditions, pp. 778–779; [4] The Merck Veterinary Manual, Generalized Conditions, p. 778

**31. What virus causes feline panleukopenia and what cells does it target?**
_[Feline Panleukopenia]_

**Book answer:** Feline parvovirus, which infects only mitotic (rapidly dividing) cells and causes their acute lysis. Clinically it causes sudden depression, vomiting, diarrhea, severe dehydration and high mortality.

**AI answer:**

Feline panleukopenia is caused by the parvovirus feline panleukopenia virus (FPV). [1][2]

FPV infects only mitotic (dividing) cells, producing acute cytolysis of rapidly dividing cell populations. [3] In particular, FPV destroys intestinal crypt cells of the jejunum and ileum. [3]

The provided evidence does not specify other target cell types beyond mitotic cells and intestinal crypt epithelium, nor does it address clinical signs, diagnosis, treatment, or host range.

**Citation(s):** [1] The Merck Veterinary Manual, Generalized Conditions, pp. 796–797; [2] Saunders Comprehensive Veterinary Dictionary, p. 424; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Feline Panleukopenia, p. 508

**32. What are the hallmark features of FIP?**
_[Feline Infectious Peritonitis (FIP)]_

**Book answer:** Insidious onset, persistent fever that does not respond to treatment, pyogranulomatous tissue reaction, exudative effusions in body cavities and high mortality.

**AI answer:**

Summary — hallmark features of FIP

- Nature and outcome: FIP is a systemic, immune-mediated, viral disease with an insidious onset and high mortality. [1]

- Forms: Two classic forms occur—“wet” or effusive FIP with accumulation of exudative effusions in body cavities, and “dry” or non-effusive FIP that targets a variety of organs. [1][2]

- Key pathologic lesions: The characteristic lesion is granulomatous phlebitis with pyogranulomatous or granulomatous perivascular inflammation. [3][4] Pyogranulomatous tissue reaction and accumulation of exudative effusions in body cavities are hallmark pathologic findings. [1]

- Effusive (wet) hallmark: Wet FIP is characterized by development of a protein-rich effusion in the thoracic and/or abdominal body cavities. [2][3]

- Clinical presentation: Common early clinical signs include fever, lethargy, anorexia, and weight loss. [3] A persistent, fluctuating, antibiotic-unresponsive fever is a typical clinical feature. [1]

- Multisystemic involvement: FIP commonly involves the eyes (uveitis, chorioretinitis, keratic precipitates, and darkening or abnormal shape of the iris or pupil), the central nervous system (ataxia, nystagmus, seizures, tremors and other multifocal signs; hydrocephalus is suggestive), and the abdomen (effusion or focal intestinal pyogranulomas). [1][4][5][2][5][2][5]

- Diagnostic gold standard: Histology demonstrating localized perivascular mixed inflammation with macrophages, neutrophils, lymphocytes, plasma cells, and pyogranulomas is typically pathognomonic and is considered the gold standard for diagnosis. [4][5]

What is not covered by the provided evidence
- Specific antemortem diagnostic tests (beyond histology as the gold standard), treatment options or protocols, and detailed prognostic or epidemiologic information are not provided in the supplied claims.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Feline Infectious Peritonitis (FIP), p. 502; [2] Ettinger's Textbook of Veterinary Internal Medicine, 200. Coronavirus Infection, PDF pp. 3999–4000; [3] Ettinger's Textbook of Veterinary Internal Medicine, 200. Coronavirus Infection, PDF pp. 3998–3999; [4] The Merck Veterinary Manual, Generalized Conditions, p. 784; [5] The Merck Veterinary Manual, Generalized Conditions, pp. 783–784

**33. Which FeLV subgroup is most transmissible?**
_[Feline Leukemia Virus Infection (FeLV)]_

**Book answer:** FeLV-A. It is present in all isolates. The other subgroups are B, C and T.

**AI answer:**

FeLV‑A is the most transmissible subgroup. [1][2]  
FeLV‑A is present in all isolates. [1][2]

The provided evidence does not supply comparative transmissibility data for other FeLV subgroups, details on transmission mechanisms, or clinical outcomes.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Feline Leukemia Virus Infection (FeLV), p. 506; [2] The Merck Veterinary Manual, Generalized Conditions, pp. 791–792

**34. What is the dose of zidovudine for FIV and what must be monitored?**
_[Feline Immunodeficiency Virus Infection (FIV)]_

**Book answer:** 5-15 mg/kg PO q12h. It is most effective against acute infection, and bone marrow toxicity must be monitored.

**AI answer:**

Dose
- Adjunctive therapy: zidovudine 5–10 mg/kg q12h PO or SC. [1]
- Alternative range reported (Merck Veterinary Manual): 5–20 mg/kg PO or SC, bid–tid. [2]

Monitoring
- Perform a CBC weekly for the first month of treatment, then monthly if values are stable. [3][4]
- If hematocrit drops below 20% treatment should be discontinued; anemia usually resolves within a few days. [3][4]
- AZT treatment is not recommended for cats with myelosuppressive diseases. [4]

Notes
- The provided claims cover dosing ranges and hematologic monitoring only; they do not specify treatment duration or other adverse effects.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Zidovudine (AZT), pp. 3678–3680; [2] The Merck Veterinary Manual, Pharmacology, pp. 2746–2747; [3] Plumb's Veterinary Drug Handbook, Systemic Monographs › Zidovudine (AZT), pp. 3679–3681; [4] Ettinger's Textbook of Veterinary Internal Medicine, 198. Feline Immunodeficiency Virus Infection, PDF pp. 3953–3955

**35. What is the typical signalment of dogs with heartworm disease?**
_[Heartworm Disease—Dogs]_

**Book answer:** Medium to large breeds more than small dogs, outdoor more than indoor dogs, most aged 3-8 years, and males more often than females.

**AI answer:**

Typical signalment for heartworm disease

- Medium- to large-breed dogs > small dogs [1].  
- Outdoor dogs > indoor dogs [1].  
- Infestation can occur at any age; most affected dogs are 3–8 years old [1].  
- Males affected more often than females [1].  
- Dogs 5-7 YT old are at higher risk of having a heavy worm burden [2].  

Limitations of the evidence: these claims address breed size, sex, general age distribution and indoor/outdoor status only. They do not provide information on specific breeds, geographic distribution, clinical signs, diagnostic findings, prevention or treatment, or other signalment details.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Heartworm Disease—Dogs, p. 574; [2] The Merck Veterinary Manual, Circulatory System, p. 129

**36. What antibiotic is used to clear Leptospira from the kidneys?**
_[Leptospirosis]_

**Book answer:** Dihydrostreptomycin 10-15 mg/kg IM q12h for 2 weeks. Procaine penicillin G is used first until kidney function returns to normal.

**AI answer:**

Direct answer: Dihydrostreptomycin is used to eliminate Leptospira from kidney interstitial tissues: dihydrostreptomycin 10–15 mg/kg IM q12h for 2 weeks. [1]

If renal function is normal, try streptomycin. [1]

Doxycycline (5 mg/kg PO or IV q12h for 3 weeks) can be used alone to clear both leptospiremia and leptospiruria. [1][2]

What is not covered by the provided evidence: no other antibiotics, monitoring, safety considerations, or patient‑selection details are given beyond the statements above.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Leptospirosis, p. 799; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Leptospirosis, p. 799

**37. What are the antibiotic options for Lyme disease in dogs?**
_[Lyme Borreliosis]_

**Book answer:** Doxycycline 5-10 mg/kg PO q12h with food, amoxicillin 20 mg/kg PO q8-12h, or azithromycin 25 mg/kg PO q24h. Doxycycline is preferred if Anaplasma phagocytophilum co-infection is present.

**AI answer:**

Summary — antibiotic options for canine Lyme disease

Primary agents and group-level statements:
- Doxycycline is used to treat Lyme disease in dogs. [1][2][3][4]  
- Tetracycline (eg, doxycycline) and penicillin (eg, amoxicillin) groups are effective antibiotics for Lyme borreliosis. [3]  
- Amoxicillin is used to treat Lyme disease in dogs. [1][5]  
- Doxycycline is preferred when a co-infection with Anaplasma phagocytophilum occurs. [2]  
- Doxycycline is preferred over penicillins, because mixed infections with other tickborne pathogens are often found in animals with clinical signs. [3]  
- Minocycline is used to treat dogs with suspected Lyme arthritis. [4]  
- Azithromycin, penicillin G, ceftriaxone, cefotaxime, and chloramphenicol also have been used. [1]

Specific antibiotic options and dosages listed in Box 34-9:
- Doxycycline (Vibramycin) 10 mg/kg PO q24 hr for a minimum of 1 month. [5]  
- Amoxicillin 22 mg/kg PO q12 hr. [5]  
- Chloramphenicol (Chloromycetin) 50 mg/kg PO q8 hr. [5]  
- Azithromycin (Zithromax) 10 mg/kg PO q12 hr for 5 to 7 days. [5]  
- Ceftriaxone (Rocephin) 50 mg/kg IM or IV q12 hr. [5]

What the provided evidence does not cover
- Comparative efficacy between these agents, complete duration recommendations for agents other than doxycycline and azithromycin, and specific therapeutic decision-making by clinical scenario are not provided in the cited claims.

**Citation(s):** [1] Small Animal Surgery (Fossum), 34 Diseases of the Joints › Suggested reading, pp. 1233.e1–1234; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Lyme Borreliosis, p. 820; [3] The Merck Veterinary Manual, Generalized Conditions, pp. 660–661; [4] Ettinger's Textbook of Veterinary Internal Medicine, 187. Lyme Disease, PDF pp. 3694–3695; [5] Small Animal Surgery (Fossum), 34 Diseases of the Joints › References, p. 1234

**38. What is the treatment of choice for canine ehrlichiosis?**
_[Ehrlichiosis (Anaplasma)]_

**Book answer:** Doxycycline 5 mg/kg PO q12h for 4 weeks, given IV for 5 days if the dog is vomiting.

**AI answer:**

Doxycycline is the drug/treatment of choice for canine ehrlichiosis.[1][2][3][4][5]

The provided evidence does not specify dosing, duration of therapy, alternative treatments, supportive care, or monitoring recommendations.

**Citation(s):** [1] The Merck Veterinary Manual, Generalized Conditions, p. 805; [2] The Merck Veterinary Manual, Generalized Conditions, pp. 804–805; [3] Ettinger's Textbook of Veterinary Internal Medicine, 193. Ehrlichiosis, Anaplasmosis, Rocky Mountain Spotted Fever, and Neorickettsiosis, PDF pp. 3822–3823; [4] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 6 Viral, Rickettsial, and Protozoal Skin Diseases, pp. 151–152; [5] Small Animal Surgery (Fossum), 34 Diseases of the Joints › General Considerations and Clinically Relevant Pathophysiology, pp. 1233–1234

**39. What drug is FDA-approved for babesiosis and at what dose?**
_[Babesiosis]_

**Book answer:** Imidocarb dipropionate 6.6 mg/kg SC or IM every 1-2 weeks. It may clear B. canis but not B. gibsoni.

**AI answer:**

Imidocarb dipropionate is FDA‑approved for babesiosis; recommended dose 6.6 mg/kg SC or IM, repeated every 1–2 weeks. [1]

The provided evidence does not specify the target host species or Babesia species, total number of treatments required, overall duration of therapy beyond the 1–2 week dosing interval, efficacy outcomes, or adverse effects.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Babesiosis, pp. 164–165

**40. What is the fenbendazole regimen for giardiasis in dogs and cats?**
_[Giardiasis]_

**Book answer:** 50 mg/kg PO q24h for 3 days in dogs or 5 days in cats; a second course may be needed. It should be combined with environmental cleaning and bathing the patient.

**AI answer:**

Summary — fenbendazole regimens reported for giardiasis

Dogs
- Fenbendazole 50 mg/kg PO once daily for 3 consecutive days; if this does not clear the infection a longer course of therapy (5–7 days) is used. [1]
- CAPC lists fenbendazole 50 mg/kg PO once daily for 3–5 days when used as monotherapy for giardiasis. [2]
- When used in combination with metronidazole (25 mg/kg PO q12h), CAPC recommends fenbendazole 50 mg/kg PO once daily for 5 days. [2]
- Fenbendazole 50 mg/kg/day for 5–10 days has been reported to effectively remove Giardia cysts from dog feces. [3]
- Fenbendazole 50 mg/kg PO q24h for 3 days is also listed for canine giardiasis. [4]
- Antiparasitic regimen listings include fenbendazole 50 mg/kg PO q24h for ≥3 days for dogs. [5]

Cats
- Fenbendazole 50 mg/kg/day for 5 days may reduce clinical signs and cyst shedding in cats (fenbendazole is not approved in cats). [3]
- An alternate reported regimen for cats is fenbendazole 20 mg/kg PO for 5 days. [4]
- Antiparasitic regimen listings include fenbendazole 50 mg/kg PO q24h for ≥3 days for cats. [5]

Notes on the evidence
- There are multiple reported dosing options and durations for both species (see above); the evidence does not specify which regimen is preferred in which clinical situations.  
- The claims do not provide further information on safety, monitoring, product formulation, or formal approval status in species beyond the single statement that fenbendazole is not approved in cats. [3]

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Fenbendazole, pp. 1470–1471; [2] Ettinger's Textbook of Veterinary Internal Medicine, 196. Enteric Protozoan Diseases, PDF p. 3901; [3] The Merck Veterinary Manual, Circulatory System, p. 213; [4] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 131–132; [5] Ettinger's Textbook of Veterinary Internal Medicine, 142. Antiparasitic Drugs, PDF pp. 2807–2809

**41. What is the recommended treatment once rabies is diagnosed?**
_[Rabies]_

**Book answer:** There is no treatment. Once the diagnosis is certain, euthanasia is indicated, and suspected cases must be securely isolated.

**AI answer:**

Recommended treatment: There is no recognized treatment for rabies; once clinical signs are present, the disease is ultimately fatal with extremely rare exceptions. [1] No treatment is available; once the diagnosis is certain, euthanasia is indicated. [2]

What is not covered by the evidence: these claims do not address prevention, post‑exposure management, public‑health actions, or any supportive measures prior to diagnostic confirmation.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 202. Rabies, PDF pp. 4060–4062; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Rabies, pp. 1152–1153

**42. What is the initial antibiotic choice for uncomplicated canine infectious respiratory disease?**
_[Canine Infectious Respiratory Disease]_

**Book answer:** Amoxicillin/clavulanic acid 12.5-25 mg/kg PO q12h or doxycycline 5 mg/kg PO q12h.

**AI answer:**

Initial antibiotic options for uncomplicated canine infectious respiratory disease are amoxicillin/clavulanic acid 12.5–25 mg/kg PO q12h [1] or doxycycline 5 mg/kg PO q12h [1].

The provided evidence does not specify treatment duration, monitoring, contraindications, alternative agents, diagnostic criteria, or management of complicated disease.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Canine Infectious Respiratory Disease, pp. 212–213

**43. What signs characterize feline herpesvirus infection?**
_[Feline Herpesvirus Infection]_

**Book answer:** Sneezing, fever, rhinitis, conjunctivitis and ulcerative keratitis. Kittens are most susceptible, and brachycephalic breeds get more severe corneal disease and corneal sequestra.

**AI answer:**

Common clinical signs of feline herpesvirus (FHV‑1) infection

- Acute onset paroxysmal sneezing. [1]  
- Fever — may reach up to 106°F (41°C). [1]  
- Rhinitis with serous, mucopurulent, or purulent nasal discharge. [1]  
- Conjunctivitis with serous or purulent ocular discharge, conjunctival hyperemia, chemosis, and blepharospasm. [1][2]  
- Ocular discharge is often serous initially and progresses to mucoid by day 5–7 of infection. [2]  
- If conjunctival cytolysis is severe, discharge can become sanguineous. [2]  
- Corneal disease: FHV‑1 is a common cause of corneal ulceration; dendritic corneal ulceration is the only pathognomonic clinical sign. [2]  
- More severe ocular complications include ulcerative keratitis (including descemetocele) and panophthalmitis. [1]  
- Herpetic stromal keratitis may occur, characterized by corneal stromal fibrosis, edema, vascularization, and white blood cell infiltration. [3]  
- Symblepharon (adhesion of conjunctiva/third eyelid to conjunctival or corneal tissues) can follow recovery. [6]  
- In adults with recrudescent disease signs may be milder: conjunctivitis, epiphora, and mild sneezing. [2]  
- Feline rhinotracheitis can produce vesicles, blisters, and ulcerations of facial and nasal regions and may cause severe alopecic, erythematous, erosive facial dermatitis. [4][5]  
- Recurrent signs occur because FHV‑1 establishes lifelong latency in ganglia and may be reactivated by stress or corticosteroid administration. [1][6]  
- Anorexia may be seen secondary to high fever, general malaise, or inability to smell. [1]

Limitations of the provided evidence
- The supplied claims describe clinical signs and mechanisms of recurrence but do not address diagnostic testing, specific management or treatment options, prognosis, or detailed timelines beyond the noted progression of ocular discharge.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Feline Herpesvirus Infection, p. 495; [2] Ettinger's Textbook of Veterinary Internal Medicine, 205. Feline Upper Respiratory Infections, PDF pp. 4102–4104; [3] Slatter's Fundamentals of Veterinary Ophthalmology, 10 Diseases of the Cornea and Sclera › Canine Herpesvirus, pp. 244–245; [4] Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, 49 Viral Dermatoses › Causes – Cat, pp. 712–713; [5] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 6 Viral, Rickettsial, and Protozoal Skin Diseases, pp. 144–146; [6] Slatter's Fundamentals of Veterinary Ophthalmology, 7 Diseases of the Conjunctiva › Feline Viral Conjunctivitis, p. 167

**44. What clinical forms can feline calicivirus cause?**
_[Feline Calicivirus Infection]_

**Book answer:** Upper respiratory disease, oral ulceration, pneumonia, occasionally arthritis, or a highly fatal systemic hemorrhagic disease.

**AI answer:**

Short answer
Three clinical forms of feline calicivirus are described: acute FCV infection, chronic FCV infection, and virulent systemic feline calicivirus disease. [2]

Typical clinical presentations reported
- Upper respiratory disease with eye and nose involvement. [1]  
- Ulcerative disease primarily of the mouth (oral ulceration of the tongue, hard palate, lips, tip of nose, or around claws). [1][2]  
- Acute arthritis — a transient “limping syndrome” with alternating leg lameness and pain on palpation of affected joints. [1][3]  
- A systemic hemorrhagic disease (virulent systemic feline calicivirus disease) that can be highly fatal. [1][2]

Limitations of the provided evidence
- The supplied claims list the three named clinical forms and the possible presentations, but do not specify which presentations map consistently to acute versus chronic FCV, nor do they provide diagnostic, prognostic, or treatment details.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Feline Calicivirus Infection, p. 492; [2] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 6 Viral, Rickettsial, and Protozoal Skin Diseases, pp. 144–146; [3] The Merck Veterinary Manual, Respiratory System, pp. 1481–1482

**45. What is the clindamycin dose for toxoplasmosis?**
_[Toxoplasmosis]_

**Book answer:** 25-50 mg/kg PO or IM daily divided into two doses, continued for at least 2 weeks after clinical signs clear. Topical 1% prednisone drops q8h are used for uveitis.

**AI answer:**

Summary of reported clindamycin regimens for toxoplasmosis

Regimen specific to clinical presentation
- Clinical toxoplasmosis: clindamycin 10 mg/kg PO q12h. [1]
- Enteroepithelial toxoplasmosis: clindamycin 8–16 mg/kg PO or SC q8h for 14–28 days. [1]
- Systemic toxoplasmosis: clindamycin 12.5–25 mg/kg PO or SC q12h for 14–28 days. [1]

Other reported regimens
- Clindamycin 25–50 mg/kg PO or IM daily, divided into two doses, continued for at least 2 weeks after clinical signs clear. [2]
- Cat dosing line: clindamycin 12.5–25 mg/kg PO q12h. [3]
- Alternative: clindamycin 8–17 mg/kg PO tid, or 10–12.5 mg/kg PO bid for 3–4 weeks. [4]

Limitations of the evidence provided
- The 10 mg/kg PO q12h regimen for “clinical toxoplasmosis” is cited without an explicit treatment duration in the provided claim. [1]
- Species specificity is explicit only in the cat dosing line; other claims do not consistently state species. [3]

You (the clinician) should choose the regimen and duration appropriate for the patient; the statements above are the available, verified dosing options from the supplied sources.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Clindamycin, pp. 838–839; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Toxoplasmosis, pp. 1322–1323; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Appendices › Appendix IX, pp. 1462–1463; [4] The Merck Veterinary Manual, Pharmacology, pp. 2566–2567

**46. Which dog breeds are predisposed to pancreatitis?**
_[Pancreatitis—Dogs]_

**Book answer:** Miniature schnauzer, Yorkshire terrier and cocker spaniel. Acute pancreatitis is most common in middle-aged and older dogs, with a mean age of 6.5 years.

**AI answer:**

Reported breed predispositions for pancreatitis include:

- Yorkshire Terrier [1][2].  
- Cocker Spaniel [1][2].  
- Dachshund [1][3].  
- Poodles (including Miniature Poodles) [1][3].  
- Miniature Schnauzer / Schnauzers [2][3].  
- Cairn Terrier [3].  
- Beagle [3].  
- Sled dogs [1].  
- “Other breeds” are also mentioned but not specified [1].

What is not covered by the provided evidence: quantitative incidence or magnitude of risk, a comprehensive list of all predisposed breeds, or details on age, sex, or whether predisposition applies to acute versus chronic pancreatitis.

**Citation(s):** [1] The Merck Veterinary Manual, Circulatory System, p. 407; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Pancreatitis—Dogs, p. 1002; [3] The Merck Veterinary Manual, Endocrine System, p. 580

**47. What are the most common signs of pancreatitis in cats?**
_[Pancreatitis—Cats]_

**Book answer:** Vague, nonspecific signs, most often anorexia, lethargy and vomiting. Siamese cats are predisposed, and the mean age for acute pancreatitis is 7.3 years.

**AI answer:**

Concise summary
- The most common clinical signs in feline pancreatitis are lethargy (incidence 51–100%). [1][2]  
- Inappetence/anorexia is also very common (62–97%). [1][3]  
- Vomiting is frequent (35–52%). [1][3]  
- Weight loss is frequently reported (30–47%). [1]

Other common findings
- Dehydration (37–92%), hypothermia (39–68%) and fever (7–26%) are common physical/clinical findings. [1]

Less common signs
- Apparent abdominal pain is reported less commonly (≈10–30%). [1]  
- Other less-frequent signs include diarrhea (11–38%), dyspnea (6–20%), and polydipsia/polyuria (PU/PD; 20%). [1]

Limitations
- These claims describe clinical signs and frequencies only; the provided evidence does not address diagnostics, laboratory/imaging findings, treatment or prognosis.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 278. Pancreatitis in Cats, PDF pp. 6855–6856; [2] Ettinger's Textbook of Veterinary Internal Medicine, 278. Pancreatitis in Cats, PDF pp. 6853–6855; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Pancreatitis—Cats, p. 1000

**48. Which breeds are predisposed to exocrine pancreatic insufficiency?**
_[Exocrine Pancreatic Insufficiency]_

**Book answer:** German shepherd dogs, rough-coated collies and Eurasians. In young adult dogs it is usually caused by pancreatic acinar atrophy.

**AI answer:**

Breeds reported as predisposed:
- German Shepherd Dogs, rough-coated Collies, and Eurasians. [1]

Additional breed-related findings:
- Pancreatic acinar atrophy (PAA) is very commonly seen in the German Shepherd Dog and less commonly seen in rough-coated Collies and Eurasians. [1]
- An association of DLA‑DQB1 alleles with exocrine pancreatic insufficiency has been reported in Pembroke Welsh Corgis. [2]

Scope limits of the provided evidence:
- The supplied claims do not list other predisposed breeds or give broader prevalence, risk estimates, or clinical management information.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Exocrine Pancreatic Insufficiency, p. 474; [2] Ettinger's Textbook of Veterinary Internal Medicine, 279. Exocrine Pancreatic Insufficiency and Rare Conditions of the Exocrine Pancreas, PDF pp. 6893–6894

**49. How are pancreatic enzymes dosed for EPI?**
_[Exocrine Pancreatic Insufficiency]_

**Book answer:** Powdered enzymes mixed into food at 1 teaspoon per 10 kg body weight with each meal, with at least two meals a day. Pre-incubating the enzymes with food does not improve their effect.

**AI answer:**

Summary — practical dosing and administration points supported by the evidence:

Dogs
- Initial dosing options reported: 1–1.5 teaspoonsful with each meal, mixed with food; mix thoroughly and allow to stand 15–20 minutes before feeding. [1]  
- Alternative initial regimens reported: two teaspoons per 20 kg body weight per meal. [1]  
- Other sources state therapy is started with 1 teaspoon (5 mL) of dried extract per 10 kg body weight per meal. [2]  
- Another recommendation: mix enzyme powder in food at a dosage of 1 teaspoon/10 kg body weight with each meal; feed at least two meals daily to promote weight gain. [3]

Cats
- Dose options reported: 0.5–0.75 teaspoonsful with each meal, mixed with food; mix thoroughly and allow to stand 15–20 minutes before feeding. [4]  
- An alternative initial recommendation is one teaspoon per cat per meal. [4]

Administration and preparation
- Pancreatic enzymes must be added to every meal. [2]  
- Some sources recommend mixing enzymes with the food and allowing the mixture to stand 15–20 minutes before feeding. [1][4]  
- However, preincubation of the food with the pancreatic extract does not appear to be necessary to achieve a therapeutic response. [4][5][6]

Formulation considerations
- Powder formulations are more effective than tablets, capsules, and especially enteric‑coated products. [2][5]  
- Micropelleted forms (capsules) protect pancreatic lipase from low pH in the stomach, allowing a much lower dose per meal. [2][6]

Alternatives
- As an alternative, 1–3 ounces (≈30–90 g) of raw pancreas is reported to replace 1 teaspoon of dried pancreatic extract. [3][5][6]

Adverse effects and dose adjustment
- Oral bleeding has been reported in 3 of 25 dogs treated with pancreatic enzyme supplements; the bleeding stopped in all 3 dogs after the dose of pancreatic enzymes was decreased, and moistening the food/powder mix may decrease this side effect. [1][4][5][6]  
- When clinical signs have resolved, the amount of pancreatic enzymes given can be gradually decreased to the lowest/minimally effective dose; this may vary between patients and between batches of supplement. [1][2][5]

Feeding frequency
- Best results are usually obtained by feeding small meals frequently (at least three times per day). [1][4]  
- A separate recommendation advises feeding at least two meals daily to promote weight gain. [3]

Limitations / what is not covered by the evidence provided
- Exact quantitative dosing for micropelleted products beyond “much lower dose per meal” is not provided. [2][6]  
- There are no product‑specific mg/IU conversions, detailed taper schedules, monitoring parameters, or duration of therapy specified in these claims.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Pancrelipase, pp. 2723–2725; [2] Ettinger's Textbook of Veterinary Internal Medicine, 279. Exocrine Pancreatic Insufficiency and Rare Conditions of the Exocrine Pancreas, PDF pp. 6884–6885; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Exocrine Pancreatic Insufficiency, p. 475; [4] Plumb's Veterinary Drug Handbook, Systemic Monographs › Pancrelipase, pp. 2725–2726; [5] The Merck Veterinary Manual, Circulatory System, p. 410; [6] Ettinger's Textbook of Veterinary Internal Medicine, 279. Exocrine Pancreatic Insufficiency and Rare Conditions of the Exocrine Pancreas, PDF pp. 6885–6886

**50. What is GDV and which dogs are at risk?**
_[Gastric Dilation and Volvulus Syndrome]_

**Book answer:** A condition where the stomach dilates and then rotates around its short axis. Large, deep-chested breeds such as Great Danes and German shepherds are at risk, and risk increases with age.

**AI answer:**

Definition and pathophysiology
- Gastric dilatation–volvulus (GDV) is enlargement of the stomach associated with rotation on its mesenteric axis. [1]
- It is characterized by distension of the stomach with gas and rotation of the stomach typically clockwise along the mesenteroaxial axis. [2]

Dogs and breeds at increased risk
- GDV primarily affects large- and deep, narrow-chested dogs (large- and giant-breed dogs / large, deep-chested breeds). [2][3][4]
- Breeds reported at risk include Great Dane, Standard Poodle, Irish Setter, Weimaraner, Rottweiler, German Shepherd Dog, and Retrievers. [2]
- Additional breeds listed as at risk include Gordon Setter, Saint Bernard, Bassett Hound, and Doberman Pinscher. [4][5]

Recognized risk factors
- Risk factors include rapid eating, dry food, elevated feeding position, larger food volume per meal, thin/lean body condition, older age, nervous/fearful temperament, and a family history of GDV. [2][4][5]
- One study found dogs fed a larger volume of food per meal were at significantly increased risk of GDV, with the highest risk for dogs fed a larger volume once daily. [1]
- Feeding dry dog foods in which one of the first four ingredients is an oil or a fat may increase the risk of GDV. [1]
- Having a first‑degree relative with a history of GDV is significantly associated with increased risk; dogs with a first‑degree relative that has had GDV are recommended not to be used for breeding. [3][5]

Limitations of the provided evidence
- The supplied evidence does not cover clinical signs, diagnostics, acute management or surgical treatment, prognosis, or absolute incidence rates.

**Citation(s):** [1] Small Animal Surgery (Fossum), 20 Surgery of the Digestive System › General Considerations and Clinically Relevant Pathophysiology, p. 482; [2] Ettinger's Textbook of Veterinary Internal Medicine, 261. Gastric Diseases, PDF pp. 6164–6166; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Gastric Dilation and Volvulus Syndrome, p. 531; [4] The Merck Veterinary Manual, Circulatory System, p. 384; [5] Small Animal Surgery (Fossum), 20 Surgery of the Digestive System › General Considerations and Clinically Relevant Pathophysiology, pp. 482–483

**51. What is megaesophagus and which cats are predisposed?**
_[Megaesophagus]_

**Book answer:** A focal or generalized dilation of the esophagus with reduced or absent peristalsis. Siamese and Siamese-related cats are predisposed.

**AI answer:**

Definition
- Megaesophagus is a focal or generalized, diffuse dilation of the esophagus with decreased to absent peristalsis. [1]

Predisposed cats
- Siamese and Siamese-related cats. [1]

Limitations of the evidence
- The provided evidence does not address causes, clinical signs, diagnostic methods, treatment options, prognosis, or overall prevalence beyond the breed predisposition stated above.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Megaesophagus, p. 859

**52. Which dogs are most commonly affected by hemorrhagic gastroenteritis?**
_[Gastroenteritis, Hemorrhagic]_

**Book answer:** Small and toy breeds, especially miniature schnauzer, dachshund, Yorkshire terrier and miniature poodle. It usually affects adults with a mean age of 5 years.

**AI answer:**

All breeds can be affected, but the incidence is greater in small‑breed and toy‑breed dogs. [1][2]

Breeds most commonly represented include miniature schnauzer, dachshund, Yorkshire terrier, and miniature poodle. [1]

Affected dogs are usually adults, with a mean age of about 5 years. [1]

The provided evidence does not address sex predisposition, specific risk factors, geographic variation, clinical signs, diagnosis, treatment, or prognosis.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Gastroenteritis, Hemorrhagic, p. 542; [2] Small Animal Medical Differential Diagnosis: A Book of Lists, SECTION IV Gastroenterologic Disorders, pp. 143–145

**53. How is IBD categorized?**
_[Inflammatory Bowel Disease]_

**Book answer:** By the predominant mucosal cellular infiltrate, for example lymphocytic-plasmacytic. It is a group of chronic enteropathies with persistent or intermittent GI signs and histologic intestinal inflammation.

**AI answer:**

The form of IBD is generally categorized by the predominant mucosal cellular infiltrate. [1]

Forms include lymphocyticplasmacytic enteritis, eosinophilic enteritis, or granulomatous enteritis. [1]

The provided evidence does not address diagnostic criteria, staging/grading, etiology, clinical management, or prognosis.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Inflammatory Bowel Disease, p. 753

**54. What cytology finding supports hepatic lipidosis in cats?**
_[Hepatic Lipidosis]_

**Book answer:** On fine-needle liver aspiration, more than 80% of hepatocytes show severe cytosolic vacuolation. Vitamin K1 is recommended for all cats with suspected lipidosis.

**AI answer:**

Cytologic evidence supporting hepatic lipidosis in cats is the presence of numerous small, discrete vacuoles or a single large vacuole in the hepatocyte cytoplasm, which indicates accumulation of fat and is prominent in feline hepatic lipidosis syndrome. [1][2]

The provided evidence addresses only this cytologic finding and does not cover other diagnostic features or differential diagnoses.

**Citation(s):** [1] The Merck Veterinary Manual, Clinical Pathology and Procedures, pp. 1608–1609; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hepatic Lipidosis, p. 603

**55. Where are congenital portosystemic shunts usually located in small dogs and cats?**
_[Portosystemic Vascular Anomaly, Congenital]_

**Book answer:** Extrahepatic shunts are more common in small-breed dogs and cats. Small purebred and mixed 'terrier' dogs are at higher risk.

**AI answer:**

In small-breed dogs and in cats, congenital portosystemic shunts are most commonly extrahepatic. [1][2]

These extrahepatic shunts most commonly connect the portal vein or its branches to the caudal vena cava or to the azygous vein. [2]

The provided evidence does not give breed-specific frequencies, numerical incidence, other anatomic variants beyond those vessels, or any clinical, diagnostic or therapeutic details.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Portosystemic Vascular Anomaly, Congenital, p. 1099; [2] The Merck Veterinary Manual, Circulatory System, pp. 169–170

**56. How long must kidney disease be present to be called chronic?**
_[Renal Failure, Chronic]_

**Book answer:** More than 3 months. Mean age at diagnosis is about 7 years in dogs and 9 years in cats.

**AI answer:**

Chronic kidney disease is defined as structural and/or functional abnormalities of one or both kidneys that have been continuously present for ≥3 months. [1][2][3]

The provided evidence does not address how to document or demonstrate that the abnormalities have been continuously present, nor does it provide diagnostic criteria, staging, or management guidance.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 301. Chronic Kidney Disease, PDF pp. 7560–7562; [2] Small Animal Surgery (Fossum), 25 Surgery of the Kidney and Ureter › Preoperative Management, p. 705; [3] Ettinger's Textbook of Veterinary Internal Medicine, 299. Clinical Approach and Laboratory Evaluation of Renal Disease, PDF pp. 7463–7464

**57. How is prerenal azotemia distinguished from acute kidney injury?**
_[Renal Failure, Acute]_

**Book answer:** Prerenal azotemia has concentrated urine (USG at least 1.030 in dogs and 1.035 in cats) and is correctable with fluid repletion.

**AI answer:**

Short answer
- Use urine concentrating ability, response to restored perfusion, and urinalysis/biochemistry patterns to distinguish prerenal azotemia from acute kidney injury (AKI).  

Key discriminators

- Urine concentrating ability: a urine specific gravity (USG) ≥1.030 in dogs and ≥1.035 in cats supports prerenal azotemia. [2] Isosthenuria (USG 1.008–1.012) or inappropriate concentrating ability (USG <1.030 in the dog or <1.035 in the cat) indicates renal azotemia. [1]  
- Caveats to USG interpretation: azotemic patients that have not been treated with fluids and have USG below those thresholds typically have primary renal azotemia; an important exception is glomerular disease, which may preserve concentrating ability and is recognized by moderate to marked proteinuria without hematuria and pyuria. [2] Administration of fluid therapy before urine collection may interfere with interpretation of low specific gravity values. [2]  
- Response to restoration of renal perfusion: in prerenal azotemia appropriate therapy to restore renal perfusion typically produces a dramatic reduction in serum urea nitrogen and creatinine within 24–48 hours. [3] Prerenal azotemia generally resolves with appropriate treatment because kidney structure has not been altered. [4] Prolonged reduction in renal blood flow, however, can cause renal hypoxic damage and lead to AKI, thereby adding a renal cause to the azotemia. [1][5]  
- Urinalysis and other laboratory features of AKI: animals with AKI usually have a compatible history and urinalysis abnormalities; marked cylindruria is a frequent and definitive finding and other UA findings may include large numbers of renal epithelial cells and leukocytes, glucosuria, crystalluria, enzymuria, and/or myoglobinuria/hemoglobinuria. [6] Animals with AKI generally have increased serum urea nitrogen, creatinine, and inorganic phosphorus concentrations and metabolic acidosis; oliguria or anuria after rehydration, often associated with hyperkalemia, is a poor prognostic sign. [6] Renal (intrarenal) azotemia is defined by a reduction in glomerular filtration rate of about 75% in acute or chronic primary renal diseases. [4]

Practical diagnostic approach (from the evidence)
- Obtain USG before giving fluids when possible, and interpret against the ≥1.030 (dog) / ≥1.035 (cat) thresholds. [2]  
- If USG is low/inappropriate and the patient was not recently fluid-resuscitated, suspect primary renal azotemia (except consider glomerulopathy if there is marked proteinuria without hematuria/pyuria). [2]  
- Rehydrate/restore perfusion and repeat serum urea nitrogen and creatinine: a dramatic fall within 24–48 hours supports prerenal azotemia. [3][4]  
- Perform urinalysis: the presence of marked cylindruria, many renal epithelial cells, leukocytes, glucosuria, etc., supports AKI. [6]  
- Monitor urine output after rehydration—oliguria or anuria, especially with hyperkalemia, indicates poor prognosis and is typical of severe AKI. [6]

Limitations of the provided evidence
- The supplied claims do not provide imaging, biopsy, staging criteria for AKI, specific numeric cutoffs for oliguria/anuria or hyperkalemia, detailed sensitivity/specificity of tests, or management/treatment protocols.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 62. Blood Urea Nitrogen, Creatinine, and SDMA, PDF pp. 1319–1320; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Azotemia and Uremia, p. 162; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Azotemia and Uremia, pp. 161–162; [4] The Merck Veterinary Manual, Urinary System, p. 1512; [5] Ettinger's Textbook of Veterinary Internal Medicine, 62. Blood Urea Nitrogen, Creatinine, and SDMA, PDF pp. 1320–1321; [6] The Merck Veterinary Manual, Urinary System, pp. 1516–1517

**58. Can calcium oxalate uroliths be dissolved medically?**
_[Urolithiasis, Calcium Oxalate]_

**Book answer:** No. No available drugs effectively dissolve them, so they are removed. Steroids and furosemide should be used with care because they promote calciuria.

**AI answer:**

No — calcium oxalate (CaOx) uroliths cannot be medically dissolved. [1][2][3][4]

The provided evidence does not address alternative management options (e.g. removal techniques), prevention strategies, recurrence risk, or prognosis.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 308. Lower Urinary Tract Urolithiasis in Dogs, PDF pp. 7818–7821; [2] Ettinger's Textbook of Veterinary Internal Medicine, 159. Nutritional Management of Lower Urinary Tract Disease, PDF pp. 3079–3081; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Urolithiasis, Calcium Oxalate, p. 1350; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Urolithiasis, Calcium Oxalate, p. 1350

**59. Which six dog breeds make up 60% of calcium oxalate urolith cases?**
_[Urolithiasis, Calcium Oxalate]_

**Book answer:** Miniature schnauzer, Lhasa apso, Yorkshire terrier, bichon frise, shih tzu and miniature poodle.

**AI answer:**

The six breeds are miniature schnauzer, Lhasa apso, Yorkshire terrier, bichon frise, shih tzu, and miniature poodle. [1]

These six breeds together account for 60% of cases, and the verified claim does not provide a breakdown by individual breed or ranking. [1]

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Urolithiasis, Calcium Oxalate, p. 1349

**60. What are most uroliths in dogs under 12 months old?**
_[Urolithiasis, Struvite—Dogs]_

**Book answer:** Infection-induced struvite (magnesium ammonium phosphate) uroliths.

**AI answer:**

In dogs under 12 months of age, calculi are often struvite and are usually secondary to urinary tract infection [1]. 

The provided evidence does not give prevalence percentages, nor does it describe other urolith types, risk factors beyond infection, or management.

**Citation(s):** [1] Small Animal Surgery (Fossum), 26 Surgery of the Bladder and Urethra › Diagnostic Imaging, pp. 761–762

**61. Which breeds are predisposed to urate uroliths?**
_[Urolithiasis, Urate]_

**Book answer:** Dalmatians, English bulldogs, and breeds at risk of portosystemic shunts such as Yorkshire terriers.

**AI answer:**

Short answer — breeds and groups identified as predisposed to urate uroliths in the provided evidence:

- Dalmatians — highest mutation prevalence for hereditary hyperuricosuria; >90% of uroliths submitted from this breed are composed of urate.[1][2]  
- English Bulldogs — listed as predisposed to urate urolithiasis.[2][3]  
- Black Russian Terriers — listed among breeds with the SLC2A9 mutation causing hereditary hyperuricosuria and urate urolith risk.[1][2]  
- Dogs with congenital portosystemic shunts are predisposed to urate uroliths; examples given are Yorkshire Terriers, Miniature Schnauzers, and Pekingese.[2][3]  
- Blackwell lists English Bulldog, Dalmatian, Yorkshire terrier, and Shih Tzu as breeds for purine nephroliths; Saunders states purine uroliths include ammonium acid urate and sodium acid urate.[4][5]  
- The SLC2A9 mutation causing hereditary hyperuricosuria exists in >30 dog breeds.[2]

What is not covered by the evidence provided:
- A complete, enumerated list of all breeds at increased urate-urolith risk beyond the specific examples above (the mutation is present in >30 breeds, but those breeds are not all named).[2]  
- Comparative quantitative risk (relative risk or prevalence) for breeds other than the Dalmatian statement above.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 308. Lower Urinary Tract Urolithiasis in Dogs, PDF pp. 7804–7807; [2] Ettinger's Textbook of Veterinary Internal Medicine, 308. Lower Urinary Tract Urolithiasis in Dogs, PDF pp. 7806–7808; [3] Small Animal Surgery (Fossum), 26 Surgery of the Bladder and Urethra › General Considerations and Clinically Relevant Pathophysiology, pp. 760–761; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Nephrolithiasis, p. 942; [5] Saunders Comprehensive Veterinary Dictionary, p. 1155

**62. When after estrus do dogs and cats with pyometra usually present?**
_[Pyometra]_

**Book answer:** Dogs within 12 weeks after their last estrus, and cats within 4 weeks of their last estrus. It is life-threatening when the cervix is closed and the bitch is systemically ill.

**AI answer:**

Summary

- Dogs: Pyometra usually presents 4–8 weeks after estrus (mean 5.7 weeks). [1][2] They may present as late as within 12 weeks after their last estrus. [3]

- Cats: Pyometra usually presents 1–4 weeks after estrus (within 4 weeks of the last call). [1][3]

Limitations of the evidence

- These claims address timing only. The provided evidence does not cover clinical signs, diagnostic workup, treatment, prognosis, or presentations outside the stated intervals beyond the dog-specific 12-week note.

**Citation(s):** [1] Small Animal Surgery (Fossum), 27 Surgery of the Reproductive and Genital Systems › Laboratory Findings, p. 820; [2] The Merck Veterinary Manual, Reproductive System, pp. 1397–1398; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Pyometra, p. 1139

**63. When does eclampsia usually occur and which breeds are at risk?**
_[Eclampsia]_

**Book answer:** Usually 1-4 weeks postpartum, most often before day 40. It is most common in toy breeds such as Chihuahua, miniature pinscher, Shih Tzu, miniature poodle and Pomeranian, and in first litters.

**AI answer:**

Timing
- Eclampsia usually develops 1–4 weeks postpartum; it may occur at term, prepartum, or during late lactation.[1]
- It is most common prior to day 40 postpartum.[1]  
- Puerperal hypocalcemia is usually seen at peak lactation, 2–3 wk after whelping.[2]

Breeds and risk factors
- Most common in toy breeds; breeds reported at increased risk include Chihuahua, miniature pinscher, Shih Tzu, miniature poodle, Mexican hairless, and Pomeranian.[1]
- The incidence is increased in small breeds, and small-breed bitches with large litters are most often affected.[2]
- In cats, eclampsia is rare.[1]

What is not covered by these claims
- The provided evidence does not include details on incidence rates, clinical signs, diagnosis, treatment, prevention, or prognosis.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Eclampsia, p. 430; [2] The Merck Veterinary Manual, Metabolic Disorders, p. 992

**64. How is eclampsia treated in the bitch?**
_[Eclampsia]_

**Book answer:** 10% calcium gluconate 0.22-0.44 mL/kg IV slowly over 5 minutes to effect, monitoring heart rate or ECG. Hyperthermia and hypoglycemia are corrected, and she is sent home on oral calcium 10-30 mg/kg PO q8h.

**AI answer:**

Immediate goals — emergency stabilization and inpatient care: manage as an emergency inpatient. [1]

Acute treatments
- Administer IV calcium gluconate 10% at 0.22–0.44 mL/kg given slowly to effect over ~5 minutes; monitor heart rate or ECG during administration. [1]
- Correct hypoglycemia. [1]
- If seizures are unresponsive, give diazepam 5 mg IV. [1]
- Treat cerebral edema if indicated. [1]
- Treat hyperthermia with cool water soak and fans; use caution with cool water enemas. [1]
- Consider magnesium supplementation in hypomagnesemic bitches. [1]

Neonatal and lactation management
- Remove puppies from the dam onto a foster dam or hand-raise; if that is not possible or is undesirable because pups need contact with the dam, remove pups from the dam for 24 hours or until serum calcium is stabilized, and provide calcium supplementation for the remainder of lactation; continue to monitor serum calcium. [1]
- Start puppies/kittens on solid food at 3–4 weeks of age. [1]
- For large litters, provide supplement feeding for puppies. [1]

Discharge and longer-term management
- Send home on calcium carbonate, or oral calcium gluconate 10–30 mg/kg PO q8h until lactation ends. [1] (Calcium carbonate [TUMS] 500 mg tablets supply 200 mg elemental calcium.) [1]
- Monitor serum calcium concentration until it is stabilized in the normal range. [1]
- Avoid corticosteroids (they decrease intestinal absorption and increase renal excretion of calcium). [1]
- Avoid calcium supplementation during gestation. [1]
- Ensure maternal diet has a calcium:phosphorus ratio of ~1:1–1.2:1 and avoid high‑phytate foods (e.g., soybeans). [1]
- Bitches with prior eclampsia will probably recur with subsequent litters; calcium supplementation can be started after parturition for bitches with a history of eclampsia. [1]

Prognosis
- Prognosis is good with immediate treatment and poor with delayed treatment. [1]

Limitations of the provided evidence
- The sources above do not provide specifics on IV fluid plans, exact methods/doses to correct hypoglycemia, target serum calcium concentrations, monitoring intervals, alternative anticonvulsants beyond diazepam, or detailed supportive-care protocols; clinical judgment is required for those aspects.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Eclampsia, p. 430

**65. Why are brachycephalic breeds prone to dystocia?**
_[Dystocia]_

**Book answer:** Because they combine a broad fetal head with a narrow maternal pelvis, as in the Bulldog, Boston terrier and pug.

**AI answer:**

Brachycephalic breeds are reported to have a higher incidence of dystocia. [1][2]

Their conformation—broad head and narrow pelvis—is described for brachycephalic dogs such as Bulldog, Boston terrier and pug. [1] Some brachycephalic breeds are also noted to have a congenitally small pelvis. [2]

The combination of broad-headed conformation and a relatively narrow or congenitally small maternal pelvis provides the anatomical basis cited for their predisposition to dystocia. [1][2]

Brachycephalic cat breeds (Persian, Himalayan) are likewise listed among cat breeds with increased incidence of dystocia. [2]

Evidence provided does not include detailed pathophysiology beyond these anatomical features, quantitative incidence rates, or guidance on management or outcomes.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Dystocia, p. 424; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Dystocia, p. 424

**66. Which breeds are at high risk of lymphoma?**
_[Lymphoma—Dogs]_

**Book answer:** Boxer, basset hound, golden retriever, Saint Bernard, Scottish terrier, Airedale terrier and bulldog. Dachshunds and Pomeranians are low-risk.

**AI answer:**

Breeds identified as being at high risk for lymphoma include Boxer, basset hound, golden retriever, Saint Bernard, Scottish terrier, Airedale terrier, and bulldog. [1][2]

Breeds with higher prevalences of B‑cell lymphoma include the Basset Hound, Cocker Spaniel, Border Collie, and Doberman Pinscher. [3][4]

Breeds with among the highest prevalences of T‑cell lymphoma include Boxer, Shih Tzu, Cavalier King Charles Spaniel, and Airedale. [3][4]

Breed influences immunophenotype: approximately 85% of boxer lymphomas are T‑cell in origin, while golden retrievers develop B‑ and T‑cell lymphoma in about a 50:50 ratio. [1][2]

What the provided evidence does not cover: overall incidence rates, age/sex or other risk factors, a complete list of all high‑risk breeds beyond those named, or management/prognostic implications.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Lymphoma—Dogs, p. 830; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Lymphoma—Dogs, p. 830; [3] Ettinger's Textbook of Veterinary Internal Medicine, 322. Hematopoietic Tumors, PDF pp. 8138–8141; [4] Ettinger's Textbook of Veterinary Internal Medicine, 322. Hematopoietic Tumors, PDF pp. 8140–8142

**67. What is the typical age of cats with lymphoma by FeLV status?**
_[Lymphoma—Cats]_

**Book answer:** About 3 years in FeLV-positive cats and 7 years in FeLV-negative cats. Lymphoma is also the most common spinal cord tumor in cats.

**AI answer:**

Typical age of cats with lymphoma by FeLV status:

- FeLV-positive cats: 3 years. [1]  
- FeLV-negative cats: 7 years. [1]

No additional age details (such as ranges or distributions) are provided in the available evidence.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Lymphoma—Cats, p. 828

**68. What is the standard chemotherapy after amputation for canine osteosarcoma?**
_[Osteosarcoma]_

**Book answer:** A platinum drug (cisplatin or carboplatin) or doxorubicin, with at least four doses recommended.

**AI answer:**

Adjunctive chemotherapy after amputation for canine osteosarcoma usually involves administration of carboplatin or doxorubicin shortly after amputation. [1]

Cisplatin is infrequently used because its adverse side effects (renal damage, nausea, vomiting, anorexia, and bone marrow suppression) are potentially life threatening and require careful monitoring during treatment. [1]

The provided evidence does not specify dosing, timing, number of cycles, comparative efficacy, or selection criteria for chemotherapy.

**Citation(s):** [1] Small Animal Surgery (Fossum), 36 Other Diseases of Bones and Joints › Bone Biopsy, p. 1399

**69. What proportion of canine splenic tumors are hemangiosarcomas, and which breeds are predisposed?**
_[Hemangiosarcoma, Spleen and Liver]_

**Book answer:** Up to 70%. German shepherds, Labrador retrievers and golden retrievers are predisposed.

**AI answer:**

Proportion
- Hemangiosarcoma (HSA) has been reported to account for up to 70% of all canine splenic tumors. [1]
- HSA represents 10–20% of all splenic samples submitted to veterinary pathology laboratories. [2]
- Canine splenic HSA accounts for approximately half of all splenic malignancies identified. [2]

Breeds reported as predisposed
- German shepherd, Labrador retriever, and golden retriever are reported as predisposed. [1]
- Typical hemangiosarcomas occur most commonly in German shepherds, Golden retrievers, Bernese Mountain dogs, and Boxers. [3]

What is not covered by the available claims
- The provided evidence gives multiple proportion estimates in different contexts (overall splenic tumors, pathology submissions, splenic malignancies) but does not reconcile these into a single overall prevalence or provide quantitative relative risks by breed beyond listing which breeds are predisposed.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Hemangiosarcoma, Spleen and Liver, p. 584; [2] Small Animal Surgery (Fossum), 24 Surgery of the Hemolymphatic System › General Considerations and Clinically Relevant Pathophysiology, p. 701; [3] Muller and Kirk's Small Animal Dermatology, Chapter 20 - Neoplastic and Non-Neoplastic Tumors, p. 1299

**70. What is the vinblastine and prednisone protocol for canine mast cell tumors?**
_[Mast Cell Tumors]_

**Book answer:** Vinblastine 2.0 mg/m2 IV every 7 days for 4 doses, then every 14 days for 4 doses, with prednisone 1 mg/kg PO q24h.

**AI answer:**

Standard vinblastine–prednisone protocol for canine mast cell tumors:
- Vinblastine 2.0 mg/m2 IV q7 days × 4, then q14 days × 4. [1]
- Prednisone 1 mg/kg PO q24h. [1]

Alternative vinblastine dosing:
- Vinblastine may be given in a range of 2.0–2.5 mg/m2 q7–14d (Dogs, Cats). [2]

What is not covered by the provided evidence:
- Dose modifications for toxicity, supportive care, antiemetics/premedications, monitoring parameters, indications/contraindications, expected response rates, and long‑term management are not addressed by these claims.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Mast Cell Tumors, p. 850; [2] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 344–346

**71. What proportion of feline mammary tumors are malignant?**
_[Mammary Gland Tumors—Cats]_

**Book answer:** 85-95%, mostly carcinomas. Siamese cats have twice the risk of other breeds.

**AI answer:**

Short answer: the large majority of feline mammary tumors are malignant. Reported proportions are 85–95% [2], and another source reports 90% [1].

Limitation: these claims only give the proportion malignant; they do not provide additional context such as study methods, populations studied, diagnostic criteria, tumor subtypes, or outcome.

**Citation(s):** [1] Small Animal Surgery (Fossum), 27 Surgery of the Reproductive and Genital Systems › Signalment., pp. 810–811; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Mammary Gland Tumors—Cats, p. 840

**72. What is the mean age of dogs with malignant versus benign mammary tumors?**
_[Mammary Gland Tumors—Dogs]_

**Book answer:** 9-11 years for malignant and 7-9 years for benign tumors. They are uncommon in dogs under 5 years.

**AI answer:**

Mean age for dogs with malignant mammary tumors: 9–11 years. [1]

Mean age for dogs with benign mammary tumors: 7–9 years. [1]

The provided evidence does not give further details such as age distribution (SD or range beyond the stated means), sample sizes, breed or parity effects, or other demographic or clinical factors.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Mammary Gland Tumors—Dogs, p. 842

**73. What is the vincristine protocol for transmissible venereal tumor?**
_[Transmissible Venereal Tumor]_

**Book answer:** 0.5-0.7 mg/m2 IV once weekly, continued for 2 weeks beyond complete resolution of visible disease. Doxorubicin can be tried if remission is partial.

**AI answer:**

Summary: Vincristine can be used alone for therapy of canine transmissible venereal tumor. [3]

Protocol options
- Vincristine 0.025 mg/kg IV, once weekly for an average of 4–6 weeks; more than 90% of dogs treated with this protocol were cured, including dogs with metastases. [1]
- Vincristine sulfate (O.fHl. 7 mg/m2, IV) once weekly for 3–6 weeks has also been reported to be effective. [2]

Expected response
- Total remission is usually expected by the sixth treatment. [2]

Monitoring and safety
- Perform a CBC and platelet count before each chemotherapy treatment. [4]
- Because vincristine may be a skin irritant, wear gloves and protective clothing when preparing or administering the drug. [3]

Limits of the evidence
- The provided claims do not include guidance on dose adjustments for toxicity, detailed adverse effects beyond skin irritation, contraindications, supportive care, or long‑term follow‑up after remission.

**Citation(s):** [1] Muller and Kirk's Small Animal Dermatology, Chapter 20 - Neoplastic and Non-Neoplastic Tumors, p. 1368; [2] The Merck Veterinary Manual, Reproductive System, p. 1408; [3] Plumb's Veterinary Drug Handbook, Systemic Monographs › Vincristine Sulfate, pp. 3622–3624; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Transmissible Venereal Tumor, p. 1329

**74. Which breeds are predisposed to dilated cardiomyopathy?**
_[Cardiomyopathy, Dilated—Dogs]_

**Book answer:** Doberman pinscher and boxer, giant breeds (Scottish deerhound, Irish wolfhound, Great Dane, Saint Bernard, Afghan hound, Newfoundland), cocker spaniel and Portuguese water dog.

**AI answer:**

Dog breeds reported as predisposed to dilated cardiomyopathy (DCM) include Doberman pinscher and boxer.[1][2][3]

Other large and giant breeds reported as predisposed include Scottish deerhound, Irish wolfhound, Great Dane, Saint Bernard, Afghan hound, and Newfoundland.[1][2]

Additional breeds cited as predisposed include Cocker spaniel (including American and English Cocker), Portuguese Water Dog, German Shepherd, and Labrador Retriever.[1][2][3]

In cats, idiopathic DCM is now uncommon; the Burmese cat may have an increased incidence.[4]

The provided evidence lists these breeds but does not provide an exhaustive breed list, comparative risk estimates, age/sex predilections, inheritance patterns, or clinical course.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Cardiomyopathy, Dilated—Dogs, p. 230; [2] The Merck Veterinary Manual, Circulatory System, pp. 115–116; [3] Saunders Comprehensive Veterinary Dictionary, p. 186; [4] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Cardiomyopathy, Dilated—Cats, p. 227

**75. Which cat breeds are predisposed to hypertrophic cardiomyopathy?**
_[Cardiomyopathy, Hypertrophic—Cats]_

**Book answer:** Maine coon, ragdoll, Sphynx, British and American shorthairs, and Persians. Typical age is 5-7 years.

**AI answer:**

Breeds reported as predisposed to hypertrophic cardiomyopathy (HCM):

- Maine Coon cats. [1][2][3]  
- Ragdolls. [1][2][4]  
- Sphynx. [1][4]  
- British Shorthair, American Shorthair, and Persian. [1]

Familial (inherited) forms of HCM have been reported or suggested in British Shorthairs, Sphynx, Norwegian Forest cats, Bengals, and non‑pedigree cats. [4]

What is not covered by the provided evidence: a comprehensive list of all predisposed breeds, prevalence or relative risk estimates, diagnostic criteria, genetic variants or testing details, and clinical management or outcomes.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Cardiomyopathy, Hypertrophic—Cats, p. 233; [2] The Merck Veterinary Manual, Circulatory System, pp. 117–118; [3] Ettinger's Textbook of Veterinary Internal Medicine, 234. Feline Myocardial Diseases, PDF pp. 5195–5196; [4] Ettinger's Textbook of Veterinary Internal Medicine, 234. Feline Myocardial Diseases, PDF pp. 5137–5139

**76. What furosemide dose is used for a critically dyspneic cat with HCM?**
_[Cardiomyopathy, Hypertrophic—Cats]_

**Book answer:** 4 mg/kg IV, which can be repeated in 1 hour if the cat is still severely dyspneic. The usual dose is 1-2 mg/kg q8-24h.

**AI answer:**

For a critically dyspneic cat with suspected cardiogenic pulmonary edema (life‑threatening emergency), the published parenteral furosemide dosing options are:

- Initial high emergency dose: 2–4 mg/kg IV or IM; this initial dose may be repeated within 1–2 hours. [1]  
- Typical parenteral regimen for life‑threatening cardiogenic pulmonary edema: 0.5–2 mg/kg every 1–8 hours IV, IM, or SC. [2]  
- Emergency therapy often uses high IV or IM doses (2–4 mg/kg), repeated at 60– to 120‑minute intervals until clinical signs are controlled. [3]  

Reduce the initial emergency dosage as soon as signs of congestive heart failure have improved, and re‑evaluate renal parameters and electrolytes within the first week. [4]

The provided evidence addresses emergency dosing for severe acute pulmonary edema/cardiogenic pulmonary edema in cats but does not offer additional HCM‑specific guidance beyond these furosemide dose ranges.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Furosemide, pp. 1613–1614; [2] The Merck Veterinary Manual, Pharmacology, p. 2528; [3] The Merck Veterinary Manual, Circulatory System, pp. 103–104; [4] Ettinger's Textbook of Veterinary Internal Medicine, 234. Feline Myocardial Diseases, PDF p. 5192

**77. Which dogs typically develop myxomatous mitral valve disease?**
_[Atrioventricular Valve (Myxomatous) Disease]_

**Book answer:** Small breeds under 20 kg, such as Cavalier King Charles spaniels, Chihuahuas, miniature schnauzers, Maltese, Pomeranians, cocker spaniels, Pekingese and poodles.

**AI answer:**

Summary answer
- Myxomatous mitral valve disease (MMVD) occurs mainly in dogs and is extremely rare in cats. [1]  
- It is the most common cardiac disease in dogs; its prevalence is strongly influenced by age. [1]

Which dogs typically develop MMVD
- Predominantly older dogs, with the disease uncommon in young individuals but common in old dogs; prevalence can exceed 90% in some affected breeds older than 10 years. [2]  
- Typically affects small breeds (< 20 kg), though it may be seen in larger dogs. [1]  
- Commonly affected breeds include Cavalier King Charles Spaniels, Chihuahuas, Miniature schnauzers, Maltese, Pomeranians, Cocker spaniels, Pekingese, Poodles, and others. [1]  
- In affected breeds such as Cavalier King Charles Spaniels, a murmur may be detected from 2 years of age, with a peak incidence at 6–8 years; congestive heart failure typically begins from 8–12 years. [2]  
- Males tend to develop the disease at a younger age than females, which produces a higher prevalence at a given age in males. [2]  
- The disease is age- and breed-related, with older, small-breed dogs demonstrating a much higher incidence. [3]  
- In Cavalier King Charles Spaniels and Dachshunds the trait is inherited. [3]

What the evidence provided does not cover
- Exact pathogenesis, full list of all predisposed breeds, detailed prevalence figures across all breeds and ages, diagnostic criteria, treatment options, and long‑term prognosis are not provided by the cited evidence.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Atrioventricular Valve (Myxomatous) Disease, p. 155; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Atrioventricular Valve (Myxomatous) Disease, p. 155; [3] The Merck Veterinary Manual, Circulatory System, p. 112

**78. What is a patent ductus arteriosus and when is it usually found?**
_[Patent Ductus Arteriosus]_

**Book answer:** Persistent patency of the fetal ductus connecting the descending aorta to the pulmonary artery. Most are found during the initial vaccination visits, and females are predisposed in many breeds.

**AI answer:**

A patent ductus arteriosus (PDA) is the persistence of an open ductus arteriosus beyond the early neonatal period. [1]

The ductus arteriosus is a normal in utero opening between the main pulmonary artery (MPA) and the aorta that allows blood to bypass the non-oxygenating fetal lungs. [2] Normally the ductus arteriosus closes within the first few days after birth and becomes the ligamentum arteriosus. [2][3]

The ductus may be probe-patent in puppies younger than 4 days of age but is usually closed securely by 7–10 days after birth; PDA denotes persistence beyond this early neonatal closure period. [1]

Patent ductus arteriosus is the most common cardiovascular shunt in dogs and cats. [2]

What is not covered by the provided evidence: clinical signs, diagnostic methods, treatment options, and prognosis.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 231. Congenital Heart Disease, PDF pp. 4933–4936; [2] Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, Chapter 3 Thorax › Cardiovascular shunts, p. 198; [3] The Merck Veterinary Manual, Circulatory System, pp. 79–80

**79. What is the main feature of boxer cardiomyopathy?**
_[Cardiomyopathy—Boxer (Arrhythmogenic Right Ventricular)]_

**Book answer:** Ventricular tachyarrhythmias, which may cause syncope or sudden death. Fewer than 5% of dogs develop congestive heart failure with systolic dysfunction.

**AI answer:**

The principal feature is ventricular tachyarrhythmias. [1][2][3][4] These arrhythmias can be accompanied by syncope or sudden death. [1][2][3][4]

The provided evidence does not address diagnostic methods, treatment, pathophysiology beyond being described as a myocardial disease, prognosis, or prevalence.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Cardiomyopathy—Boxer (Arrhythmogenic Right Ventricular), p. 226; [2] Saunders Comprehensive Veterinary Dictionary, p. 186; [3] The Merck Veterinary Manual, Circulatory System, p. 117; [4] Ettinger's Textbook of Veterinary Internal Medicine, 233. Myocardial Diseases of Dogs, PDF pp. 5096–5098

**80. When should antiepileptic treatment be started in a dog with genetic epilepsy?**
_[Epilepsy, Genetic (Idiopathic)—Dogs]_

**Book answer:** At the second generalized seizure if the dog is under 2 years old, and in other dogs when the interval between seizures is gradually getting shorter.

**AI answer:**

Short answer
- Start antiepileptic treatment at the second generalized seizure in dogs younger than 2 years of age; for older dogs, start when the interictal period is gradually shortening. [1]

When to consider maintenance AEDs
- Consider a maintenance antiepileptic drug if the animal has had more than one or two seizures within a 6‑month period. [2]
- Also consider a maintenance AED if the animal has had more than one seizure of unknown cause on any particular day. [2]

What the evidence does not cover
- The provided statements do not specify which AED to use, dosing, monitoring, specific management for single first seizures, or expected prognosis.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Epilepsy, Genetic (Idiopathic)—Dogs, pp. 450–451; [2] The Merck Veterinary Manual, Pharmacology, pp. 2595–2596

**81. Which breeds get Hansen type I disc disease?**
_[Intervertebral Disc Disease, Thoracolumbar]_

**Book answer:** Dachshund, shih tzu, Lhasa apso, Pekingese, cocker spaniel, Welsh corgi, and toy and miniature poodles. Type II disease affects mainly large breeds.

**AI answer:**

Hansen type I disc extrusions are reported most commonly in small, chondrodystrophic breeds, but certain larger non‑chondrodystrophic breeds can also be affected. [3][4]

Commonly reported small/chondrodystrophic breeds include Dachshund, Beagle, Shih Tzu, Lhasa Apso, Pekingese, Cocker Spaniel, Bassett Hound, and poodles (including toy and miniature poodles), and Welsh corgis. [1][2][3][5]

Large breeds reported with type I extrusions include mixed‑breed dogs, German Shepherds, Labrador Retrievers, Doberman Pinschers, and Rottweilers. [3][4]

The provided evidence lists breeds known to be affected but does not provide a comprehensive inventory of all susceptible breeds, nor does it give information on incidence, age predilection, clinical presentation, diagnostics, treatment, or prognosis.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Intervertebral Disc Disease, Cervical, p. 760; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Intervertebral Disc Disease, Thoracolumbar, p. 763; [3] Small Animal Surgery (Fossum), 40 Surgery of the Cervical Spine › Diagnostic Imaging, p. 1479; [4] Ettinger's Textbook of Veterinary Internal Medicine, 250. Spinal Cord Diseases: Congenital (Developmental), Inflammatory, and Degenerative Disorders, PDF pp. 5772–5775; [5] The Merck Veterinary Manual, Nervous System, pp. 1246–1247

**82. Which breed accounts for about half of wobbler syndrome cases?**
_[Cervical Spondylomyelopathy (Wobbler Syndrome)]_

**Book answer:** The Doberman pinscher. Great Dane, rottweiler, Weimaraner and Dalmatian also have a high incidence.

**AI answer:**

Doberman pinschers are the most commonly affected breed, accounting for approximately 50% of wobbler syndrome cases.[1]

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Cervical Spondylomyelopathy (Wobbler Syndrome), p. 248

**83. What gene mutation causes degenerative myelopathy, and is there an effective drug?**
_[Degenerative Myelopathy]_

**Book answer:** A mutation in the superoxide dismutase 1 gene (SOD1). No drug has been proven to slow or halt progression.

**AI answer:**

Degenerative myelopathy is caused by a mutation in the superoxide dismutase 1 (SOD1) gene. [1][2][3] Mutations in SOD1 are causative for degenerative myelopathy but are incompletely penetrant. [1][2]

There is no effective drug treatment for DM: there is no specific treatment and no evidence that glucocorticoids, other drugs, or supplements alter the course of the disease. [4] No proved effective therapies are available for DM; treatment is supportive care. [5] Intensive daily physiotherapy may improve survival time in dogs with DM. [5]

What the evidence does not cover: these sources do not identify any pharmacologic therapy proven effective, nor do they provide detailed protocols for supportive care beyond noting the potential benefit of intensive physiotherapy.

**Citation(s):** [1] The Merck Veterinary Manual, Nervous System, p. 1246; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Degenerative Myelopathy, p. 353; [3] Ettinger's Textbook of Veterinary Internal Medicine, 250. Spinal Cord Diseases: Congenital (Developmental), Inflammatory, and Degenerative Disorders, PDF pp. 5815–5816; [4] The Merck Veterinary Manual, Nervous System, pp. 1246–1247; [5] Small Animal Surgery (Fossum), 43 Nonsurgical Disorders of the Brain and Spine › General Considerations and Clinically Relevant Pathophysiology, pp. 1549–1550

**84. What is the pyridostigmine dose for myasthenia gravis?**
_[Myasthenia Gravis]_

**Book answer:** 1-3 mg/kg PO q8-12h, with the syrup diluted half and half in water.

**AI answer:**

Pyridostigmine dosing reported for myasthenia gravis:

Dogs
- 1–3 mg/kg PO q8–12h. [1]  
- 0.5–3 mg/kg PO q8–12 hours with food. [1]  
- 0.5–3 mg/kg PO two to three times a day. [2]  
- 0.5–1 mg/kg PO two to three times a day. [2]  
- For acquired MG, after oral regurgitation is abolished with parenteral therapy: 7.5–30 mg PO two times a day. [1][2]

Cats
- 0.5–3 mg/kg daily PO in divided doses. [2]  
- 1–3 mg/kg PO q8–12h. [2]  
- 0.5–3 mg/kg PO per day when given with corticosteroids. [2]

Limitations of the available evidence
- The provided claims give dose ranges and some context (food, concurrent corticosteroids, post-parenteral transition) but do not specify how to choose a starting dose within these ranges, tapering or adjustment strategies, monitoring parameters, maximum single doses, or safety/contraindication details.

**Citation(s):** [1] Plumb's Veterinary Drug Handbook, Systemic Monographs › Pyridostigmine Bromide, pp. 3087–3088; [2] Plumb's Veterinary Drug Handbook, Systemic Monographs › Pyridostigmine Bromide, pp. 3088–3089

**85. What is geriatric vestibular disease in dogs?**
_[Vestibular Disease, Geriatric—Dogs]_

**Book answer:** An acute, non-progressive disturbance of the peripheral vestibular system in older dogs, usually over 8 years old. The cause is unknown.

**AI answer:**

Definition and epidemiology
- Geriatric vestibular disease is an acute onset, non‑progressive disturbance of the peripheral vestibular system in older dogs. [1]
- It is a common, sporadic, acquired disease of older dogs. [1]
- Patients usually are geriatric (usually > 8 years old), with a mean age suggested at 12.5 years. [1][2]

Typical presentation and examination
- Clinical signs are sudden onset of imbalance, disorientation, reluctance to stand, and usually head tilt and irregular eye movements; signs may be preceded or accompanied by nausea and vomiting. [1]
- Physical examination commonly shows a head tilt directed toward the side of the lesion, abnormal resting nystagmus (horizontal or rotatory) with the fast phase opposite the head tilt, and mild to marked disorientation and vestibular ataxia with a tendency to lean or fall in the direction of the head tilt; strength and proprioception are normal. [1]
- Signs most often reflect unilateral peripheral vestibular dysfunction, although bilateral disease is occasionally seen. [3]

Etiology, course, and diagnosis
- The etiology is unknown; a suspected abnormal flow of endolymphatic fluid in the semicircular canals secondary to disturbance in production, circulation, or absorption of the fluid is assumed. [1][3]
- Onset is usually peracute and clinical signs typically improve over 24 to 48 hours and resolve in 1 to 3 weeks, although the head tilt may persist; recurrence after several weeks to months is possible. [4]
- Diagnosis is based on history, examination findings, and exclusion of other causes of peripheral disease. [3]

Limitations of the provided evidence
- The supplied evidence does not cover specific diagnostic tests or imaging protocols, treatment or management recommendations, or definitive mechanistic proof beyond the suspected endolymph disturbance.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Vestibular Disease, Geriatric—Dogs, p. 1393; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Vestibular Disease, Geriatric—Dogs, p. 1394; [3] Ettinger's Textbook of Veterinary Internal Medicine, 248. Vestibular Disease, PDF pp. 5720–5721; [4] Slatter's Fundamentals of Veterinary Ophthalmology, 16 Neuroophthalmic Diseases › Otitis Media and Otitis Interna, pp. 419–420

**86. Which breeds have an increased incidence of cranial cruciate ligament disease at a young age?**
_[Cruciate Ligament Disease, Cranial]_

**Book answer:** Rottweilers and Labrador retrievers under 4 years old. The West Highland white terrier is the overrepresented small breed.

**AI answer:**

Breeds with increased incidence at a young age:
- Rottweiler and Labrador retriever — increased incidence when < 4 years of age [1].

The provided evidence only identifies these two breeds and the <4‑year age association; it does not provide information about other breeds or other age ranges.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Cruciate Ligament Disease, Cranial, p. 334

**87. Which dogs are most commonly affected by patellar luxation?**
_[Patellar Luxation]_

**Book answer:** Toy and miniature breeds, such as miniature and toy poodles, Yorkshire terriers, Pomeranians, Pekingese, Chihuahuas and Boston terriers.

**AI answer:**

Any dog can be affected by patellar luxation, regardless of gender, age or breed. [1]

Medial patellar luxation is the commoner form overall. [1][2] It is most often reported in small dogs, particularly toy and miniature breeds. [2] Femoropatellar instability leading to medial patellar luxation is a common inherited disease in small‑breed dogs. [3]

Lateral patellar luxation occurs less commonly overall but is seen more frequently in large breeds than in small and toy breeds. [1][2]

What is not covered by the evidence provided: exact prevalence rates, specific breed-by-breed risk comparisons beyond the small vs large distinction, and any effects of age or sex on risk.

**Citation(s):** [1] Small Animal Surgery (Fossum), 34 Diseases of the Joints › Preoperative Management, p. 1361; [2] Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, Chapter 5 Musculoskeleton › Tibial cartilage rest, p. 470; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Joint Luxations, p. 772

**88. What is panosteitis and at what age does it usually occur?**
_[Panosteitis]_

**Book answer:** A self-limiting, painful condition of the long bones of young medium to large-breed dogs, seen radiographically as increased marrow density. It usually occurs at 5-18 months of age, mostly in males.

**AI answer:**

Panosteitis is a disease of young dogs that causes lameness, bone pain, endosteal bone production, and occasionally subperiosteal bone production.[1] It produces acute, cyclical clinical signs and usually occurs in dogs 6–16 months of age.[2] It is most often reported in young, large and giant‑breed dogs.[3]

The provided evidence does not address causes, diagnostic criteria, specific treatment or prognosis, nor does it list implicated breeds beyond the general “large and giant” category.

**Citation(s):** [1] Small Animal Surgery (Fossum), 36 Other Diseases of Bones and Joints › Medical Treatment, p. 1392; [2] The Merck Veterinary Manual, Musculoskeletal System, p. 1204; [3] Radiography of the Dog and Cat: Guide to Making and Interpreting Radiographs, Chapter 5 Musculoskeleton › Panosteitis, pp. 425–427

**89. Which breeds are predisposed to Demodex canis demodicosis?**
_[Demodicosis]_

**Book answer:** American Staffordshire terrier, Shar-Pei, Boston terrier, English bulldog and West Highland white terrier.

**AI answer:**

Breeds reported with increased risk

- The 10 breeds with the highest statistical risk of generalized demodicosis in the Cornell population are: Shar pei, West Highland white terrier, Scottish terrier, English bulldog, Boston terrier, Great Dane, Weimaraner, Airedale terrier, Alaskan malamute, and Afghan hound. [1]

- Specific breed predilections reported for Demodex canis include: American Staffordshire terrier, Shar‑Pei, Boston terrier, English bulldog, and West Highland white terrier. [2]

Other breed note

- The Doberman pinscher is commonly diagnosed with demodicosis but, in the Cornell population, its frequency was not out of proportion to the number of dogs of that breed (local clinic frequencies may differ). [1]

Limitations of the evidence

- These statements are limited to the breeds named and (for the first list) to the Cornell population; the evidence does not provide an exhaustive global list of breeds predisposed to D. canis, nor does it give prevalence rates, age-related risk, or other epidemiologic details.

**Citation(s):** [1] Muller and Kirk's Small Animal Dermatology, Chapter 6 - Parasitic Skin Disease, pp. 461–463; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Demodicosis, p. 355

**90. Which cats and dogs are predisposed to dermatophytosis?**
_[Dermatophytosis]_

**Book answer:** Longhaired cats such as Persians and Himalayans, and Yorkshire and Manchester terriers. M. canis is more common in younger animals.

**AI answer:**

Short answer
- Cats at increased risk: longhaired cats (particularly Persians and Himalayans). [1][2] Dermatophytosis is more common in young cats (<1 year). [1] Immunosuppressed cats are predisposed. [2][3] Communally housed shelter cats have an increased incidence compared with individually housed, privately owned cats. [3][4] FIV‑infected cats have about a three times higher prevalence of dermatophytosis. [4] Hot, humid climates increase incidence. [2][3][5] Excessive bathing and grooming are listed risk factors. [4] Clinical signs are more common in young and older animals. [4]

- Dogs at increased risk: certain breeds (Yorkshire terriers — increased susceptibility to severe M. canis infection; Manchester terriers reported as a breed predilection; Jack Russell terriers — more susceptible to T. mentagrophytes). [3][2][3] Long‑haired animals in general are a risk factor. [3] Young and immunosuppressed dogs are recognized risk groups. [2][3] Hot, humid climates increase incidence. [2][3][5] Excessive bathing and grooming are listed risk factors. [4] Clinical signs are more common in young and older animals. [4]

Limitations of the provided evidence
- The sources list specific breeds and general risk categories but do not provide comprehensive lists of all predisposed breeds, nor do they quantify risk for most factors (except FIV, which is reported as three times higher). [4]  
- The evidence does not cover diagnostic criteria, treatment, prognosis, or specific preventive measures beyond the risk factors noted.

**Citation(s):** [1] Muller and Kirk's Small Animal Dermatology, Chapter 5 - Fungal Skin Diseases, p. 347; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Dermatophytosis, p. 363; [3] Saunders Solutions in Veterinary Practice: Small Animal Dermatology, Chapter 9. Dermatophytosis in a Jack Russell terrier › AETIOPATHOGENESIS OF TRICHOPHYTOSIS, pp. 56–57; [4] Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology, 21 Dermatophytosis › Incidence/Prevalence, pp. 320–321; [5] Muller and Kirk's Small Animal Dermatology, Chapter 5 - Fungal Skin Diseases, pp. 338–339

**91. How is selamectin used for scabies in dogs?**
_[Sarcoptic Mange]_

**Book answer:** It is labeled every 30 days, but application every 2 weeks for at least three treatments may be more effective.

**AI answer:**

Summary
- Selamectin treats and controls canine scabies. [1][2][3]

Formulation and dose
- Selamectin is a spot‑on (topical) formulation. [4]
- A commonly used nominal dose is 6 mg/kg. [4]
- The manufacturer’s recommended topical dose range is 6–12 mg/kg. [3]

Application site and frequency
- Apply topically at the base of the neck in front of the shoulder blades. [1]
- The label and common regimen is application every 30 days (monthly). [1]
- The manufacturer specifically recommends topical application of 6–12 mg/kg twice, 1 month apart. [3]
- Some sources/reports indicate that applying 6–12 mg/kg every 2 weeks (fortnightly) for at least four applications may be more effective. [3]
- The product is labeled for monthly use, but application every 2 weeks for at least three treatments may be more effective. [2]

Safety and adverse effects
- When used according to the manufacturer’s directions, selamectin is safe in ivermectin‑sensitive dogs, in breeding animals, and in puppies and kittens 6 weeks of age or older. [1]
- The manufacturer recommends caution when using in sick, underweight, or debilitated dogs, and it is not recommended for use in dogs under 6 weeks of age. [5]
- Occasional local reactions (inflammation, alopecia) are reported after topical application. [1]

Pharmacokinetics relevant to dosing intervals
- After topical administration to dogs, about 5% of the drug is bioavailable, peak plasma levels occur about 3 days later, and elimination half‑life after topical administration is about 11 days. [5]

Limits of the provided evidence
- The provided claims do not include comparative efficacy data, detailed guidance on monitoring response, specific recommendations for treatment of treatment failures or reinfestation, or quantified adverse‑event rates beyond “occasional local reactions.” Use clinical judgment to choose among the labeled monthly regimen, the manufacturer’s two‑dose monthly recommendation, or more frequent (every‑2‑week) regimens reported as potentially more effective.

**Citation(s):** [1] Muller and Kirk's Small Animal Dermatology, Chapter 6 - Parasitic Skin Disease, pp. 429–430; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Sarcoptic Mange, p. 1199; [3] Small Animal Dermatology: A Color Atlas and Therapeutic Guide, CHAPTER 5 Parasitic Skin Disorders, pp. 112–113; [4] The Merck Veterinary Manual, lntegumentary System, p. 921; [5] Plumb's Veterinary Drug Handbook, Systemic Monographs › Selamectin, pp. 3188–3189

**92. What intraocular pressure is diagnostic of glaucoma in dogs and cats?**
_[Glaucoma]_

**Book answer:** Above 25-30 mmHg in dogs and above 31 mmHg in cats.

**AI answer:**

Short answer
- Dogs: IOP values exceeding 25 mm Hg in conjunction with compatible clinical signs are sufficient for a presumptive diagnosis of glaucoma. [1] Diagnostic criteria cited include IOP >25–30 mm Hg (dogs) as determined via applanation, rebound, or Schiotz tonometry together with changes in vision or the appearance of the globe, optic nerve, and/or retina. [2]

- Cats: IOP values exceeding 27 mm Hg in conjunction with compatible clinical signs are sufficient for a presumptive diagnosis of glaucoma. [1] Diagnostic criteria cited include IOP >31 mm Hg (cats) as determined via applanation, rebound, or Schiotz tonometry together with changes in vision or the appearance of the globe, optic nerve, and/or retina. [2]

Additional note
- IOP values greater than 20 mm Hg are considered suspicious for glaucoma if other clinical signs or anterior uveitis are present. [1]

Limits of the provided evidence
- These claims give diagnostic IOP thresholds and the requirement for compatible clinical/ophthalmoscopic changes, but do not provide management, treatment, or prognostic guidance.

**Citation(s):** [1] Slatter's Fundamentals of Veterinary Ophthalmology, 12 The Glaucomas › Clinical Signs, pp. 282–283; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Glaucoma, p. 551

**93. What Schirmer tear test values indicate KCS in dogs?**
_[Keratoconjunctivitis Sicca]_

**Book answer:** Normal is at least 15 mm/min of wetting; symptomatic dogs usually have less than 10 mm/min. Treatment uses lacrimostimulants such as cyclosporine 0.2% ointment or tacrolimus q12h.

**AI answer:**

Short answer
- Normal (dogs): at least 15 mm/min of wetting. [1]  
- KCS should be suspected if the STT‑1 is less than 15 mm/min (or less than that of the fellow eye). [2]  
- Symptomatic patients are usually < 10 mm/min. [1]

Limits of the evidence
- The provided evidence does not give additional diagnostic cutoffs, grading, or guidance on interpretation/management beyond the statements above.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Keratoconjunctivitis Sicca, p. 779; [2] Slatter's Fundamentals of Veterinary Ophthalmology, 9 Diseases of the Lacrimal System › Medical Treatment, pp. 194–195

**94. Why should the prolapsed third eyelid gland be replaced rather than removed?**
_[Prolapsed Gland of the Third Eyelid (Cherry Eye)]_

**Book answer:** Because the gland produces up to 50% of the aqueous tear film, and excising it predisposes to KCS. Surgical replacement (imbrication technique) is recommended.

**AI answer:**

Short answer
Replace the prolapsed third eyelid gland rather than remove it because the gland has critical lacrimal and immunologic functions and removal substantially increases the risk of keratoconjunctivitis sicca (KCS) later in life. [1][2][3][5]

Key points
- The third eyelid gland has critical immunologic and lacrimal functions, so prolapse is best managed by replacement rather than excision. [1][2]  
- The gland produces up to 50% of the aqueous tear film. [3]  
- Excision of the gland should be avoided because it puts the patient at substantial risk of developing KCS as the dog ages. [3]  
- Replacement is recommended to reduce the incidence of KCS later in life. [4][5]  
- Removal of the gland frequently results in KCS and therefore is not recommended. [5]

Limits of the provided evidence
The supplied claims explain why replacement is preferred and that removal increases KCS risk, but they do not provide details on surgical techniques, comparative success or complication rates, immediate postoperative management, quantitative risk estimates, breed or age-specific data, or long‑term outcome statistics.

**Citation(s):** [1] Slatter's Fundamentals of Veterinary Ophthalmology, 8 Diseases of the Third Eyelid › Prolapse of the Gland of the Third Eyelid (“Cherry Eye”), pp. 181–182; [2] Slatter's Fundamentals of Veterinary Ophthalmology, 8 Diseases of the Third Eyelid › Prolapse of the Gland of the Third Eyelid (“Cherry Eye”), p. 181; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Prolapsed Gland of the Third Eyelid (Cherry Eye), p. 1105; [4] Small Animal Surgery (Fossum), 17 Surgery of the Eye › Surgical Techniques, p. 316; [5] Small Animal Surgery (Fossum), 17 Surgery of the Eye › Postoperative Care and Assessment, pp. 317–318

**95. What cough suppressants are used for tracheal collapse?**
_[Tracheal and Airway Collapse]_

**Book answer:** Butorphanol 0.5-1 mg/kg PO q4-8h or hydrocodone 0.22 mg/kg PO q4-8h, reduced to the least frequent dosing that controls the cough.

**AI answer:**

Short answer: Reported cough suppressants for tracheal collapse include butorphanol, hydrocodone (including Hydrocodone Bitartrate/Hycoden), diphenoxylate with atropine, and — less reliably — over‑the‑counter cough suppressants.

Details:

- Butorphanol — oral and injectable regimens have been used: oral 0.5–1 mg/kg PO q4–8h. [1] Oral 0.5–1.0 mg/kg PO q6–12hr. [3] Injectable 50 μg/kg SC for sedation and cough suppression. [2] Injectable 0.055 mg/kg SC q6–12hr. [3] Injectable 0.05–0.2 mg/kg q4–6h. [4]

- Hydrocodone — oral regimens reported: 0.22 mg/kg PO q4–8h. [1] 0.22 mg/kg PO q12h. [4] Hydrocodone Bitartrate (Hycoden) 0.5 mg/kg PO q8hr is also listed. [3]

- Diphenoxylate with atropine — listed as an antitussive: product concentration 2.5 mg diphenoxylate HCl + 0.025 mg atropine per 5 ml or per tablet; dosing 0.2–0.5 mg/kg diphenoxylate PO q8–12hr. [3]

- Over‑the‑counter cough suppressants — mentioned as alternative drugs but “rarely reduce cough.” [1]

What the provided evidence does not cover: comparative efficacy between these agents, adverse effects, contraindications, dose adjustments, monitoring, combination therapy, or long‑term management.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Tracheal and Airway Collapse, p. 1325; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Tracheal and Airway Collapse, pp. 1324–1325; [3] Small Animal Surgery (Fossum), 29 Surgery of the Upper Respiratory System › Anesthesia, p. 940; [4] Ettinger's Textbook of Veterinary Internal Medicine, 215. Large Airway Diseases, PDF pp. 4394–4397

**96. What components make up brachycephalic airway syndrome?**
_[Brachycephalic Airway Syndrome]_

**Book answer:** Stenotic nares, overlong soft palate, everted laryngeal saccules and laryngeal collapse; a hypoplastic trachea may also be present. English bulldogs are most commonly affected (up to 55% of the breed).

**AI answer:**

Short answer
- Core/classic components are elongated (overlong) soft palate, stenotic nares, and everted laryngeal saccules. [1][2][3]

Expanded definition
- Brachycephalic Airway Syndrome is defined as partial upper‑airway obstruction caused by stenotic nares, overlong soft palate, everted laryngeal saccules, and laryngeal collapse; hypoplastic trachea can also be present and worsen respiratory distress. [1][3]

Common concurrent/associated lesions
- Common concurrent and other findings include hypoplastic trachea, aryepiglottic collapse, corniculate collapse, tracheal collapse, tonsil eversion, macroglossia, pharyngeal collapse, and epiglottic collapse. [1]

Additional anatomic abnormalities reported (Ettinger)
- Ettinger additionally lists stenosis of the nares and vestibulum, immobility of the nasal bulb, malformed rostral and caudal aberrant turbinates (RAT, CAT), increased length and thickness of the soft palate, narrowing of the hamuli pterygoidei, enlarged palatine tonsils, macroglossia, laryngomalacia with impaired arytenoid abduction, laryngocele, malformed over‑thick vocal folds with impaired opening function, hypotrachea, and tracheobronchomalacia. [4][5]

Limitations of the provided evidence
- The cited claims describe the anatomic components and associated lesions but do not provide information on prevalence, clinical staging, diagnostic protocols, management options, or prognosis.

**Citation(s):** [1] Small Animal Surgery (Fossum), 29 Surgery of the Upper Respiratory System › General Considerations and Clinically Relevant Pathophysiology, pp. 923–924; [2] Small Animal Surgery (Fossum), 29 Surgery of the Upper Respiratory System › General Considerations and Clinically Relevant Pathophysiology, pp. 924–925; [3] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Brachycephalic Airway Syndrome, p. 193; [4] Ettinger's Textbook of Veterinary Internal Medicine, 213. Diseases of the Nose, Sinuses, and Nasopharynx, PDF pp. 4323–4325; [5] Ettinger's Textbook of Veterinary Internal Medicine, 213. Diseases of the Nose, Sinuses, and Nasopharynx, PDF pp. 4326–4328

**97. What is the emergency treatment for a cat in an asthma crisis?**
_[Asthma, Bronchitis—Cats]_

**Book answer:** Oxygen and a parenteral bronchodilator such as terbutaline 0.01 mg/kg IV or SC, repeated if there is no improvement in 20-30 minutes.

**AI answer:**

Immediate emergency measures
- Provide oxygen and a parenteral bronchodilator. [2]
- Administer inhaled albuterol, 2–4 puffs every 5 minutes until clinical signs resolve. [1]
- Injectable terbutaline 0.01 mg/kg IV or SC; repeat if no clinical improvement (decrease in respiratory rate or effort) in 20–30 minutes. [2]
- Consider a short-acting parenteral corticosteroid: dexamethasone sodium phosphate 0.1–0.25 mg/kg IV or SC; can repeat if no improvement within 20–30 minutes. [2] Additional therapy may include oxygen and an IV dose of a rapid-acting glucocorticoid. [1]
- A sedative can aid in decreasing anxiety (butorphanol tartrate 0.2–0.4 mg/kg IV or IM, buprenorphine 0.01 mg/kg IV or IM, or acepromazine 0.01–0.05 mg/kg SC). [2]

Logistics
- All hospitals and clinics should have oxygen readily available (tanks or liquid oxygen); oxygen therapy can serve as a bridge to focused therapy. [3]

Limitations
- The above statements summarize the emergency interventions supported by the provided evidence. The claims do not address diagnostics, monitoring parameters, contraindications, or longer-term management beyond the listed interventions.

**Citation(s):** [1] The Merck Veterinary Manual, Pharmacology, pp. 2615–2616; [2] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Asthma, Bronchitis—Cats, pp. 124–125; [3] Ettinger's Textbook of Veterinary Internal Medicine, 123. Respiratory Crisis, PDF pp. 2509–2511

**98. What is the starting corticosteroid dose for IMHA and when is it reduced?**
_[Anemia, Immune-Mediated]_

**Book answer:** Prednisone 1-2 mg/kg/day divided q12h for 2-4 weeks (prednisolone in cats). Once the PCV is above 30%, the dose drops to 1 mg/kg q12h and is then tapered by no more than 25-50% per month over 3-6 months.

**AI answer:**

Starting doses

- Cats: prednisolone 1.5–2 mg/kg PO q12h for about 3 days, then reduce to prednisolone 1 mg/kg PO q12h. [1]  
- Alternatively in cats: give single IV methylprednisolone 10 mg/kg once, then change to oral treatment. [1]  
- Dogs: immunosuppressive prednisolone 1–3 mg/kg PO q12h, reducing to 1–2 mg/kg PO q48h. [2]

When to reduce corticosteroid dose

- After the first 1–2 weeks, if the PCV is stable, the prednisolone dosage can be carefully reduced. [1]  
- Reduction strategy (dependant on stability): if PCV is >30% for 2 weeks, with reduction of RBC agglutination and number of spherocytes and decreasing bilirubin values, prednisolone can be reduced by approximately 25% every 3 weeks. [1]

Limits of the provided evidence
- The statements above are the extent of the provided evidence; no other specifics on total treatment duration, additional tapering variations, or adjunctive therapies are supplied.

**Citation(s):** [1] Ettinger's Textbook of Veterinary Internal Medicine, 174. Immune-Mediated Hemolytic Anemia and Other Regenerative Anemias, PDF pp. 3395–3396; [2] BSAVA Small Animal Formulary, DRUG LISTINGS, pp. 214–215

**99. How is desmopressin used before surgery in dogs with von Willebrand disease?**
_[Von Willebrand Disease]_

**Book answer:** 1 µg/kg SC given 30 minutes before surgery in dogs with mild to moderate Type 1 vWD. The response is variable.

**AI answer:**

Summary for perioperative use of desmopressin (DDAVP)

- Desmopressin acetate (DDAVP) can be given preoperatively to dogs with mild to moderate Type 1 von Willebrand disease to enhance surgical hemostasis. [1]  
- Recommended administration is 1 μg/kg SC given 30 minutes before surgery. [1]  
- Clinical response is variable; have blood products/transfusion available in case DDAVP alone does not prevent bleeding. [1]  
- Limit dosing to not more than once daily because of the risk of water retention, hyponatremia, and tachyphylaxis. [2]

Not covered by the available evidence: effectiveness in severe Type 1 or other von Willebrand disease types, duration of the hemostatic effect after administration, monitoring parameters, contraindications, or specific transfusion triggers.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Von Willebrand Disease, pp. 1404–1405; [2] Ettinger's Textbook of Veterinary Internal Medicine, 175. Immune Thrombocytopenia, von Willebrand Disease, and Other Platelet Disorders, PDF pp. 3439–3440

**100. Which animals are predisposed to heat stroke?**
_[Heat Stroke and Hyperthermia]_

**Book answer:** Longhaired and brachycephalic animals, very young or old animals, young dogs that overexert, and old dogs with preexisting disease. Cats are uncommonly affected.

**AI answer:**

Summary
- Species: Dogs are the primary species; cats can be affected but are uncommon. [1]

Risk groups and traits
- Breed/coat/anatomy: Can occur in any breed; longhaired animals and brachycephalic breeds are predisposed. [1]
- Age: All ages may be affected but extremes are overrepresented — young dogs (tendency to overexert) and geriatric dogs with preexisting disease. [1]
- Specific predisposing factors include: lack of acclimatization; confinement and/or poor ventilation; brachycephalic anatomy; laryngeal paralysis; obesity; increased ambient humidity (>80%); water deprivation; administration of furosemide; use of negative inotropic drugs; phenothiazines; exposure to tremorgenic toxins; cardiovascular disease; neurologic dysfunction; advanced age (geriatric); and hair coat and color. [2]
- Metabolic association: Hypoglycaemia has been associated with heatstroke. [2]
- Equine note: Horses competing in 3‑day eventing, endurance rides, or combined driving are at risk of presenting with life‑threatening exhaustion. [3]

Limitations of the evidence
- The provided evidence addresses dogs (primarily), cats (uncommon), and the specific equine sporting context; it does not provide information on other species, quantitative risk estimates, or clinical management.

**Citation(s):** [1] Blackwell's Five-Minute Veterinary Consult: Canine and Feline, Heat Stroke and Hyperthermia, p. 576; [2] Ettinger's Textbook of Veterinary Internal Medicine, 130. Hyperthermia and Hypothermia, PDF pp. 2619–2620; [3] The Merck Veterinary Manual, Metabolic Disorders, pp. 1010–1011
