from django import forms

from .models import Item

INPUT_CLASSES = 'w-full px-4 py-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    supply_period_choices = (
        ('Yanvar', 'Yanvar'),
        ('Fevral', 'Fevral'),
        ('Mart', 'Mart'),
        ('Aprel', 'Aprel'),
        ('May', 'May'),
        ('Iyun', 'Iyun'),
        ('Iyul', 'Iyul'),
        ('Avgust', 'Avgust'),
        ('Sentabr', 'Sentabr'),
        ('Oktabr', 'Oktabr'),
        ('Noyabr', 'Noyabr'),
        ('Dekabr', 'Dekabr'),
    )

    supply_ability_choices = (
        ('dona', 'dona'),
        ('kg', 'kg'),
        ('tonna', 'tonna'),
    )

    supply_ability_length_choices = (
        ('kuniga', 'kuniga'),
        ('haftasiga', 'haftasiga'),
        ('oyiga', 'oyiga'),
        ('yiliga', 'yiliga'),
    )

    payment_method_choices = (
        ('Naqd pul', 'Naqd pul'),
        ('Click', 'Click'),
        ('Plastik karta', 'Plastik karta'),
        ('Bank Hisob', 'Bank Hisob'),
    )

    supply_period = forms.MultipleChoiceField(
        choices=supply_period_choices,
        widget=forms.CheckboxSelectMultiple,
    )
    supply_ability_unit = forms.ChoiceField(
        choices=supply_ability_choices,
        widget=forms.Select(attrs={
            'class': 'px-4 py-6 border'
        }),
    )
    supply_ability_length = forms.ChoiceField(
        choices=supply_ability_length_choices,
        widget=forms.Select(attrs={
            'class': 'px-4 py-6 rounded-r-xl border'
        }),
    )
    payment_method = forms.MultipleChoiceField(
        choices=payment_method_choices,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'shipping', 'supply_ability',
                  'supply_ability_unit', 'supply_ability_length', 'supply_period', 'payment_method')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES}),
            'supply_ability': forms.TextInput(attrs={
                'class': 'px-4 py-6 rounded-l-xl border',
            })
        }


class EditItemForm(forms.ModelForm):
    supply_period_choices = (
        ('Yanvar', 'Yanvar'),
        ('Fevral', 'Fevral'),
        ('Mart', 'Mart'),
        ('Aprel', 'Aprel'),
        ('May', 'May'),
        ('Iyun', 'Iyun'),
        ('Iyul', 'Iyul'),
        ('Avgust', 'Avgust'),
        ('Sentabr', 'Sentabr'),
        ('Oktabr', 'Oktabr'),
        ('Noyabr', 'Noyabr'),
        ('Dekabr', 'Dekabr'),
    )

    supply_ability_choices = (
        ('dona', 'dona'),
        ('kg', 'kg'),
        ('tonna', 'tonna'),
    )

    supply_ability_length_choices = (
        ('kuniga', 'kuniga'),
        ('haftasiga', 'haftasiga'),
        ('oyiga', 'oyiga'),
        ('yiliga', 'yiliga'),
    )

    payment_method_choices = (
        ('Naqd pul', 'Naqd pul'),
        ('Click', 'Click'),
        ('Plastik karta', 'Plastik karta'),
        ('Bank Hisob', 'Bank Hisob'),
    )

    supply_period = forms.MultipleChoiceField(
        choices=supply_period_choices,
        widget=forms.CheckboxSelectMultiple,
    )
    supply_ability_unit = forms.ChoiceField(
        choices=supply_ability_choices,
        widget=forms.Select(attrs={
            'class': 'px-4 py-6 border'
        }),
    )
    supply_ability_length = forms.ChoiceField(
        choices=supply_ability_length_choices,
        widget=forms.Select(attrs={
            'class': 'px-4 py-6 rounded-r-xl border'
        }),
    )
    payment_method = forms.MultipleChoiceField(
        choices=payment_method_choices,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'shipping', 'supply_ability',
                  'supply_ability_unit', 'supply_ability_length', 'supply_period', 'payment_method')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES}),
            'supply_ability': forms.TextInput(attrs={
                'class': 'px-4 py-6 rounded-l-xl border',
            })
        }
