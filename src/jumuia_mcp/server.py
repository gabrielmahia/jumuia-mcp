"""JumuiaMCP — Kenya Community Finance Tools (5 tools). All data DEMO."""
from __future__ import annotations
from typing import Optional
from fastmcp import FastMCP
mcp = FastMCP(name="jumuia-mcp", description="Kenya SACCO, chama, and cooperative finance tools. DEMO data only.")

SACCO_TYPES = {
    "deposit_taking": "DT-SACCO: Regulated by SASRA. Offers savings + loans + mobile banking. Minimum capital KES 25M.",
    "non_deposit": "Non-DT SACCO: Smaller, workplace-based. Regulated by Cooperatives Act.",
    "chama": "Investment group/merry-go-round. Informal. No regulatory body. Members bind by constitution.",
}

@mcp.tool(name="sacco_finder", description="Find accredited SACCOs in Kenya by county or sector. DEMO.")
def sacco_finder(county: Optional[str] = None, sector: Optional[str] = None) -> dict:
    SAMPLES = [
        {"name": "Harambee SACCO", "type": "DT-SACCO", "sector": "civil_service", "aum_kes": "47B", "sasra": True},
        {"name": "Mwalimu National SACCO", "type": "DT-SACCO", "sector": "teachers", "aum_kes": "60B", "sasra": True},
        {"name": "Stima SACCO", "type": "DT-SACCO", "sector": "energy", "aum_kes": "25B", "sasra": True},
        {"name": "Kenya Police SACCO", "type": "DT-SACCO", "sector": "police", "aum_kes": "12B", "sasra": True},
        {"name": "Unaitas SACCO", "type": "DT-SACCO", "sector": "general", "county": "Murang a", "sasra": True},
    ]
    if sector: SAMPLES = [s for s in SAMPLES if sector.lower() in s["sector"]]
    return {"source": "DEMO — sasra.or.ke for full registry", "county": county, "sector": sector,
            "sample_saccos": SAMPLES, "full_registry": "sasra.or.ke — SACCO Societies Regulatory Authority",
            "tip": "Choose SASRA-regulated DT-SACCOs for safety. Check audited accounts before joining."}

@mcp.tool(name="chama_formation_guide", description="Guide to forming a chama/investment group in Kenya. DEMO.")
def chama_formation_guide(members: Optional[int] = 10, purpose: Optional[str] = "savings") -> dict:
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

@mcp.tool(name="cooperative_benefits", description="Benefits and obligations of Kenya cooperative membership. DEMO.")
def cooperative_benefits(coop_type: Optional[str] = "sacco") -> dict:
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
            "benefits": BENEFITS.get(ctype, BENEFITS["sacco"]),
            "obligations": OBLIGATIONS.get(ctype, OBLIGATIONS["sacco"]),
            "sasra": "DT-SACCOs regulated by SASRA — sasra.or.ke"}

@mcp.tool(name="sacco_loan_guide", description="SACCO loan types, eligibility, and process in Kenya. DEMO.")
def sacco_loan_guide(loan_type: Optional[str] = "development", sacco_name: Optional[str] = None) -> dict:
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
    return {"source": "DEMO — rates vary by SACCO", "loan_type": loan_type, "sacco": sacco_name, **data,
            "tip": "Compare: SACCO loans are significantly cheaper than bank personal loans."}

@mcp.tool(name="cooperative_rights_query", description="Rights and protections for Kenya cooperative members. DEMO.")
def cooperative_rights_query(topic: str) -> dict:
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
