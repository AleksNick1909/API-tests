from enum import Enum


class ParamValueEnum(Enum):
    @property
    def value_hyphen(self):
        """Возвращает значение с заменой _ на -."""
        return self.value.replace('_', '-')


class PrescriptionsType(ParamValueEnum):
    PRESCRIPTION_RD = 'rd_11_04_2006'
    WARNING_STOP_SMR = 'warning_possible_stop_cmp'
    PRESCRIPTION_STOP_SMR = 'prescription_stop_cmp'
    NOTIFICATION_VIOLATIONS = 'notification_of_violations'


class PrescriptionsStatuses(ParamValueEnum):
    CREATED = 'created'
    DONE = 'done'
    REPEATED = 'repeated'
    CHECKED = 'checked'
    REJECTED = 'rejected'
