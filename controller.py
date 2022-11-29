import threading
import time
import os
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, CallbackContext, MessageHandler, Filters, filters
import logging
import export_data_csv
import export_data_xml
import import_data_csv
import import_data_xml
import bot_commands
import view



data = None
infinite_cycle = True


type_file = None
last_file_name = None

# Этапы/состояния разговора
FIRST, SECOND = range(2)
# Данные обратного вызова
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGTH, NINE, TEN, ELEVEN = range(11)

def stop_while():
    # Из окна tkinter получаем флаг закрытия окна и остановки основного цикла
    global infinite_cycle
    infinite_cycle = view.stop_programm()


def load_data_xml(file_name):
    # Считывает данные из файла xml 
    global data
    data = import_data_xml.parse_xml(file_name)


def load_data_csv(file_name):
    # Считывает данные из файла csv
    global data
    data = import_data_csv.read_data_csv(file_name)


def write_data_xml():
    # Запись данных в файл xml
    global data
    global last_file_name
    # print(last_file_name)
    # print(f'++{data}')
    export_data_xml.write_new_data_xml(data, last_file_name)


def write_data_csv():
    # Запись данных в файл csv
    global data
    global last_file_name
    # print(last_file_name)
    # print(f'++{data}')
    export_data_csv.write_new_data_csv(data, last_file_name)


def start_work_with_data():
    print('start controller')
    i = 0
    while infinite_cycle:
        global data
        global type_file
        global last_file_name
        # Загрузка данных в бота       
        load_file, type_file, last_file_name = bot_commands.transfer_load_file()
        if load_file and type_file == 'xml':
            load_data_xml(last_file_name)
            bot_commands.transfer_data(data)
            bot_commands.transfer_load_file_reset()
        if load_file and type_file == 'csv':
            load_data_csv(last_file_name)
            bot_commands.transfer_data(data)
            bot_commands.transfer_load_file_reset()

        # Изменение данных
        add_data_info = bot_commands.transfer_add_data()
        # print(add_data_info)
        if add_data_info:
            data = bot_commands.transfer_data_from_bot()
            bot_commands.transfer_add_data_reset()
            if type_file == 'xml':
                write_data_xml()
            if type_file == 'csv':
                write_data_csv()
        
        time.sleep(0.01)
        stop_while()
    print('stop controller')
    print('stop bot server ')
    os.abort()

def start_telegram_bot():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    level=logging.INFO, filename='bot.log')
    # logging.getLogger(__name__)
    
    if __name__ == '__main__':
        with open('F:/Учеба в ГикБрэйнс/21. Знакомство с языком Python/telegram_bot_token.txt', 'r') as f:
            token = str(f.read())
        updater = Updater(token)
        
        logging.info('Start bot')

        dispatcher = updater.dispatcher
        updater.dispatcher.add_handler(CommandHandler('help', bot_commands.help_command))
        updater.dispatcher.add_handler(CommandHandler('search', bot_commands.search))
        updater.dispatcher.add_handler(CommandHandler('listing', bot_commands.listing))

        conv_handler = ConversationHandler(entry_points=[CommandHandler('start', bot_commands.start)],
            states={ # словарь состояний разговора, возвращаемых callback функциями
                FIRST: [CallbackQueryHandler(bot_commands.one, pattern='^' + str(ONE) + '$'),
                        CallbackQueryHandler(bot_commands.two, pattern='^' + str(TWO) + '$'),
                        CallbackQueryHandler(bot_commands.three, pattern='^' + str(THREE) + '$'),
                        CallbackQueryHandler(bot_commands.four, pattern='^' + str(FOUR) + '$'),
                        CallbackQueryHandler(bot_commands.five, pattern='^' + str(FIVE) + '$'),
                        CallbackQueryHandler(bot_commands.six, pattern='^' + str(SIX) + '$'),
                        CallbackQueryHandler(bot_commands.seven, pattern='^' + str(SEVEN) + '$'),
                        CallbackQueryHandler(bot_commands.eigth, pattern='^' + str(EIGTH) + '$'),
                        CallbackQueryHandler(bot_commands.eleven, pattern='^' + str(ELEVEN) + '$'),],
                SECOND: [CallbackQueryHandler(bot_commands.start_over, pattern='^' + str(NINE) + '$'),
                        CallbackQueryHandler(bot_commands.end, pattern='^' + str(TEN) + '$'),],},
            fallbacks=[CommandHandler('start', bot_commands.start)],)
        dispatcher.add_handler(conv_handler)
        updater.dispatcher.add_handler(MessageHandler(Filters.text, bot_commands.add_data))
        
        print('start bot server')
        updater.start_polling()
        updater.idle()
        
 
def start_programm():
    thr1 = threading.Thread(target = start_work_with_data).start()
    thr2 = threading.Thread(target = view.quit_window).start()
    thr3 = threading.Thread(target = start_telegram_bot()).start()
    
start_programm()
    
