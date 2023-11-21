from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .check import WorkingHoursMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(WorkingHoursMiddleware())
    dp.middleware.setup(ThrottlingMiddleware())
    

