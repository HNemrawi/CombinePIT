import streamlit as st

# Mapping of keys to their corresponding worksheet names
sheet_names = {
    'Adult-Child': 'Adult-Child',
    'Without Children': 'Without Children',
    'Only Children': 'Only Children',
    'Veteran Adult-Child': 'Veteran Adult-Child',
    'Veteran Without Children': 'Veteran Without Children',
    'Unaccompanied Youth': 'Unaccompanied Youth',
    'Parenting Youth': 'Parenting Youth',
    'PIT Sub Data': 'PIT Sub Data',
    'HDX_TOTAL': 'HDX_TOTAL',
    'HDX_Veterans': 'HDX_Veterans',
    'HDX_Youth': 'HDX_Youth',
    'HDX_Subpopulations': 'HDX_Subpopulations',
    'All Households': 'All Households',
    'Veteran Households Only': 'Veteran Households Only',
    'Youth Households': 'Youth Households',
    'Additional Homeless Populations': 'Additional Homeless Populations'
}

# Specifications for which data ranges to sum from the HMIS/Non-HMIS workbooks
range_specs = [
    # Households with at Least One Adult and One Child
    ([('Adult-Child', 'D', 17, 25), ('HDX_TOTAL', 'C', 3, 11)], 'All Households', 'B', 3, 11),
    ([('Adult-Child', 'D', 27, 34), ('HDX_TOTAL', 'C', 12, 19)], 'All Households', 'B', 13, 20),
    ([('Adult-Child', 'D', 36, 42), ('HDX_TOTAL', 'C', 20, 26)], 'All Households', 'B', 22, 28),
    ([('Adult-Child', 'D', 44, 58), ('HDX_TOTAL', 'C', 27, 41)], 'All Households', 'B', 30, 44),
    ([('Adult-Child', 'D', 60, 61), ('HDX_TOTAL', 'C', 42, 43)], 'All Households', 'B', 46, 47),

    ([('Adult-Child', 'E', 17, 25), ('HDX_TOTAL', 'D', 3, 11)], 'All Households', 'C', 3, 11),
    ([('Adult-Child', 'E', 27, 34), ('HDX_TOTAL', 'D', 12, 19)], 'All Households', 'C', 13, 20),
    ([('Adult-Child', 'E', 36, 42), ('HDX_TOTAL', 'D', 20, 26)], 'All Households', 'C', 22, 28),
    ([('Adult-Child', 'E', 44, 58), ('HDX_TOTAL', 'D', 27, 41)], 'All Households', 'C', 30, 44),
    ([('Adult-Child', 'E', 60, 61), ('HDX_TOTAL', 'D', 42, 43)], 'All Households', 'C', 46, 47),

    ([('HDX_TOTAL', 'E', 3, 11)], 'All Households', 'D', 3, 11),
    ([('HDX_TOTAL', 'E', 12, 19)], 'All Households', 'D', 13, 20),
    ([('HDX_TOTAL', 'E', 20, 26)], 'All Households', 'D', 22, 28),
    ([('HDX_TOTAL', 'E', 27, 41)], 'All Households', 'D', 30, 44),
    ([('HDX_TOTAL', 'E', 42, 43)], 'All Households', 'D', 46, 47),

    # Households without Children
    ([('Without Children', 'C', 13, 20), ('HDX_TOTAL', 'C', 52, 59)], 'All Households', 'B', 53, 60),
    ([('Without Children', 'C', 22, 29), ('HDX_TOTAL', 'C', 60, 67)], 'All Households', 'B', 62, 69),
    ([('Without Children', 'C', 31, 37), ('HDX_TOTAL', 'C', 68, 74)], 'All Households', 'B', 71, 77),
    ([('Without Children', 'C', 39, 53), ('HDX_TOTAL', 'C', 75, 89)], 'All Households', 'B', 79, 93),
    ([('Without Children', 'C', 55, 55), ('HDX_TOTAL', 'C', 90, 90)], 'All Households', 'B', 95, 95),

    ([('Without Children', 'D', 13, 20), ('HDX_TOTAL', 'D', 52, 59)], 'All Households', 'C', 53, 60),
    ([('Without Children', 'D', 22, 29), ('HDX_TOTAL', 'D', 60, 67)], 'All Households', 'C', 62, 69),
    ([('Without Children', 'D', 31, 37), ('HDX_TOTAL', 'D', 68, 74)], 'All Households', 'C', 71, 77),
    ([('Without Children', 'D', 39, 53), ('HDX_TOTAL', 'D', 75, 89)], 'All Households', 'C', 79, 93),
    ([('Without Children', 'D', 55, 55), ('HDX_TOTAL', 'D', 90, 90)], 'All Households', 'C', 95, 95),

    ([('HDX_TOTAL', 'E', 52, 59)], 'All Households', 'D', 53, 60),
    ([('HDX_TOTAL', 'E', 60, 67)], 'All Households', 'D', 62, 69),
    ([('HDX_TOTAL', 'E', 68, 74)], 'All Households', 'D', 71, 77),
    ([('HDX_TOTAL', 'E', 75, 89)], 'All Households', 'D', 79, 93),
    ([('HDX_TOTAL', 'E', 90, 90)], 'All Households', 'D', 95, 95),

    # Households with only Children
    ([('Only Children', 'C', 13, 14), ('HDX_TOTAL', 'C', 99, 100)], 'All Households', 'B', 101, 102),
    ([('Only Children', 'C', 16, 23), ('HDX_TOTAL', 'C', 101, 108)], 'All Households', 'B', 104, 111),
    ([('Only Children', 'C', 25, 31), ('HDX_TOTAL', 'C', 109, 115)], 'All Households', 'B', 113, 119),
    ([('Only Children', 'C', 33, 47), ('HDX_TOTAL', 'C', 116, 130)], 'All Households', 'B', 121, 135),
    ([('Only Children', 'C', 49, 49), ('HDX_TOTAL', 'C', 131, 131)], 'All Households', 'B', 137, 137),

    ([('Only Children', 'D', 13, 14), ('HDX_TOTAL', 'D', 99, 100)], 'All Households', 'C', 101, 102),
    ([('Only Children', 'D', 16, 23), ('HDX_TOTAL', 'D', 101, 108)], 'All Households', 'C', 104, 111),
    ([('Only Children', 'D', 25, 31), ('HDX_TOTAL', 'D', 109, 115)], 'All Households', 'C', 113, 119),
    ([('Only Children', 'D', 33, 47), ('HDX_TOTAL', 'D', 116, 130)], 'All Households', 'C', 121, 135),
    ([('Only Children', 'D', 49, 49), ('HDX_TOTAL', 'D', 131, 131)], 'All Households', 'C', 137, 137),

    ([('HDX_TOTAL', 'E', 99, 100)], 'All Households', 'D', 101, 102),
    ([('HDX_TOTAL', 'E', 101, 108)], 'All Households', 'D', 104, 111),
    ([('HDX_TOTAL', 'E', 109, 115)], 'All Households', 'D', 113, 119),
    ([('HDX_TOTAL', 'E', 116, 130)], 'All Households', 'D', 121, 135),
    ([('HDX_TOTAL', 'E', 131, 131)], 'All Households', 'D', 137, 137),

    # Veteran Households with at Least One Adult and One Child
    ([('Veteran Adult-Child', 'D', 15, 17), ('HDX_Veterans', 'C', 3, 5)], 'Veteran Households Only', 'B', 3, 5),
    ([('Veteran Adult-Child', 'D', 19, 26), ('HDX_Veterans', 'C', 6, 13)], 'Veteran Households Only', 'B', 7, 14),
    ([('Veteran Adult-Child', 'D', 28, 34), ('HDX_Veterans', 'C', 14, 20)], 'Veteran Households Only', 'B', 16, 22),
    ([('Veteran Adult-Child', 'D', 36, 50), ('HDX_Veterans', 'C', 21, 35)], 'Veteran Households Only', 'B', 24, 38),
    ([('Veteran Adult-Child', 'D', 52, 53), ('HDX_Veterans', 'C', 36, 37)], 'Veteran Households Only', 'B', 40, 41),

    ([('Veteran Adult-Child', 'E', 15, 17), ('HDX_Veterans', 'D', 3, 5)], 'Veteran Households Only', 'C', 3, 5),
    ([('Veteran Adult-Child', 'E', 19, 26), ('HDX_Veterans', 'D', 6, 13)], 'Veteran Households Only', 'C', 7, 14),
    ([('Veteran Adult-Child', 'E', 28, 34), ('HDX_Veterans', 'D', 14, 20)], 'Veteran Households Only', 'C', 16, 22),
    ([('Veteran Adult-Child', 'E', 36, 50), ('HDX_Veterans', 'D', 21, 35)], 'Veteran Households Only', 'C', 24, 38),
    ([('Veteran Adult-Child', 'E', 52, 53), ('HDX_Veterans', 'D', 36, 37)], 'Veteran Households Only', 'C', 40, 41),

    ([('HDX_Veterans', 'E', 3, 5)], 'Veteran Households Only', 'D', 3, 5),
    ([('HDX_Veterans', 'E', 6, 13)], 'Veteran Households Only', 'D', 7, 14),
    ([('HDX_Veterans', 'E', 14, 20)], 'Veteran Households Only', 'D', 16, 22),
    ([('HDX_Veterans', 'E', 21, 35)], 'Veteran Households Only', 'D', 24, 38),
    ([('HDX_Veterans', 'E', 36, 37)], 'Veteran Households Only', 'D', 40, 41),

    # Veteran Households without Children
    ([('Veteran Without Children', 'C', 13, 15), ('HDX_Veterans', 'C', 46, 48)], 'Veteran Households Only', 'B', 47, 49),
    ([('Veteran Without Children', 'C', 17, 24), ('HDX_Veterans', 'C', 49, 56)], 'Veteran Households Only', 'B', 51, 58),
    ([('Veteran Without Children', 'C', 26, 32), ('HDX_Veterans', 'C', 57, 63)], 'Veteran Households Only', 'B', 60, 66),
    ([('Veteran Without Children', 'C', 34, 48), ('HDX_Veterans', 'C', 64, 78)], 'Veteran Households Only', 'B', 68, 82),
    ([('Veteran Without Children', 'C', 50, 50), ('HDX_Veterans', 'C', 79, 79)], 'Veteran Households Only', 'B', 84, 84),

    ([('Veteran Without Children', 'D', 13, 15), ('HDX_Veterans', 'D', 46, 48)], 'Veteran Households Only', 'C', 47, 49),
    ([('Veteran Without Children', 'D', 17, 24), ('HDX_Veterans', 'D', 49, 56)], 'Veteran Households Only', 'C', 51, 58),
    ([('Veteran Without Children', 'D', 26, 32), ('HDX_Veterans', 'D', 57, 63)], 'Veteran Households Only', 'C', 60, 66),
    ([('Veteran Without Children', 'D', 34, 48), ('HDX_Veterans', 'D', 64, 78)], 'Veteran Households Only', 'C', 68, 82),
    ([('Veteran Without Children', 'D', 50, 50), ('HDX_Veterans', 'D', 79, 79)], 'Veteran Households Only', 'C', 84, 84),

    ([('HDX_Veterans', 'E', 46, 48)], 'Veteran Households Only', 'D', 47, 49),
    ([('HDX_Veterans', 'E', 49, 56)], 'Veteran Households Only', 'D', 51, 58),
    ([('HDX_Veterans', 'E', 57, 63)], 'Veteran Households Only', 'D', 60, 66),
    ([('HDX_Veterans', 'E', 64, 78)], 'Veteran Households Only', 'D', 68, 82),
    ([('HDX_Veterans', 'E', 79, 79)], 'Veteran Households Only', 'D', 84, 84),

    # Unaccompanied Youth Households
    ([('Unaccompanied Youth', 'C', 15, 18), ('HDX_Youth', 'C', 3, 6)], 'Youth Households', 'B', 3, 6),
    ([('Unaccompanied Youth', 'C', 20, 27), ('HDX_Youth', 'C', 7, 14)], 'Youth Households', 'B', 8, 15),
    ([('Unaccompanied Youth', 'C', 29, 35), ('HDX_Youth', 'C', 15, 21)], 'Youth Households', 'B', 17, 23),
    ([('Unaccompanied Youth', 'C', 37, 51), ('HDX_Youth', 'C', 22, 36)], 'Youth Households', 'B', 25, 39),
    ([('Unaccompanied Youth', 'C', 53, 53), ('HDX_Youth', 'C', 37, 37)], 'Youth Households', 'B', 41, 41),

    ([('Unaccompanied Youth', 'D', 15, 18), ('HDX_Youth', 'D', 3, 6)], 'Youth Households', 'C', 3, 6),
    ([('Unaccompanied Youth', 'D', 20, 27), ('HDX_Youth', 'D', 7, 14)], 'Youth Households', 'C', 8, 15),
    ([('Unaccompanied Youth', 'D', 29, 35), ('HDX_Youth', 'D', 15, 21)], 'Youth Households', 'C', 17, 23),
    ([('Unaccompanied Youth', 'D', 37, 51), ('HDX_Youth', 'D', 22, 36)], 'Youth Households', 'C', 25, 39),
    ([('Unaccompanied Youth', 'D', 53, 53), ('HDX_Youth', 'D', 37, 37)], 'Youth Households', 'C', 41, 41),

    ([('HDX_Youth', 'E', 3, 6)], 'Youth Households', 'D', 3, 6),
    ([('HDX_Youth', 'E', 7, 14)], 'Youth Households', 'D', 8, 15),
    ([('HDX_Youth', 'E', 15, 21)], 'Youth Households', 'D', 17, 23),
    ([('HDX_Youth', 'E', 22, 36)], 'Youth Households', 'D', 25, 39),
    ([('HDX_Youth', 'E', 37, 37)], 'Youth Households', 'D', 41, 41),

    # Parenting Youth Households
    ([('Parenting Youth', 'D', 13, 20), ('HDX_Youth', 'C', 46, 53)], 'Youth Households', 'B', 47, 54),
    ([('Parenting Youth', 'D', 22, 29), ('HDX_Youth', 'C', 54, 61)], 'Youth Households', 'B', 56, 63),
    ([('Parenting Youth', 'D', 31, 37), ('HDX_Youth', 'C', 62, 68)], 'Youth Households', 'B', 65, 71),
    ([('Parenting Youth', 'D', 39, 51), ('HDX_Youth', 'C', 69, 83)], 'Youth Households', 'B', 73, 87),
    ([('Parenting Youth', 'D', 55, 56), ('HDX_Youth', 'C', 84, 85)], 'Youth Households', 'B', 89, 90),

    ([('Parenting Youth', 'E', 13, 20), ('HDX_Youth', 'D', 46, 53)], 'Youth Households', 'C', 47, 54),
    ([('Parenting Youth', 'E', 22, 29), ('HDX_Youth', 'D', 54, 61)], 'Youth Households', 'C', 56, 63),
    ([('Parenting Youth', 'E', 31, 37), ('HDX_Youth', 'D', 62, 68)], 'Youth Households', 'C', 65, 71),
    ([('Parenting Youth', 'E', 39, 53), ('HDX_Youth', 'D', 69, 83)], 'Youth Households', 'C', 73, 87),
    ([('Parenting Youth', 'E', 55, 56), ('HDX_Youth', 'D', 84, 85)], 'Youth Households', 'C', 89, 90),

    ([('HDX_Youth', 'E', 46, 53)], 'Youth Households', 'D', 47, 54),
    ([('HDX_Youth', 'E', 54, 61)], 'Youth Households', 'D', 56, 63),
    ([('HDX_Youth', 'E', 62, 68)], 'Youth Households', 'D', 65, 71),
    ([('HDX_Youth', 'E', 69, 83)], 'Youth Households', 'D', 73, 87),
    ([('HDX_Youth', 'E', 84, 85)], 'Youth Households', 'D', 89, 90),

    # Additional Homeless Populations
    ([('PIT Sub Data', 'C', 13, 16), ('HDX_Subpopulations', 'C', 3, 6)], 'Additional Homeless Populations', 'B', 3, 6),
    ([('PIT Sub Data', 'D', 13, 16), ('HDX_Subpopulations', 'D', 3, 6)], 'Additional Homeless Populations', 'C', 3, 6),
    ([('HDX_Subpopulations', 'E', 3, 6)], 'Additional Homeless Populations', 'D', 3, 6),
]


HTML_HEADER_LOGO = """
<div style="font-style: italic; color: #808080; text-align: left;">
    <a href="https://icalliances.org/" target="_blank">
        <img src="https://images.squarespace-cdn.com/content/v1/54ca7491e4b000c4d5583d9c/eb7da336-e61c-4e0b-bbb5-1a7b9d45bff6/Dash+Logo+2.png?format=750w" width="250">
    </a>
</div>
"""

HTML_HEADER_TITLE = '<h2 style="color:#00629b; text-align:center;">Point in Time Data Combiner</h2>'

HTML_FOOTER = """
<div style="font-style: italic; color: #808080; text-align: center;">
    <a href="https://icalliances.org/" target="_blank">
        <img src="https://images.squarespace-cdn.com/content/v1/54ca7491e4b000c4d5583d9c/eb7da336-e61c-4e0b-bbb5-1a7b9d45bff6/Dash+Logo+2.png?format=750w" width="99">
    </a>
    DASH™ is a trademark of Institute for Community Alliances.
</div>
<div style="font-style: italic; color: #808080; text-align: center;">
    <a href="https://icalliances.org/" target="_blank">
        <img src="https://images.squarespace-cdn.com/content/v1/54ca7491e4b000c4d5583d9c/1475614371395-KFTYP42QLJN0VD5V9VB1/ICA+Official+Logo+PNG+%28transparent%29.png?format=1500w" width="99">
    </a>
    © 2024 Institute for Community Alliances (ICA). All rights reserved.
</div>
"""

def setup_header():
    """Set up the header of the Streamlit page."""
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(HTML_HEADER_LOGO, unsafe_allow_html=True)
    with col2:
        st.markdown(HTML_HEADER_TITLE, unsafe_allow_html=True)

def setup_footer():
    """Set up the footer of the Streamlit page."""
    st.markdown(HTML_FOOTER, unsafe_allow_html=True)
