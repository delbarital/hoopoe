import hoopoe
import pytest
import units_conversion
import pandas as pd

def test_us_state_name_abbr_to_full_name():
    # String tests
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
    
    #df tests
    state_abbr = ["ca", "nm", "nj", "wa", "NY"]
    df = pd.DataFrame(state_abbr, columns={"state_abbr"})    
    target_df = pd.DataFrame()
    target_df['state_abbr'] = state_abbr
    target_df['us_state_name_full'] = ["california", "new mexico", "new jersey", "washington", "new york"]
    assert target_df.equals(hoopoe.enrich(df, source_data_type="us_state_name_abbr", source_data_name="state_abbr", target_data_type="us_state_name_full")) == True 



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