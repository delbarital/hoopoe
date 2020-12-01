from .src import hoopoe
import pytest


# print(enrich.enrich("asda", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full"))

def test_us_state_name_abbr_to_full_name():
    assert hoopoe.enrich("ca", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full") == "california"
    assert hoopoe.enrich("wa", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full") == "washington"
    assert hoopoe.enrich("NY", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full") == "new york"
    assert hoopoe.enrich("nY", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full") == "new york"
    with pytest.raises(KeyError) as excinfo:
        hoopoe.enrich("n", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full")
        assert "KeyError" in str(excinfo.value)
    with pytest.raises(KeyError) as excinfo:
        hoopoe.enrich(" ", source_data_type="us_state_name_abbr", target_data_type="us_state_name_full")
        assert "KeyError" in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        hoopoe.enrich(source_data_type="us_state_name_abbr", target_data_type="us_state_name_full")
        assert "ValueError" in str(excinfo.value)
    


# print(test_us_state_name_abbr_to_full_name())