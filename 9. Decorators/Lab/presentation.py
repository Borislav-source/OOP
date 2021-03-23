# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
#
#
# hello = hello_function()
# print(hello())

def print_message(message):
    def message_sender():
        "Nested Function"
        print(message)
    return message_sender()

print_message("Some random message")
