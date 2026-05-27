"""
Bilingual (English / Italian) string catalogue for the Brindisi app.

`data.py` stays the single source of *numbers*; this module holds every piece of
*displayed text* in both languages so a single toggle can switch the whole UI.
English entries reuse the strings already in `data.py` where they are plain
citations, to avoid drift. Templates use ``str.format`` placeholders filled in
``app.py`` from the numeric data.
"""

import data

LANG_OPTIONS = {"🇬🇧 EN": "en", "🇮🇹 IT": "it"}

# --------------------------------------------------------------------------- units / labels
UNIT_MAP_IT = {"€/year": "€/anno", "%": "%", "years": "anni"}


def unit(code: str, u: str) -> str:
    return UNIT_MAP_IT.get(u, u) if code == "it" else u


METRIC_LABELS = {
    "en": {k: v["label"] for k, v in data._CROSS.items()},
    "it": {
        "disposable_income": "Reddito disponibile pro capite",
        "avg_pay": "Retribuzione media annua",
        "employment_rate": "Tasso di occupazione (20-64)",
        "youth_employment_rate": "Tasso di occupazione giovanile (15-29)",
        "labour_underuse": "Tasso di mancata partecipazione al lavoro",
        "neet": "NEET (15-29 fuori da lavoro/studio)",
        "diploma": "Adulti (25-64) con almeno il diploma",
        "graduates": "Giovani (25-39) laureati",
        "university_transition": "Diplomati che si iscrivono all'università",
        "life_expectancy": "Speranza di vita alla nascita",
    },
}

POLARITY = {
    "en": {"higher_better": "Higher is better.", "lower_better": "Lower is better."},
    "it": {"higher_better": "Più alto è meglio.", "lower_better": "Più basso è meglio."},
}

# Legend / colour categories (order: subject, other province, benchmark)
TAGS = {
    "en": {"subject": "Brindisi", "province": "Other province",
           "bench": "Benchmark (Puglia / South / Italy)"},
    "it": {"subject": "Brindisi", "province": "Altra provincia",
           "bench": "Riferimento (Puglia / Sud / Italia)"},
}

# EU league table (same row order as data.EU_RANKING)
EU_INDICATORS = {
    "en": list(data.EU_RANKING["indicator"]),
    "it": ["Tasso di occupazione 20-64", "Adulti con diploma", "NEET (15-29)",
           "Formazione continua", "Speranza di vita", "Mortalità infantile"],
}
EU_VALUES = {
    "en": list(data.EU_RANKING["puglia_value"]),
    "it": ["54,7%", "55,7%", "22,2%", "8,5%", "82,8 anni", "2,7 per 1.000"],
}

# --------------------------------------------------------------------------- example cards (IT)
# EN reuses data.UNI_EXAMPLES verbatim; IT spreads it and overrides text fields,
# keeping name / sources (and numeric-only `founded`) single-sourced.
_ex = data.UNI_EXAMPLES
EXAMPLES = {
    "en": _ex,
    "it": [
        {**_ex[0],
         "place": "Foggia, Puglia",
         "tag": "Stessa regione · università statale",
         "model": ("Nata come polo decentrato dell'Università di Bari (dal 1990/91), "
                   "poi scorporata in università statale pienamente autonoma."),
         "outcome": ("Accreditata di aver innescato una 'metamorfosi' della città "
                     "(riconoscimento ANCSA *Premio Gubbio*, 2012). Oggi Foggia — la "
                     "provincia più povera della Puglia per reddito — ha un tasso di "
                     "passaggio all'università del 55,0%, ben sopra il 48,3% di Brindisi."),
         "cost": ("Nessun capitale privato di fondazione: essendo un'università "
                  "**statale** ricavata dal preesistente polo di Bari, vive sul Fondo di "
                  "Finanziamento Ordinario (FFO) ministeriale e ha ereditato personale ed "
                  "edifici di Bari. L''investimento' è finanziamento statale ricorrente, "
                  "non capitale iniziale — non risulta pubblicata una cifra di fondazione."),
         "why_brindisi": ("Il precedente più vicino: un capoluogo di provincia pugliese "
                          "con profilo simile, passato da corsi decentrati a un'università "
                          "completa, e che oggi trattiene più diplomati nell'istruzione "
                          "superiore di quanto faccia Brindisi.")},
        {**_ex[1],
         "place": "Enna, Sicilia",
         "tag": "Cittadina · costruita da zero",
         "founded": "2004 (operativa dal 2005/06)",
         "model": ("Università non statale creata su impulso della Regione Siciliana — "
                   "un'istituzione del tutto nuova in una città più piccola di Brindisi."),
         "outcome": ("Diventata l'unica università della Sicilia centrale; ha costruito un "
                     "nuovo polo scientifico con fondi UE, tra cui il più grande simulatore "
                     "di terremoti d'Europa e l'unico simulatore di volo full-motion "
                     "presente in un'università europea (ingegneria aerospaziale)."),
         "cost": ("Concreto e documentato: **INAIL ha investito 78 milioni di €** per "
                  "costruire il campus di oltre 60.000 m², con altri **25+ milioni di €** "
                  "per i laboratori di ricerca di ingegneria e architettura (e 4 mln più di "
                  "recente per il rettorato). La dotazione patrimoniale iniziale privata — "
                  "Consorzio Ennese Universitario e Regione Siciliana ai sensi della legge "
                  "regionale 6/2001 — non è mai stata pubblicata come cifra unica."),
         "why_brindisi": ("La prova che una modesta città del Sud può creare da zero "
                          "un'università di livello, ancorata all'industria — significativo "
                          "vista la presenza aerospaziale di Brindisi.")},
        {**_ex[2],
         "place": "Fabriano, Marche",
         "tag": "Legata all'industria · modello più rapido ed economico",
         "founded": "Rete ITS riformata nel 2022; espansione finanziata dal PNRR",
         "model": ("Un'academy tecnica superiore — non un'università — che forma tecnici "
                   "in automazione, energia e ICT/security, progettata con e a servizio "
                   "delle imprese locali."),
         "outcome": ("82% degli studenti occupati entro 12 mesi e ~90% impiegati nel campo "
                     "per cui si sono formati. A livello nazionale la rete ITS Academy "
                     "supera l'85% di occupazione entro un anno; le iscrizioni sono "
                     "triplicate da ~13.000 (2021) a oltre 40.000."),
         "cost": ("Gli ITS Academy non sono capitalizzati come le università — vivono sul "
                  "*Fondo per l'istruzione tecnologica superiore* nazionale più "
                  "cofinanziamento regionale e imprese socie. La dotazione pubblica è ampia "
                  "e orientata al Sud: il **PNRR destina 1,5 mld di € agli ITS fino al "
                  "2026, di cui 50 mln specificamente per *nuove* fondazioni ITS** e 500 "
                  "mln per i laboratori 4.0, con ≥40% riservato al Mezzogiorno."),
         "why_brindisi": ("La mossa realistica nel breve termine: un ITS Academy è molto "
                          "più rapido ed economico da avviare di un'università e può essere "
                          "collegato direttamente ai datori di lavoro del porto, "
                          "dell'energia e dell'aerospazio di Brindisi.")},
    ],
}

# --------------------------------------------------------------------------- course pick (IT)
_bc = data.BRINDISI_COURSE
COURSE = {
    "en": _bc,
    "it": {**_bc,
           "headline": ("Una filiera di livello universitario in **Ingegneria Aerospaziale "
                        "e della Transizione Energetica** — creata *potenziando l'ITS "
                        "aerospaziale e il distretto tecnologico già presenti a Brindisi e "
                        "trasformandoli in un polo che rilascia titoli*, non partendo da "
                        "zero."),
           "pillars": [
               {"name": "1 · Ingegneria aerospaziale e manifattura avanzata",
                "evidence": ("Brindisi è la **sede del DTA — il Distretto Tecnologico "
                             "Aerospaziale, 1° distretto tecnologico d'Italia (1° su 195)** "
                             "— e ospita la **Divisione Elicotteri di Leonardo e Avio "
                             "Aero**, che produce il turboelica Catalyst per l'Eurodrone "
                             "tra i siti di Brindisi e Bari. In città esiste già un seme di "
                             "formazione tecnica superiore: l'**ITS Aerospazio Puglia** "
                             "(alla Cittadella della Ricerca), i cui diplomati hanno "
                             "raggiunto ~71% di occupazione entro un anno (88 su 124, "
                             "2011–2018). La domanda industriale e il nucleo formativo sono "
                             "già qui — manca il livello della *laurea*, per cui oggi gli "
                             "studenti devono partire per il Politecnico di Bari o Torino.")},
               {"name": "2 · Energie rinnovabili e ingegneria dei sistemi energetici",
                "evidence": ("La **centrale a carbone Enel 'Federico II' di Cerano cessa la "
                             "produzione ordinaria a carbone (fine 2025)**, e l'area è "
                             "riconosciuta ufficialmente **'area di crisi complessa' con "
                             "oltre 60 proposte di reindustrializzazione** — eolico "
                             "offshore, idrogeno verde e agrivoltaico. Un indirizzo sui "
                             "sistemi energetici riqualificherebbe i lavoratori del fossile "
                             "in uscita e catturerebbe gli investimenti della transizione "
                             "giusta, mentre la base petrolchimica del porto mantiene "
                             "l'ingegneria di processo/chimica ancorata all'industria "
                             "esistente.")},
           ],
           "why_it_fits": ("Entrambi i pilastri corrispondono a datori di lavoro **già "
                           "fisicamente presenti a Brindisi**, così i laureati avrebbero "
                           "lavori locali e qualificati per cui restare — chiudendo il "
                           "cerchio tra la raccomandazione #1 (alzare il 48,3% di passaggio "
                           "all'università) e la #2 (creare lavoro a maggior valore). La "
                           "Kore di Enna dimostra il modello anche in una piccola città del "
                           "Sud: ha realizzato un laboratorio di ingegneria aerospaziale "
                           "con l'unico simulatore di volo full-motion in un'università "
                           "europea."),
           "caveat": ("Brindisi **non parte da zero**. La mossa rapida e a basso rischio è "
                      "potenziare l'ITS Aerospazio Puglia esistente e collaborare con "
                      "l'Università del Salento per aggiungere corsi di livello "
                      "universitario — non fondare una nuova università generalista in "
                      "concorrenza con Bari e Lecce. Puntare su ambiti ristretti e "
                      "applicati, dove Brindisi ha un reale vantaggio industriale."),
           },
}

# --------------------------------------------------------------------------- main string table
T = {
    "en": {
        # header
        "title": "📉 Is Brindisi really falling behind?",
        "intro": ("A data check on the long-standing claim that **Brindisi** is losing "
                  "ground — in wealth, jobs, education and population — against comparable "
                  "Italian towns. Subject of study: the **city and province of Brindisi "
                  "(Puglia)**. Benchmarks: the other five Puglia provinces, the South "
                  "(*Mezzogiorno*), and Italy."),
        "tab_dash": "📊 Dashboard", "tab_paper": "📄 One-pager",
        "tab_uni": "🎓 University deep-dive",
        # dashboard
        "kpi_header": "Brindisi vs the Italian average — headline gaps",
        "kpi_caption": "Green/red shows whether Brindisi sits above or below the national figure.",
        "vs_country": "vs Italy",
        "compare": "Compare a metric",
        "source_label": "Source:",
        "verdict_below": "below", "verdict_above": "at or above",
        "explorer_verdict": ("➡️ Brindisi is **{verdict}** the Italian average for this "
                             "metric ({b} vs {r})."),
        "depop_header": "The depopulation story",
        "city_title": "**City of Brindisi — population at each census, 1861-2021**",
        "axis_census_year": "Census year", "axis_residents": "Residents", "axis_year": "Year",
        "city_caption": ("Peaked at **{peak} (1991)**, down to **{latest} (2021)** — −12.6% "
                         "in 30 years. {src_label} {src}"),
        "prov_title": "**Province of Brindisi — resident population, 2001-2024**",
        "prov_caption": "Peaked at **{peak} (2010)**, down to **{latest} (2024)**. {src_label} {src}",
        "popchange_title": "**2023 population change — Brindisi is shrinking fastest in Puglia**",
        "popchange_x": "Net population change (per 1,000 residents), 2023",
        "eu_header": "Puglia in the European league table",
        "eu_caption": ("Where the Puglia region (which contains Brindisi) ranks among ~234 "
                       "EU NUTS-2 regions. Rank 1 = best."),
        "eu_col_indicator": "Indicator", "eu_col_puglia": "Puglia",
        "eu_col_rank": "Rank", "eu_col_year": "Year",
        "wealth_header": "Wealth produced per person",
        "va_inhab_label": "Puglia value added per inhabitant ({yr})",
        "va_worker_label": "Puglia value added per worker ({yr})",
        "va_delta_inhab": "€{diff:+,} vs Italy (€{ita:,})",
        "va_delta_worker": "€{diff:+,} vs Italy",
        "va_caption": ("Provincial value added per capita ranges €{lo:,}–€{hi:,} across "
                       "Puglia. {src}"),
        "expander_title": "Fertility, ageing & economic structure",
        "demog_md": ("- **Fertility (2023):** Puglia **{fert}** children per woman, ≈ Italy "
                     "({ita}); range {frange}.\n"
                     "- **Ageing (2024):** old-age index **{oai}** over-65s per 100 "
                     "under-15s (Italy {itaoai}); range {oairange}.\n- {econ}"),
        "fert_range": data.DEMOG_CONTEXT["fertility_range"],
        "oai_range": data.DEMOG_CONTEXT["old_age_index_range"],
        "demog_source": data.DEMOG_CONTEXT["source"],
        "econ_note": data.ECON_STRUCTURE["note"], "econ_source": data.ECON_STRUCTURE["source"],
        "src_city": data.CITY_SOURCE, "src_prov": data.PROVINCE_SOURCE,
        "src_popchange": data.POP_CHANGE_SOURCE, "src_eu": data.EU_RANKING_SOURCE,
        "va_source": data.VALUE_ADDED["source"],
        "footer": ("Built with Streamlit · All figures traceable to ISTAT, Eurostat and "
                   "Centro Studi Tagliacarne. See the One-pager tab for sources."),
        # one-pager
        "op_subheader": "One-pager: is Brindisi falling behind?",
        "op_intro": """
**The claim.** For decades, residents of Brindisi have argued that the town is
slipping behind comparable Italian towns: young people leave for the north or
abroad, there is no strong local university, entrepreneurship is thin, and
politics has lacked a vision — despite good transport links, a petro-chemical
industrial base and some seasonal tourism.

**What the data says — a nuanced *yes*.** Tested against official ISTAT, Eurostat
and Tagliacarne figures, the claim is **largely supported, but with an important
correction**: Brindisi is unambiguously poorer and emptier than the Italian and
European norm, yet it is **not the worst performer within Puglia** — it sits
mid-pack regionally, with Foggia and Taranto usually faring worse.
""",
        "op_evidence_h": "#### The evidence, in four lines",
        "op_evidence": """
1. **Wealth is well below the national norm.** Disposable income per head in the
   province of Brindisi was **€15,267 (2022)** versus **€21,089 for Italy** — a
   **−28%** gap. Value added per inhabitant for Puglia (€18,216) trails Italy
   (€27,688) by a third. *(ISTAT, 2021–2022)*
2. **The town is emptying, faster than its neighbours.** The city peaked at
   **95,383 residents in 1991** and fell to **83,317 by 2021 (−12.6%)**; the
   province slid from **403,229 (2010)** to **375,567 (2024)**. In 2023 Brindisi
   recorded the **steepest population decline in Puglia (−6.5 per 1,000)**.
   *(ISTAT)*
3. **The brain-drain narrative checks out.** Brindisi has the region's **lowest
   university-transition rate (48.3%)**, a low graduate share among young adults
   (21.6% vs 30.0% in Italy), and a fertility rate (regional 1.20) that cannot
   offset out-migration. *(ISTAT, 2022–2023)*
4. **The whole region is a European laggard.** Puglia ranks **231st of 234 EU
   regions for employment**, 225th for diploma attainment and 219th for NEETs —
   so Brindisi's struggle is real but shared across the South. *(Eurostat)*
""",
        "op_spotlight_h": "#### Spotlight: the university gap that feeds the brain drain",
        "op_spotlight_warn": ("**Only 48.3% of Brindisi's school-leavers go on to university "
                              "(2022) — the lowest rate of any Puglia province.** It sits "
                              "below the national average (51.7%) and Puglia's own (52.8%), "
                              "barely above the broad Southern figure (47.4%), and trails "
                              "the regional front-runners — Barletta-Andria-Trani (56.0%), "
                              "Lecce (55.2%) and Foggia (55.0%) — by seven to eight points."),
        "op_spotlight": """
**Why this number matters more than it looks.** A university-transition rate is
not just an education statistic for Brindisi — it is the **first valve of the
brain drain**. Unlike Bari, Lecce and Foggia, each of which anchors a full
university, Brindisi has no degree-granting institution of its own. So for a
local eighteen-year-old, *"going to university" almost always means leaving the
city*. That relocation cost depresses enrolment at the margin — and, more
corrosively, the minority who do enrol study in Lecce, Bari or the north and
rarely come back. The result is a self-reinforcing loop, and the numbers line up
exactly with it: Brindisi simultaneously posts **the region's lowest university
take-up, a below-average share of young graduates (21.6% of 25–39s vs 30.0%
nationally), and its steepest population decline (−6.5 per 1,000)**. The town
exports its most educated cohort and never recovers it.

**An honest caveat — it's not purely the missing university.** Barletta-Andria-
Trani also lacks its own university yet records the *highest* transition rate in
Puglia, helped by sitting between the Bari and Foggia campuses; and Brindisi's
petro-chemical and agricultural economy plausibly channels some school-leavers
straight into work rather than study. So the gap is partly a participation
shortfall (a few points) and partly *what happens after enrolment*: an
out-migration the local labour market gives graduates no compelling reason to
reverse. Fixing the take-up rate alone would not help much if the graduate jobs
to come home to still aren't there.
""",
        "op_correct_h": "#### Where the popular story needs correcting",
        "op_correct": """
- On **jobs**, Brindisi is actually one of Puglia's better provinces: its
  employment rate (57.4%) is **second only to Bari** and above the regional and
  Mezzogiorno averages — though still ~9 points under Italy. The problem is less
  "no jobs" than **low pay, few graduate-level roles, and youth outflow**.
- Brindisi is **not Puglia's poorest** province (Foggia is, on income), nor its
  most jobless (Taranto is). Its distinctive problem is **demographic bleeding** —
  it is shrinking fastest — combined with a thin higher-education pipeline.
""",
        "op_verdict_h": "#### Verdict",
        "op_verdict": ("**Hypothesis: supported, with nuance.** Brindisi is clearly faring "
                       "worse than the typical Italian town on wealth, education and "
                       "especially population retention, and it is losing people faster "
                       "than any other Puglia province. But within its own region it is "
                       "roughly average — the deeper story is a structural Southern/EU gap "
                       "plus an acute local depopulation and brain-drain problem, not a "
                       "town uniquely worse than its immediate neighbours."),
        "op_rec_h": "#### Three actions for the medium-to-long term",
        "op_rec_intro": """
These follow directly from what the data flags as Brindisi's binding
constraints — a leaky education pipeline, low-value-added jobs, and out-migration
the labour market never reverses. They are **directional priorities inferred from
the indicators**, not a costed policy plan.
""",
        "op_rec": """
1. **Give Brindisi a higher-education anchor of its own — tied to local
   industry.** The single worst education number is the **48.3% university
   take-up (lowest in Puglia)**, and it is structural: there is no degree-granting
   institution in the city, so studying means leaving at eighteen. Establishing a
   real university presence or applied higher-technical institutes (*ITS
   Academy*-style) built around the town's actual sectors — port & logistics,
   energy, agri-food, aerospace — would keep more school-leavers studying locally
   *and* feed graduates straight into local employers. This attacks the brain
   drain at its first valve. *(Data: university transition 48.3%; young-graduate
   share 21.6% vs 30.0% nationally.)* **→ It can be done — see the 🎓 University
   deep-dive tab for the Foggia, Enna and ITS Fabriano precedents.**

2. **Upgrade the industrial base from low-value to high-value work, using the
   energy transition as the lever.** Brindisi's jobs problem is **pay and
   productivity, not headcount** — the employment rate (57.4%) is second-best in
   Puglia, yet average employee pay (€16,979) trails Italy (€22,808) by ~26% and
   regional value added per worker (€51,329) sits a fifth below the national
   €65,031. The existing petro-chemical, port and energy assets are the platform:
   steering investment and *just-transition* funding toward renewables, clean
   energy and higher-tech port/logistics activity would create the **graduate-
   level, better-paid roles that give the educated diaspora a reason to return**.
   *(Data: avg pay −26% vs Italy; value added per worker −21%; agriculture 11.6%
   of local employment, 2nd-highest in Puglia.)*

3. **Court the diaspora and entrepreneurs back — turn the town's real assets into
   reasons to stay.** Brindisi loses people faster than any Puglia province
   (**−6.5 per 1,000 in 2023**), and fertility (1.20) cannot offset it, so growth
   has to come from **retention and return**. Use the connectivity the town
   already has (rail, airport, port) plus low living costs to support return-and-
   remote-work incentives, start-up and self-employment programmes, and a shift
   from seasonal to year-round tourism — converting assets that today only pass
   people *through* Brindisi into reasons to base a career *in* it. *(Data:
   steepest provincial depopulation −6.5‰; fertility 1.20 ≈ national.)*
""",
        "op_method_h": "#### Method & caveats",
        "op_method": """
- **Geographic unit:** economic metrics (income, value added) are only published
  at *province* level, so the province of Brindisi is the unit for those;
  population uses both city and province. Comparators are the five other Puglia
  provinces plus Mezzogiorno and Italy benchmarks.
- **Vintages differ by metric** (2021–2024) — each chart is labelled with its
  year. Figures are taken as published; no estimates were invented to fill gaps
  (missing cells are shown as gaps, not guesses).
""",
        "op_sources_h": "#### Sources",
        # deep-dive
        "dd_subheader": "University deep-dive: can a town really build one from scratch?",
        "dd_intro": ("Recommendation #1 in the one-pager calls for giving Brindisi a "
                     "higher-education anchor of its own. It is fair to ask whether that is "
                     "realistic — **it is, and there are three Italian precedents, one of "
                     "them in Puglia.**"),
        "dd_natexp": ("**A natural experiment next door.** Foggia is Puglia's *poorest* "
                      "province by income, yet **{foggia:.1f}%** of its school-leavers go "
                      "on to university — against Brindisi's **{brindisi:.1f}%**, the "
                      "regional low. The likeliest difference: Foggia gave them a local "
                      "university to enrol in (founded 1999); Brindisi has none."),
        "dd_card_how": "**How it was done.**", "dd_card_what": "**What happened.**",
        "dd_card_cost": "**What it cost / how it was funded.**",
        "dd_card_why": "**Why it matters for Brindisi.**",
        "dd_sources_label": "Sources:", "dd_founded_word": "Founded",
        "dd_teach_h": "### What Brindisi should teach — a specific, evidence-based pick",
        "dd_reco_label": "**Recommendation.**",
        "dd_whyfit_label": "**Why this fits Brindisi.**",
        "dd_reality_label": "**Reality check.**",
        "dd_lesson": ("**The lesson for Brindisi.** Start with the fast, cheap, high-yield "
                      "move — an **ITS Academy wired to the port, energy and aerospace "
                      "employers** (the Fabriano model shows 85%+ employment) — and build "
                      "toward a permanent university presence as Foggia and Enna did. But "
                      "pair it with recommendation #2: a degree only stops the brain drain "
                      "if there are graduate-level jobs locally to fill afterwards."),
    },
    "it": {
        # header
        "title": "📉 Brindisi sta davvero restando indietro?",
        "intro": ("Una verifica sui dati della tesi, ormai radicata, che **Brindisi** stia "
                  "perdendo terreno — in ricchezza, lavoro, istruzione e popolazione — "
                  "rispetto a città italiane comparabili. Oggetto di studio: la **città e "
                  "provincia di Brindisi (Puglia)**. Riferimenti: le altre cinque province "
                  "pugliesi, il Sud (*Mezzogiorno*) e l'Italia."),
        "tab_dash": "📊 Cruscotto", "tab_paper": "📄 Sintesi",
        "tab_uni": "🎓 Approfondimento università",
        # dashboard
        "kpi_header": "Brindisi rispetto alla media italiana — i divari principali",
        "kpi_caption": "Il verde/rosso indica se Brindisi è sopra o sotto il dato nazionale.",
        "vs_country": "vs Italia",
        "compare": "Confronta un indicatore",
        "source_label": "Fonte:",
        "verdict_below": "sotto", "verdict_above": "pari o sopra",
        "explorer_verdict": ("➡️ Per questo indicatore Brindisi è **{verdict}** la media "
                             "italiana ({b} vs {r})."),
        "depop_header": "La storia dello spopolamento",
        "city_title": "**Città di Brindisi — popolazione a ogni censimento, 1861-2021**",
        "axis_census_year": "Anno del censimento", "axis_residents": "Residenti",
        "axis_year": "Anno",
        "city_caption": ("Picco di **{peak} (1991)**, sceso a **{latest} (2021)** — −12,6% "
                         "in 30 anni. {src_label} {src}"),
        "prov_title": "**Provincia di Brindisi — popolazione residente, 2001-2024**",
        "prov_caption": "Picco di **{peak} (2010)**, sceso a **{latest} (2024)**. {src_label} {src}",
        "popchange_title": "**Variazione di popolazione 2023 — Brindisi cala più di tutte in Puglia**",
        "popchange_x": "Variazione netta di popolazione (per 1.000 residenti), 2023",
        "eu_header": "La Puglia nella classifica europea",
        "eu_caption": ("Posizione della regione Puglia (che comprende Brindisi) tra le ~234 "
                       "regioni UE di livello NUTS-2. Posizione 1 = migliore."),
        "eu_col_indicator": "Indicatore", "eu_col_puglia": "Puglia",
        "eu_col_rank": "Posizione", "eu_col_year": "Anno",
        "wealth_header": "Ricchezza prodotta per persona",
        "va_inhab_label": "Valore aggiunto per abitante in Puglia ({yr})",
        "va_worker_label": "Valore aggiunto per occupato in Puglia ({yr})",
        "va_delta_inhab": "€{diff:+,} vs Italia (€{ita:,})",
        "va_delta_worker": "€{diff:+,} vs Italia",
        "va_caption": ("Il valore aggiunto pro capite provinciale va da €{lo:,} a €{hi:,} "
                       "in Puglia. {src}"),
        "expander_title": "Fecondità, invecchiamento e struttura economica",
        "demog_md": ("- **Fecondità (2023):** Puglia **{fert}** figli per donna, ≈ Italia "
                     "({ita}); intervallo {frange}.\n"
                     "- **Invecchiamento (2024):** indice di vecchiaia **{oai}** over-65 "
                     "ogni 100 under-15 (Italia {itaoai}); intervallo {oairange}.\n- {econ}"),
        "fert_range": "da 1,16 (Taranto) a 1,29 (Foggia)",
        "oai_range": "da 170 (Barletta-Andria-Trani) a 230 (Lecce)",
        "demog_source": "ISTAT BesT Puglia 2024, sezione 4 (Figura 4.3, nowcast demografico).",
        "econ_note": ("La Puglia è più agricola dell'Italia (8,4% dell'occupazione contro "
                      "3,6%) e leggermente più industriale (12,7%). Nella regione, Foggia "
                      "(14,1%) e Brindisi (11,6%) hanno la maggiore specializzazione "
                      "agricola; Barletta-Andria-Trani (15,9%) e Taranto (15,3%) la maggiore "
                      "industria; Bari (74,3%) e Lecce (73,0%) la maggiore vocazione ai "
                      "servizi."),
        "econ_source": "ISTAT BesT Puglia 2024, sezione 4.",
        "src_city": "Censimenti ISTAT della popolazione 1861-2021 (via tuttitalia.it)",
        "src_prov": "Bilancio ISTAT popolazione residente 2001-2024 (via tuttitalia.it)",
        "src_popchange": ("ISTAT BesT Puglia 2024, sezione 4. L'ISTAT indica Brindisi e "
                          "Taranto come i cali provinciali più marcati in Puglia; per "
                          "Foggia, Lecce e BAT non sono fornite cifre esatte."),
        "src_eu": "ISTAT BesT Puglia 2024, Tav. 3.1 (fonte: Eurostat). Posizione 1 = migliore.",
        "va_source": ("ISTAT Conti Economici Territoriali 2021 (via BesT Puglia 2024, sez. "
                      "4). Valore aggiunto pro capite provinciale Tagliacarne 2023: Bari "
                      "24.911 (75ª in Italia), Taranto 21.502 (84ª), Barletta-Andria-Trani "
                      "18.184 (minimo in Puglia); Brindisi ~85ª a livello nazionale."),
        "footer": ("Realizzato con Streamlit · Tutti i dati sono tracciabili a ISTAT, "
                   "Eurostat e Centro Studi Tagliacarne. Vedi la scheda Sintesi per le fonti."),
        # one-pager
        "op_subheader": "Sintesi: Brindisi sta restando indietro?",
        "op_intro": """
**La tesi.** Da decenni gli abitanti di Brindisi sostengono che la città stia
restando indietro rispetto a città italiane comparabili: i giovani partono per il
nord o per l'estero, manca una vera università locale, l'imprenditoria è debole e
la politica non ha avuto una visione — nonostante buoni collegamenti, una base
industriale petrolchimica e un po' di turismo stagionale.

**Cosa dicono i dati — un *sì* con sfumature.** Alla prova delle cifre ufficiali
di ISTAT, Eurostat e Tagliacarne, la tesi è **in larga parte confermata, ma con
una correzione importante**: Brindisi è inequivocabilmente più povera e più vuota
della norma italiana ed europea, eppure **non è la peggiore della Puglia** — si
colloca a metà classifica regionale, con Foggia e Taranto di solito messe peggio.
""",
        "op_evidence_h": "#### Le prove, in quattro righe",
        "op_evidence": """
1. **La ricchezza è ben sotto la norma nazionale.** Il reddito disponibile pro
   capite della provincia di Brindisi era di **15.267 € (2022)** contro **21.089 €
   dell'Italia** — un divario del **−28%**. Il valore aggiunto per abitante della
   Puglia (18.216 €) è inferiore di un terzo a quello italiano (27.688 €).
   *(ISTAT, 2021–2022)*
2. **La città si svuota, più in fretta delle vicine.** La città ha toccato il
   picco di **95.383 residenti nel 1991** ed è scesa a **83.317 nel 2021
   (−12,6%)**; la provincia è passata da **403.229 (2010)** a **375.567 (2024)**.
   Nel 2023 Brindisi ha registrato il **calo di popolazione più marcato della
   Puglia (−6,5 per 1.000)**. *(ISTAT)*
3. **La fuga dei cervelli trova conferma.** Brindisi ha il **tasso di passaggio
   all'università più basso della regione (48,3%)**, una quota bassa di laureati
   tra i giovani (21,6% contro 30,0% in Italia) e una fecondità (regionale 1,20)
   che non compensa l'emigrazione. *(ISTAT, 2022–2023)*
4. **L'intera regione è fanalino di coda in Europa.** La Puglia è **231ª su 234
   regioni UE per occupazione**, 225ª per diploma e 219ª per i NEET — quindi la
   difficoltà di Brindisi è reale ma condivisa con tutto il Sud. *(Eurostat)*
""",
        "op_spotlight_h": "#### Focus: il divario universitario che alimenta la fuga dei cervelli",
        "op_spotlight_warn": ("**Solo il 48,3% dei diplomati di Brindisi prosegue "
                              "all'università (2022) — il tasso più basso di qualsiasi "
                              "provincia pugliese.** È sotto la media nazionale (51,7%) e "
                              "quella pugliese (52,8%), appena sopra il dato del Sud "
                              "(47,4%), e resta indietro di sette-otto punti rispetto alle "
                              "province di testa della regione — Barletta-Andria-Trani "
                              "(56,0%), Lecce (55,2%) e Foggia (55,0%)."),
        "op_spotlight": """
**Perché questo numero conta più di quanto sembri.** Per Brindisi il tasso di
passaggio all'università non è solo una statistica scolastica — è la **prima
valvola della fuga dei cervelli**. A differenza di Bari, Lecce e Foggia, ognuna
con una propria università, Brindisi non ha un ateneo che rilasci titoli. Così,
per un diciottenne del posto, *"andare all'università" significa quasi sempre
partire*. Quel costo di trasferimento abbassa le iscrizioni al margine — e, cosa
più corrosiva, la minoranza che si iscrive studia a Lecce, Bari o al nord e
raramente torna. Il risultato è un circolo che si autoalimenta, e i numeri lo
confermano in pieno: Brindisi mostra contemporaneamente **il passaggio
all'università più basso della regione, una quota di giovani laureati sotto la
media (21,6% dei 25–39enni contro 30,0% in Italia) e il calo di popolazione più
marcato (−6,5 per 1.000)**. La città esporta la sua fascia più istruita e non la
recupera mai.

**Una precisazione onesta — non è solo l'università mancante.** Anche
Barletta-Andria-Trani non ha un proprio ateneo eppure registra il tasso di
passaggio *più alto* della Puglia, favorita dalla posizione tra i poli di Bari e
Foggia; e l'economia petrolchimica e agricola di Brindisi probabilmente avvia
parte dei diplomati direttamente al lavoro anziché allo studio. Il divario è
quindi in parte un deficit di partecipazione (pochi punti) e in parte *ciò che
succede dopo l'iscrizione*: un'emigrazione che il mercato del lavoro locale non dà
ai laureati alcun motivo convincente di invertire. Correggere il solo tasso di
iscrizione servirebbe a poco se i lavori qualificati a cui tornare continuano a
non esserci.
""",
        "op_correct_h": "#### Dove la versione popolare va corretta",
        "op_correct": """
- Sul **lavoro**, Brindisi è in realtà una delle province migliori della Puglia:
  il tasso di occupazione (57,4%) è **secondo solo a Bari** e sopra le medie
  regionale e del Mezzogiorno — pur restando ~9 punti sotto l'Italia. Il problema
  non è tanto la "mancanza di lavoro" quanto **bassi salari, pochi ruoli da
  laureato e l'uscita dei giovani**.
- Brindisi **non è la provincia più povera** della Puglia (lo è Foggia, per
  reddito), né quella con più disoccupazione (lo è Taranto). Il suo problema
  distintivo è l'**emorragia demografica** — cala più di tutte — unita a una
  filiera dell'istruzione superiore debole.
""",
        "op_verdict_h": "#### Verdetto",
        "op_verdict": ("**Ipotesi: confermata, con sfumature.** Brindisi sta chiaramente "
                       "peggio della tipica città italiana per ricchezza, istruzione e "
                       "soprattutto capacità di trattenere la popolazione, e perde abitanti "
                       "più in fretta di ogni altra provincia pugliese. Ma all'interno "
                       "della sua regione è all'incirca nella media — la storia di fondo è "
                       "un divario strutturale Sud/UE più un acuto problema locale di "
                       "spopolamento e fuga dei cervelli, non una città unicamente peggiore "
                       "delle vicine immediate."),
        "op_rec_h": "#### Tre azioni per il medio-lungo termine",
        "op_rec_intro": """
Discendono direttamente da ciò che i dati indicano come i vincoli stringenti di
Brindisi — una filiera dell'istruzione che perde pezzi, lavori a basso valore
aggiunto ed emigrazione che il mercato del lavoro non inverte mai. Sono
**priorità d'indirizzo dedotte dagli indicatori**, non un piano di policy con i
costi.
""",
        "op_rec": """
1. **Dare a Brindisi un proprio polo di istruzione superiore — legato
   all'industria locale.** Il peggior dato sull'istruzione è il **48,3% di
   passaggio all'università (il più basso della Puglia)**, ed è strutturale: in
   città non c'è un ateneo che rilasci titoli, quindi studiare significa partire a
   diciott'anni. Creare una vera presenza universitaria o istituti tecnici
   superiori applicati (tipo *ITS Academy*) costruiti attorno ai settori reali
   della città — porto e logistica, energia, agroalimentare, aerospazio —
   tratterrebbe più diplomati a studiare in loco *e* alimenterebbe direttamente i
   datori di lavoro locali. Così si colpisce la fuga dei cervelli alla sua prima
   valvola. *(Dati: passaggio all'università 48,3%; quota giovani laureati 21,6%
   contro 30,0% nazionale.)* **→ Si può fare — vedi la scheda 🎓 Approfondimento
   università per i precedenti di Foggia, Enna e dell'ITS di Fabriano.**

2. **Trasformare la base industriale da basso ad alto valore, usando la
   transizione energetica come leva.** Il problema occupazionale di Brindisi è
   **salari e produttività, non quantità di posti** — il tasso di occupazione
   (57,4%) è il secondo della Puglia, ma la retribuzione media (16.979 €) è
   inferiore del ~26% a quella italiana (22.808 €) e il valore aggiunto per
   occupato regionale (51.329 €) è un quinto sotto i 65.031 € nazionali. Gli asset
   esistenti — petrolchimico, porto, energia — sono la piattaforma: indirizzare
   investimenti e fondi della *transizione giusta* verso rinnovabili, energia
   pulita e attività portuali/logistiche a più alta tecnologia creerebbe i **ruoli
   qualificati e meglio pagati che darebbero alla diaspora istruita un motivo per
   tornare**. *(Dati: retribuzione media −26% vs Italia; valore aggiunto per
   occupato −21%; agricoltura 11,6% dell'occupazione locale, 2ª in Puglia.)*

3. **Richiamare la diaspora e gli imprenditori — trasformare gli asset reali della
   città in motivi per restare.** Brindisi perde abitanti più di ogni altra
   provincia pugliese (**−6,5 per 1.000 nel 2023**), e la fecondità (1,20) non
   basta a compensare, quindi la crescita deve venire da **trattenimento e
   ritorno**. Usare i collegamenti che la città già possiede (treno, aeroporto,
   porto) e il basso costo della vita per sostenere incentivi al rientro e al
   lavoro da remoto, programmi per start-up e lavoro autonomo, e un passaggio dal
   turismo stagionale a quello tutto l'anno — convertendo asset che oggi fanno solo
   *transitare* le persone *per* Brindisi in motivi per costruirci *dentro* una
   carriera. *(Dati: spopolamento provinciale più marcato −6,5‰; fecondità 1,20 ≈
   nazionale.)*
""",
        "op_method_h": "#### Metodo e avvertenze",
        "op_method": """
- **Unità geografica:** gli indicatori economici (reddito, valore aggiunto) sono
  pubblicati solo a livello *provinciale*, quindi per quelli l'unità è la provincia
  di Brindisi; la popolazione usa sia città sia provincia. I termini di confronto
  sono le altre cinque province pugliesi più i riferimenti Mezzogiorno e Italia.
- **Le annate variano per indicatore** (2021–2024) — ogni grafico riporta il
  proprio anno. Le cifre sono prese così come pubblicate; non sono state inventate
  stime per colmare i vuoti (le celle mancanti restano vuote, non indovinate).
""",
        "op_sources_h": "#### Fonti",
        # deep-dive
        "dd_subheader": "Approfondimento università: una città può davvero costruirne una da zero?",
        "dd_intro": ("La raccomandazione #1 della sintesi chiede di dare a Brindisi un "
                     "proprio polo di istruzione superiore. È legittimo chiedersi se sia "
                     "realistico — **lo è, e ci sono tre precedenti italiani, uno dei quali "
                     "in Puglia.**"),
        "dd_natexp": ("**Un esperimento naturale a due passi.** Foggia è la provincia *più "
                      "povera* della Puglia per reddito, eppure il **{foggia:.1f}%** dei "
                      "suoi diplomati prosegue all'università — contro il **{brindisi:.1f}%** "
                      "di Brindisi, il minimo regionale. La differenza più probabile: Foggia "
                      "ha dato loro un'università locale dove iscriversi (fondata nel 1999); "
                      "Brindisi non ne ha."),
        "dd_card_how": "**Come è stata realizzata.**", "dd_card_what": "**Cosa è successo.**",
        "dd_card_cost": "**Quanto è costata / come è stata finanziata.**",
        "dd_card_why": "**Perché conta per Brindisi.**",
        "dd_sources_label": "Fonti:", "dd_founded_word": "Fondazione",
        "dd_teach_h": "### Cosa dovrebbe insegnare Brindisi — una scelta specifica e basata sui dati",
        "dd_reco_label": "**Raccomandazione.**",
        "dd_whyfit_label": "**Perché si adatta a Brindisi.**",
        "dd_reality_label": "**Verifica di realtà.**",
        "dd_lesson": ("**La lezione per Brindisi.** Partire dalla mossa rapida, economica e "
                      "ad alto rendimento — un **ITS Academy collegato ai datori di lavoro "
                      "del porto, dell'energia e dell'aerospazio** (il modello Fabriano "
                      "mostra oltre l'85% di occupazione) — e costruire verso una presenza "
                      "universitaria permanente, come hanno fatto Foggia ed Enna. Ma "
                      "abbinarla alla raccomandazione #2: una laurea ferma la fuga dei "
                      "cervelli solo se poi ci sono lavori qualificati da occupare in loco."),
    },
}
