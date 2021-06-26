from fpdf import FPDF
from PIL import Image
from typing import NoReturn
from pathlib import Path

full_path = lambda x: Path(x).absolute()  # ignored: PEP8 standard # noqa


class Report(FPDF):
    """
    Functionality:
    Generation of graph for the given graph
       :PDF:
    orient: Landscape
    measurement: pt
    Paper size: A4
    """

    def __init__(self):
        super(Report, self).__init__('l', "pt", 'A4')
        self.set_font('helvetica', size=12)
        self.line_height = 20
        self.t_margin = 50

    def cover_page(self) -> NoReturn:
        """
        Generation of the cover page with report title
        :return: None
        """
        self.add_page()
        self.set_font_size(30)
        self.set_text_color(255, 0, 0)
        self.set_y(int(self.h / 2))
        self.set_x(self.l_margin + self.r_margin)
        self.cell(0, self.line_height, 'Report on Emission Data', align='C',
                  ln=2)

    def header(self) -> NoReturn:
        """
        For every new page header will execute for the common header
        :return: None
        """
        self.set_x(self.t_margin + self.b_margin)
        self.ln(self.line_height)

    def graphs(self, title: str, graph_name: str) -> NoReturn:
        """
        Generation of the grpah page,
        with the title and graph image.

        :param title: str
        :param graph_name: str
        :return: None
        """
        self.add_page()
        self.set_text_color(0, 250, 154)
        self.cell(0, 0, title, align='C', ln=2)
        self.ln(self.line_height)
        img = Image.open(full_path(f'./output/{graph_name}'))
        image_width = self.w - (self.l_margin + self.r_margin)
        image_height = self.h - (self.t_margin + self.b_margin + self.get_y())
        self.image(img, self.get_x(), self.get_y(), w=image_width,
                   h=image_height)
