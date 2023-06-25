from django import forms

from PythonWebBasicExam.fruit.models import FruitModel


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class FruitCreateForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()

    def __set_placeholders(self):
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
            field.label = ""


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    class Meta:
        model = FruitModel
        fields = ['name', 'image_url', 'description']

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
