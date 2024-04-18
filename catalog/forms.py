from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "is_actual":
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    wrong_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "purchase_price",)

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]
        for word in set(cleaned_data.lower().split()):
            if word in self.wrong_words:
                raise forms.ValidationError("Указано запрещенное слово в названии продукта")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]
        for word in set(cleaned_data.lower().split()):
            if word in self.wrong_words:
                raise forms.ValidationError("Указано запрещенное слово в описании продукта")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
