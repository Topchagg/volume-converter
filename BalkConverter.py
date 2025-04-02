class BalkConverter:
    # ключь: название измерения
    # значение: сколько кубичных метров в единице данного измерения
    ratios = {
        'mm^3': 1e-9,       # кубический миллиметр
        'cm^3': 1e-6,       # кубический сантиметр
        'dm^3': 1e-3,       # кубический дециметр
         'm^3': 1,          # кубический метр
      'bushel': 0.03524,    # бушель
        'peck': 0.00881,    # пек
       'quart': 0.001136    # кварт
    }

    @classmethod
    def convert(cls, value: float, unit_from: str, unit_to: str) -> float:
        '''
        параметры для передачи:
         value - значение
         unit_from - из чего перевести
         unit_to - во что перевести
        '''

        if (unit_from not in cls.ratios.keys() or
            unit_to   not in cls.ratios.keys()):
            raise 'Ошибка: параметр "unit_from" или "unit_to" не были найдены. Убедись, что передаешь параметры, которые есть в ключах словаря "ratios"'

        return value * cls.ratios[unit_from] / cls.ratios[unit_to]
