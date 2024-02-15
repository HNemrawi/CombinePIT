import streamlit as st

# Define your sheet names
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

range_specs = [
#Households with at Least One Adult and One Child
    
    # ES
    ([('Adult-Child', 'D', 16, 24), ('HDX_TOTAL', 'C', 3, 11)], 'All Households', 'B', 3, 11),
    # Gender (adults and children)
    ([('Adult-Child', 'D', 26, 33), ('HDX_TOTAL', 'C', 12, 19)], 'All Households', 'B', 13, 20),
    # More Than One Gender
    ([('Adult-Child', 'D', 35, 41), ('HDX_TOTAL', 'C', 20, 26)], 'All Households', 'B', 22, 28),
    # Race and Ethnicity (adults and children)
    ([('Adult-Child', 'D', 43, 57), ('HDX_TOTAL', 'C', 27, 41)], 'All Households', 'B', 30, 44),
    # Chronically Homeless
    ([('Adult-Child', 'D', 60, 61), ('HDX_TOTAL', 'C', 42, 43)], 'All Households', 'B', 46, 47),
    
    # TH
    ([('Adult-Child', 'E', 16, 24), ('HDX_TOTAL', 'D', 3, 11)], 'All Households', 'C', 3, 11),
    # Gender (adults and children)
    ([('Adult-Child', 'E', 26, 33), ('HDX_TOTAL', 'D', 12, 19)], 'All Households', 'C', 13, 20),
    # More Than One Gender
    ([('Adult-Child', 'E', 35, 41), ('HDX_TOTAL', 'D', 20, 26)], 'All Households', 'C', 22, 28),
    # Race and Ethnicity (adults and children)
    ([('Adult-Child', 'E', 43, 57), ('HDX_TOTAL', 'D', 27, 41)], 'All Households', 'C', 30, 44),
    # Chronically Homeless
    ([('Adult-Child', 'E', 60, 61), ('HDX_TOTAL', 'D', 42, 43)], 'All Households', 'C', 46, 47),
    
    # Unsheltered
    ([('HDX_TOTAL', 'E', 3, 11)], 'All Households', 'D', 3, 11),
    # Gender (adults and children)
    ([('HDX_TOTAL', 'E', 12, 19)], 'All Households', 'D', 13, 20),
    # More Than One Gender
    ([('HDX_TOTAL', 'E', 20, 26)], 'All Households', 'D', 22, 28),
    # Race and Ethnicity (adults and children)
    ([('HDX_TOTAL', 'E', 27, 41)], 'All Households', 'D', 30, 44),
    # Chronically Homeless
    ([('HDX_TOTAL', 'E', 42, 43)], 'All Households', 'D', 46, 47),
    
#Households without Children
    
    # ES
    ([('Without Children', 'C', 12, 19), ('HDX_TOTAL', 'C', 52, 59)], 'All Households', 'B', 53, 60),
    # Gender (adults and children)
    ([('Without Children', 'C', 21, 28), ('HDX_TOTAL', 'C', 60, 67)], 'All Households', 'B', 62, 69),
    # More Than One Gender
    ([('Without Children', 'C', 30, 36), ('HDX_TOTAL', 'C', 68, 74)], 'All Households', 'B', 71, 77),
    # Race and Ethnicity (adults and children)
    ([('Without Children', 'C', 38, 52), ('HDX_TOTAL', 'C', 75, 89)], 'All Households', 'B', 79, 93),
    # Chronically Homeless
    ([('Without Children', 'C', 56, 56), ('HDX_TOTAL', 'C', 90, 90)], 'All Households', 'B', 95, 95),
    
    # TH
    ([('Without Children', 'D', 12, 19), ('HDX_TOTAL', 'D', 52, 59)], 'All Households', 'C', 53, 60),
    # Gender (adults and children)
    ([('Without Children', 'D', 21, 28), ('HDX_TOTAL', 'D', 60, 67)], 'All Households', 'C', 62, 69),
    # More Than One Gender
    ([('Without Children', 'D', 30, 36), ('HDX_TOTAL', 'D', 68, 74)], 'All Households', 'C', 71, 77),
    # Race and Ethnicity (adults and children)
    ([('Without Children', 'D', 38, 52), ('HDX_TOTAL', 'D', 75, 89)], 'All Households', 'C', 79, 93),
    # Chronically Homeless
    ([('Without Children', 'D', 56, 56), ('HDX_TOTAL', 'D', 90, 90)], 'All Households', 'C', 95, 95),
    
    #Unsheltered
    ([('HDX_TOTAL', 'E', 52, 59)], 'All Households', 'D', 53, 60),
    # Gender (adults and children)
    ([('HDX_TOTAL', 'E', 60, 67)], 'All Households', 'D', 62, 69),
    # More Than One Gender
    ([('HDX_TOTAL', 'E', 68, 74)], 'All Households', 'D', 71, 77),
    # Race and Ethnicity (adults and children)
    ([('HDX_TOTAL', 'E', 75, 89)], 'All Households', 'D', 79, 93),
    # Chronically Homeless
    ([('HDX_TOTAL', 'E', 90, 90)], 'All Households', 'D', 95, 95),
    
#Households with only Children
    
    # ES
    ([('Only Children', 'C', 12, 13), ('HDX_TOTAL', 'C', 99, 100)], 'All Households', 'B', 101, 102),
    # Gender (adults and children)
    ([('Only Children', 'C', 15, 22), ('HDX_TOTAL', 'C', 101, 108)], 'All Households', 'B', 104, 111),
    # More Than One Gender
    ([('Only Children', 'C', 24, 30), ('HDX_TOTAL', 'C', 109, 115)], 'All Households', 'B', 113, 119),
    # Race and Ethnicity (adults and children)
    ([('Only Children', 'C', 32, 46), ('HDX_TOTAL', 'C', 116, 130)], 'All Households', 'B', 121, 135),
    # Chronically Homeless
    ([('Only Children', 'C', 49, 49), ('HDX_TOTAL', 'C', 131, 131)], 'All Households', 'B', 137, 137),
    
    # TH
    ([('Only Children', 'D', 12, 13), ('HDX_TOTAL', 'D', 99, 100)], 'All Households', 'C', 101, 102),
    # Gender (adults and children)
    ([('Only Children', 'D', 15, 22), ('HDX_TOTAL', 'D', 101, 108)], 'All Households', 'C', 104, 111),
    # More Than One Gender
    ([('Only Children', 'D', 24, 30), ('HDX_TOTAL', 'D', 109, 115)], 'All Households', 'C', 113, 119),
    # Race and Ethnicity (adults and children)
    ([('Only Children', 'D', 32, 46), ('HDX_TOTAL', 'D', 116, 130)], 'All Households', 'C', 121, 135),
    # Chronically Homeless
    ([('Only Children', 'D', 49, 49), ('HDX_TOTAL', 'D', 131, 131)], 'All Households', 'C', 137, 137),
    
    #Unsheltered
    ([('HDX_TOTAL', 'E', 99, 100)], 'All Households', 'D', 101, 102),
    # Gender (adults and children)
    ([('HDX_TOTAL', 'E', 101, 108)], 'All Households', 'D', 104, 111),
    # More Than One Gender
    ([('HDX_TOTAL', 'E', 109, 115)], 'All Households', 'D', 113, 119),
    # Race and Ethnicity (adults and children)
    ([('HDX_TOTAL', 'E', 116, 130)], 'All Households', 'D', 121, 135),
    # Chronically Homeless
    ([('HDX_TOTAL', 'E', 131, 131)], 'All Households', 'D', 137, 137),
    
#Veteran Households with at Least One Adult and One Child
    
    # ES
    ([('Veteran Adult-Child', 'D', 14, 16), ('HDX_Veterans', 'C', 3, 5)], 'Veteran Households Only', 'B', 3, 5),
    # Gender (adults and children)
    ([('Veteran Adult-Child', 'D', 18, 25), ('HDX_Veterans', 'C', 6, 13)], 'Veteran Households Only', 'B', 7, 14),
    # More Than One Gender
    ([('Veteran Adult-Child', 'D', 27, 33), ('HDX_Veterans', 'C', 14, 20)], 'Veteran Households Only', 'B', 16, 22),
    # Race and Ethnicity (adults and children)
    ([('Veteran Adult-Child', 'D', 35, 49), ('HDX_Veterans', 'C', 21, 35)], 'Veteran Households Only', 'B', 24, 38),
    # Chronically Homeless
    ([('Veteran Adult-Child', 'D', 51, 52), ('HDX_Veterans', 'C', 36, 37)], 'Veteran Households Only', 'B', 40, 41),
    
    # TH
    ([('Veteran Adult-Child', 'E', 14, 16), ('HDX_Veterans', 'D', 3, 5)], 'Veteran Households Only', 'C', 3, 5),
    # Gender (adults and children)
    ([('Veteran Adult-Child', 'E', 18, 25), ('HDX_Veterans', 'D', 6, 13)], 'Veteran Households Only', 'C', 7, 14),
    # More Than One Gender
    ([('Veteran Adult-Child', 'E', 27, 33), ('HDX_Veterans', 'D', 14, 20)], 'Veteran Households Only', 'C', 16, 22),
    # Race and Ethnicity (adults and children)
    ([('Veteran Adult-Child', 'E', 35, 49), ('HDX_Veterans', 'D', 21, 35)], 'Veteran Households Only', 'C', 24, 38),
    # Chronically Homeless
    ([('Veteran Adult-Child', 'E', 51, 52), ('HDX_Veterans', 'D', 36, 37)], 'Veteran Households Only', 'C', 40, 41),
    
    # UNSHELTERED
    ([('HDX_Veterans', 'E', 3, 5)], 'Veteran Households Only', 'D', 3, 5),
    # Gender (adults and children)
    ([('HDX_Veterans', 'E', 6, 13)], 'Veteran Households Only', 'D', 7, 14),
    # More Than One Gender
    ([('HDX_Veterans', 'E', 14, 20)], 'Veteran Households Only', 'D', 16, 22),
    # Race and Ethnicity (adults and children)
    ([('HDX_Veterans', 'E', 21, 35)], 'Veteran Households Only', 'D', 24, 38),
    # Chronically Homeless
    ([('HDX_Veterans', 'E', 36, 37)], 'Veteran Households Only', 'D', 40, 41),
    
#Veteran Households without Children
    
    # ES
    ([('Veteran Without Children', 'C', 12, 14), ('HDX_Veterans', 'C', 46, 48)], 'Veteran Households Only', 'B', 47, 49),
    # Gender (adults and children)
    ([('Veteran Without Children', 'C', 16, 23), ('HDX_Veterans', 'C', 49, 56)], 'Veteran Households Only', 'B', 51, 58),
    # More Than One Gender
    ([('Veteran Without Children', 'C', 25, 31), ('HDX_Veterans', 'C', 57, 63)], 'Veteran Households Only', 'B', 60, 66),
    # Race and Ethnicity (adults and children)
    ([('Veteran Without Children', 'C', 33, 47), ('HDX_Veterans', 'C', 64, 78)], 'Veteran Households Only', 'B', 68, 82),
    # Chronically Homeless
    ([('Veteran Without Children', 'C', 49, 49), ('HDX_Veterans', 'C', 79, 79)], 'Veteran Households Only', 'B', 84, 84),
    
    # TH
    ([('Veteran Without Children', 'D', 12, 14), ('HDX_Veterans', 'D', 46, 48)], 'Veteran Households Only', 'C', 47, 49),
    # Gender (adults and children)
    ([('Veteran Without Children', 'D', 16, 23), ('HDX_Veterans', 'D', 49, 56)], 'Veteran Households Only', 'C', 51, 58),
    # More Than One Gender
    ([('Veteran Without Children', 'D', 25, 31), ('HDX_Veterans', 'D', 57, 63)], 'Veteran Households Only', 'C', 60, 66),
    # Race and Ethnicity (adults and children)
    ([('Veteran Without Children', 'D', 33, 47), ('HDX_Veterans', 'D', 64, 78)], 'Veteran Households Only', 'C', 68, 82),
    # Chronically Homeless
    ([('Veteran Without Children', 'D', 49, 49), ('HDX_Veterans', 'D', 79, 79)], 'Veteran Households Only', 'C', 84, 84),
    
    # UNSHELTERED
    ([('HDX_Veterans', 'E', 46, 48)], 'Veteran Households Only', 'D', 47, 49),
    # Gender (adults and children)
    ([('HDX_Veterans', 'E', 49, 56)], 'Veteran Households Only', 'D', 51, 58),
    # More Than One Gender
    ([('HDX_Veterans', 'E', 57, 63)], 'Veteran Households Only', 'D', 60, 66),
    # Race and Ethnicity (adults and children)
    ([('HDX_Veterans', 'E', 64, 78)], 'Veteran Households Only', 'D', 68, 82),
    # Chronically Homeless
    ([('HDX_Veterans', 'E', 79, 79)], 'Veteran Households Only', 'D', 84, 84),
    
#Unaccompanied Youth Households
    
    # ES
    ([('Unaccompanied Youth', 'C', 14, 17), ('HDX_Youth', 'C', 3, 6)], 'Youth Households', 'B', 3, 6),
    # Gender (adults and children)
    ([('Unaccompanied Youth', 'C', 19, 26), ('HDX_Youth', 'C', 7, 14)], 'Youth Households', 'B', 8, 15),
    # More Than One Gender
    ([('Unaccompanied Youth', 'C', 28, 34), ('HDX_Youth', 'C', 15, 21)], 'Youth Households', 'B', 17, 23),
    # Race and Ethnicity (adults and children)
    ([('Unaccompanied Youth', 'C', 36, 50), ('HDX_Youth', 'C', 22, 36)], 'Youth Households', 'B', 25, 39),
    # Chronically Homeless
    ([('Unaccompanied Youth', 'C', 54, 54), ('HDX_Youth', 'C', 37, 37)], 'Youth Households', 'B', 41, 41),
    
    # TH
    ([('Unaccompanied Youth', 'D', 14, 17), ('HDX_Youth', 'D', 3, 6)], 'Youth Households', 'C', 3, 6),
    # Gender (adults and children)
    ([('Unaccompanied Youth', 'D', 19, 26), ('HDX_Youth', 'D', 7, 14)], 'Youth Households', 'C', 8, 15),
    # More Than One Gender
    ([('Unaccompanied Youth', 'D', 28, 34), ('HDX_Youth', 'D', 15, 21)], 'Youth Households', 'C', 17, 23),
    # Race and Ethnicity (adults and children)
    ([('Unaccompanied Youth', 'D', 36, 50), ('HDX_Youth', 'D', 22, 36)], 'Youth Households', 'C', 25, 39),
    # Chronically Homeless
    ([('Unaccompanied Youth', 'D', 54, 54), ('HDX_Youth', 'D', 37, 37)], 'Youth Households', 'C', 41, 41),
    
    # UNSHELTERED
    ([('HDX_Youth', 'E', 3, 6)], 'Youth Households', 'D', 3, 6),
    # Gender (adults and children)
    ([('HDX_Youth', 'E', 7, 14)], 'Youth Households', 'D', 8, 15),
    # More Than One Gender
    ([('HDX_Youth', 'E', 15, 21)], 'Youth Households', 'D', 17, 23),
    # Race and Ethnicity (adults and children)
    ([('HDX_Youth', 'E', 22, 36)], 'Youth Households', 'D', 25, 39),
    # Chronically Homeless
    ([('HDX_Youth', 'E', 37, 37)], 'Youth Households', 'D', 41, 41),
    
#Parenting Youth Households
    
    # ES
    ([('Parenting Youth', 'D', 12, 19), ('HDX_Youth', 'C', 46, 53)], 'Youth Households', 'B', 47, 54),
    # Gender (adults and children)
    ([('Parenting Youth', 'D', 21, 28), ('HDX_Youth', 'C', 54, 61)], 'Youth Households', 'B', 56, 63),
    # More Than One Gender
    ([('Parenting Youth', 'D', 30, 36), ('HDX_Youth', 'C', 62, 68)], 'Youth Households', 'B', 65, 71),
    # Race and Ethnicity (adults and children)
    ([('Parenting Youth', 'D', 38, 52), ('HDX_Youth', 'C', 69, 83)], 'Youth Households', 'B', 73, 87),
    # Chronically Homeless
    ([('Parenting Youth', 'D', 54, 55), ('HDX_Youth', 'C', 84, 85)], 'Youth Households', 'B', 89, 90),
    
    # TH
    ([('Parenting Youth', 'E', 12, 19), ('HDX_Youth', 'D', 46, 53)], 'Youth Households', 'C', 47, 54),
    # Gender (adults and children)
    ([('Parenting Youth', 'E', 21, 28), ('HDX_Youth', 'D', 54, 61)], 'Youth Households', 'C', 56, 63),
    # More Than One Gender
    ([('Parenting Youth', 'E', 30, 36), ('HDX_Youth', 'D', 62, 68)], 'Youth Households', 'C', 65, 71),
    # Race and Ethnicity (adults and children)
    ([('Parenting Youth', 'E', 38, 52), ('HDX_Youth', 'D', 69, 83)], 'Youth Households', 'C', 73, 87),
    # Chronically Homeless
    ([('Parenting Youth', 'E', 54, 55), ('HDX_Youth', 'D', 84, 85)], 'Youth Households', 'C', 89, 90),
    
    # UNSHELTERED
    ([('HDX_Youth', 'E', 46, 53)], 'Youth Households', 'D', 47, 54),
    # Gender (adults and children)
    ([('HDX_Youth', 'E', 54, 61)], 'Youth Households', 'D', 56, 63),
    # More Than One Gender
    ([('HDX_Youth', 'E', 62, 68)], 'Youth Households', 'D', 65, 71),
    # Race and Ethnicity (adults and children)
    ([('HDX_Youth', 'E', 69, 83)], 'Youth Households', 'D', 73, 87),
    # Chronically Homeless
    ([('HDX_Youth', 'E', 84, 85)], 'Youth Households', 'D', 89, 90),
    
# Additional Homeless Populations
    # ES
    ([('PIT Sub Data', 'C', 12, 15), ('HDX_Subpopulations', 'C', 3, 6)], 'Additional Homeless Populations', 'B', 3, 6),

    # TH
    ([('PIT Sub Data', 'D', 12, 15), ('HDX_Subpopulations', 'D', 3, 6)], 'Additional Homeless Populations', 'C', 3, 6),

    # Unsheltered
    ([('HDX_Subpopulations', 'E', 3, 6)], 'Additional Homeless Populations', 'D', 3, 6),
]

HTML_HEADER_LOGO = """
            <div style="font-style: italic; color: #808080; text-align: left;">
            <a href="https://icalliances.org/" target="_blank"><img src="https://images.squarespace-cdn.com/content/v1/54ca7491e4b000c4d5583d9c/eb7da336-e61c-4e0b-bbb5-1a7b9d45bff6/Dash+Logo+2.png?format=750w" width="250"></a>
            </div>
            """

HTML_HEADER_TITLE = f'<h2 style="color:#00629b; text-align:center;">Point in Time Data Combiner</h2>'

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