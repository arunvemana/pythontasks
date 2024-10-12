import streamlit as st
import altair as alt
from .data import DataProcess,GraphProcess

class Theme:

    def main_view(self, df,_template,_status):
        if _template:
            df = df[df['TMPLT_ID'].isin(_template)]
        if _status:
            df = df[df['STS'].isin(_status)]
        GP = GraphProcess()
        combined_counts,monthly_counts,quarterly_counts = GP.grouping(df)
        # Create the figure and axis
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.Column('month:O',title=None),
            y='count(TICKET_ID):Q',
            color='year:N',
            column=alt.Column('quarter:O', spacing = 5, header = alt.Header(labelOrient = "bottom"))
        )
        st.altair_chart(chart)
        st.dataframe(df)
        st.dataframe(combined_counts)
        st.write("monthly")
        st.dataframe(monthly_counts)
        st.write("Quaterly")
        st.dataframe(quarterly_counts)


    def load_app(self):
        st.sidebar.header("Choose the filter options")
        st.sidebar.write("*************")
        # upload data file
        raw_datasheet = st.sidebar.file_uploader("Upload your Data excel file", type=['xls', 'xlsx'])
        if raw_datasheet:
            with st.spinner("Processing data......."):
                _data_frame = DataProcess(raw_datasheet).process
            st.success("Data processing Successfully")
            # multi select1
            template_filter_values = st.sidebar.multiselect('TemplateID', _data_frame['TMPLT_ID'].unique(), None)
            # multi select2
            status_filter_values = st.sidebar.multiselect('Progress', _data_frame['STS'].unique(), None)
            self.main_view(_data_frame, template_filter_values, status_filter_values)
        else:
            st.error('**Note:** Please upload the Excel file on Sidebar to start process.')
            st.info("If you want sample of Upload datasheet,Please download for structure")
            with open('./resources/test_data.xls','rb') as f:
                file_content = f.read()
            st.download_button(
                label="Download Excel file",
                file_name='Sample_dataSheet.xls',
                data=file_content,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_excel"
            )
        return None
