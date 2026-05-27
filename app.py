"""
Is Brindisi really falling behind? A data-driven check.

Streamlit app with two tabs:
  1. Dashboard  - interactive charts comparing Brindisi to its Puglia peers and
                  to the Italy / Mezzogiorno benchmarks.
  2. One-pager  - a written, sourced verdict on the hypothesis.

All figures live in data.py and are traceable to ISTAT / Eurostat / Tagliacarne.
"""

import altair as alt
import pandas as pd
import streamlit as st

import data

st.set_page_config(page_title="Brindisi: falling behind?",
                   page_icon="📉", layout="wide")

SUBJECT = data.SUBJECT
BRINDISI_COLOR = "#d6336c"   # highlight
PROVINCE_COLOR = "#74a9cf"
BENCH_COLOR = "#969696"

meta = data.metric_meta()
cs = data.cross_section_long()


# --------------------------------------------------------------------------- helpers
def colour_scale():
    """Three-way colour: Brindisi highlighted, other provinces, benchmarks."""
    return alt.Color(
        "highlight:N",
        scale=alt.Scale(
            domain=["Brindisi", "Other province", "Benchmark (Puglia / South / Italy)"],
            range=[BRINDISI_COLOR, PROVINCE_COLOR, BENCH_COLOR],
        ),
        legend=alt.Legend(title=None, orient="top"),
    )


def tag(area: str) -> str:
    if area == SUBJECT:
        return "Brindisi"
    if area in data.PROVINCES:
        return "Other province"
    return "Benchmark (Puglia / South / Italy)"


def metric_bar(metric_key: str):
    """Horizontal bar chart for one metric, Brindisi highlighted."""
    m = meta[metric_key]
    d = cs[cs.metric_key == metric_key].dropna(subset=["value"]).copy()
    d["highlight"] = d["area"].map(tag)

    higher_better = m["polarity"] == "higher_better"
    d = d.sort_values("value", ascending=higher_better)

    # number format: no currency symbol inside Altair format strings (kept in titles)
    fmt = ",.0f" if m["unit"].startswith("€") else (".1f" if m["unit"] == "%" else ".1f")
    axis_title = f'{m["label"]} ({m["unit"]})'

    bars = (
        alt.Chart(d)
        .mark_bar()
        .encode(
            x=alt.X("value:Q", title=axis_title),
            y=alt.Y("area:N", sort=list(d["area"]), title=None),
            color=colour_scale(),
            tooltip=[
                alt.Tooltip("area:N", title="Area"),
                alt.Tooltip("value:Q", title=m["label"], format=fmt),
            ],
        )
    )
    labels = bars.mark_text(align="left", dx=3, fontSize=11).encode(
        text=alt.Text("value:Q", format=fmt), color=alt.value("#333")
    )
    return (bars + labels).properties(height=28 * len(d) + 30)


def gap_vs(metric_key: str, ref: str = "Italia"):
    """Brindisi value, reference value, and signed gap (in 'good' direction)."""
    m = meta[metric_key]
    vals = data._CROSS[metric_key]["values"]
    b, r = vals.get(SUBJECT), vals.get(ref)
    if b is None or r is None:
        return None
    diff = b - r
    pct = diff / r * 100 if r else None
    # Is Brindisi better or worse than the reference?
    worse = (diff < 0) if m["polarity"] == "higher_better" else (diff > 0)
    return {"brindisi": b, "ref": r, "diff": diff, "pct": pct,
            "worse": worse, "unit": m["unit"], "label": m["label"], "year": m["year"]}


def fmt_val(v, unit):
    if v is None:
        return "n/a"
    if unit.startswith("€"):
        return f"€{v:,.0f}"
    if unit == "%":
        return f"{v:.1f}%"
    if unit == "years":
        return f"{v:.1f}"
    return f"{v:,.0f}"


# =========================================================================== HEADER
st.title("📉 Is Brindisi really falling behind?")
st.markdown(
    "A data check on the long-standing claim that **Brindisi** is losing ground — "
    "in wealth, jobs, education and population — against comparable Italian towns. "
    "Subject of study: the **city and province of Brindisi (Puglia)**. "
    "Benchmarks: the other five Puglia provinces, the South (*Mezzogiorno*), and Italy."
)

tab_dash, tab_paper = st.tabs(["📊 Dashboard", "📄 One-pager"])

# =========================================================================== DASHBOARD
with tab_dash:
    st.subheader("Brindisi vs the Italian average — headline gaps")
    st.caption("Green/red shows whether Brindisi sits above or below the national figure.")

    kpi_metrics = ["disposable_income", "employment_rate", "graduates", "neet"]
    cols = st.columns(len(kpi_metrics))
    for col, key in zip(cols, kpi_metrics):
        g = gap_vs(key, "Italia")
        if not g:
            continue
        delta = f"{g['diff']:+,.0f}" if g["unit"].startswith("€") else f"{g['diff']:+.1f}"
        delta += "" if g["unit"].startswith("€") else (" pp" if g["unit"] == "%" else "")
        # For "lower is better" metrics, invert the colour meaning so red = bad.
        m = meta[key]
        delta_color = "normal" if m["polarity"] == "higher_better" else "inverse"
        col.metric(
            label=f'{g["label"]} ({g["year"]})',
            value=fmt_val(g["brindisi"], g["unit"]),
            delta=f"{delta} vs Italy ({fmt_val(g['ref'], g['unit'])})",
            delta_color=delta_color,
        )

    st.divider()

    # ---- Metric explorer
    left, right = st.columns([1, 2.4])
    with left:
        st.subheader("Compare a metric")
        labels = {k: meta[k]["label"] for k in data._CROSS}
        choice = st.radio(
            "Pick an indicator", options=list(labels.keys()),
            format_func=lambda k: labels[k], label_visibility="collapsed",
        )
        m = meta[choice]
        arrow = "Higher is better." if m["polarity"] == "higher_better" else "Lower is better."
        st.info(f"**{m['label']}** · {m['unit']} · {m['year']}\n\n{arrow}")
        st.caption(f"Source: {m['source']}")

        g = gap_vs(choice, "Italia")
        if g:
            verdict = "below" if g["worse"] else "at or above"
            st.markdown(
                f"➡️ Brindisi is **{verdict}** the Italian average for this metric "
                f"({fmt_val(g['brindisi'], g['unit'])} vs {fmt_val(g['ref'], g['unit'])})."
            )
    with right:
        st.altair_chart(metric_bar(choice), width="stretch")

    st.divider()

    # ---- Population trends
    st.subheader("The depopulation story")
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("**City of Brindisi — population at each census, 1861-2021**")
        city = data.CITY_CENSUS
        line = (
            alt.Chart(city)
            .mark_area(line={"color": BRINDISI_COLOR}, color=alt.Gradient(
                gradient="linear",
                stops=[alt.GradientStop(color="white", offset=0),
                       alt.GradientStop(color=BRINDISI_COLOR, offset=1)],
                x1=1, x2=1, y1=1, y2=0))
            .encode(
                x=alt.X("year:O", title="Census year",
                        axis=alt.Axis(labelAngle=-45)),
                y=alt.Y("population:Q", title="Residents",
                        scale=alt.Scale(zero=False)),
                tooltip=["year", alt.Tooltip("population:Q", format=",.0f")],
            )
        )
        peak = alt.Chart(pd.DataFrame([data.CITY_PEAK])).mark_point(
            size=90, color=BRINDISI_COLOR, filled=True).encode(x="year:O", y="population:Q")
        st.altair_chart(line + peak, width="stretch")
        st.caption(
            f"Peaked at **{data.CITY_PEAK['population']:,} (1991)**, down to "
            f"**{data.CITY_LATEST['population']:,} (2021)** — −12.6% in 30 years. "
            f"Source: {data.CITY_SOURCE}"
        )

    with c2:
        st.markdown("**Province of Brindisi — resident population, 2001-2024**")
        prov = data.PROVINCE_POP
        pline = (
            alt.Chart(prov)
            .mark_line(point=True, color=BRINDISI_COLOR)
            .encode(
                x=alt.X("year:O", title="Year", axis=alt.Axis(labelAngle=-45,
                        values=list(range(2001, 2025, 2)))),
                y=alt.Y("population:Q", title="Residents", scale=alt.Scale(zero=False)),
                tooltip=["year", alt.Tooltip("population:Q", format=",.0f")],
            )
        )
        st.altair_chart(pline, width="stretch")
        st.caption(
            f"Peaked at **{data.PROVINCE_PEAK['population']:,} (2010)**, down to "
            f"**{data.PROVINCE_LATEST['population']:,} (2024)**. "
            f"Source: {data.PROVINCE_SOURCE}"
        )

    st.markdown(" ")
    st.markdown("**2023 population change — Brindisi is shrinking fastest in Puglia**")
    pc = data.POP_CHANGE_2023.copy()
    pc["highlight"] = pc["area"].map(tag)
    pc_chart = (
        alt.Chart(pc)
        .mark_bar()
        .encode(
            x=alt.X("rate_per_1000:Q", title="Net population change (per 1,000 residents), 2023"),
            y=alt.Y("area:N", sort=list(pc.sort_values("rate_per_1000")["area"]), title=None),
            color=colour_scale(),
            tooltip=["area", alt.Tooltip("rate_per_1000:Q", format=".1f")],
        )
        .properties(height=200)
    )
    st.altair_chart(pc_chart, width="stretch")
    st.caption(data.POP_CHANGE_SOURCE)

    st.divider()

    # ---- EU context + wealth produced
    c3, c4 = st.columns([1.4, 1])
    with c3:
        st.subheader("Puglia in the European league table")
        st.caption("Where the Puglia region (which contains Brindisi) ranks among "
                   "~234 EU NUTS-2 regions. Rank 1 = best.")
        eu = data.EU_RANKING.copy()
        eu["Rank"] = eu.apply(lambda r: f"{r['rank']} / {r['of_total']}", axis=1)
        eu_show = eu.rename(columns={"indicator": "Indicator",
                                     "puglia_value": "Puglia",
                                     "year": "Year"})[["Indicator", "Puglia", "Rank", "Year"]]
        st.dataframe(eu_show, hide_index=True, width="stretch")
        st.caption(data.EU_RANKING_SOURCE)

    with c4:
        st.subheader("Wealth produced per person")
        va = data.VALUE_ADDED
        st.metric(f"Puglia value added per inhabitant ({va['year_region']})",
                  f"€{va['puglia_per_capita']:,}",
                  delta=f"€{va['puglia_per_capita'] - va['italia_per_capita']:+,} vs Italy "
                        f"(€{va['italia_per_capita']:,})",
                  delta_color="normal")
        st.metric(f"Puglia value added per worker ({va['year_region']})",
                  f"€{va['puglia_per_worker']:,}",
                  delta=f"€{va['puglia_per_worker'] - va['italia_per_worker']:+,} vs Italy",
                  delta_color="normal")
        st.caption(
            f"Provincial value added per capita ranges €{va['prov_range_2021'][0]:,}–"
            f"€{va['prov_range_2021'][1]:,} across Puglia. {va['source']}"
        )

    with st.expander("Fertility, ageing & economic structure"):
        dc = data.DEMOG_CONTEXT
        st.markdown(
            f"- **Fertility (2023):** Puglia **{dc['fertility_puglia_2023']}** children per "
            f"woman, ≈ Italy ({dc['fertility_italia_2023']}); range {dc['fertility_range']}.\n"
            f"- **Ageing (2024):** old-age index **{dc['old_age_index_puglia_2024']}** "
            f"over-65s per 100 under-15s (Italy {dc['old_age_index_italia_2024']}); "
            f"range {dc['old_age_index_range']}.\n"
            f"- {data.ECON_STRUCTURE['note']}"
        )
        st.caption(f"{dc['source']} · {data.ECON_STRUCTURE['source']}")

# =========================================================================== ONE-PAGER
with tab_paper:
    st.subheader("One-pager: is Brindisi falling behind?")

    st.markdown("""
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
""")

    st.markdown("#### The evidence, in four lines")
    st.markdown(f"""
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
""")

    st.markdown("#### Where the popular story needs correcting")
    st.markdown("""
- On **jobs**, Brindisi is actually one of Puglia's better provinces: its
  employment rate (57.4%) is **second only to Bari** and above the regional and
  Mezzogiorno averages — though still ~9 points under Italy. The problem is less
  "no jobs" than **low pay, few graduate-level roles, and youth outflow**.
- Brindisi is **not Puglia's poorest** province (Foggia is, on income), nor its
  most jobless (Taranto is). Its distinctive problem is **demographic bleeding** —
  it is shrinking fastest — combined with a thin higher-education pipeline.
""")

    st.markdown("#### Verdict")
    st.success(
        "**Hypothesis: supported, with nuance.** Brindisi is clearly faring worse "
        "than the typical Italian town on wealth, education and especially "
        "population retention, and it is losing people faster than any other "
        "Puglia province. But within its own region it is roughly average — the "
        "deeper story is a structural Southern/EU gap plus an acute local "
        "depopulation and brain-drain problem, not a town uniquely worse than its "
        "immediate neighbours."
    )

    st.markdown("#### Method & caveats")
    st.markdown("""
- **Geographic unit:** economic metrics (income, value added) are only published
  at *province* level, so the province of Brindisi is the unit for those;
  population uses both city and province. Comparators are the five other Puglia
  provinces plus Mezzogiorno and Italy benchmarks.
- **Vintages differ by metric** (2021–2024) — each chart is labelled with its
  year. Figures are taken as published; no estimates were invented to fill gaps
  (missing cells are shown as gaps, not guesses).
""")

    st.markdown("#### Sources")
    for name, url in data.SOURCES:
        st.markdown(f"- [{name}]({url})")

st.divider()
st.caption("Built with Streamlit · All figures traceable to ISTAT, Eurostat and "
           "Centro Studi Tagliacarne. See the One-pager tab for sources.")
