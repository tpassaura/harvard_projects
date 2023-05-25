from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 48)
        self._pdf.cell(0, 60, "CS50 Shirtificate", ln=True, align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.w - 20)
        self._pdf.set_font_size(25)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")


    def save(self, name):
        self._pdf.output(name)

def main():
    name = input("name: ")
    pdf = PDF(name)
    pdf.save('shirtificate.pdf')



if __name__ == "__main__":
    main()