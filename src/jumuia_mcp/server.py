"""JumuiaMCP — Kenya Community Finance Tools (5 tools). All data DEMO."""
from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version
from typing import Annotated, Optional

from fastmcp import FastMCP
from pydantic import Field

try:
    _VERSION = _pkg_version("jumuia-mcp")
except PackageNotFoundError:  # a source tree that was never installed
    _VERSION = "0+unknown"


mcp = FastMCP(name="jumuia-mcp", instructions="Kenya SACCO, chama, and cooperative finance tools. DEMO data only.", version=_VERSION)

SACCO_TYPES = {
    "deposit_taking": "DT-SACCO: Regulated by SASRA. Offers savings + loans + mobile banking. Minimum capital KES 25M.",
    "non_deposit": "Non-DT SACCO: Smaller, workplace-based. Regulated by Cooperatives Act.",
    "chama": "Investment group/merry-go-round. Informal. No regulatory body. Members bind by constitution.",
}

@mcp.tool(name="sacco_finder", description="List sample SACCOs (savings and credit cooperatives) in Kenya by sector, with type, sector, a regulation flag and, for some, assets under management. Use when someone asks which SACCOs exist for their sector. Only sector filters the list (matching text, for example teachers or energy); county is only echoed back. Returns the source label, the echoed county and sector, the matching sample_saccos (empty if none match), a pointer to the full SASRA registry and a safety tip. A short hand-written sample labelled DEMO, not the SASRA register: figures are unverified, so check sasra.or.ke before joining. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def sacco_finder(county: str | None = Field(None, description="Kenyan county to search for SACCOs in, e.g. 'Nairobi', 'Mombasa'."), sector: str | None = Field(None, description="SACCO sector, e.g. 'transport', 'teachers', 'farmers'.")) -> dict:
    """Find SACCOs (Savings and Credit Cooperatives) in Kenya by sector, county, or type."""
    SAMPLES = [
        {"name": "Harambee SACCO", "type": "DT-SACCO", "sector": "civil_service", "aum_kes": "47B", "sasra": True},
        {"name": "Mwalimu National SACCO", "type": "DT-SACCO", "sector": "teachers", "aum_kes": "60B", "sasra": True},
        {"name": "Stima SACCO", "type": "DT-SACCO", "sector": "energy", "aum_kes": "25B", "sasra": True},
        {"name": "Kenya Police SACCO", "type": "DT-SACCO", "sector": "police", "aum_kes": "12B", "sasra": True},
        {"name": "Unaitas SACCO", "type": "DT-SACCO", "sector": "general", "county": "Murang'a", "sasra": True},
    ]
    if sector: SAMPLES = [s for s in SAMPLES if sector.lower() in s["sector"]]
    return {"source": "DEMO — sasra.or.ke for full registry", "county": county, "sector": sector,
            "sample_saccos": SAMPLES, "full_registry": "sasra.or.ke — SACCO Societies Regulatory Authority",
            "tip": "Choose SASRA-regulated DT-SACCOs for safety. Check audited accounts before joining."}

@mcp.tool(name="chama_formation_guide", description="Step-by-step guide to forming a chama (investment group) in Kenya: recruiting members, a constitution, a joint account, registration and the first meeting, with the legal structures to choose between. Use when a group asks how to set up and register a chama. members and purpose are only echoed back; the steps are the same for every group. Returns the source label, the echoed inputs, numbered steps and legal_structures with their trade-offs. Indicative fees labelled DEMO: confirm with the Registrar of Societies or the Ministry of Cooperatives. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def chama_formation_guide(members: Annotated[int | None, Field(description="Number of members; only echoed back (default 10).")] = 10, purpose: Annotated[str | None, Field(description="Purpose such as savings; only echoed back.")] = "savings") -> dict:
    """Return step-by-step guide to forming a chama (investment group) in Kenya."""
    return {"source": "DEMO — Ministry of Cooperatives for official guidance", "members": members, "purpose": purpose,
            "steps": ["1. Recruit members (3–50 typical). Define shared goal.",
                      "2. Draft constitution: objectives, contributions, meetings, dispute resolution",
                      "3. Open joint bank account (all signatories or elected officials)",
                      "4. Register: at Registrar of Societies (optional but recommended). Fee: KES 1,000",
                      "5. First meeting: elect officials, set rules, collect first contributions"],
            "legal_structures": {"unregistered_group": "Flexible but no legal standing",
                                  "registered_society": "Legal entity, can own property, KES 1,000 to register",
                                  "limited_company": "Investment company, KES 10,000+ to form"},
            "merry_go_round": f"For {members} members at KES 1,000/meeting: each receives KES {members*1000:,} per cycle"}

@mcp.tool(name="cooperative_benefits", description="Benefits and member obligations of a cooperative type in Kenya: sacco, chama or farmers_coop. Use when someone is deciding whether to join. An unrecognised coop_type returns the SACCO entry and coop_type_applied says so. Returns the source label, coop_type, coop_type_applied, benefits, obligations and the SASRA pointer. Rates quoted are indicative and labelled DEMO: compare actual SACCO and bank terms. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def cooperative_benefits(coop_type: Annotated[str | None, Field(description="sacco (default), chama or farmers_coop.")] = "sacco") -> dict:
    """Return benefits, structures, and types of cooperatives available in Kenya."""
    BENEFITS = {
        "sacco": ["Higher savings rates (8–14%) vs bank (2–4%)", "Loans at 1–1.5% monthly vs banks 15–20% p.a.",
                  "Benevolent fund (death/disability)", "Dividends on shares", "Mobile banking (DT-SACCOs)"],
        "chama":  ["Pooled investment power", "Social accountability", "Access to group loans",
                   "Financial literacy among members"],
        "farmers_coop": ["Bulk input purchases (cheaper)", "Collective bargaining for produce prices",
                         "Storage facilities", "Extension services"],
    }
    OBLIGATIONS = {"sacco": ["Monthly contributions mandatory", "Loan guarantees for members",
                             "Attend AGMs", "Observe by-laws"],
                   "chama": ["Agreed contributions", "Attend meetings", "Honour group loans"]}
    ctype = coop_type.lower()
    return {"source": "DEMO", "coop_type": coop_type,
            "coop_type_applied": ctype if ctype in BENEFITS else "sacco",
            "benefits": BENEFITS.get(ctype, BENEFITS["sacco"]),
            "obligations": OBLIGATIONS.get(ctype, OBLIGATIONS["sacco"]),
            "sasra": "DT-SACCOs regulated by SASRA — sasra.or.ke"}

@mcp.tool(name="sacco_loan_guide", description="Indicative SACCO loan terms by product: development, emergency, school_fees or super_loan, with the borrowing multiple on shares or deposits, the monthly rate, maximum term and what is required. Use when a member asks how much they could borrow or what a loan type costs. An unrecognised loan_type returns the development terms and loan_type_applied says so. Returns the source label, loan_type, loan_type_applied, the sacco filter (echoed) and the terms. Indicative figures labelled DEMO: rates vary by SACCO, so ask the SACCO for its schedule. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def sacco_loan_guide(loan_type: Annotated[str | None, Field(description="development (default), emergency, school_fees or super_loan.")] = "development", sacco_name: str | None = Field(None, description="Optional filter for sacco name. Pass None to return all results.")) -> dict:
    """Return indicative terms for a Kenyan SACCO loan product.

    SACCO lending is priced off a member's shares and deposits rather than a
    credit score, which is why it reaches people banks will not. The multiple
    (typically 3x shares for a development loan) is the number that actually
    determines what someone can borrow, and it is the figure least well
    understood by first-time members.

    Args:
        loan_type: one of "development", "emergency", "school_fees",
            "super_loan". Unrecognised values fall back to "development".
        sacco_name: optional label echoed back in the response; this function
            does not look up a specific SACCO's published rates.

    Returns:
        dict with max_multiple, rate, max_term and product-specific fields,
        plus a `source` marker.

    Note:
        DEMO reference data. Rates and multiples vary materially between SACCOs
        and are revised by each society's board — confirm with the SACCO
        directly or via sasra.or.ke before relying on a figure.
    """
    LOANS = {
        "development": {"max_multiple": "3× shares/deposits", "rate": "1–1.25%/month reducing balance",
                        "max_term": "48 months", "purpose": "Any: housing, education, business, vehicle"},
        "emergency": {"max_multiple": "1× shares", "rate": "1%/month", "max_term": "12 months",
                      "processing": "24–48 hours"},
        "school_fees": {"max_multiple": "2× shares", "rate": "1%/month", "max_term": "12 months",
                        "purpose": "School fees, HELB top-up"},
        "super_loan": {"max_multiple": "5× shares (some SACCOs)", "rate": "1–1.5%/month",
                       "max_term": "60–84 months", "requires": "Property collateral or additional guarantors"},
    }
    lt = loan_type.lower()
    data = LOANS.get(lt, LOANS["development"])
    loan_type_applied = lt if lt in LOANS else "development"
    return {"source": "DEMO — rates vary by SACCO", "loan_type": loan_type, "loan_type_applied": loan_type_applied, "sacco": sacco_name, **data,
            "tip": "Compare: SACCO loans are significantly cheaper than bank personal loans."}

@mcp.tool(name="cooperative_rights_query", description="Rights of a cooperative or SACCO member on a topic such as audit, voting, exit or disputes, including the escalation path to the Cooperative Tribunal and which deposits SASRA protects. Use when a member asks what they can demand or where to complain. Keywords in topic select entries; if none match, ALL rights are returned. Returns the source label, topic, rights, the SASRA pointer and the tribunal. Static summary labelled DEMO and not legal advice: verify with the Commissioner for Cooperatives or an advocate. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def cooperative_rights_query(topic: Annotated[str, Field(description="Topic such as audit, vote, exit or dispute.")]) -> dict:
    """Return the rights a Kenyan cooperative or SACCO member holds on a topic.

    Members frequently do not know that voting is one-member-one-vote regardless
    of shareholding, or that the escalation path for a dispute runs through the
    County Cooperative Director to the Cooperative Tribunal rather than the
    ordinary courts. The deposit-protection distinction matters most: deposit-
    taking SACCOs are covered by SASRA, while non-deposit-taking SACCOs and
    chamas carry no formal protection at all.

    Args:
        topic: free text matched against known areas — audit, vote, exit,
            dispute, information, protection. An unmatched topic returns the
            full set rather than nothing, so a vague question still helps.

    Returns:
        dict with matched rights, plus SASRA and Cooperative Tribunal pointers.

    Note:
        DEMO reference data summarising the Cooperative Societies Act and SASRA
        Act. Not legal advice — for a live dispute, consult an advocate or the
        County Cooperative Director.
    """
    RIGHTS = {
        "audit": "Members have right to audited accounts annually. AGM must present accounts.",
        "vote": "One member one vote regardless of share size.",
        "exit": "Right to withdraw shares with notice period per by-laws (typically 3–6 months).",
        "dispute": "Disputes: internal dispute committee → County Cooperative Director → Cooperative Tribunal.",
        "information": "Right to minutes, financial statements, and by-laws.",
        "protection": "DT-SACCO deposits protected by SASRA. Non-DT/chamas: no formal protection.",
    }
    t = topic.lower()
    matched = {k: v for k, v in RIGHTS.items() if k in t or any(w in t for w in k.split("_"))}
    return {"source": "DEMO — Cooperative Societies Act, SASRA Act", "topic": topic,
            "rights": matched or RIGHTS, "sasra": "sasra.or.ke", "tribunal": "Cooperative Tribunal, Nairobi"}

def main() -> None:
    """Console entry point."""
    mcp.run()
