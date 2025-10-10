from enum import Enum


class InspectionStatuses(str, Enum):
    CREATED = 'Создано'
    ACCEPTED = 'Принято'
    REJECTED = 'Отклонено'
    IN_WORK = 'В работе'


class InspectionTypes(str, Enum):
    SK = 'СК'
    VK = 'ВК'
