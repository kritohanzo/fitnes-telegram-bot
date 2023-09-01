from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrationState(State):
    async def set_contact(self, contact):
        self.contact = contact

    async def get_contact(self):
        return self.contact

class Registation(StatesGroup):
    intro = State()
    add_contact = RegistrationState()
    add_name = State()

class AdminMenu(StatesGroup):
    intro = State()
    add_spam = State()
    delete_spam = State()
    add_administrator = State()
    delete_administrator = State()

class UserMenu(StatesGroup):
    check_spam = State()