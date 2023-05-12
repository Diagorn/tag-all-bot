from dto.inside.notification_dto import NotificationDto
from dto.inside.faq_category_container import FaqCategoryContainer
from dto.inside.faq_question_container import FaqQuestionContainer


def transform_notification(dto: NotificationDto):
    return dto.message


def transform_faq_categories(dto: FaqCategoryContainer):
    return 'Список категорий FAQ:\n\n' + '\n'.join(f"{category.id}. {category.text}" for category in dto.categories)


def transform_faq_questions(dto: FaqQuestionContainer):
    return 'Список вопросов по категории:\n\n' + '\n'.join(f"{question.number}. {question.text}" for question in dto.questions)
