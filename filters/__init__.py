from aiogram import Dispatcher

from loader import dp
from .admin_filter import AdminFilter
from .group_filters import IsGroup
from .private_filter import IsPrivate
# from .is_admin import AdminFilter


if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
    pass