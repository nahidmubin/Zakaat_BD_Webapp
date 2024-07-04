from django import forms


class Zakaatform(forms.Form):
    gs_field_style = forms.TextInput(attrs={'class': 'form-control form-control-sm mx-1', 'placeholder': 'Qty'})
    lm_field_style = forms.TextInput(attrs={'class': 'form-control form-control-sm mx-1', 'placeholder': 'Amount'})
    
    
    gold_22k_gram = forms.FloatField(widget= gs_field_style)
    gold_21k_gram = forms.FloatField(widget= gs_field_style)
    gold_18k_gram = forms.FloatField(widget= gs_field_style)
    gold_trad_gram = forms.FloatField(widget= gs_field_style)
    gold_22k_vori = forms.FloatField(widget= gs_field_style)
    gold_21k_vori = forms.FloatField(widget= gs_field_style)
    gold_18k_vori = forms.FloatField(widget= gs_field_style)
    gold_trad_vori = forms.FloatField(widget= gs_field_style)
    
    silver_22k_gram = forms.FloatField(widget= gs_field_style)
    silver_21k_gram = forms.FloatField(widget= gs_field_style)
    silver_18k_gram = forms.FloatField(widget= gs_field_style)
    silver_trad_gram = forms.FloatField(widget= gs_field_style)
    silver_22k_vori = forms.FloatField(widget= gs_field_style)
    silver_21k_vori = forms.FloatField(widget= gs_field_style)
    silver_18k_vori = forms.FloatField(widget= gs_field_style)
    silver_trad_vori = forms.FloatField(widget= gs_field_style)
    
    cash = forms.FloatField(widget= lm_field_style)
    bank_balance = forms.FloatField(widget= lm_field_style)
    liquid_money = forms.FloatField(widget= lm_field_style)
    
    business_asset = forms.FloatField(widget= lm_field_style)
    stock = forms.FloatField(widget= lm_field_style)
    
    debt = forms.FloatField(widget= lm_field_style)