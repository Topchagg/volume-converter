from metrics import ratios

class VolumeConverter:

    def convert(unit_from, unit_to):
        return ratios[unit_from] / ratios[unit_to]