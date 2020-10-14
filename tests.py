import enrich
import pytest


# print(enrich.enrich("asda", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full"))

def test_us_state_name_abbr_to_full_name():
    assert enrich.enrich("ca", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full") == "california"
    assert enrich.enrich("wa", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full") == "washington"
    assert enrich.enrich("NY", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full") == "new york"
    assert enrich.enrich("nY", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full") == "new york"
    with pytest.raises(KeyError) as excinfo:
        enrich.enrich("n", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full")
        assert "KeyError" in str(excinfo.value)
    with pytest.raises(KeyError) as excinfo:
        enrich.enrich(" ", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full")
        assert "KeyError" in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        enrich.enrich(source_data_type="us_state_name_abbr", target_data_type="us_state_name_full")
        assert "ValueError" in str(excinfo.value)
    


# print(test_us_state_name_abbr_to_full_name())