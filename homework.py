import typing as t

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

    def hello():
        return 'How can I help you?'

    def add(name, phone):
        if name in phone_book:
            return f'The contact with name {name} is already exist!'
        else:
            phone_book[name] = phone
            return f'The contact with name {name} and phone number {phone} was successfully added'
    
    def change(name, phone):
        if name not in phone_book:
            return f'The contact with name {name} does not exist!'
        else:
            phone_book[name] = phone
            return f'{name}\'s contact phone number was successfully changed to {phone}'
        
    def phone(name):
        if name in phone_book:
            return phone_book[name]
        else:
            return f'The contact with name {name} does not exist!'
    
    def show_all():
        return phone_book

    def close():
        return 'break'
    
    def unknown_command(command):
        return f'Command {command} does not exist!'

    @input_error
    def main_handler():
        COMMANDS: dict[str, t.Callable] = {
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
            command, *data = input('Write command: ').lower().strip().split(' ', 1)
            if data:
                data = data[0].split(',')

            if (handler := COMMANDS.get(command)) is not None:
                result = handler(*data)

            elif len(data) == 1 and (handler := COMMANDS.get(f'{command} {data[0]}')) is not None:
                result = handler()

            else:
                result = unknown_command(command)

            if result == 'break':
                return 'break'
            else:
                print(result)
    




if '__main__' == __name__:
    main()