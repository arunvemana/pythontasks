import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "sucess"}


@app.post('/file/')
async def file_load(document: UploadFile = File(...)):
    data = xls_to_json(document.file, document.filename)

    if data.get("error"):
        raise HTTPException(status_code=data["Status_Code"], detail=data["error"])
    else:
        return data


def _current_or_tier(check: str):
    return True if check.lower() == "current" else False


def xls_to_json(file_data: object, file_name: str)-> {}:
    if file_name.split('.')[-1] in ["xls", "xlsx"]:

        DF = pd.ExcelFile("requirement_source_data.xlsx", engine='openpyxl')
        sheet_columns_Data = {"strategies": [], "productSegment": []}
        for sheet_name in DF.sheet_names:
            sheet_data = pd.read_excel(DF, sheet_name)
            sheet_data.dropna()
            column_names = sheet_data.columns
            sheet_name_split = sheet_name.split(',')

            if sheet_name_split[1].lower() == "current":
                row_values = [i for i in sheet_data[column_names[0]]]
            sheet_names = column_names.tolist()

            data = {}
            key_value: str
            for row_id, row in sheet_data.iterrows():
                if type(row.iloc[0]) is str:
                    data[str(row.iloc[0])] = {}
                    key_value = row.iloc[0]
                else:
                    try:
                        data[row_values[row_id]] = {}
                        key_value = row_values[row_id]
                    except IndexError:
                        break

                for col_name in sheet_names[1:]:
                    if col_name.lower() in ["discount", "industry share (%)"]:
                        data[key_value][col_name] = f'{row.loc[col_name] * 100}%'
                    else:
                        data[key_value][col_name] = f'${str(row.loc[col_name])}'

            if sheet_name_split[0] == "Table3":
                if _current_or_tier(sheet_name_split[1]):
                    sheet_columns_Data['strategies'].append({"current": [{sheet_name: column_names.tolist()}, data]})
                else:
                    sheet_columns_Data['strategies'].append({"tierOne": [{sheet_name: column_names.tolist()}, data]})

            elif sheet_name_split[0] == "Table4":
                if _current_or_tier(sheet_name_split[1]):
                    sheet_columns_Data['productSegment'].append(
                        {"current": [{sheet_name: column_names.tolist()}, data]})
                else:
                    sheet_columns_Data['productSegment'].append(
                        {"tierOne": [{sheet_name: column_names.tolist()}, data]})

            else:
                sheet_columns_Data['Mischievous'].append({"Mischievous": [{sheet_name: column_names.tolist()}, data]})

        return sheet_columns_Data
    else:
        return {"error": "uploded file should be in xls or xlsx", "Status_Code": 400}


uvicorn.run(app)
