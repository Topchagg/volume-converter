from metrics import ratios

class VolumeConverter:
    def convert(form, unit_from, unit_to):
        return ratios[form][unit_from] / ratios[form][unit_to]