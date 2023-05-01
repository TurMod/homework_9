def main():

    phone_book = {}

    def input_error(func):
        while True:
            try:
                result = func()
                if result == 'break':
                    break
            except IndexError:
                print('This command was misspelled!')
            except TypeError:
                print('You didn\'t put user\'s phone or name!')
            except (UnboundLocalError, KeyError):
                print('Error!')

    def hello(_):
        return 'How can I help you?'

    def add(name, phone):
        if name in phone_book:
            return 'This contact is already exist!'
        else:
            phone_book[name] = phone
            return 'The contact was successfully added.'
    
    def change(name, phone):
        if name not in phone_book:
            return 'This contact does not exist!'
        else:
            phone_book[name] = phone
            return 'The user`s phone was successfully changed.'
        
    def phone(name):
        if name in phone_book:
            return phone_book[name]
        else:
            return 'This contact does not exist!'
    
    def show_all(string):
        return phone_book

    def close(_):
        return 'break'

    @input_error
    def handler():
        COMMANDS = {
            'hello': hello,
            'add': add,
            'change': change,
            'phone': phone,
            'show all': show_all,
            'good bye': close,
            'exit': close,
            'close': close
        }
        
        while True:
            user_input = str(input('Write command: ')).lower()
            command_list = user_input.split(' ')
            for command in COMMANDS:
                if len(command_list) == 1:
                    if command_list[0] in command:
                        result = COMMANDS[command_list[0]](command_list[0])
                        break
                elif len(command_list) == 2:
                    if f'{command_list[0]} {command_list[1]}' in command:
                        result = COMMANDS[f'{command_list[0]} {command_list[1]}'](command_list[1])
                        break
                    elif command_list[0] in command:
                        result = COMMANDS[command_list[0]](command_list[1])
                        break
                elif len(command_list) == 3:
                    if command_list[0] in command:
                        result = COMMANDS[command_list[0]](command_list[1], command_list[2])
                        break
            if result == 'break':
                return 'break'
            else:
                print(result)
    




if '__main__' == __name__:
    main()