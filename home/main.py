from Bard import Chatbot

def ai(postive_cash_flow, total_savings, total_return, user):
    Secure_1PSID = 'awjMJqkOLhWYDUe9H3kHXHjnYUn0WLhShqEG66KYRUzCNhMEZBHw37t7jd6wHV37ngciKQ.'
    Secure_1PSIDTS = 'sidts-CjIBSAxbGab_INBvBg9pm0A2TpfZtGmLX2sjjQli_Wrnb0rk7fmG68hL3i7VJdlDTZOjshAA'
    chatbot = Chatbot(Secure_1PSID, Secure_1PSIDTS)

    advice = chatbot.ask("hello " + "my name is " + str(user) + "can you advice me by seeing these values?" + "my calculated posetive cash flow,total_saving and total return is " + str(postive_cash_flow) + str(total_savings) + str(total_return) + "respectively, advice me with african standards")
    print(advice['content'])
