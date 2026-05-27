# Is Brindisi falling behind?

A data-driven check of the long-standing claim that **Brindisi (Puglia, Italy)**
is faring worse than comparable Italian towns on wealth, jobs, education and
population.

## What it shows

- **Dashboard tab** — interactive comparison of Brindisi against the other five
  Puglia provinces and the Italy / *Mezzogiorno* benchmarks across income, pay,
  employment, youth employment, NEETs, education and life expectancy; plus the
  long-run depopulation of the city and province, Puglia's EU ranking, and
  wealth produced per person.
- **One-pager tab** — a written, sourced verdict on the hypothesis.

## Data & sources

Every figure is traceable (see `data.py`) to official sources:

- **ISTAT — Benessere Equo e Sostenibile dei Territori (BesT), Puglia 2024** — the
  backbone cross-sectional dataset (income, employment, education, health by province).
- **ISTAT — Conti Economici Territoriali** — value added per capita / per worker.
- **Eurostat** (via ISTAT BesT Tav. 3.1) — Puglia's rank among EU regions.
- **Centro Studi Tagliacarne / Unioncamere** — provincial value added 2023.
- **ISTAT censuses & demographic balance** (via tuttitalia.it) — population series.

Reference years differ by metric (2021–2024) and are labelled on every chart.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Headline finding

The hypothesis is **supported, with nuance**: Brindisi is clearly below the
Italian/EU norm on wealth, education and population retention — and is shrinking
faster than any other Puglia province — but within its own region it is roughly
mid-pack (Foggia and Taranto generally fare worse). The deeper story is a
structural Southern/EU gap plus an acute local depopulation and brain-drain
problem.
