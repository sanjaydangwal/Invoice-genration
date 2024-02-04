import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*.xlsx")
for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_no, date = filename.split('-')
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_no}", ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Add header
    columns = [item.replace("_", " ") for item in df.columns]
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Add rows to table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font(family="Times", style="B", size=10)
    pdf.cell(w=30, h=8, txt=f"The Total price is {total_sum}", ln=1)

    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=25, h=8, txt="HowPython", ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
