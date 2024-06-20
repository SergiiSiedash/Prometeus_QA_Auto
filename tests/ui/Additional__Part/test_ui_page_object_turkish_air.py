from modules.ui.page_objects.Additional_Part_TurkishAir.turkishair_home_page import (
    TurkishAir,
)
import pytest


@pytest.mark.ui_additional
def test_check_incorrect_route_page_object():

    turkish_air_home_page = TurkishAir()

    turkish_air_home_page.go_to()

    turkish_air_home_page.try_to_search_flight("Earth", "Mars")

    # Test to compare text reliability
    r = turkish_air_home_page.check_alert_box()
    assert r == "Error.DepartureNotSelected"

    turkish_air_home_page.close()
