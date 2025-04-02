from metrics import ratios, names

class BalkConverter:

    def convert(value: float, unit_from: str, unit_to: str) -> tuple[float, str]:
        '''
        принемает параметры:
           value - значение
           unit_from - из чего перевести
           unit_to - во что перевести

        возвращает кортеж:
           индекс 0: значение
           индект 1: родовой падеж названия измерения во множественном числе
        '''

        if (unit_from not in ratios.keys() or
            unit_to   not in ratios.keys()):
            raise 'Ошибка: параметр "unit_from" или "unit_to" не были найдены. Убедись, что передаешь параметры, которые есть в ключах словаря "ratios"'

        return (value * ratios[unit_from] / ratios[unit_to], names[unit_to])