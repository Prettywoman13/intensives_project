from django.db import models


# class Section(models.Model):
    # name = models.CharField(max_length=70)
# 

# class Theme(models.Model):
    # name = models.CharField(max_length=70)


class Question(models.Model):
    # тут переделай
    # class SectionChoices(models.TextChoices):
    #     FRESHMAN = 'FR', _('Freshman')
    #     SOPHOMORE = 'SO', _('Sophomore')
    #     JUNIOR = 'JR', _('Junior')
    #     SENIOR = 'SR', _('Senior')
    #     GRADUATE = 'GR', _('Graduate')
    # class ThemeChoices(models.TextChoices):
    #     FRESHMAN = 'FR', _('Freshman')
    #     SOPHOMORE = 'SO', _('Sophomore')
    #     JUNIOR = 'JR', _('Junior')
    #     SENIOR = 'SR', _('Senior')
    #     GRADUATE = 'GR', _('Graduate')
    text = models.TextField(max_length=1500)
    section = models.ForeignKey('section', on_delete=models.CASCADE)
    theme = models.ForeignKey('theme', on_delete=models.CASCADE)
    answer = models.TextField(max_length=1500)
