"""
Is Brindisi really falling behind? A data-driven check (EN / IT).

Three tabs — Dashboard, One-pager, University deep-dive — all driven by a single
language toggle at the top. Numbers live in data.py; every displayed string lives
in lang.py in both English and Italian.
"""

import altair as alt
import pandas as pd
import streamlit as st

import data
import lang

st.set_page_config(page_title="Brindisi: falling behind?",
                   page_icon="📉", layout="wide")

SUBJECT = data.SUBJECT
BRINDISI_COLOR = "#d6336c"
PROVINCE_COLOR = "#74a9cf"
BENCH_COLOR = "#969696"

# --------------------------------------------------------------------------- language toggle
_, lang_col = st.columns([5, 1.3])
with lang_col:
    sel = st.radio("Language / Lingua", list(lang.LANG_OPTIONS),
                   horizontal=True, label_visibility="collapsed", key="lang_sel")
code = lang.LANG_OPTIONS[sel]
S = lang.T[code]
LABELS = lang.METRIC_LABELS[code]

meta = data.metric_meta()
cs = data.cross_section_long()


# --------------------------------------------------------------------------- helpers
def colour_scale():
    tags = lang.TAGS[code]
    return alt.Color(
        "highlight:N",
        scale=alt.Scale(domain=[tags["subject"], tags["province"], tags["bench"]],
                        range=[BRINDISI_COLOR, PROVINCE_COLOR, BENCH_COLOR]),
        legend=alt.Legend(title=None, orient="top"),
    )


def tag(area: str) -> str:
    tags = lang.TAGS[code]
    if area == SUBJECT:
        return tags["subject"]
    if area in data.PROVINCES:
        return tags["province"]
    return tags["bench"]


def metric_bar(metric_key: str):
    m = meta[metric_key]
    d = cs[cs.metric_key == metric_key].dropna(subset=["value"]).copy()
    d["highlight"] = d["area"].map(tag)
    d = d.sort_values("value", ascending=(m["polarity"] == "higher_better"))

    fmt = ",.0f" if m["unit"].startswith("€") else ".1f"
    axis_title = f'{LABELS[metric_key]} ({lang.unit(code, m["unit"])})'
    x = alt.X("value:Q", title=axis_title,
              scale=alt.Scale(domain=[0, float(d["value"].max()) * 1.18]))
    base = alt.Chart(d).encode(y=alt.Y("area:N", sort=list(d["area"]), title=None))
    bars = base.mark_bar().encode(
        x=x, color=colour_scale(),
        tooltip=[alt.Tooltip("area:N", title="Area"),
                 alt.Tooltip("value:Q", title=LABELS[metric_key], format=fmt)],
    )
    labels = base.mark_text(align="left", dx=3, fontSize=11, color="#333").encode(
        x=x, text=alt.Text("value:Q", format=fmt))
    return (bars + labels).properties(height=28 * len(d) + 30)


def gap_vs(metric_key: str, ref: str = "Italia"):
    m = meta[metric_key]
    vals = data._CROSS[metric_key]["values"]
    b, r = vals.get(SUBJECT), vals.get(ref)
    if b is None or r is None:
        return None
    diff = b - r
    worse = (diff < 0) if m["polarity"] == "higher_better" else (diff > 0)
    signed_good = diff if m["polarity"] == "higher_better" else -diff
    return {"brindisi": b, "ref": r, "diff": diff, "signed_good": signed_good,
            "worse": worse, "unit": m["unit"], "year": m["year"]}


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
st.title(S["title"])
st.markdown(S["intro"])

tab_dash, tab_paper, tab_uni = st.tabs([S["tab_dash"], S["tab_paper"], S["tab_uni"]])

# =========================================================================== DASHBOARD
with tab_dash:
    st.subheader(S["kpi_header"])
    st.caption(S["kpi_caption"])

    kpi_metrics = ["disposable_income", "employment_rate", "graduates", "neet"]
    cols = st.columns(len(kpi_metrics))
    for col, key in zip(cols, kpi_metrics):
        g = gap_vs(key, "Italia")
        if not g:
            continue
        sg = g["signed_good"]
        if g["unit"].startswith("€"):
            delta = f"{sg:+,.0f}"
        else:
            delta = f"{sg:+.1f}" + (" pp" if g["unit"] == "%" else "")
        col.metric(
            label=f'{LABELS[key]} ({g["year"]})',
            value=fmt_val(g["brindisi"], g["unit"]),
            delta=f"{delta} {S['vs_country']} ({fmt_val(g['ref'], g['unit'])})",
            delta_color="normal",
        )

    st.divider()

    left, right = st.columns([1, 2.4])
    with left:
        st.subheader(S["compare"])
        choice = st.radio("metric", options=list(data._CROSS),
                          format_func=lambda k: LABELS[k], label_visibility="collapsed")
        m = meta[choice]
        arrow = lang.POLARITY[code][m["polarity"]]
        st.info(f"**{LABELS[choice]}** · {lang.unit(code, m['unit'])} · {m['year']}\n\n{arrow}")
        st.caption(f"{S['source_label']} {m['source']}")
        g = gap_vs(choice, "Italia")
        if g:
            verdict = S["verdict_below"] if g["worse"] else S["verdict_above"]
            st.markdown(S["explorer_verdict"].format(
                verdict=verdict, b=fmt_val(g["brindisi"], g["unit"]),
                r=fmt_val(g["ref"], g["unit"])))
    with right:
        st.altair_chart(metric_bar(choice), width="stretch")

    st.divider()

    st.subheader(S["depop_header"])
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(S["city_title"])
        city = data.CITY_CENSUS
        line = (
            alt.Chart(city).mark_area(
                line={"color": BRINDISI_COLOR},
                color=alt.Gradient(gradient="linear",
                                   stops=[alt.GradientStop(color="white", offset=0),
                                          alt.GradientStop(color=BRINDISI_COLOR, offset=1)],
                                   x1=1, x2=1, y1=1, y2=0))
            .encode(x=alt.X("year:O", title=S["axis_census_year"],
                            axis=alt.Axis(labelAngle=-45)),
                    y=alt.Y("population:Q", title=S["axis_residents"],
                            scale=alt.Scale(zero=False)),
                    tooltip=["year", alt.Tooltip("population:Q", format=",.0f")]))
        peak = alt.Chart(pd.DataFrame([data.CITY_PEAK])).mark_point(
            size=90, color=BRINDISI_COLOR, filled=True).encode(x="year:O", y="population:Q")
        st.altair_chart(line + peak, width="stretch")
        st.caption(S["city_caption"].format(
            peak=f"{data.CITY_PEAK['population']:,}",
            latest=f"{data.CITY_LATEST['population']:,}",
            src_label=S["source_label"], src=S["src_city"]))
    with c2:
        st.markdown(S["prov_title"])
        prov = data.PROVINCE_POP
        pline = (
            alt.Chart(prov).mark_line(point=True, color=BRINDISI_COLOR)
            .encode(x=alt.X("year:O", title=S["axis_year"],
                            axis=alt.Axis(labelAngle=-45, values=list(range(2001, 2025, 2)))),
                    y=alt.Y("population:Q", title=S["axis_residents"],
                            scale=alt.Scale(zero=False)),
                    tooltip=["year", alt.Tooltip("population:Q", format=",.0f")]))
        st.altair_chart(pline, width="stretch")
        st.caption(S["prov_caption"].format(
            peak=f"{data.PROVINCE_PEAK['population']:,}",
            latest=f"{data.PROVINCE_LATEST['population']:,}",
            src_label=S["source_label"], src=S["src_prov"]))

    st.markdown(" ")
    st.markdown(S["popchange_title"])
    pc = data.POP_CHANGE_2023.copy()
    pc["highlight"] = pc["area"].map(tag)
    pc_order = list(pc.sort_values("rate_per_1000")["area"])
    pc_min = float(pc["rate_per_1000"].min())
    pc_x = alt.X("rate_per_1000:Q", title=S["popchange_x"],
                 scale=alt.Scale(domain=[pc_min * 1.25, 0.6]))
    pc_base = alt.Chart(pc).encode(y=alt.Y("area:N", sort=pc_order, title=None))
    pc_bars = pc_base.mark_bar().encode(
        x=pc_x, color=colour_scale(),
        tooltip=["area", alt.Tooltip("rate_per_1000:Q", format=".1f")])
    pc_labels = pc_base.mark_text(align="right", dx=-4, fontSize=11, color="#333").encode(
        x=pc_x, text=alt.Text("rate_per_1000:Q", format=".1f"))
    st.altair_chart((pc_bars + pc_labels).properties(height=200), width="stretch")
    st.caption(S["src_popchange"])

    st.divider()

    c3, c4 = st.columns([1.4, 1])
    with c3:
        st.subheader(S["eu_header"])
        st.caption(S["eu_caption"])
        eu = data.EU_RANKING
        eu_show = pd.DataFrame({
            S["eu_col_indicator"]: lang.EU_INDICATORS[code],
            S["eu_col_puglia"]: lang.EU_VALUES[code],
            S["eu_col_rank"]: [f"{r} / {t}" for r, t in zip(eu["rank"], eu["of_total"])],
            S["eu_col_year"]: list(eu["year"]),
        })
        st.dataframe(eu_show, hide_index=True, width="stretch")
        st.caption(S["src_eu"])
    with c4:
        st.subheader(S["wealth_header"])
        va = data.VALUE_ADDED
        st.metric(S["va_inhab_label"].format(yr=va["year_region"]),
                  f"€{va['puglia_per_capita']:,}",
                  delta=S["va_delta_inhab"].format(
                      diff=va["puglia_per_capita"] - va["italia_per_capita"],
                      ita=va["italia_per_capita"]),
                  delta_color="normal")
        st.metric(S["va_worker_label"].format(yr=va["year_region"]),
                  f"€{va['puglia_per_worker']:,}",
                  delta=S["va_delta_worker"].format(
                      diff=va["puglia_per_worker"] - va["italia_per_worker"]),
                  delta_color="normal")
        st.caption(S["va_caption"].format(
            lo=va["prov_range_2021"][0], hi=va["prov_range_2021"][1], src=S["va_source"]))

    with st.expander(S["expander_title"]):
        dc = data.DEMOG_CONTEXT
        st.markdown(S["demog_md"].format(
            fert=dc["fertility_puglia_2023"], ita=dc["fertility_italia_2023"],
            frange=S["fert_range"], oai=dc["old_age_index_puglia_2024"],
            itaoai=dc["old_age_index_italia_2024"], oairange=S["oai_range"],
            econ=S["econ_note"]))
        st.caption(f"{S['demog_source']} · {S['econ_source']}")

# =========================================================================== ONE-PAGER
with tab_paper:
    st.subheader(S["op_subheader"])
    st.markdown(S["op_intro"])
    st.markdown(S["op_evidence_h"])
    st.markdown(S["op_evidence"])
    st.markdown(S["op_spotlight_h"])
    st.warning(S["op_spotlight_warn"])
    st.markdown(S["op_spotlight"])
    st.markdown(S["op_correct_h"])
    st.markdown(S["op_correct"])
    st.markdown(S["op_verdict_h"])
    st.success(S["op_verdict"])
    st.markdown(S["op_rec_h"])
    st.markdown(S["op_rec_intro"])
    st.markdown(S["op_rec"])
    st.markdown(S["op_method_h"])
    st.markdown(S["op_method"])
    st.markdown(S["op_sources_h"])
    for name, url in data.SOURCES:
        st.markdown(f"- [{name}]({url})")

# =========================================================================== UNIVERSITY
with tab_uni:
    st.subheader(S["dd_subheader"])
    st.markdown(S["dd_intro"])

    ut = data._CROSS["university_transition"]["values"]
    st.info(S["dd_natexp"].format(foggia=ut["Foggia"], brindisi=ut["Brindisi"]))

    for ex in lang.EXAMPLES[code]:
        with st.container(border=True):
            st.markdown(f"### {ex['name']}")
            st.caption(f"📍 {ex['place']}  ·  🗓️ {S['dd_founded_word']} {ex['founded']}  ·  {ex['tag']}")
            st.markdown(f"{S['dd_card_how']} {ex['model']}")
            st.markdown(f"{S['dd_card_what']} {ex['outcome']}")
            st.markdown(f"{S['dd_card_cost']} {ex['cost']}")
            st.markdown(f"{S['dd_card_why']} {ex['why_brindisi']}")
            srcs = "  ·  ".join(f"[{n}]({u})" for n, u in ex["sources"])
            st.caption(f"{S['dd_sources_label']} {srcs}")

    st.markdown(S["dd_teach_h"])
    bc = lang.COURSE[code]
    st.markdown(f"{S['dd_reco_label']} {bc['headline']}")
    for p in bc["pillars"]:
        with st.container(border=True):
            st.markdown(f"**{p['name']}**")
            st.markdown(p["evidence"])
    st.markdown(f"{S['dd_whyfit_label']} {bc['why_it_fits']}")
    st.warning(f"{S['dd_reality_label']} {bc['caveat']}")
    course_srcs = "  ·  ".join(f"[{n}]({u})" for n, u in bc["sources"])
    st.caption(f"{S['dd_sources_label']} {course_srcs}")
    st.success(S["dd_lesson"])

st.divider()
st.caption(S["footer"])
