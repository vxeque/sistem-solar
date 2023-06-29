from django import forms

# FORMULARIO PARA LA TEMPLANTE SOLARSISTEM.HTML
class TestSistemSolar(forms.Form):
    CHOICES1 = [("1", "Jupiter"), ("2", "Venus"), ("sol", "Sol"), ("4", "Tierra")]

    CHOICES2 = [
        ("1400000", "1 400 000 km"),
        ("2", "1 410 000 km"),
        ("3", "2 400 000 km"),
        ("4", "1 800 000 km"),
    ]

    CHOICES3 = [
        ("1", "compone de un 45 % de hidrógeno, un 50 % de helio y 5 % de oxígeno"),
        ("2", "compone de un 65 % de hidrógeno, un 30 % de helio y 5 % de oxígeno"),
        ("3", "compone de un 85 % de hidrógeno, un 10% de helio y 5 % de oxígeno"),
        ("75_hidrógeno_20_helio_5_oxígeno", "compone de un 75 % de hidrógeno, un 20 % de helio y 5 % de oxígeno"),
    ]

    CHOICES4 = [("saturno_jupiter", "Saturno"), ("2", "Venus"), ("3", "Neptuno"), ("saturno_jupiter", "Jupiter")]

    CHOICES5 = [
        ("1", "4578 millones de años"),
        ("4568", "4568 millones de años"),
        ("3", "4569 millones de años"),
        ("4", "4658 millones de años"),
    ]

    ask1 = forms.ChoiceField(
        label="¿Cúal es el objeto que ocupa el 99,86% de la masa del sistema solar?. Elige una opción",
        choices=CHOICES1,
        widget=forms.RadioSelect(attrs={"class":"ask"}),
        required=False,
    )

    ask2 = forms.ChoiceField(
        label="¿Cúal es el diametro del Sol?. Elige una opción",
        choices=CHOICES2,
        widget=forms.RadioSelect(attrs={"class":"ask"}),
        required=False,
    )

    ask3 = forms.ChoiceField(
        label="¿Cúales son los elementos y sus porcentajes con los que esta formado el Sol?. Elige una opción",
        choices=CHOICES3,
        widget=forms.RadioSelect(attrs={"class":"ask"}),
        required=False,
    )

    ask4 = forms.ChoiceField(
        label="¿Cúales son los planetas que son denominados gigantes gaseosos?. Selecciona dos respuestas",
        choices=CHOICES4,
        widget=forms.RadioSelect(attrs={"class":"ask"}),
        required=False
    )

    ask5 = forms.ChoiceField(
        label="¿Cúal es la edad del sistema solar?. Elige una respuesta",
        choices=CHOICES5,
        widget=forms.RadioSelect(attrs={"class":"ask"}),
        required=False,
    )


class TestMercurio(forms.Form):
    CHOICES1 = [("1", "Jupiter"), ("2", "Venus"), ("3", "Sol"), ("mercurio", "Mercurio")]

    CHOICES2 = [
        ("1", "45.7 millones de km"),
        ("2", "41 millones de km"),
        ("57.91", "57.91 millones de km"),
        ("4", "800 millones de km"),
    ]

    CHOICES3 = [
        ("1", "4.869 km"),
        ("2", "5.879 km"),
        ("4.879", "4.879 km"),
        ("4", "4.897 km"),
    ]

    CHOICES4 = [("1", "457°C"), ("427°C", "427°C"), ("3", "472°C"), ("4", "422°C")]

    CHOICES5 = [
        ("5,43", "5,43g/cm³"),
        ("2", "5,34g/cm³"),
        ("3", "5,44g/cm³"),
        ("4", "5,33g/cm³"),
    ]

    ask1 = forms.ChoiceField(
        label="¿Es el planeta mas cercano al Sol?. Elige una opción",
        choices=CHOICES1,
        widget=forms.RadioSelect(attrs={"class":"test-mercurio"}),
        required=False,
    )

    ask2 = forms.ChoiceField(
        label="¿Cúal es la distancia al Sol?. Elige una opción",
        choices=CHOICES2,
        widget=forms.RadioSelect(attrs={"class":"test-mercurio"}),
        required=False,
    )

    ask3 = forms.ChoiceField(
        label="¿Cúal es el diametro del Mercurio?. Elige una opción",
        choices=CHOICES3,
        widget=forms.RadioSelect(attrs={"class":"test-mercurio"}),
        required=False,
    )

    ask4 = forms.ChoiceField(
        label="¿Cúal es la temperatura maxima de mercurio?. Selecciona una respuestas",
        choices=CHOICES4,
        widget=forms.RadioSelect(attrs={"class":"test-mercurio"}),
        required=False
    )

    ask5 = forms.ChoiceField(
        label="¿Cúal es la densidad de mercurio?. Elige una respuesta",
        choices=CHOICES5,
        widget=forms.RadioSelect(attrs={"class":"test-mercurio"}),
        required=False,
    )

# FORMA COMENTARIOS 
class Comentarios_Bandeja(forms.Form):
    # comentarios = forms.CharField(
    #     label="comentarios",
    #     max_length=200,
    #     widget=forms.TextInput(attrs={"class": "cajaComentarios"}),
    # )
    areaDeTexto = forms.CharField(
        required=False,
        label="areaTexto",
        widget=forms.Textarea(attrs={"class": "Caja de comentarios"}),
    )


# field1 = forms.CharField(label='Campo 1', widget=forms.TextInput(attrs={'class': 'mi-clase-css'}))
# field2 = forms.CharField(label='Campo 2', widget=forms.TextInput(attrs={'class': 'mi-otra-clase-css'}))


# FORMA PARA LA TEMPLATE PLANETS.HTML









