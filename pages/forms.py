from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import InlineCheckboxes
from .models import RealizacjeTugger, RealizacjeRacks, RealizacjeVNA
from crispy_forms.layout import Field
from django.urls import reverse
from pages.models import RealizacjeAGV


class TuggerForm(forms.ModelForm):
    class Meta:
        model = RealizacjeTugger
        fields = ('podnoszenie', 'typ', 'wymiar')

    mapatyp = forms.ChoiceField(
        #label = "Jakich realizacji chcesz wyszukać?",
        #choices = (('T', "Zestawy transportowe"), ('R', "Systemy regałowe"), ('S', "Wózki systemowe"), ('A', "Automatyzacja")),
        widget = forms.HiddenInput,
        required = True,
    )

    choose = forms.CharField(
        initial = 'T',
        widget = forms.HiddenInput,
        required = True,
    )
    
    podnoszenie = forms.MultipleChoiceField(
        choices = RealizacjeTugger.PODNOSZENIE.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )
    
    typ = forms.MultipleChoiceField(
        choices = RealizacjeTugger.TYP.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    wymiar = forms.MultipleChoiceField(
        choices = RealizacjeTugger.WYMIAR.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {'novalidate': ''}
        #self.initial['podnoszenie'] = list(map(str, RealizacjeTugger.PODNOSZENIE))
        #self.initial['typ'] = list(map(str, RealizacjeTugger.TYP))
        #self.initial['wymiar'] = list(map(str, RealizacjeTugger.WYMIAR))

        self.helper.add_input(Submit('submit', 'Filtruj'))
        self.helper.add_input(Submit('cancel', 'Powrót', onclick="document.getElementById('id_choose').value = ''"))
        #self.helper.add_input(Submit('cancel', 'Powrót', onclick="window.location.href = '{}';".format(reverse('mapa'))))
        self.helper.form_show_errors = False
        #self.helper.error_text_inline = False

        #self.helper.layout = Layout(
        #      InlineCheckboxes('podnoszenie'),
        #      Field('typ'), 
        #      Field('wymiar'),
        #      Field('mapatyp', type="hidden"),
        #      Submit('submit', 'Filtruj'),
        #      Submit('cancel', 'Powrót', onclick="document.getElementById('id_mapatyp').value = ''")
        #)

# class TypyForm(forms.Form): 
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.layout = Layout(
#             Fieldset(
#                 'first arg is the legend of the fieldset',
#                 'like_website',
#                 'favorite_number',
#                 'favorite_color',
#                 'favorite_food',
#                 'notes'
#             ),
#             ButtonHolder(
#                 Submit('submit', 'Submit')
#             )
#         )

class TypyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Dalej', onclick="document.getElementById('id_choose').value = $('input:checked', '#mapform').val(); Submit();"))
        #self.helper.add_input(Submit('Submit', 'Dalej'))
        #self.initial['mapatyp'] = 'T'
        self.helper.attrs = {'novalidate': ''}#, 'onchange': "document.getElementById('id_choose').value = $('input:checked', '#mapform').val();"}

    mapatyp = forms.ChoiceField(
        label = "Jakich realizacji chcesz wyszukać?",
        choices = (('T', "Zestawy transportowe"), ('R', "Systemy regałowe"), ('S', "Wózki systemowe"), ('A', "Automatyzacja")),
        widget = forms.RadioSelect,
        required = False,
        initial = 'T',
    )

    choose = forms.CharField(
        initial = 'T',
        widget = forms.HiddenInput,
        required = True,
    )

class RacksForm(forms.ModelForm):
    class Meta:
        model = RealizacjeRacks
        fields = ('typ', 'ilosc', 'wysokosc', 'korytarz')#, 'krata', 'siatka', 'oslony', 'siatka_tylna')

    mapatyp = forms.ChoiceField(
        initial = 'R',
        #label = "Jakich realizacji chcesz wyszukać?",
        #choices = (('T', "Zestawy transportowe"), ('R', "Systemy regałowe"), ('S', "Wózki systemowe"), ('A', "Automatyzacja")),
        widget = forms.HiddenInput,
        required = True,
    )

    choose = forms.CharField(
        
        widget = forms.HiddenInput,
        required = True,
    )
    
    typ = forms.MultipleChoiceField(
        choices = RealizacjeRacks.TYP.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )
    
    ilosc = forms.MultipleChoiceField(
        choices = RealizacjeRacks.ILOSC.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    wysokosc = forms.MultipleChoiceField(
        choices = RealizacjeRacks.WYSOKOSC.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    korytarz = forms.MultipleChoiceField(
        choices = RealizacjeRacks.KORYTARZ.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    #krata = forms.BooleanField(required = False,)
    #siatka = forms.BooleanField(required = False,)
    #oslony = forms.BooleanField(required = False,)
    #siatka_tylna = forms.BooleanField(required = False,)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        #self.initial['podnoszenie'] = list(map(str, RealizacjeTugger.PODNOSZENIE))
        #self.initial['typ'] = list(map(str, RealizacjeTugger.TYP))
        #self.initial['wymiar'] = list(map(str, RealizacjeTugger.WYMIAR))

        self.helper.add_input(Submit('submit', 'Filtruj'))
        self.helper.add_input(Submit('cancel', 'Powrót', onclick="document.getElementById('id_choose').value = ''"))
        self.helper.form_show_errors = False
        #self.helper.error_text_inline = False

class VNAForm(forms.ModelForm):
    class Meta:
        model = RealizacjeVNA
        fields = ('typ', 'wysokosc', 'prowadzenie', 'hamowanie', 'trog', 'typbaterii')#, 'navigation')

    mapatyp = forms.ChoiceField(widget = forms.HiddenInput, required = True)

    choose = forms.CharField(initial = 'S', widget = forms.HiddenInput, required = True)
    
    typ = forms.MultipleChoiceField(
        choices = RealizacjeVNA.TYP.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )
    
    wysokosc = forms.MultipleChoiceField(
        choices = RealizacjeVNA.WYSOKOSC.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    prowadzenie = forms.MultipleChoiceField(
        choices = RealizacjeVNA.PROWADZENIE.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    hamowanie = forms.MultipleChoiceField(
        choices = RealizacjeVNA.HAMOWANIE.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    trog = forms.MultipleChoiceField(
        choices = RealizacjeVNA.TROG.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    typbaterii = forms.MultipleChoiceField(
        choices = RealizacjeVNA.TYPBATERII.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    #navigation = forms.BooleanField(required = False,)
    #siatka = forms.BooleanField(required = False,)
    #oslony = forms.BooleanField(required = False,)
    #siatka_tylna = forms.BooleanField(required = False,)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        #self.initial['podnoszenie'] = list(map(str, RealizacjeTugger.PODNOSZENIE))
        #self.initial['typ'] = list(map(str, RealizacjeTugger.TYP))
        #self.initial['wymiar'] = list(map(str, RealizacjeTugger.WYMIAR))

        self.helper.add_input(Submit('submit', 'Filtruj'))
        self.helper.add_input(Submit('cancel', 'Powrót', onclick="document.getElementById('id_choose').value = ''"))
        self.helper.form_show_errors = False
        #self.helper.error_text_inline = False

class AGVForm(forms.ModelForm):
    class Meta:
        model = RealizacjeAGV
        fields = ('typ', 'truck')

    mapatyp = forms.ChoiceField(widget = forms.HiddenInput, required = True)

    choose = forms.CharField(initial = 'A', widget = forms.HiddenInput, required = True)
    
    typ = forms.MultipleChoiceField(
        choices = RealizacjeAGV.TYP.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )
    
    truck = forms.MultipleChoiceField(
        choices = RealizacjeAGV.TRUCK.choices,
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.add_input(Submit('submit', 'Filtruj'))
        self.helper.add_input(Submit('cancel', 'Powrót', onclick="document.getElementById('id_choose').value = ''"))
        self.helper.form_show_errors = False
