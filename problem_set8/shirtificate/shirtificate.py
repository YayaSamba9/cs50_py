from fpdf import FPDF


class PDF(FPDF):

    def header(self):
        self.set_font("helvetica", "B", 48)
        title = "CS50 Shirtificate"
        title_w = self.get_string_width(title)
        doc_w = self.w

        self.set_x((doc_w - title_w) / 2)
        self.cell(title_w, 20, title, align="C", new_x="LMARGIN", new_y="NEXT")


    def shirt_text(self, name):
        text = f"{name} took CS50"

        self.set_font("helvetica", "B", 24)
        self.set_text_color(255, 255, 255)

        text_w = self.get_string_width(text)
        doc_w = self.w

        self.set_x((doc_w - text_w) / 2)
        self.set_y(140)

        self.cell(text_w, 10, text, align="C")


def main():
    name = input("What's your name? ")

    pdf = PDF()
    pdf.add_page()

    pdf.image("shirtificate.png", x=10, y=60, w=pdf.w - 20)

    pdf.shirt_text(name)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
