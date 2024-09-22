import bs4.element
from bs4 import BeautifulSoup
import requests
from pydantic import BaseModel
from typing import List, Dict

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors, fonts
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak


class SyllabusData(BaseModel):
    data: Dict[str, List[str]]  # dynamic keys with list of values.


class Syllabus:
    def __init__(self):
        self.url: str = "https://pythonlife.in/python-course-in-telugu.html"
        self.pdf_file: str = 'syllabus.pdf'
        self.styles = getSampleStyleSheet()

    @staticmethod
    def parse_data(data: bytes) -> BeautifulSoup:
        return BeautifulSoup(data, 'html.parser')

    def raw_data(self) -> bytes | bool:
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        return False

    @staticmethod
    def data_clean(raw_data: str | bs4.element.Tag) -> str:
        if isinstance(raw_data, str):
            _data = raw_data.strip()
        else:
            _data = raw_data.get_text(strip=True)
        return _data

    def extract_sub_topic(self, data: SyllabusData, topic: str, ul: BeautifulSoup, recurise=False):
        for li in ul.find_all('li', recurise=False):  # only immediate Childern
            if not recurise:
                data.data.setdefault(topic, []).append(self.data_clean(li.contents[0]))
            else:
                data.data.setdefault(topic, []).append('->' + self.data_clean(li.contents[0]))
            nested_li = li.find('ul')
            if nested_li:
                self.extract_sub_topic(data, topic, li, recurise=True)

    def extract_data(self, data: BeautifulSoup) -> dict:
        model = SyllabusData(data={})
        table = data.find(id='accordionExample')
        _syllabus: dict = dict()
        for item in table.find_all(class_='accordion-item'):
            topic = self.data_clean(item.find('h2').text)
            topics = item.find('div', class_='accordion-body')
            if topic:
                if topics and topics.find('p'):
                    model.data[topic] = [self.data_clean(topics.text)]
                if topics and topics.find('ul'):
                    self.extract_sub_topic(model, topic, topics)

        return model

    @staticmethod
    def custom_add_or_delete(data: SyllabusData):
        data.data.pop('React JS Library', None)
        data.data.setdefault('FastAPI', []).extend(
            ['Overview of FastAPI', 'Basic Application Structure', 'Path and Query Parameters',
             'Request Body and Data Models',
             'Response Handling', 'Background Tasks and Middleware', 'Sample project'])
        data.data.pop('Django for Python Developer', None)

    def generate_pdf(self, data: SyllabusData):
        document = SimpleDocTemplate(self.pdf_file, pagesize=A4)
        fonts.addMapping('Courier', 0, 0, 'Courier')  # normal
        fonts.addMapping('Courier', 0, 1, 'Courier-Bold')  # Bold
        header_style = ParagraphStyle('HeaderStyle', parent=self.styles['Heading1'], alignment=1, fontsize=14,
                                      fontName='Courier', spaceAfter=20, textColor=colors.blue)
        main_topic_style = ParagraphStyle('MainTopic', parent=self.styles['Heading1'], fontName='Courier')
        subtopic_style = ParagraphStyle('subtopicStyle', parent=self.styles['BodyText'], fontName='Courier')
        sub_subtopic_style = ParagraphStyle('SubSubTopicStyle', parent=subtopic_style, leftIndent=20)

        content = []
        content.append(Paragraph('Python Course Syllabus', header_style))
        for main_topic, subtopics in data.data.items():
            content.append(Paragraph(main_topic, main_topic_style))
            content.append(Spacer(1, 12))  # adding the space after the main Topic

            # Add Subtopics
            for subtopic in subtopics:
                if subtopic.startswith('->'):
                    content.append(Paragraph(f"    • {subtopic.replace('->', '')}", sub_subtopic_style))
                else:
                    content.append(Paragraph(f"• {subtopic}", subtopic_style))
                content.append(Spacer(1, 6))
            content.append(Spacer(1, 10))

        document.build(content)

    def let_generate(self):
        # first
        data = self.raw_data()
        if data:
            data = self.parse_data(data)
            table = self.extract_data(data)
            self.custom_add_or_delete(table)
            self.generate_pdf(table)


a = Syllabus()
a.let_generate()
