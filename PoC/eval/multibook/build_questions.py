"""Source of truth for the multi-book test set -> questions.jsonl.

    python -m eval.multibook.build_questions

Written by hand (Claude, from reading the cleaned library pages). Questions are
paraphrased - not copied from the books - and every key fact carries the book,
PDF page, printed page and a short verbatim quote, so `run_multibook check-keys`
can prove each fact really is on the cited page.

LEAKAGE RULES: this folder is never indexed, chunked or put in any prompt of the
system under test. Only the judge sees `key_facts`, and only after the answer exists.
split: "dev" = may be used to choose settings; "test" = held out, run once at the end.
"""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "questions.jsonl"


def F(book, pdf, printed, quote, fact):
    return {"book_id": book, "pdf_page": pdf, "printed_page": printed, "quote": quote, "fact": fact}


Q = []


def q(qid, split, qtype, question, facts, conflict=None, absent_terms=None, behaviour=None):
    books = sorted({f["book_id"] for f in facts})
    Q.append({
        "id": qid, "split": split, "type": qtype, "question": question,
        "required_books": books, "key_facts": facts,
        "conflict": conflict, "absent_terms": absent_terms or [],
        "expected_behaviour": behaviour or (
            "Answer from the books, citing every required book." if qtype != "unanswerable"
            else "Say the books do not cover this; do not invent a dose or recommendation."),
    })


# ---------------- two-book (14) ----------------
q("mb-01", "dev", "two_book",
  "A dog has drunk antifreeze. What antidote regimen is given, and what urine crystal finding supports the diagnosis?",
  [F("plumbs-drug-handbook", 1596, "1596", "Initially load at 20 mg/kg IV",
     "Fomepizole for ethylene glycol in dogs: 20 mg/kg IV load, 15 mg/kg IV at 12 h, 15 mg/kg at 24 h, 5 mg/kg at 36 h."),
   F("merck-vet-manual", 1659, "1618", "typically seen in association with ethylene glycol toxicity",
     "Calcium oxalate (monohydrate, dumb-bell shaped) crystals are associated with ethylene glycol toxicity.")])

q("mb-02", "test", "two_book",
  "When ivermectin is used for canine demodicosis, how should it be given to work, and which breeds need special caution?",
  [F("muller-kirk-dermatology", 433, "429", "it can be effective when it is administered orally daily",
     "Weekly protocols used for other ectoparasites were not effective for Demodex; daily oral ivermectin can be effective."),
   F("plumbs-drug-handbook", 1977, "1977", "Caution in breeds susceptible to ABCB1",
     "Caution in ABCB1 (MDR1) mutation breeds: Collies, Australian Shepherds, Shelties, Long-haired Whippets - higher CNS toxicity risk.")])

q("mb-03", "test", "two_book",
  "At what ages is a puppy vaccinated against parvovirus in the suggested schedule, and which drugs support a puppy already sick with parvo?",
  [F("vaccination-schedule", 7, None, "Canine Parvo virus Live attenuated 6 weeks",
     "Parvovirus: live attenuated vaccine at 6 weeks, then 10 and 14 weeks, subcutaneous."),
   F("blackwell-5min-canine-feline", 287, "217", "ampicillin and gentamicin",
     "Supportive drugs: parenteral ampicillin + gentamicin, antiemetics such as ondansetron or maropitant; gentamicin can harm the kidneys of dehydrated puppies.")])

q("mb-04", "dev", "two_book",
  "For suspected free air in the chest, which radiographic view makes it easier to see and what does auscultation typically reveal?",
  [F("radiography-dog-cat", 173, "161", "making detection easier in a DV view",
     "Pleural gas rises dorsally in ventral recumbency, so it is easier to detect on a DV view than a VD view."),
   F("fossum-small-animal-surgery", 799, "739", "absence of pulmonary sounds in the dorsal lateral chest wall",
     "Pneumothorax: lung sounds are absent over the dorsal lateral chest wall.")])

q("mb-05", "test", "two_book",
  "In glaucoma management, what pressure value guides whether to keep going with medical treatment or move to surgery, and which oral agent can lower pressure quickly in an emergency?",
  [F("slatter-ophthalmology", 314, "298", "IOP < 20 Continue medical Rx",
     "If IOP stays below 20 mm Hg continue medical treatment; above 20 mm Hg consider surgery."),
   F("plumbs-drug-handbook", 1688, "1688", "short-term reduction of IOP in small animals with acute glaucoma",
     "Oral glycerin is used for short-term IOP reduction in acute glaucoma; its effect is more variable than mannitol.")])

q("mb-06", "test", "two_book",
  "How is dry eye confirmed with a tear test, and what kind of drug is commonly used to treat immune-mediated eye disease such as this?",
  [F("blackwell-5min-canine-feline", 845, "775", "values < 15 mm/min suggest KCS",
     "Schirmer tear test: normal >= 15 mm/min; < 15 mm/min suggests KCS (interpret with breed)."),
   F("slatter-ophthalmology", 88, "72", "Cyclosporine is a potent immunosuppressive drug",
     "Cyclosporine is a potent immunosuppressive used often for immune-mediated ocular disease.")])

q("mb-07", "test", "two_book",
  "In a dog in anaphylactic shock, what epinephrine dose is suggested and why does epinephrine help?",
  [F("blackwell-5min-canine-feline", 146, "76", "1:1,000; 0.01 mL/kg",
     "Epinephrine 1:1,000 at 0.01 mL/kg parenterally for anaphylactic shock."),
   F("applied-pharmacology-vet-tech", 89, "77", "hypotension and bronchoconstriction of anaphylactic shock",
     "Epinephrine reverses the hypotension and bronchoconstriction of anaphylactic shock.")])

q("mb-08", "dev", "two_book",
  "How common is pancreatitis among pancreatic diseases of dogs and cats, and which specific blood test is listed for it?",
  [F("merck-vet-manual", 448, "407", "most conm1on exoc1ine pancreatic disease",
     "Pancreatitis is the most common exocrine pancreatic disease in dogs and cats; it may be acute or chronic."),
   F("blackwell-5min-canine-feline", 465, "395", "Spec cPL (pancreatitis)",
     "Spec cPL is the test listed for pancreatitis.")])

q("mb-09", "test", "two_book",
  "How is chronic kidney disease staged in dogs and cats, and what urine protein:creatinine range counts as borderline proteinuria in each species?",
  [F("blackwell-5min-canine-feline", 1234, "1164", "IRIS CKD stages 1",
     "IRIS stages 1-4 use two or more fasting, well-hydrated serum creatinine values over several weeks; CKD = present > 3 months."),
   F("merck-vet-manual", 1554, "1513", "Borderline 0.2-0.5 0.2-0.4",
     "IRIS proteinuria substage 'borderline': UPC 0.2-0.5 in dogs, 0.2-0.4 in cats.")])

q("mb-10", "test", "two_book",
  "How is primidone related to phenobarbital, and what organ toxicity is a concern with both drugs?",
  [F("bsava-formulary", 304, "286", "conversion of mysoline to phenobarbitone",
     "Primidone (Mysoline) is converted to phenobarbitone (phenobarbital)."),
   F("applied-pharmacology-vet-tech", 98, "86", "hepatotoxicity (phenobarbital and primidone)",
     "Hepatotoxicity is an adverse effect of phenobarbital and primidone.")])

q("mb-11", "test", "two_book",
  "Which skin changes point to Cushing's syndrome, including the ones typical in cats, and which dexamethasone dose is used for the suppression test in cats?",
  [F("blackwell-5min-dermatology", 74, "60", "curling of tips of pinnae and skin fragility",
     "Cushing's: truncal alopecia, comedones, rat tail, thin skin, phlebectasia, potbelly; in cats curled pinnal tips and skin fragility."),
   F("plumbs-drug-handbook", 1062, "1062", "uses a higher dose of dexamethasone (0.1 mg/kg IV) than in dogs",
     "LDDS is the test of choice for feline HAC and uses 0.1 mg/kg IV dexamethasone, higher than in dogs.")])

q("mb-12", "dev", "two_book",
  "Against which parasites is selamectin indicated in dogs and cats, and how often is it applied for prevention?",
  [F("merck-vet-manual", 178, "137", "monthly dosage of -6 mg/kg",
     "Selamectin is applied topically monthly at ~6 mg/kg; kills fleas and treats Otodectes and sarcoptic mange."),
   F("bsava-formulary", 323, "305", "prevention of heartworm disease",
     "Selamectin is used for fleas, ear mites (Otodectes), sarcoptic mange, lice, roundworms and heartworm prevention in dogs.")])

q("mb-13", "test", "two_book",
  "How should a kennel be disinfected after a parvovirus case, and which antiemetic drugs can be used for the affected puppies?",
  [F("merck-vet-manual", 417, "376", "dilute bleach",
     "Clean organic matter, then disinfect with dilute bleach (1:30) or peroxygen / accelerated hydrogen peroxide products."),
   F("blackwell-5min-canine-feline", 287, "217", "ondansetron, maropitant",
     "Antiemetics for parvovirus: ondansetron, maropitant.")])

q("mb-14", "test", "two_book",
  "Why can a single injection of meloxicam be risky in an anaesthetised animal or one with liver disease, and how is the drug handled by the body?",
  [F("bsava-formulary", 224, "206", "Liver disease will prolong the metabolism of meloxicam",
     "Delay meloxicam if anaesthetic hypotension is expected (renal perfusion); liver disease prolongs metabolism and risks accumulation."),
   F("plumbs-drug-handbook", 2259, "2259", "about 97% is bound to plasma proteins",
     "In dogs meloxicam is well absorbed, peaks at 7-8 h, ~97% protein bound and extensively metabolised in the liver.")])

# ---------------- three-book (10) ----------------
q("mb-15", "dev", "three_book",
  "What are the main mechanisms behind increased thirst and urination in dogs, and which diseases cause the kidneys to stop responding to ADH?",
  [F("ettinger-internal-medicine", 1149, None, "primary polydipsia",
     "PU results from excess water intake (primary polydipsia) or reduced urine concentrating ability (primary polyuria)."),
   F("differential-diagnosis-lists", 122, "118", "Polyuria caused by nonresponsiveness to antidiuretic hormone",
     "Secondary nephrogenic DI causes: renal failure, hyperadrenocorticism, hypoadrenocorticism, hepatic insufficiency, pyometra, hypercalcemia, hypokalemia ..."),
   F("blackwell-5min-canine-feline", 1164, "1094", "impaired renal response to ADH",
     "Primary PU from impaired renal response to ADH: renal failure, HAC (dogs), hyperthyroidism (cats).")])

q("mb-16", "test", "three_book",
  "A cat has inflammation inside the front of the eye. Which systemic infections should be ruled out, and what anti-inflammatory regimen can be given by mouth or injection?",
  [F("ettinger-internal-medicine", 549, None, "Toxoplasma gondii",
     "Feline uveitis causes: FeLV, FIV, FIP, Toxoplasma gondii, systemic fungi, neoplasia; Bartonella role debated."),
   F("blackwell-5min-canine-feline", 167, "97", "limit duration of use to 4 days",
     "Meloxicam 0.2 mg/kg once, then 0.05 mg/kg q24h for 2 days, then 0.025 mg/kg; limit to 4 days (renal risk)."),
   F("slatter-ophthalmology", 395, "379", "Feline infectious peritonitis",
     "Infectious causes listed include FIV, FIP (feline coronavirus), FeLV.")])

q("mb-17", "test", "three_book",
  "Which laboratory tests are used to diagnose hyperadrenocorticism, and how does the suppression test differ in cats?",
  [F("merck-vet-manual", 586, "545", "the diagnosis of hyperadrenocorticism can be confim1ed",
     "UCCR with oral dexamethasone: if UCCR does not fall into normal range HAC is confirmed; ACTH stimulation is also used."),
   F("blackwell-5min-canine-feline", 130, "60", "ACTH-response test, LDDST, and HDDST",
     "ACTH-response test, LDDST and HDDST diagnose HAC; abdominal ultrasound assesses the adrenals."),
   F("plumbs-drug-handbook", 1062, "1062", "Test of choice for diagnosis of feline hyperadrenocorticism",
     "Feline LDDS uses 0.1 mg/kg IV dexamethasone, higher than in dogs.")])

q("mb-18", "test", "three_book",
  "What drugs control an overactive thyroid in cats, how do they relate to each other, and can they be given through the skin?",
  [F("bsava-formulary", 67, "49", "Carbimazole is metabolized to the active drug methimazole",
     "Carbimazole is converted to the active drug methimazole, which blocks thyroid hormone synthesis."),
   F("wsava-essential-medicines", 16, "15", "compounded as transdermal preparations",
     "Methimazole (thiamazole) is given orally but can be compounded as a transdermal preparation."),
   F("plumbs-drug-handbook", 2317, "2317", "Transdermal methimazole (in PLO gel; 2.5 mg twice daily)",
     "Methimazole is the agent of choice in North America; transdermal PLO gel 2.5 mg twice daily; propylthiouracil has more adverse effects.")])

q("mb-19", "dev", "three_book",
  "In a dog with a twisted, bloated stomach, where should IV catheters be placed during stabilisation, and how is recurrence prevented?",
  [F("ettinger-internal-medicine", 6167, None, "large-gauge catheters in veins cranial to the gastric volvulus",
     "Place large-gauge catheters in veins cranial to the volvulus (jugular/cephalic), then intensive fluid resuscitation."),
   F("blackwell-5min-canine-feline", 602, "532", "Prevention of recurrence is achieved through a permanent gastropexy",
     "Recurrence is prevented by permanent gastropexy."),
   F("merck-vet-manual", 427, "386", "Prophylactic gastropexy",
     "Prophylactic gastropexy is recommended for at-risk breeds or dogs whose relatives had GDV.")])

q("mb-20", "test", "three_book",
  "Which drug is preferred for treating an underactive thyroid in dogs, what starting dose is used, and when would a T3 product be considered?",
  [F("applied-pharmacology-vet-tech", 182, "170", "T3 products are recommended only when a poor response to T4 occurs",
     "Synthetic T4 (levothyroxine) is the compound of choice; T3 only if response to T4 is poor."),
   F("plumbs-drug-handbook", 2100, "2100", "0.02 mg/kg PO twice daily to start",
     "Start 0.02 mg/kg PO twice daily; 0.5 mg/m2 may avoid hyperthyroid effects in large breeds."),
   F("wsava-essential-medicines", 16, "15", "Levothyroxine is the most common form",
     "Synthetic thyroxine (levothyroxine) treats canine hypothyroidism.")])

q("mb-21", "test", "three_book",
  "How common is outer ear inflammation, what role do ear mites play in cats, and how are the contributing causes grouped?",
  [F("fossum-small-animal-surgery", 365, "338", "up to 20% of hospital admissions",
     "Otitis externa: up to 20% of dog admissions (7% cats); 50-89% of affected dogs have otitis media; O. cynotis causes > 50% of feline otitis externa."),
   F("muller-kirk-dermatology", 1203, "1204", "primary causes, secondary causes, or perpetuating factors",
     "Predisposing factors act with primary causes, secondary causes and perpetuating factors."),
   F("merck-vet-manual", 178, "137", "Otodectes",
     "Selamectin is indicated for Otodectes cynotis in dogs and cats.")])

q("mb-22", "test", "three_book",
  "Why might a dog's meloxicam overdose need several days of monitoring, and which patient factors raise the risk of accumulation?",
  [F("ettinger-internal-medicine", 2765, None, "terminal half-life",
     "Meloxicam terminal half-life ~24 h in dogs; after 5 days concentration falls ~97%."),
   F("bsava-formulary", 224, "206", "Liver disease will prolong the metabolism of meloxicam",
     "Liver disease prolongs metabolism and risks accumulation with repeated dosing."),
   F("plumbs-drug-handbook", 2259, "2259", "extensively biotransformed",
     "Meloxicam is extensively biotransformed in the liver; ~97% protein bound.")])

q("mb-23", "test", "three_book",
  "How reliable are skin scrapings for finding scabies mites in dogs, and what topical treatment regimens are recommended?",
  [F("dermatology-color-atlas", 26, "13", "Low (only 20%)",
     "Superficial scrapings find Sarcoptes in only ~20% of cases."),
   F("saunders-solutions-dermatology", 35, "26", "6–12 mg/kg twice 30 days apart",
     "Selamectin 6-12 mg/kg twice, 30 days apart (some use three times at 14-day intervals)."),
   F("merck-vet-manual", 178, "137", "sarcoptic mange",
     "Selamectin (monthly ~6 mg/kg) is indicated for sarcoptic mange.")])

q("mb-24", "test", "three_book",
  "How is the mite that causes feline scabies managed in a household, and how widespread is it?",
  [F("muller-kirk-dermatology", 488, "484", "All cats on the premises must be treated",
     "Treat all cats on the premises; ivermectin SC two or three times, or one doramectin dose 0.2-0.3 mg/kg."),
   F("blackwell-5min-dermatology", 648, "634", "Notoedres cati",
     "Notoedres cati causes notoedric mange in cats."),
   F("merck-vet-manual", 562, "521", "Notoedres cati is conunon in cats",
     "Notoedres cati is common in cats throughout the world.")])

# ---------------- conflicts (5) ----------------
q("mb-25", "dev", "conflict",
  "What meloxicam dose do the books give for cats?",
  [F("applied-pharmacology-vet-tech", 471, "459", "0.3 mg/kg SC one-time injection",
     "Applied Pharmacology: 0.3 mg/kg SC one-time; 0.05 mg/kg q24-48h PO chronic."),
   F("merck-vet-manual", 1234, "1193", "cats: 0.1 mg/kg/day",
     "Merck: 0.1 mg/kg/day for 1-3 days."),
   F("blackwell-5min-canine-feline", 167, "97", "then 0.025 mg/kg q24–48h",
     "Blackwell: 0.2 mg/kg once, 0.05 mg/kg q24h x2 days, then 0.025 mg/kg q24-48h; max 4 days."),
   F("fossum-small-animal-surgery", 176, "152", "Cat: 0.05-0.1 mg/kg SC",
     "Fossum: preoperative 0.05-0.1 mg/kg SC.")],
  conflict="Initial cat doses range from 0.05 to 0.3 mg/kg and durations from a single dose to chronic use; a good answer shows the different regimens with their books instead of picking one.")

q("mb-26", "test", "conflict",
  "What is a normal Schirmer tear test result?",
  [F("blackwell-5min-canine-feline", 845, "775", "normal values are ≥15 mm/min",
     "Blackwell: normal >= 15 mm/min."),
   F("ettinger-internal-medicine", 5933, None, "21 +/− 4 mm/min",
     "Ettinger: dogs 21 +/- 4 mm/min; cats 9-34 mm/min (median 18).")],
  conflict="One book gives a single >= 15 mm/min cut-off, the other species-specific ranges (dogs 21 +/- 4; cats 9-34).")

q("mb-27", "test", "conflict",
  "After the puppy series, how often should dogs be revaccinated against parvovirus?",
  [F("vaccination-schedule", 7, None, "then yearly",
     "Vaccination Schedule: 6, 10, 14 weeks then yearly."),
   F("merck-vet-manual", 417, "376", "and then every 3 yr",
     "Merck: 6-8, 10-12, 14-16 wk, booster 1 yr later, then every 3 years.")],
  conflict="Yearly boosters vs. every 3 years after the 1-year booster.")

q("mb-28", "test", "conflict",
  "How often and how many times should selamectin be applied to treat sarcoptic mange?",
  [F("saunders-solutions-dermatology", 35, "26", "three times at 14-day intervals",
     "Saunders: 6-12 mg/kg twice 30 days apart; some apply three times at 14-day intervals."),
   F("merck-vet-manual", 178, "137", "monthly dosage of -6 mg/kg",
     "Merck: monthly ~6 mg/kg topical.")],
  conflict="Two applications 30 days apart (or three at 14 days) vs. monthly application.")

q("mb-29", "test", "conflict",
  "What daily oral meloxicam dose is used in dogs?",
  [F("applied-pharmacology-vet-tech", 471, "459", "Dog: 0.2 mg/kg initially PO, then 0.1 mg/kg q24h PO",
     "Applied Pharmacology: 0.2 mg/kg initially then 0.1 mg/kg q24h."),
   F("blackwell-5min-canine-feline", 169, "99", "Meloxicam 0.2 mg/kg PO q24h",
     "Blackwell (uveitis, dogs): 0.2 mg/kg PO q24h."),
   F("merck-vet-manual", 1234, "1193", "dogs: 0.1 mg/kg/day",
     "Merck: 0.1 mg/kg/day.")],
  conflict="0.2 mg/kg q24h ongoing vs 0.2 then 0.1 mg/kg vs 0.1 mg/kg/day.")

# ---------------- unanswerable (6) ----------------
for qid, split, question, terms in [
    ("mb-30", "dev", "What is the dose of bedinvetmab (Librela) for osteoarthritis pain in dogs?", ["bedinvetmab", "librela"]),
    ("mb-31", "test", "What dose of ilunocitinib (Zenrelia) is recommended for atopic dermatitis in dogs?", ["ilunocitinib", "zenrelia"]),
    ("mb-32", "test", "How is molidustat (Varenzin) used for anaemia in cats with chronic kidney disease?", ["molidustat", "varenzin"]),
    ("mb-33", "test", "What tirzepatide dose helps obese cats lose weight?", ["tirzepatide"]),
    ("mb-34", "test", "How long does one injection of the 12-month injectable fluralaner protect a dog against fleas and ticks?", ["fluralaner injectable", "bravecto 12", "12-month fluralaner"]),
    ("mb-35", "test", "What is the dose of the NexGard COMBO (esafoxolaner, eprinomectin, praziquantel) spot-on for cats?", ["esafoxolaner", "nexgard combo"]),
]:
    q(qid, split, "unanswerable", question, [], absent_terms=terms)

# ---------------- single-book controls (5) ----------------
q("mb-36", "dev", "single_book",
  "What happens to the darkness of a radiograph when the kVp is raised, and why?",
  [F("radiography-dog-cat", 32, "20", "the higher the kVp, the more transmitted x",
     "Higher kVp = more penetrating, more transmitted x-rays, darker radiograph.")])
q("mb-37", "test", "single_book",
  "What does the term azotemia mean?",
  [F("saunders-vet-dictionary", 125, "105", "an excess of nitrogen-containing compounds in the blood",
     "Azotemia: excess nitrogen-containing compounds in the blood.")])
q("mb-38", "test", "single_book",
  "When and how is a breeder chicken flock first vaccinated against Marek's disease?",
  [F("vaccination-schedule", 1, None, "Day old (1st day) in hatchery Marek",
     "Marek's disease vaccine on day 1 in the hatchery, subcutaneous, 0.2 ml.")])
q("mb-39", "test", "single_book",
  "What is nephrogenic diabetes insipidus, and which dog breed has a familial primary form?",
  [F("differential-diagnosis-lists", 122, "118", "Primary familial (Husky)",
     "Nephrogenic DI = polyuria from nonresponsiveness to ADH; primary familial form in Huskies.")])
q("mb-40", "test", "single_book",
  "What is a gastropexy and what is it mainly done for?",
  [F("saunders-vet-dictionary", 494, "474", "surgical ﬁxation of the stomach",
     "Gastropexy: surgical fixation of the stomach, usually to the abdominal wall, to prevent recurrence of gastric volvulus.")])


# Topic keyword groups (chosen from each question's content, NOT from retrieval
# results). A page/chunk is "on topic" if it contains every keyword of any one
# group. Used to (1) list other books that also answer the question
# (also_valid_books) and (2) score retrieved chunks as relevant, so a correct
# answer from a book outside required_books is not counted as a miss.
TOPICS = {
    "mb-01": [["ethylene glycol", "fomepizole"], ["ethylene glycol", "oxalate"]],
    "mb-02": [["ivermectin", "demodicosis"], ["ivermectin", "abcb1"], ["ivermectin", "mdr1"]],
    "mb-03": [["parvovirus", "vaccin", "weeks"], ["parvovirus", "maropitant"], ["parvovirus", "ondansetron"]],
    "mb-04": [["pneumothorax", "dv view"], ["pneumothorax", "lung sounds"], ["pneumothorax", "radiograph"]],
    "mb-05": [["glaucoma", "glycerin"], ["glaucoma", "mannitol"], ["intraocular pressure", "20 mm hg"]],
    "mb-06": [["schirmer", "keratoconjunctivitis sicca"], ["keratoconjunctivitis sicca", "cyclosporine"]],
    "mb-07": [["anaphyla", "epinephrine"], ["anaphyla", "adrenaline"]],
    "mb-08": [["pancreatitis", "cpl"], ["pancreatitis", "exocrine pancreatic disease"]],
    "mb-09": [["iris", "stage", "creatinine"], ["proteinuria", "borderline"]],
    "mb-10": [["primidone", "phenobarb"]],
    "mb-11": [["hyperadrenocorticism", "skin fragility"], ["hyperadrenocorticism", "cats", "dexamethasone suppression"]],
    "mb-12": [["selamectin", "otodectes"], ["selamectin", "heartworm"]],
    "mb-13": [["parvovirus", "bleach"], ["parvovirus", "disinfect"], ["parvovirus", "maropitant"]],
    "mb-14": [["meloxicam", "liver"], ["meloxicam", "protein bound"], ["meloxicam", "hypotension"]],
    "mb-15": [["polyuria", "primary polydipsia"], ["nephrogenic diabetes insipidus"]],
    "mb-16": [["uveitis", "toxoplasm", "cat"], ["uveitis", "meloxicam", "cat"]],
    "mb-17": [["hyperadrenocorticism", "acth stimulation"], ["hyperadrenocorticism", "dexamethasone suppression"]],
    "mb-18": [["methimazole", "transdermal"], ["carbimazole", "methimazole"]],
    "mb-19": [["gastric dilat", "gastropexy"], ["volvulus", "catheter"]],
    "mb-20": [["levothyroxine", "hypothyroidism", "mg/kg"], ["levothyroxine", "liothyronine"]],
    "mb-21": [["otitis externa", "otodectes"], ["otitis externa", "perpetuating"]],
    "mb-22": [["meloxicam", "half-life"], ["meloxicam", "liver"]],
    "mb-23": [["sarcoptes", "scraping"], ["sarcoptic", "selamectin"]],
    "mb-24": [["notoedres", "cat"]],
    "mb-25": [["meloxicam", "cats", "mg/kg"]],
    "mb-26": [["schirmer", "mm/min"]],
    "mb-27": [["parvovirus", "vaccin", "every 3"], ["parvo", "booster", "yearly"], ["parvovirus", "revaccinat"]],
    "mb-28": [["selamectin", "sarcoptic"], ["selamectin", "scabies"]],
    "mb-29": [["meloxicam", "dogs", "mg/kg"]],
    "mb-36": [["kvp", "darker"], ["kvp", "density"]],
    "mb-37": [["azotemia", "nitrogen"]],
    "mb-38": [["marek", "day old"], ["marek", "vaccin"]],
    "mb-39": [["nephrogenic diabetes insipidus"]],
    "mb-40": [["gastropexy", "volvulus"]],
}


def on_topic(text: str, groups: list[list[str]]) -> bool:
    low = text.lower()
    return any(all(k in low for k in g) for g in groups)


def add_also_valid() -> None:
    """For each question: books outside required_books that also have on-topic pages."""
    import config
    from src import library

    config.set_profile("library")
    pages = {b["book_id"]: library.load_pages(b["book_id"]) for b in library.load_manifest()}
    for row in Q:
        groups = TOPICS.get(row["id"], [])
        row["topic_groups"] = groups
        also = {}
        for book_id, rows in pages.items():
            if book_id in row["required_books"]:
                continue
            hits = [r["pdf_page"] for r in rows if on_topic(r["text"], groups)] if groups else []
            if hits:
                also[book_id] = hits[:5]
        row["also_valid_books"] = also


if __name__ == "__main__":
    add_also_valid()
    with OUT.open("w", encoding="utf-8") as handle:
        for row in Q:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    from collections import Counter
    print(f"Wrote {len(Q)} questions -> {OUT}")
    print(" types:", dict(Counter(r["type"] for r in Q)))
    print(" split:", dict(Counter(r["split"] for r in Q)))
