import telebot
from telebot import types
import math
from Translation import ru
from Translation import uk
from Translation import eng

bot = telebot.TeleBot("7768845863:AAFbu0aDimoj0k6Zb1GLZYmOYT1p9GRdFAM")
@bot.message_handler(commands=["start"])
def Languages(message):
    bot.send_message(message.chat.id, "Choose language /Russian /Ukrainian /English or press /Stop.")
    bot.register_next_step_handler(message, choose_language)

def choose_language(message):
    if message.text == "/Russian":
        Start_Rus(message)
    elif message.text == "/Ukrainian":
        Start_Ukr(message)
    elif message.text == "/English":
        Start_Eng(message)
    elif message.text == "/Stop":
        Сancel(message)   
    else:
        bot.send_message(message.chat.id, "Error")
        bot.register_next_step_handler(message, choose_language)

@bot.message_handler(commands=["cancel"])
def Сancel(message):
    bot.send_message(message.chat.id, "The program has stopped press /start to run the program.")
    bot.clear_step_handler_by_chat_id(message.chat.id)


def Start_Rus(message):
    bot.send_message(message.chat.id, ru.new_light)
    bot.register_next_step_handler(message, Light_readings_for_this_month_Rus)

@bot.message_handler(commands=["cancel"])
def Сancel_Rus(message):
    bot.send_message(message.chat.id, ru.stop)
    bot.clear_step_handler_by_chat_id(message.chat.id)

def Light_readings_for_this_month_Rus(message):
    if message.text == "/stop":
        Сancel_Rus(message)
        return
    try:
        global x
        x = int(message.text)
        if len(str(x)) == 5:
            bot.send_message(message.chat.id, ru.old_light)
            bot.register_next_step_handler(message, Light_readings_for_the_past_month_Rus)
        else:
            if len(str(x)) < 5 or len(str(x)) > 5:
                bot.send_message(message.chat.id, ru.error_five_num)
            bot.register_next_step_handler(message, Light_readings_for_this_month_Rus)    
            bot.send_message(message.chat.id, ru.new_light)
    except ValueError:
        bot.send_message(message.chat.id, ru.error_num)
        bot.register_next_step_handler(message, Light_readings_for_this_month_Rus)
        bot.send_message(message.chat.id, ru.new_light)
        
        

def Light_readings_for_the_past_month_Rus(message):
    if message.text == "/stop":
        Сancel_Rus(message)
        return    
    try:
        global y
        y = int(message.text)
        if len(str(y)) == 5 and y < x:
            bot.send_message(message.chat.id, ru.new_water)
            bot.register_next_step_handler(message, Water_readings_for_this_month_Rus)
        elif message.text == "/stop":
            bot.register_next_step_handler(message, Light_readings_for_this_month_Rus)
        else:
            if len(str(y)) < 5 or len(str(y)) > 5:
                bot.send_message(message.chat.id, ru.error_five_num)
            else:
                bot.send_message(message.chat.id, ru.error_last_num)
            bot.register_next_step_handler(message, Light_readings_for_the_past_month_Rus)
            bot.send_message(message.chat.id,ru.old_light)
    except ValueError:
        bot.send_message(message.chat.id, ru.error_num)
        bot.register_next_step_handler(message, Light_readings_for_the_past_month_Rus)
        bot.send_message(message.chat.id, ru.old_light)

def Water_readings_for_this_month_Rus(message):
    if message.text == "/stop":
        Сancel_Rus(message)
        return
    try:
        global p
        p = int(message.text)
        if len(str(p)) == 3:
            bot.send_message(message.chat.id, ru.old_water)
            bot.register_next_step_handler(message, Water_readings_for_last_month_Rus)
        else:
            if len(str(p)) < 3 or len(str(p)) > 3:
                bot.send_message(message.chat.id, ru.error_three_num)
            bot.register_next_step_handler(message, Water_readings_for_this_month_Rus)
            bot.send_message(message.chat.id, ru.new_water)
    except ValueError:
        bot.send_message(message.chat.id, ru.error_num)
        bot.register_next_step_handler(message, Water_readings_for_this_month_Rus)
        bot.send_message(message.chat.id, ru.new_water)

def Water_readings_for_last_month_Rus(message):
    if message.text == "/stop":
        Сancel_Rus(message)
        return
    try:
        global k
        k = int(message.text)
        if len(str(k)) == 3 and k < p:
            bot.send_message(message.chat.id, ru.kl)
            bot.register_next_step_handler(message, Kilowatts_Rus)
        else:
            if len(str(k)) < 3 or len(str(k)) > 3:
                bot.send_message(message.chat.id, ru.error_three_num)
            else:
                bot.send_message(message.chat.id, ru.error_last_num)
            bot.register_next_step_handler(message, Water_readings_for_last_month_Rus)
            bot.send_message(message.chat.id, ru.old_water)
    except ValueError:
        bot.send_message(message.chat.id, ru.error_num)
        bot.register_next_step_handler(message, Water_readings_for_last_month_Rus)
        bot.send_message(message.chat.id, ru.old_water)

def Kilowatts_Rus(message):
    if message.text == "/stop":
        Сancel_Rus(message)
        return
    try:
        global n
        n = float(message.text)
        bot.send_message(message.chat.id, ru.kb)
        bot.register_next_step_handler(message, Cubometers_Rus)
    except ValueError:
        bot.send_message(message.chat.id, ru.error_num)
        bot.register_next_step_handler(message, Kilowatts_Rus)
        bot.send_message(message.chat.id, ru.kl )

def Cubometers_Rus(message):
    if message.text == "/stop":
        Сancel_Rus(message)
        return
    try:
        global u
        u = float(message.text)
        bot.send_message(message.chat.id, ru.tr)
        bot.register_next_step_handler(message, Trush_Rus)
    except ValueError:
        bot.send_message(message.chat.id, ru.error_num)
        bot.register_next_step_handler(message, Cubometers_Rus)
        bot.send_message(message.chat.id, ru.kb )

def Trush_Rus(message):
    if message.text == "/stop":
        Сancel_Rus(message)
        return
    try:
        global trush
        trush = int(message.text)
        Сalculations_light_Rus(message)
    except ValueError:
        bot.send_message(message.chat.id, ru.error)
        bot.register_next_step_handler(message, Trush_Rus)
        bot.send_message(message.chat.id, ru.tr)

def Сalculations_light_Rus(message):
    global light
    light = (x - y) * n
    Сalculations_water_Rus(message)

def Сalculations_water_Rus(message):
    global water
    water = (p - k) * u
    Сalculations_summ_Rus(message)

def Сalculations_summ_Rus(message):
    global summ
    summ = light + water + trush
    results_table_Rus(message)

def results_table_Rus(message):
    bot.send_message(message.chat.id, f"Мусор: {trush} грн.", parse_mode="html")
    bot.send_message(message.chat.id, f"Свет: {light} квт", parse_mode="html")
    bot.send_message(message.chat.id, f"Вода: {water} кбм", parse_mode="html")
    bot.send_message(message.chat.id, f"Сумма за коммунальные услуги: {round(summ, 1)} грн.", parse_mode="html")

def Start_Ukr(message):
    bot.send_message(message.chat.id, uk.new_light)
    bot.register_next_step_handler(message, Light_readings_for_this_month_Ukr)

def Сancel_Ukr(message):
    bot.send_message(message.chat.id, uk.stop)
    bot.clear_step_handler_by_chat_id(message.chat.id)

def Light_readings_for_this_month_Ukr(message):
    if message.text == "/stop":
        Сancel_Ukr(message)
        return
    try:
        global x
        x = int(message.text)
        if len(str(x)) == 5:
            bot.send_message(message.chat.id, uk.old_light)
            bot.register_next_step_handler(message, Light_readings_for_the_past_month_Ukr)
        else:
            if len(str(x)) < 5 or len(str(x)) > 5:
                bot.send_message(message.chat.id, uk.error_five_num)
            bot.register_next_step_handler(message, Light_readings_for_this_month_Ukr)    
            bot.send_message(message.chat.id, uk.new_light)
    except ValueError:
        bot.send_message(message.chat.id, uk.error_num)
        bot.register_next_step_handler(message, Light_readings_for_this_month_Ukr)
        bot.send_message(message.chat.id, uk.new_light)

def Light_readings_for_the_past_month_Ukr(message):
    if message.text == "/stop":
        Сancel_Ukr(message)
        return
    try:
        global y
        y = int(message.text)
        if len(str(y)) == 5 and y < x:
            bot.send_message(message.chat.id, uk.new_water)
            bot.register_next_step_handler(message, Water_readings_for_this_month_Ukr)
        else:
            if len(str(y)) < 5 or len(str(y)) > 5:
                bot.send_message(message.chat.id, uk.error_five_num)
            else:
                bot.send_message(message.chat.id, uk.error_last_num)
            bot.register_next_step_handler(message, Light_readings_for_the_past_month_Ukr)
            bot.send_message(message.chat.id,uk.old_light)
    except ValueError:
        bot.send_message(message.chat.id, uk.error_num)
        bot.register_next_step_handler(message, Light_readings_for_the_past_month_Ukr)
        bot.send_message(message.chat.id, uk.old_light)

def Water_readings_for_this_month_Ukr(message):
    if message.text == "/stop":
        Сancel_Ukr(message)
        return
    try:
        global p
        p = int(message.text)
        if len(str(p)) == 3:
            bot.send_message(message.chat.id, uk.old_water)
            bot.register_next_step_handler(message, Water_readings_for_last_month_Ukr)
        else:
            if len(str(p)) < 3 or len(str(p)) > 3:
                bot.send_message(message.chat.id, uk.error_three_num)
            bot.register_next_step_handler(message, Water_readings_for_this_month_Ukr)
            bot.send_message(message.chat.id, uk.new_water)
    except ValueError:
        bot.send_message(message.chat.id, uk.error_num)
        bot.register_next_step_handler(message, Water_readings_for_this_month_Ukr)
        bot.send_message(message.chat.id, uk.new_water)

def Water_readings_for_last_month_Ukr(message):
    if message.text == "/stop":
        Сancel_Ukr(message)
        return
    try:
        global k
        k = int(message.text)
        if len(str(k)) == 3 and k < p:
            bot.send_message(message.chat.id, uk.kl)
            bot.register_next_step_handler(message, Kilowatts_Ukr)
        else:
            if len(str(k)) < 3 or len(str(k)) > 3:
                bot.send_message(message.chat.id, uk.error_three_num)
            else:
                bot.send_message(message.chat.id, uk.error_last_num)
            bot.register_next_step_handler(message, Water_readings_for_last_month_Ukr)
            bot.send_message(message.chat.id, uk.old_water)
    except ValueError:
        bot.send_message(message.chat.id, uk.error_num)
        bot.register_next_step_handler(message, Water_readings_for_last_month_Ukr)
        bot.send_message(message.chat.id, uk.old_water)

def Kilowatts_Ukr(message):
    if message.text == "/stop":
        Сancel_Ukr(message)
        return
    try:
        global n
        n = float(message.text)
        bot.send_message(message.chat.id, uk.kb)
        bot.register_next_step_handler(message, Cubometers_Ukr)
    except ValueError:
        bot.send_message(message.chat.id, uk.error_num)
        bot.register_next_step_handler(message, Kilowatts_Ukr)
        bot.send_message(message.chat.id, uk.kl )

def Cubometers_Ukr(message):
    if message.text == "/stop":
        Сancel_Ukr(message)
        return
    try:
        global u
        u = float(message.text)
        bot.send_message(message.chat.id, uk.tr)
        bot.register_next_step_handler(message, Trush_Ukr)
    except ValueError:
        bot.send_message(message.chat.id, uk.error_num)
        bot.register_next_step_handler(message, Cubometers_Ukr)
        bot.send_message(message.chat.id, uk.kb)

def Trush_Ukr(message):
    if message.text == "/stop":
        Сancel_Ukr(message)
        return
    try:
        global trush
        trush = int(message.text)
        Сalculations_light_Ukr(message)
    except ValueError:
        bot.send_message(message.chat.id, uk.error)
        bot.register_next_step_handler(message, Trush_Ukr)
        bot.send_message(message.chat.id, uk.tr)

def Сalculations_light_Ukr(message):
    global light
    light = (x - y) * n
    Сalculations_water_Ukr(message)

def Сalculations_water_Ukr(message):
    global water
    water = (p - k) * u
    Сalculations_summ_Ukr(message)

def Сalculations_summ_Ukr(message):
    global summ
    summ = light + water + trush
    results_table_Ukr(message)

def results_table_Ukr(message):
    bot.send_message(message.chat.id, f"Сміття: {trush} грн.", parse_mode="html")
    bot.send_message(message.chat.id, f"Світло: {light} квт", parse_mode="html")
    bot.send_message(message.chat.id, f"Вода: {water} кбм", parse_mode="html")
    bot.send_message(message.chat.id, f"Сума за комунальні послуги: {round(summ, 1)} грн.", parse_mode="html")

def Start_Eng(message):
    bot.send_message(message.chat.id, eng.new_light)
    bot.register_next_step_handler(message, Light_readings_for_this_month_Eng)

def Сancel_Eng(message):
    bot.send_message(message.chat.id, eng.stop)
    bot.clear_step_handler_by_chat_id(message.chat.id)

def Light_readings_for_this_month_Eng(message):
    if message.text == "/stop":
        Сancel_Eng(message)
        return
    try:
        global x
        x = int(message.text)
        if len(str(x)) == 5:
            bot.send_message(message.chat.id, eng.old_light)
            bot.register_next_step_handler(message, Light_readings_for_the_past_month_Eng)
        else:
            if len(str(x)) < 5 or len(str(x)) > 5:
                bot.send_message(message.chat.id, eng.error_five_num)
            bot.register_next_step_handler(message, Light_readings_for_this_month_Eng)    
            bot.send_message(message.chat.id, eng.new_light)
    except ValueError:
        bot.send_message(message.chat.id, eng.error_num)
        bot.register_next_step_handler(message, Light_readings_for_this_month_Eng)
        bot.send_message(message.chat.id, eng.new_light)  

def Light_readings_for_the_past_month_Eng(message):
    if message.text == "/stop":
        Сancel_Eng(message)
        return
    try:
        global y
        y = int(message.text)
        if len(str(y)) == 5 and y < x:
            bot.send_message(message.chat.id, eng.new_water)
            bot.register_next_step_handler(message, Water_readings_for_this_month_Eng)
        else:
            if len(str(y)) < 5 or len(str(y)) > 5:
                bot.send_message(message.chat.id, eng.error_five_num)
            else:
                bot.send_message(message.chat.id, eng.error_last_num)
            bot.register_next_step_handler(message, Light_readings_for_the_past_month_Eng)
            bot.send_message(message.chat.id,eng.old_light)
    except ValueError:
        bot.send_message(message.chat.id, eng.error_num)
        bot.register_next_step_handler(message, Light_readings_for_the_past_month_Eng)
        bot.send_message(message.chat.id, eng.old_light)

def Water_readings_for_this_month_Eng(message):
    if message.text == "/stop":
        Сancel_Eng(message)
        return
    try:
        global p
        p = int(message.text)
        if len(str(p)) == 3:
            bot.send_message(message.chat.id, eng.old_water)
            bot.register_next_step_handler(message, Water_readings_for_last_month_Eng)
        else:
            if len(str(p)) < 3 or len(str(p)) > 3:
                bot.send_message(message.chat.id, eng.error_three_num)
            bot.register_next_step_handler(message, Water_readings_for_this_month_Eng)
            bot.send_message(message.chat.id, eng.new_water)
    except ValueError:
        bot.send_message(message.chat.id, eng.error_num)
        bot.register_next_step_handler(message, Water_readings_for_this_month_Eng)
        bot.send_message(message.chat.id, eng.new_water)

def Water_readings_for_last_month_Eng(message):
    if message.text == "/stop":
        Сancel_Eng(message)
        return
    try:
        global k
        k = int(message.text)
        if len(str(k)) == 3 and k < p:
            bot.send_message(message.chat.id, eng.kl)
            bot.register_next_step_handler(message, Kilowatts_Eng)
        else:
            if len(str(k)) < 3 or len(str(k)) > 3:
                bot.send_message(message.chat.id, eng.error_three_num)
            else:
                bot.send_message(message.chat.id, eng.error_last_num)
            bot.register_next_step_handler(message, Water_readings_for_last_month_Eng)
            bot.send_message(message.chat.id, eng.old_water)
    except ValueError:
        bot.send_message(message.chat.id, eng.error_num)
        bot.register_next_step_handler(message, Water_readings_for_last_month_Eng)
        bot.send_message(message.chat.id, eng.old_water)

def Kilowatts_Eng(message):
    if message.text == "/stop":
        Сancel_Eng(message)
        return
    try:
        global n
        n = float(message.text)
        bot.send_message(message.chat.id, eng.kb)
        bot.register_next_step_handler(message, Cubometers_Eng)
    except ValueError:
        bot.send_message(message.chat.id, eng.error_num)
        bot.register_next_step_handler(message, Kilowatts_Eng)
        bot.send_message(message.chat.id, eng.kl)

def Cubometers_Eng(message):
    if message.text == "/stop":
        Сancel_Eng(message)
        return
    try:
        global u
        u = float(message.text)
        bot.send_message(message.chat.id, eng.tr)
        bot.register_next_step_handler(message, Trush_Eng)
    except ValueError:
        bot.send_message(message.chat.id, eng.error_num)
        bot.register_next_step_handler(message, Cubometers_Eng)
        bot.send_message(message.chat.id, eng.kb)

def Trush_Eng(message):
    if message.text == "/stop":
        Сancel_Eng(message)
        return
    try:
        global trush
        trush = int(message.text)
        Сalculations_light_Eng(message)
    except ValueError:
        bot.send_message(message.chat.id, eng.error)
        bot.register_next_step_handler(message, Trush_Eng)
        bot.send_message(message.chat.id, eng.tr)

def Сalculations_light_Eng(message):
    global light
    light = (x - y) * n
    Сalculations_water_Eng(message)

def Сalculations_water_Eng(message):
    global water
    water = (p - k) * u
    Сalculations_summ_Eng(message)

def Сalculations_summ_Eng(message):
    global summ
    summ = light + water + trush
    results_table_Eng(message)

def results_table_Eng(message):
    bot.send_message(message.chat.id, f"Trash: {trush} UAH", parse_mode="html")
    bot.send_message(message.chat.id, f"Light: {light} kWh", parse_mode="html")
    bot.send_message(message.chat.id, f"Water: {water} cubic meters", parse_mode="html")
    bot.send_message(message.chat.id, f"Sum for utilities : {round(summ, 1)} UAH", parse_mode="html")
bot.infinity_polling()
