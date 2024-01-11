import streamlit as st
from openpyxl import load_workbook
from io import BytesIO
from datetime import datetime
from helpers import *

# Set page configuration
st.set_page_config(page_title="PIT Combiner", page_icon=":house:", layout="wide")


# Function to load and sum the data
def load_and_sum(hmis_stream, non_hmis_stream, range_specs, sheet_names):
    # Load workbooks from file streams
    hmis_wb = load_workbook(filename=BytesIO(hmis_stream.read()))
    non_hmis_wb = load_workbook(filename=BytesIO(non_hmis_stream.read()))
    
    # Use a template file from the local directory
    with open("template.xlsx", "rb") as template_file:
        template_wb = load_workbook(filename=BytesIO(template_file.read()))

    # Processing logic
    for source_ranges, target_sheet_name, target_col, target_start_row, target_end_row in range_specs:
        if target_sheet_name in template_wb.sheetnames:
            output_sheet = template_wb[target_sheet_name]
        else:
            continue

        for row_offset in range(target_end_row - target_start_row + 1):
            sum_value = 0
            for sheet_name, col_prefix, start_row, end_row in source_ranges:
                workbook = hmis_wb if 'HDX' not in sheet_name else non_hmis_wb
                sheet = workbook[sheet_names[sheet_name]]
                row = start_row + row_offset
                if row > end_row:
                    continue
                cell_value = sheet[col_prefix + str(row)].value
                if isinstance(cell_value, (int, float)):
                    sum_value += cell_value

            output_sheet[target_col + str(target_start_row + row_offset)].value = sum_value

    # Save the output to a BytesIO object
    output = BytesIO()
    template_wb.save(output)
    output.seek(0)
    return output

# Streamlit app layout
setup_header()
st.warning("Upload the HMIS and Non-HMIS Excel files")

# File uploaders
hmis_file = st.file_uploader("Upload HMIS Data", type=['xlsx'])
non_hmis_file = st.file_uploader("Upload Non-HMIS Data", type=['xlsx'])

# Button to process files
if st.button("Process Files"):
    if hmis_file and non_hmis_file:
        # Call the processing function
        output_file = load_and_sum(hmis_file, non_hmis_file, range_specs, sheet_names)

        # Convert the BytesIO stream to bytes for download
        output_bytes = output_file.getvalue()

        # Provide a download link for the output
        st.download_button(
            label="Download Output File",
            data=output_bytes,
            file_name=f"combined_data_{datetime.now().strftime('%Y%m%d-%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.error("Please upload both HMIS and Non-HMIS files to proceed.")
    setup_footer()