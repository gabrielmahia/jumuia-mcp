from jumuia_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_unknown_loan_and_cooperative_types_say_which_entry_was_applied():
    assert _fn("sacco_loan_guide")("zzz", None)["loan_type_applied"] == "development"
    assert _fn("sacco_loan_guide")("emergency", None)["loan_type_applied"] == "emergency"
    assert _fn("cooperative_benefits")("zzz")["coop_type_applied"] == "sacco"
    assert _fn("cooperative_benefits")("chama")["coop_type_applied"] == "chama"
