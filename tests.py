import hoopoe
import pytest

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
    

def test_us_state_full_name_to_state_abbr():
    assert hoopoe.enrich("california", source_data_type="us_state_name_full", target_data_type="us_state_name_abbr") == "ca"
    assert hoopoe.enrich("washington", source_data_type="us_state_name_full", target_data_type="us_state_name_abbr") == "wa"
    assert hoopoe.enrich("New-york", source_data_type="us_state_name_full", target_data_type="us_state_name_abbr") == "ny"
    assert hoopoe.enrich("NEW jersey", source_data_type="us_state_name_full", target_data_type="us_state_name_abbr") == "nj"
    assert hoopoe.enrich("TEXAS", source_data_type="us_state_name_full", target_data_type="us_state_name_abbr") == "tx"
    assert hoopoe.enrich("NORTH CAROLINA", source_data_type="us_state_name_full", target_data_type="us_state_name_abbr") == "nc"

    with pytest.raises(KeyError) as excinfo:
        hoopoe.enrich("n", source_data_type="us_state_name_full", target_data_type="us_state_name_abbr")
        assert "KeyError" in str(excinfo.value)
    with pytest.raises(KeyError) as excinfo:
        hoopoe.enrich(" ", source_data_type="us_state_name_name", target_data_type="us_state_name_abbr")
        assert "KeyError" in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        hoopoe.enrich(source_data_type="us_state_name_name", target_data_type="us_state_name_abbr")
        assert "ValueError" in str(excinfo.value)

# print(test_us_state_name_abbr_to_full_name())