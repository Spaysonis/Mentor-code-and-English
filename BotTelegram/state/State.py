from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    waiting_for_text = State() # State text user
    waiting_for_answers = State() # State answers user


