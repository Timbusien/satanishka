from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def choice():
    buttons = types.ReplyKeyboardMarkup(row_width=2)
    reg = types.KeyboardButton('send request')
    help_bar = types.KeyboardButton('Help')
    buttons.add(reg, help_bar)
    return buttons


def get_number():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    number = types.KeyboardButton('send number', request_contact=True)
    back = types.KeyboardButton('accept')
    buttons.add(number, back)
    return buttons


def geo():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    geo_button = types.KeyboardButton('send location', request_location=True)
    buttons.add(geo_button)
    return buttons