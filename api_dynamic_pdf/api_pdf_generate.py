import fpdf
from fastapi import FastAPI, Response
import uvicorn

app = FastAPI()


@app.get("/download/", response_class=Response)
async def get_download():
    customer = {'name': 'John Doe', 'tax_id': '00-000000-0', 'vat': True}
    items = [
        {'qty': 12, 'description': 'Eggs', 'price': 1.00},
        {'qty': 20, 'description': 'Spam', 'price': 3.00},
        {'qty': 1, 'description': 'Varios', 'price': 0.50},
    ]

    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    with open("simple-csv-invoice.txt") as file:
        for line in file.readlines():
            args = eval(line.strip())
            pdf.text(x=args[0], y=args[1], txt=str(args[2]))

    res = Response(content=pdf.output(dest='S', name="test.pdf").encode('latin-1'),
                   media_type='application/pdf')
    res.headers["Content-Disposition"] = "attachment; filename=test.pdf"
    return res


uvicorn.run(app)
