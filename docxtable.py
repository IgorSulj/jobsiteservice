from docx import Document
from fields import Base64ImageStr
from models import Additional, Contacts, Education, Experience, Personal
from models import WorkBlankModel


class Image:
    def __init__(self, base64str: Base64ImageStr) -> None:
        self.data = base64str


TableValue = str | Image
TableRow = tuple[str, TableValue]
TableRows = tuple[TableRow, ...]


class DocxTable:
    def __init__(self, *tables: TableRows) -> None:
        self.tables = tables

    @staticmethod
    def from_blank(blank: WorkBlankModel) -> 'DocxTable':
        return DocxTable(
            get_personal_rows(blank.personal),
            get_contacts_rows(blank.contacts),
            *(get_education_rows(i) for i in blank.education),
            *(get_experience_rows(i) for i in blank.experience),
            get_additional_rows(blank.additional)
        )

    def as_docx_bytes(self):
        raise NotImplementedError()


def get_personal_rows(personal: Personal) -> TableRows:
    return (
        ('Имя на русском', personal.russian_name),
        ('Имя латиницей', personal.english_name),
        ('Семейный статус', personal.family_status.to_human_name()),
        ('День рождения', format(personal.birthday, "%d.%m.%Y")),
        ('Зарплата', str(personal.salary)),
        ('Желаемая работа', personal.wanted_job.to_human_name())
    )


def get_contacts_rows(contacts: Contacts):
    return (
        ('Страна', contacts.country),
        ('Город', contacts.city),
        ('Улица', contacts.street),
        ('Квартира', contacts.flat),
        ('Индекс', contacts.index),
        ('Телефон', contacts.phone),
        ('E-mail', contacts.email)
    )


def get_education_rows(education: Education) -> TableRows:
    return (
        ('Период обучения', f'{education.start}-{education.end}'),
        ('Название ВУЗа', education.name),
        ('Специализация', education.specialization),
        ('Квалификация', education.qualification),
        ('Фото', Image(education.photo))
    )


def get_experience_rows(experience: Experience) -> TableRows:
    return (
        ('Период работы', f'{experience.start}-{experience.end}'),
        ('Организация', experience.organization),
        ('Позиция', experience.position),
        ('Навыки', experience.skills)
    )


def get_additional_rows(additional: Additional) -> TableRows:
    return (
        ('Водительские права', additional.driving_license),
        (
            'Привлекался ли к уголовной ответственности',
            "Да" if additional.had_criminal_liability else "Нет"
        ),
        ('Дополнительно', additional.additional)
    )
