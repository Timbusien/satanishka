import telebot
import button

bot = telebot.TeleBot('7736182557:AAGLSOr--tC3_nX-H7y3wA5plf4erGGQGUM')

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.id
    print(message)

    bot.send_message(user, 'Welcome to the DodgeLovers', reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.send_message(user, 'Choose an option', reply_markup=button.choice())
    if message.text.lower() == 'help':
        bot.send_message(user, 'Just press button "send request"')

@bot.message_handler(content_types=['text'])
def start_reg(message):
    if message.text == 'send request':
        bot.send_message(message.from_user.id, 'what is your name and surname?',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)


def get_name(message):
    user = message.from_user.id
    name = message.text
    bot.send_message(user, f'Nice to meet you {name}')
    bot.send_message(user, 'Great, what is your telegram @user')
    bot.register_next_step_handler(message, get_user_tg, name)


def get_user_tg(message, name):
    user = message.from_user.id
    tg_user = message.text
    bot.send_message(user, 'great, which car would you like to order')
    bot.register_next_step_handler(message, get_product, tg_user, name)


def get_product(message, name, tg_user):
    user = message.from_user.id
    product = message.text
    bot.send_message(user, 'Insert your number', reply_markup=button.get_number())
    bot.register_next_step_handler(message, get_num, product, tg_user, name)


def get_num(message, name, tg_user, product):
    user = message.from_user.id
    if message.contact and message.contact.phone_number:
        user_num = message.contact.phone_number
        print(user_num)
        # base.register(user, name, group, user_num)
        bot.register_next_step_handler(message, get_location, name, product, tg_user, user_num)
    # elif message.text.lower() == 'далее':
    #     bot.send_message(user, 'возвращаю, нажмите поделиться а потом далее!', reply_markup=button.choice())


# def get_loc(message, name, user_num, tg_user, product):
#     user = message.from_user.id
#     if message.location:
#         user_location = message.location
#         bot.send_message(user, 'send what you want', reply_markup=button.geo())
#         bot.register_next_step_handler(message, chat_tg, name, tg_user, user_num, user_location, product)
#     else:
#         bot.send_message(user, 'send by button')
#         bot.register_next_step_handler(message, get_loc, name, user_num, product)

def get_location(message, name, tg_user, product, user_num):
    user_location = message.location



    bot.send_message(message.chat.id, 'Please, send your location:', reply_markup=button.geo())
    bot.register_next_step_handler(message, chat_tg, name, tg_user, user_num, user_location, product)


def chat_tg(message,  name, tg_user, user_num,  user_location, product):
    user = message.from_user.id
    bot.send_message(-1001500295547 , f'New client here\n\nGuy name: {product}\n'
                                     f'User: {tg_user}\n'
                                     f'product: {name}\n'
                                     f'Number: {user_num}\n')
    bot.send_message(-1001500295547, f'{user_location}')
    bot.send_message(user, "Great, we are already preparing your car✅")
    bot.register_next_step_handler(message, start_reg)

bot.infinity_polling()







