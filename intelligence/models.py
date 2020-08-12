from django.db import models


# Create your models here.
class TestIntelligence(models.Model):
    # Pregunta 01
    RQ01 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question01 = models.CharField(max_length=50, choices=RQ01, verbose_name='¿Cuál de las siguientes actividades '
                                                                            'disfrutas más?')
    # Pregunta 02
    RQ02 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'), ('C', 'Noticias '
                                                                                                           'del '
                                                                                                           'mundo')]
    question02 = models.CharField(max_length=50, choices=RQ02, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 03
    RQ03 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question03 = models.CharField(max_length=50, choices=RQ03, verbose_name='¿Cuál de las siguientes actividades '
                                                                            'disfrutas más?')
    # Pregunta 04
    RQ04 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'), ('C', 'Noticias '
                                                                                                           'del '
                                                                                                           'mundo')]
    question04 = models.CharField(max_length=50, choices=RQ04, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 05
    RQ05 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question05 = models.CharField(max_length=50, choices=RQ05, verbose_name='¿Cuál de las siguientes actividades '
                                                                            'disfrutas más?')
    # Pregunta 06
    RQ06 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'), ('C', 'Noticias '
                                                                                                           'del '
                                                                                                           'mundo')]
    question06 = models.CharField(max_length=50, choices=RQ06, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 07
    RQ07 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question07 = models.CharField(max_length=50, choices=RQ07, verbose_name='¿Cuál de las siguientes actividades '
                                                                            'disfrutas más?')
    # Pregunta 08
    RQ08 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'), ('C', 'Noticias '
                                                                                                           'del '
                                                                                                           'mundo')]
    question08 = models.CharField(max_length=50, choices=RQ08, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 09
    RQ09 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question09 = models.CharField(max_length=50, choices=RQ09, verbose_name='¿Cuál de las siguientes actividades '
                                                                            'disfrutas más?')
    # Pregunta 10
    RQ10 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question10 = models.CharField(max_length=50, choices=RQ10, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 11
    RQ11 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question11 = models.CharField(max_length=50, choices=RQ11,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 12
    RQ12 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question12 = models.CharField(max_length=50, choices=RQ12, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 13
    RQ13 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question13 = models.CharField(max_length=50, choices=RQ13,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 14
    RQ14 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question14 = models.CharField(max_length=50, choices=RQ14, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 15
    RQ15 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question15 = models.CharField(max_length=50, choices=RQ15,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 16
    RQ16 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question16 = models.CharField(max_length=50, choices=RQ16, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 17
    RQ17 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question17 = models.CharField(max_length=50, choices=RQ17,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 18
    RQ18 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question18 = models.CharField(max_length=50, choices=RQ18, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 19
    RQ19 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question19 = models.CharField(max_length=50, choices=RQ19,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 20
    RQ20 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question20 = models.CharField(max_length=50, choices=RQ20, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 21
    RQ21 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question21 = models.CharField(max_length=50, choices=RQ21,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 22
    RQ22 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question22 = models.CharField(max_length=50, choices=RQ22, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 23
    RQ23 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question23 = models.CharField(max_length=50, choices=RQ23,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 24
    RQ24 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question24 = models.CharField(max_length=50, choices=RQ24, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 25
    RQ25 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question25 = models.CharField(max_length=50, choices=RQ25,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 26
    RQ26 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question26 = models.CharField(max_length=50, choices=RQ26, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 27
    RQ27 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question27 = models.CharField(max_length=50, choices=RQ27,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 28
    RQ28 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question28 = models.CharField(max_length=50, choices=RQ28, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 29
    RQ29 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question29 = models.CharField(max_length=50, choices=RQ29,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 30
    RQ30 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question30 = models.CharField(max_length=50, choices=RQ30, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 31
    RQ31 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question31 = models.CharField(max_length=50, choices=RQ31,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 32
    RQ32 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question32 = models.CharField(max_length=50, choices=RQ32, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 33
    RQ33 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question33 = models.CharField(max_length=50, choices=RQ33,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 34
    RQ34 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question34 = models.CharField(max_length=50, choices=RQ34, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 35
    RQ35 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question35 = models.CharField(max_length=50, choices=RQ35,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 36
    RQ36 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question36 = models.CharField(max_length=50, choices=RQ36, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 37
    RQ37 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question37 = models.CharField(max_length=50, choices=RQ37,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 38
    RQ38 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question38 = models.CharField(max_length=50, choices=RQ38, verbose_name='¿Qué programa de televisión prefieres?')
    # Pregunta 39
    RQ39 = [('A', 'Escuchar música'), ('B', 'Ver películas'), ('C', 'Bailar con buena música')]
    question39 = models.CharField(max_length=50, choices=RQ39,
                                  verbose_name='¿Cuál de las siguientes actividades disfrutas más?')
    # Pregunta 40
    RQ40 = [('A', 'Reportajes de descubrimientos y lugares'), ('B', ' Cómico y de entretenimiento'),
            ('C', 'Noticias del mundo')]
    question40 = models.CharField(max_length=50, choices=RQ40, verbose_name='¿Qué programa de televisión prefieres?')

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, " \
               "{18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, " \
               "{35}, {36}, {37}, {38}, {39}".format(
            self.question01, self.question02, self.question03, self.question04, self.question05, self.question06,
            self.question07, self.question08, self.question09, self.question10, self.question11, self.question12,
            self.question13, self.question14, self.question15, self.question16, self.question17, self.question18,
            self.question19, self.question20, self.question21, self.question22, self.question23, self.question24,
            self.question25, self.question26, self.question27, self.question28, self.question29, self.question30,
            self.question31, self.question32, self.question33, self.question34, self.question35, self.question36,
            self.question37, self.question38, self.question39, self.question40)

    class Meta:
        verbose_name = 'Pregunta del Test'
        verbose_name_plural = 'Preguntas del Test'
