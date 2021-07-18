# Register your models here.
from shareholder.models import ShareHolder, Share, Installment
from utils.admin import register_many

register_many(ShareHolder, Share, Installment)
