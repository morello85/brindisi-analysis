"""
Validated dataset for the Brindisi socio-economic analysis.

EVERY number in this file is traceable to an official source (ISTAT, Eurostat,
Centro Studi Tagliacarne/Unioncamere). The reference year is stored next to each
metric so the app can label charts honestly. Where a figure is an ISTAT estimate
or refers to a different vintage, it is flagged in NOTES.

Primary source for the cross-sectional comparison:
ISTAT, "Il Benessere Equo e Sostenibile dei Territori (BesT) - Puglia 2024"
(published Dec 2024), tables 2.1-2.4, 3.1 and section 4.
https://www.istat.it/wp-content/uploads/2024/12/Puglia_BesT_2024.pdf
"""

import pandas as pd

# Geographic ordering used across the app. Brindisi is the subject of the study.
PROVINCES = ["Foggia", "Bari", "Taranto", "Brindisi", "Lecce", "Barletta-Andria-Trani"]
BENCHMARKS = ["Puglia", "Mezzogiorno", "Italia"]
SUBJECT = "Brindisi"

# ---------------------------------------------------------------------------
# 1. CROSS-SECTIONAL COMPARISON  (latest available year per metric)
#    Source: ISTAT BesT Puglia 2024 - tables 2.2, 2.3, 2.4, 2.1
#    ".." in the source (figure below half the minimum unit) is stored as None.
# ---------------------------------------------------------------------------

# Each metric: dict of name -> {area: value}, plus metadata
_CROSS = {
    # 04-01 Reddito medio disponibile pro capite (euro) - 2022
    "disposable_income": {
        "label": "Disposable income per capita",
        "unit": "€/year",
        "year": "2022",
        "polarity": "higher_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.4 (Conti Economici Territoriali)",
        "values": {
            "Foggia": 13984, "Bari": 18992, "Taranto": 14816, "Brindisi": 15267,
            "Lecce": 15440, "Barletta-Andria-Trani": 15618,
            "Puglia": 16241, "Mezzogiorno": 16062, "Italia": 21089,
        },
    },
    # 04-02 Retribuzione media annua dei lavoratori dipendenti (euro) - 2022
    "avg_pay": {
        "label": "Average annual employee pay",
        "unit": "€/year",
        "year": "2022",
        "polarity": "higher_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.4 (INPS)",
        "values": {
            "Foggia": 15560, "Bari": 18034, "Taranto": 17556, "Brindisi": 16979,
            "Lecce": 15043, "Barletta-Andria-Trani": None,
            "Puglia": 16942, "Mezzogiorno": 16863, "Italia": 22808,
        },
    },
    # 03-01 Tasso di occupazione 20-64 anni (%) - 2023
    "employment_rate": {
        "label": "Employment rate (20-64)",
        "unit": "%",
        "year": "2023",
        "polarity": "higher_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.3",
        "values": {
            "Foggia": 49.3, "Bari": 60.1, "Taranto": 47.5, "Brindisi": 57.4,
            "Lecce": 55.6, "Barletta-Andria-Trani": 51.8,
            "Puglia": 54.7, "Mezzogiorno": 52.2, "Italia": 66.3,
        },
    },
    # 03-04 Tasso di occupazione giovanile 15-29 anni (%) - 2023
    "youth_employment_rate": {
        "label": "Youth employment rate (15-29)",
        "unit": "%",
        "year": "2023",
        "polarity": "higher_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.3",
        "values": {
            "Foggia": 25.3, "Bari": 32.7, "Taranto": 16.3, "Brindisi": 30.1,
            "Lecce": 28.3, "Barletta-Andria-Trani": 31.9,
            "Puglia": 28.0, "Mezzogiorno": 24.7, "Italia": 34.7,
        },
    },
    # 03-02 Tasso di mancata partecipazione al lavoro (%) - 2023 (broad unemployment)
    "labour_underuse": {
        "label": "Labour non-participation rate",
        "unit": "%",
        "year": "2023",
        "polarity": "lower_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.3",
        "values": {
            "Foggia": 26.7, "Bari": 17.8, "Taranto": 33.2, "Brindisi": 23.3,
            "Lecce": 22.3, "Barletta-Andria-Trani": 21.2,
            "Puglia": 23.0, "Mezzogiorno": 28.0, "Italia": 14.8,
        },
    },
    # 02-06 Giovani che non lavorano e non studiano - NEET (%) - 2023
    "neet": {
        "label": "NEET (15-29 not in work/education)",
        "unit": "%",
        "year": "2023",
        "polarity": "lower_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.2",
        "values": {
            "Foggia": 26.7, "Bari": 18.6, "Taranto": 28.5, "Brindisi": 21.7,
            "Lecce": 20.4, "Barletta-Andria-Trani": 21.7,
            "Puglia": 22.2, "Mezzogiorno": 24.7, "Italia": 16.1,
        },
    },
    # 02-03 Persone con almeno il diploma (25-64) (%) - 2023
    "diploma": {
        "label": "Adults (25-64) with at least a diploma",
        "unit": "%",
        "year": "2023",
        "polarity": "higher_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.2",
        "values": {
            "Foggia": 51.6, "Bari": 62.0, "Taranto": 52.7, "Brindisi": 53.0,
            "Lecce": 56.1, "Barletta-Andria-Trani": 47.8,
            "Puglia": 55.7, "Mezzogiorno": 57.7, "Italia": 65.5,
        },
    },
    # 02-04 Laureati e altri titoli terziari (25-39) (%) - 2023
    "graduates": {
        "label": "Young adults (25-39) with a degree",
        "unit": "%",
        "year": "2023",
        "polarity": "higher_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.2",
        "values": {
            "Foggia": 16.3, "Bari": 28.0, "Taranto": 17.9, "Brindisi": 21.6,
            "Lecce": 22.5, "Barletta-Andria-Trani": 26.0,
            "Puglia": 22.9, "Mezzogiorno": 24.4, "Italia": 30.0,
        },
    },
    # 02-05 Passaggio all'universita (%) - 2022
    "university_transition": {
        "label": "School-leavers going to university",
        "unit": "%",
        "year": "2022",
        "polarity": "higher_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.2",
        "values": {
            "Foggia": 55.0, "Bari": 52.2, "Taranto": 49.5, "Brindisi": 48.3,
            "Lecce": 55.2, "Barletta-Andria-Trani": 56.0,
            "Puglia": 52.8, "Mezzogiorno": 47.4, "Italia": 51.7,
        },
    },
    # 01-01 Speranza di vita alla nascita (anni) - 2023 (provv.)
    "life_expectancy": {
        "label": "Life expectancy at birth",
        "unit": "years",
        "year": "2023",
        "polarity": "higher_better",
        "source": "ISTAT BesT Puglia 2024, Tav. 2.1",
        "values": {
            "Foggia": 82.5, "Bari": 83.4, "Taranto": 82.7, "Brindisi": 82.4,
            "Lecce": 83.2, "Barletta-Andria-Trani": 83.2,
            "Puglia": 82.8, "Mezzogiorno": 82.1, "Italia": 83.1,
        },
    },
}


def cross_section_long() -> pd.DataFrame:
    """Tidy long-format frame: one row per (metric, area)."""
    rows = []
    for key, m in _CROSS.items():
        for area, val in m["values"].items():
            rows.append({
                "metric_key": key,
                "metric": m["label"],
                "unit": m["unit"],
                "year": m["year"],
                "polarity": m["polarity"],
                "source": m["source"],
                "area": area,
                "value": val,
                "kind": "Province" if area in PROVINCES else "Benchmark",
            })
    return pd.DataFrame(rows)


def metric_meta() -> dict:
    """Metadata (label/unit/year/polarity/source) keyed by metric_key."""
    return {k: {kk: vv for kk, vv in v.items() if kk != "values"} for k, v in _CROSS.items()}


# ---------------------------------------------------------------------------
# 2. CITY OF BRINDISI - population at every census 1861-2021
#    Source: ISTAT censuses via tuttitalia.it
# ---------------------------------------------------------------------------
CITY_CENSUS = pd.DataFrame({
    "year": [1861, 1871, 1881, 1901, 1911, 1921, 1931, 1936, 1951, 1961,
             1971, 1981, 1991, 2001, 2011, 2021],
    "population": [9137, 13552, 16618, 23106, 25692, 35440, 39885, 41699, 58313,
                   70657, 81893, 89786, 95383, 89081, 88812, 83317],
})
CITY_PEAK = {"year": 1991, "population": 95383}
CITY_LATEST = {"year": 2021, "population": 83317}
CITY_SOURCE = "ISTAT population censuses 1861-2021 (via tuttitalia.it)"

# ---------------------------------------------------------------------------
# 3. PROVINCE OF BRINDISI - resident population 2001-2024 (1 Jan)
#    Source: ISTAT demographic balance via tuttitalia.it
# ---------------------------------------------------------------------------
PROVINCE_POP = pd.DataFrame({
    "year": list(range(2001, 2025)),
    "population": [402093, 400974, 400569, 401217, 403786, 402831, 402985, 402891,
                   403096, 403229, 400504, 399835, 401652, 400721, 398661, 397083,
                   394977, 387817, 385235, 381946, 381273, 379522, 377240, 375567],
})
PROVINCE_PEAK = {"year": 2010, "population": 403229}
PROVINCE_LATEST = {"year": 2024, "population": 375567}
PROVINCE_SOURCE = "ISTAT resident population balance 2001-2024 (via tuttitalia.it)"

# ---------------------------------------------------------------------------
# 4. POPULATION CHANGE RATE 2023 (per 1,000 residents) - provinces reported by ISTAT
#    Source: ISTAT BesT Puglia 2024, section 4. Only the values explicitly stated.
# ---------------------------------------------------------------------------
POP_CHANGE_2023 = pd.DataFrame({
    "area": ["Brindisi", "Taranto", "Bari", "Puglia", "Italia"],
    "rate_per_1000": [-6.5, -6.3, -2.7, -4.5, -0.1],
})
POP_CHANGE_SOURCE = ("ISTAT BesT Puglia 2024, section 4. ISTAT reports Brindisi and "
                     "Taranto as the steepest provincial declines in Puglia; Foggia, "
                     "Lecce and BAT were not given as exact figures.")

# ---------------------------------------------------------------------------
# 5. PUGLIA's RANK AMONG 234 EU NUTS-2 REGIONS  (Eurostat, latest year)
#    Source: ISTAT BesT Puglia 2024, Tav. 3.1 (data: Eurostat)
# ---------------------------------------------------------------------------
EU_RANKING = pd.DataFrame({
    "indicator": ["Employment rate 20-64", "Adults with a diploma", "NEET (15-29)",
                  "Continuing training", "Life expectancy", "Infant mortality"],
    "puglia_value": ["54.7%", "55.7%", "22.2%", "8.5%", "82.8 yrs", "2.7 per 1,000"],
    "rank": [231, 225, 219, 153, 33, 80],
    "of_total": [234, 234, 228, 234, 234, 232],
    "year": ["2023", "2023", "2023", "2023", "2022", "2022"],
})
EU_RANKING_SOURCE = "ISTAT BesT Puglia 2024, Tav. 3.1 (source: Eurostat). Ranking 1 = best."

# ---------------------------------------------------------------------------
# 6. WEALTH PRODUCED - value added per inhabitant (context, region/nation)
#    Source: ISTAT Conti Territoriali 2021 (via BesT 2024 sec. 4) and
#            Centro Studi Tagliacarne 2023 for selected provinces.
# ---------------------------------------------------------------------------
VALUE_ADDED = {
    "year_region": "2021",
    "puglia_per_capita": 18216,
    "italia_per_capita": 27688,
    "puglia_per_worker": 51329,
    "italia_per_worker": 65031,
    "prov_range_2021": (15342, 20991),  # min-max across the 6 Puglia provinces, BesT fig 4.4
    "source": ("ISTAT Conti Economici Territoriali 2021 (via BesT Puglia 2024, sec. 4). "
               "Tagliacarne 2023 provincial value added per capita: Bari 24,911 (75th in "
               "Italy), Taranto 21,502 (84th), Barletta-Andria-Trani 18,184 (lowest in "
               "Puglia); Brindisi ranked ~85th nationally."),
}

# ---------------------------------------------------------------------------
# 7. ECONOMIC STRUCTURE - share of employment by sector (qualitative context)
#    Source: ISTAT BesT Puglia 2024, section 4.
# ---------------------------------------------------------------------------
ECON_STRUCTURE = {
    "note": ("Puglia is more agricultural than Italy (8.4% of employment vs 3.6%) and "
             "slightly more industrial (12.7%). Within the region, Foggia (14.1%) and "
             "Brindisi (11.6%) have the highest agricultural specialisation; "
             "Barletta-Andria-Trani (15.9%) and Taranto (15.3%) the most industry; "
             "Bari (74.3%) and Lecce (73.0%) the most service-oriented."),
    "source": "ISTAT BesT Puglia 2024, section 4.",
}

# ---------------------------------------------------------------------------
# 8. FERTILITY & AGEING (regional, with provincial extremes)
# ---------------------------------------------------------------------------
DEMOG_CONTEXT = {
    "fertility_puglia_2023": 1.20,
    "fertility_italia_2023": 1.20,       # "in linea con la media nazionale"
    "fertility_mezzogiorno_2023": 1.24,
    "fertility_range": "1.16 (Taranto) to 1.29 (Foggia)",
    "old_age_index_puglia_2024": 201,    # over-65s per 100 under-15s
    "old_age_index_italia_2024": 200,
    "old_age_index_range": "170 (Barletta-Andria-Trani) to 230 (Lecce)",
    "source": "ISTAT BesT Puglia 2024, section 4 (Figura 4.3, demographic nowcast).",
}

# ---------------------------------------------------------------------------
# 9. HIGHER-EDUCATION PRECEDENTS - Italian towns that built a university / ITS
#    Academy from scratch. Supports the one-pager's recommendation #1.
# ---------------------------------------------------------------------------
UNI_EXAMPLES = [
    {
        "name": "Università degli Studi di Foggia",
        "place": "Foggia, Puglia",
        "tag": "Same region · state university",
        "founded": "1999",
        "model": ("Began as a decentralised pole of the University of Bari (from "
                  "1990/91), then spun off into a fully autonomous state university."),
        "outcome": ("Credited with catalysing a 'metamorphosis' of the city (ANCSA "
                    "*Premio Gubbio* recognition, 2012). Today Foggia — Puglia's "
                    "poorest province by income — has a university-transition rate of "
                    "55.0%, well above Brindisi's 48.3%."),
        "why_brindisi": ("The closest precedent: a Puglia provincial capital with a "
                         "similar profile that went from satellite courses to a full "
                         "university, and now keeps more of its school-leavers in "
                         "higher education than Brindisi does."),
        "cost": ("No private founding capital: as a **state** university carved out of "
                 "the pre-existing Bari pole, Foggia runs on the ministerial operating "
                 "fund (FFO) and inherited Bari's staff and buildings. The 'investment' "
                 "is recurring state funding, not upfront capital — no clean founding-"
                 "cost figure is published."),
        "sources": [
            ("Università di Foggia — Wikipedia",
             "https://it.m.wikipedia.org/wiki/Universit%C3%A0_degli_Studi_di_Foggia"),
            ("History — UniFg", "https://www.unifg.it/en/university/identity-and-history/history"),
        ],
    },
    {
        "name": "Università Kore di Enna",
        "place": "Enna, Sicilia",
        "tag": "Small town · built from scratch",
        "founded": "2004 (operational 2005/06)",
        "model": ("A non-state university created on the initiative of the Regione "
                  "Siciliana — a brand-new institution in a town smaller than Brindisi."),
        "outcome": ("Became central Sicily's only university; built a new science "
                    "campus with EU funds, including the largest earthquake simulator "
                    "in Europe and the only full-motion flight simulator in a European "
                    "university (aerospace engineering)."),
        "why_brindisi": ("Proof that a modest Southern town can stand up a research-"
                         "grade, industry-relevant university from zero — notable given "
                         "Brindisi's own aerospace presence."),
        "cost": ("Concrete and documented: **INAIL invested €78 million** to build the "
                 "60,000+ m² campus, with a further **€25 million+** for the engineering "
                 "& architecture research labs (and €4 m more recently for the "
                 "rectorate). The private founding endowment — Consorzio Ennese "
                 "Universitario plus the Regione Siciliana under regional law 6/2001 — "
                 "was never published as a single figure."),
        "sources": [
            ("Campus da 78 mln per la Kore — MilanoFinanza",
             "https://www.milanofinanza.it/news/campus-da-78-mln-per-la-kore-di-enna-1202913"),
            ("Università Kore di Enna — Wikipedia",
             "https://it.wikipedia.org/wiki/Universit%C3%A0_Kore_di_Enna"),
        ],
    },
    {
        "name": "ITS Fabriano Academy (+ national ITS network)",
        "place": "Fabriano, Marche",
        "tag": "Industry-linked · faster, cheaper model",
        "founded": "ITS network reformed 2022; PNRR-funded expansion",
        "model": ("A higher-technical academy — not a university — training technicians "
                  "in automation, energy and ICT/security, co-designed with and feeding "
                  "local firms."),
        "outcome": ("82% of students employed within 12 months and ~90% working in the "
                    "field they trained for. Nationally the ITS Academy network exceeds "
                    "85% employment within a year; enrolment tripled from ~13,000 (2021) "
                    "to over 40,000."),
        "why_brindisi": ("The realistic near-term move: an ITS Academy is far quicker "
                         "and cheaper to launch than a university and can be wired "
                         "directly to Brindisi's port, energy and aerospace employers."),
        "cost": ("ITS Academies aren't capitalised like universities — they live on the "
                 "national *Fondo per l'istruzione tecnologica superiore* plus regional "
                 "co-funding and member firms. The public envelope is large and tilted "
                 "south: the **PNRR commits €1.5 bn to ITS through 2026, including €50 m "
                 "specifically for *new* ITS foundations** and €500 m for 4.0 "
                 "laboratories, with ≥40% reserved for the Mezzogiorno."),
        "sources": [
            ("ITS Academy — finanziamenti PNRR (itsvita.it)",
             "https://itsvita.it/finanziamenti-pnrr/"),
            ("ITS Fabriano Academy — Il Resto del Carlino",
             "https://www.ilrestodelcarlino.it/ancona/cronaca/il-successo-dellits-fabriano-academy-56a8d148"),
            ("ITS Academy, occupazione all'84% — ItaliaOggi",
             "https://www.italiaoggi.it/settori/scuola/its-academy-occupazione-all84-e-iscrizioni-in-aumento-lx62ga23"),
        ],
    },
]

# ---------------------------------------------------------------------------
# 10. WHAT BRINDISI SHOULD TEACH - evidence-based course recommendation
# ---------------------------------------------------------------------------
BRINDISI_COURSE = {
    "headline": ("A degree-level pipeline in **Aerospace & Energy-Transition "
                 "Engineering** — created by *upgrading Brindisi's existing aerospace "
                 "ITS and tech district into a degree-granting anchor*, not by starting "
                 "from a blank sheet."),
    "pillars": [
        {
            "name": "1 · Aerospace engineering & advanced manufacturing",
            "evidence": ("Brindisi is the **headquarters of the DTA — the Distretto "
                         "Tecnologico Aerospaziale, ranked Italy's #1 technological "
                         "district (1st of 195)** — and hosts **Leonardo's Helicopter "
                         "Division and Avio Aero**, which builds the Catalyst turboprop "
                         "for the Eurodrone across its Brindisi and Bari sites. A higher-"
                         "technical seed already exists in the city: the **ITS Aerospazio "
                         "Puglia** (at the Cittadella della Ricerca), whose graduates "
                         "reached ~71% employment within a year (88 of 124, 2011–2018). "
                         "The industrial demand and the training nucleus are already "
                         "here — what is missing is the *degree (laurea)* level, so "
                         "today's students must leave for the Politecnico di Bari or "
                         "Turin to study it."),
        },
        {
            "name": "2 · Renewable energy & energy-systems engineering",
            "evidence": ("Brindisi's Enel 'Federico II' **coal plant at Cerano is ceasing "
                         "ordinary coal generation (end-2025)**, and the area is an "
                         "officially recognised **'complex crisis area' with 60+ "
                         "reindustrialisation proposals** — offshore wind, green hydrogen "
                         "and agrivoltaic. An energy-systems strand would retrain "
                         "displaced fossil-fuel workers and capture the just-transition "
                         "investment, while the port's petro-chemical base keeps "
                         "process/chemical engineering grounded in existing industry."),
        },
    ],
    "why_it_fits": ("Both pillars map onto employers **already physically in Brindisi**, "
                    "so graduates would have local, graduate-level jobs to stay for — "
                    "closing the loop between recommendation #1 (lift the 48.3% "
                    "university take-up) and #2 (create higher-value work). Enna's Kore "
                    "even proves the academic model in a small Southern town: it built an "
                    "aerospace-engineering lab with the only full-motion flight simulator "
                    "in a European university."),
    "caveat": ("Brindisi is **not greenfield**. The fast, low-risk move is to upgrade the "
               "existing ITS Aerospazio Puglia and partner with the University of Salento "
               "to add degree-level courses — not to charter a brand-new generalist "
               "university competing with Bari and Lecce. Aim narrow and applied, where "
               "Brindisi has a real industrial edge."),
    "sources": [
        ("DTA – Distretto Tecnologico Aerospaziale (Brindisi)",
         "https://www.dtascarl.org/en/at-a-glance/"),
        ("ITS Aerospazio Puglia (Brindisi)", "https://www.itsaerospaziopuglia.it/"),
        ("Avio Aero Catalyst / Eurodrone — DTA",
         "https://www.dtascarl.org/2022/03/28/motore-turboelica-catalyst-per-leurodrone-sviluppato-in-parte-da-avio-aero-nei-siti-di-brindisi-e-bari/"),
        ("Cerano coal phase-out & reindustrialisation — MIMIT",
         "https://www.mimit.gov.it/it/notizie-stampa/mimit-al-via-consultazione-pubblica-per-la-reindustrializzazione-dellarea-dellex-centrale-a-carbone-di-brindisi"),
    ],
}

# ---------------------------------------------------------------------------
# Master source list (shown in the app)
# ---------------------------------------------------------------------------
SOURCES = [
    ("ISTAT - Il Benessere Equo e Sostenibile dei Territori (BesT), Puglia 2024",
     "https://www.istat.it/wp-content/uploads/2024/12/Puglia_BesT_2024.pdf"),
    ("ISTAT - Conti Economici Territoriali 2021-2023",
     "https://www.istat.it/comunicato-stampa/conti-economici-territoriali-anni-2021-2023/"),
    ("Eurostat - Regional statistics (NUTS-2/NUTS-3), via ISTAT BesT Tav. 3.1",
     "https://ec.europa.eu/eurostat/web/regions/database"),
    ("Centro Studi Tagliacarne / Unioncamere - Valore aggiunto provinciale 2023",
     "https://www.tagliacarne.it/news/valore_aggiunto_tutte_le_province_italiane_in_crescita_sul_podio_4_del_sud_nel_2023-3890/"),
    ("ISTAT population censuses & demographic balance (via tuttitalia.it)",
     "https://www.tuttitalia.it/puglia/12-brindisi/statistiche/"),
]
