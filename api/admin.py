from django.contrib import admin
from .models.product import Product
from .models.productImage import ProductImage
from .models.review import Review   
from .models.conversation import Conversation
from .models.support_chat import SupportChat


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(Conversation)
admin.site.register(SupportChat)
