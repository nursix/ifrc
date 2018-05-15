# -*- coding: utf-8 -*-

from gluon import current

def config(settings):
    """
        Template settings for Myanmar
        - designed to be used in a Cascade with an application template
    """

    #T = current.T

    # Pre-Populate
    settings.base.prepopulate.append("locations/MM")

    # Uncomment to restrict to specific country/countries
    settings.gis.countries.append("MM")

    # L10n (Localization) settings
    settings.L10n.languages["my"] = "Burmese"
    # Default Language (put this in custom template if-required)
    #settings.L10n.default_language = "my"
    # Default timezone for users
    settings.L10n.utc_offset = "+0630"
    # Default Country Code for telephone numbers
    settings.L10n.default_country_code = 95

    settings.fin.currencies["MMK"] = "Myanmar Kyat"
    settings.fin.currency_default = "MMK"

# END =========================================================================
