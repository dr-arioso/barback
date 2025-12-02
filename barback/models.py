from stashkit.models import Product

class Bottle(Product):
    labeled_volume_ml: int
    distiller: str
    bottler: str

    @property
    def manufacturer(self):
        return self.distiller or self.bottler or super().manufacturer
