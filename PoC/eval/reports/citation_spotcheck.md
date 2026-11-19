# Citation spot-check — verify against the original PDFs

30 random citations (seed 7) out of 223 from the `openai:gpt-5.5` run. For each row:
open the PDF at the **PDF page**, check the claim is supported there, and that the printed page
number matches. Put ✔ or ✘ in the last two columns. The `Auto` columns are the script's own check.

| # | Q | Book | PDF page | Printed page | Claim | Auto: supported | Auto: page | You: supported | You: page |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mb-02 | Blackwell's Five-Minute Veterinary Consult Clinical Companion: Small Animal Dermatology | 315 | 301 | Ivermectin is contraindicated in collies, Shetland sheepdogs, Australian shepherds, Old English sheepdogs, white German shepherds, long-haired whippets, greyhounds, silken windhound, other herding breeds, and crosses with these breeds. | ✔ (0.947) | ✔ |  |  |
| 2 | mb-09 | The Merck Veterinary Manual | 1554–1555 | 1513 | Animals with CKD should also be substaged on the basis of proteinuria, using the protein:creatinine ratio. | ✔ (1.0) | ✔ |  |  |
| 3 | mb-21 | The Merck Veterinary Manual | 568–569 | 527 | Factors are subdivided into predisposing factors, which are present before the development of the ear disease, and perpetuating factors, which occur as a result of the inflammation. | ✔ (1.0) | ✔ |  |  |
| 4 | mb-28 | Saunders Solutions in Veterinary Practice: Small Animal Dermatology | 35 | 26 | Some dermatologists recommend applying the product three times at 14-day intervals, based on anecdotal reports of an improved response, but owners should be warned of the extra-label use. | ✔ (1.0) | ✔ |  |  |
| 5 | mb-20 | Plumb's Veterinary Drug Handbook | 2125–2126 | 2125 | Liothyronine is only indicated in those few situations when T4 supplementation has failed to achieve a response in a dog with confirmed hypothyroidism, perhaps due to impaired GI T4 absorption. | ✔ (1.0) | ✔ |  |  |
| 6 | mb-13 | Ettinger's Textbook of Veterinary Internal Medicine | 4038–4039 | — | Metoclopramide, ondansetron and maropitant appear to be equally effective. | ✔ (1.0) | n/a |  |  |
| 7 | mb-21 | Muller and Kirk's Small Animal Dermatology | 1207–1210 | 1208 | In recurrent cases of parasitic otitis externa, the possibility of other in-contact animals being asymptomatic carriers should be considered. | ✔ (1.0) | ✔ |  |  |
| 8 | mb-16 | Blackwell's Five-Minute Veterinary Consult: Canine and Feline | 167 | 97 | Systemic corticosteroids and nonsteroidal anti-inflammatory drugs should not be used concurrently. | ✔ (1.0) | ✔ |  |  |
| 9 | mb-25 | Plumb's Veterinary Drug Handbook | 2262–2263 | 2262 | Cats, chronic musculoskeletal disorders: Initial treatment is a single oral dose of 0.1 mg meloxicam/kg body weight on the first day. | ✔ (1.0) | ✔ |  |  |
| 10 | mb-11 | Blackwell's Five-Minute Veterinary Consult: Canine and Feline | 719 | 649 | In cats with hyperadrenocorticism, fragile skin described as bruising, tearing, and thin skin is among the most common signs. | ✔ (0.818) | ✔ |  |  |
| 11 | mb-22 | Ettinger's Textbook of Veterinary Internal Medicine | 2765–2766 | — | After a dog ingested a bottle of meloxicam, the passage states that in 5 days (120 hours) the plasma concentration will decrease by ∼97% from the time of presentation and in 7 days by ∼99%. | ✔ (0.857) | n/a |  |  |
| 12 | mb-24 | Small Animal Dermatology: A Color Atlas and Therapeutic Guide | 128 | 115 | In multiple-cat households and catteries, more than one cat is usually affected. | ✔ (1.0) | ✔ |  |  |
| 13 | mb-23 | Small Animal Dermatology: A Color Atlas and Therapeutic Guide | 125–126 | 112 | Selamectin application of 6 to 12 mg/kg every 2 weeks at least four times may be more effective. | ✔ (0.875) | ✔ |  |  |
| 14 | mb-10 | BSAVA Small Animal Formulary | 303 | 285 | The organ toxicity concern is hepatic injury: chronic primidone therapy induces progressive hepatic injury; liver enzymes should be monitored every 6 months. | ✔ (0.8) | ✔ |  |  |
| 15 | mb-15 | Ettinger's Textbook of Veterinary Internal Medicine | 1148–1150 | — | PU results from excessive intake of water (primary polydipsia) or decreased urinary concentrating ability (primary polyuria). | ✔ (1.0) | n/a |  |  |
| 16 | mb-13 | The Merck Veterinary Manual | 416–417 | 375 | In dogs with CPV enteritis, maropitant (1 mg/kg/day, IV) and ondansetron (0.5 mg/kg, IV, tid) appear to be equally effective at controlling vomiting. | ✔ (1.0) | ✔ |  |  |
| 17 | mb-07 | Ettinger's Textbook of Veterinary Internal Medicine | 2608–2609 | — | Epinephrine's adrenergic effects include "decreased mediator release from mast cells and basophils, vasoconstriction, positive inotropy and chronotropy, bronchodilation, and decreased mucosal edema." | ✔ (1.0) | n/a |  |  |
| 18 | mb-16 | Blackwell's Five-Minute Veterinary Consult: Canine and Feline | 167 | 97 | Robenacoxib 1 mg/kg PO once daily; limit duration of use to 3 days. | ✔ (1.0) | ✔ |  |  |
| 19 | mb-23 | Small Animal Dermatology: A Color Atlas and Therapeutic Guide | 125–126 | 112 | 0.025%-0.03% amitraz solution may be applied to the entire body three times at 2-week intervals, or once weekly for 2-6 weeks. | ✔ (1.0) | ✔ |  |  |
| 20 | mb-21 | The Merck Veterinary Manual | 568–569 | 527 | This system is CU1Tently refen-ed to as the PSPP classifica­tion system. | ✔ (1.0) | ✔ |  |  |
| 21 | mb-11 | Muller and Kirk's Small Animal Dermatology | 818–820 | 816 | Muller and Kirk describes thin, fragile skin in a cat with hyperglucocorticoidism. | ✔ (0.625) | ✔ |  |  |
| 22 | mb-16 | Blackwell's Five-Minute Veterinary Consult: Canine and Feline | 167 | 97 | Subconjunctival corticosteroids are indicated only in severe cases as one-time injection, followed by topical and/or systemic anti-inflammatories. | ✔ (1.0) | ✔ |  |  |
| 23 | mb-21 | The Merck Veterinary Manual | 568 | 527 | Secondary causes are those that cause disease in an abnom1al ear. | ✔ (1.0) | ✔ |  |  |
| 24 | mb-14 | BSAVA Small Animal Formulary | 224–225 | 206 | Cats: Initial injectable dose is 0.3 mg/kg s.c.; if given as a single preoperative injection effects last for 24 hours. | ✔ (1.0) | ✔ |  |  |
| 25 | mb-06 | Plumb's Veterinary Drug Handbook | 3784–3785 | 3784 | Cyclosporine is described as an immunomodulating agent. | ✔ (0.75) | ✔ |  |  |
| 26 | mb-07 | Plumb's Veterinary Drug Handbook | 1354–1355 | 1354 | Plumb's states that, in less severe cases, epinephrine "may be given IM or SC." | ✔ (0.714) | ✔ |  |  |
| 27 | mb-09 | Ettinger's Textbook of Veterinary Internal Medicine | 7564–7565 | — | Once the diagnosis of CKD has been confirmed and the dog or cat is stable, International Renal Interest Society (IRIS) staging should be performed. | ✔ (1.0) | n/a |  |  |
| 28 | mb-25 | BSAVA Small Animal Formulary | 224–225 | 206 | Cats: Initial oral dose is 0.1 mg/kg p.o. q24h, which can be followed by a maintenance dose of 0.05 mg/kg p.o q24h. | ✔ (1.0) | ✔ |  |  |
| 29 | mb-01 | The Merck Veterinary Manual | 3088–3089 | 3047 | Calcium oxalate crystalluria may be observed as early as 6 hr after ingestion in dogs. | ✔ (0.857) | ✔ |  |  |
| 30 | mb-13 | Ettinger's Textbook of Veterinary Internal Medicine | 4046–4047 | — | Household bleach diluted 1:30 and left on a surface for 30 minutes is an effective decontaminating agent. | ✔ (1.0) | n/a |  |  |
