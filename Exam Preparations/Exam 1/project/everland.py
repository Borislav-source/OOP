class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    @staticmethod
    def calculate_children_costs(room):
        costs = 0
        for child in room.children:
            costs += child.cost * 30
        return costs

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            expenses = room.expenses + room.room_cost
            if expenses <= room.budget:
                result += f"{room.family_name} paid {expenses:.2f}$ and have {room.budget:.2f}$ left.\n"
                room.budget -= expenses
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms[self.rooms.index(room)] = None
        self.rooms = [room for room in self.rooms if room is not None]
        return result.strip()

    def get_people_count(self):
        peoples_count = 0
        for room in self.rooms:
            peoples_count += room.members_count
        return peoples_count

    def status(self):
        result = f'Total population: {self.get_people_count()}\n'
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. ' \
                      f'Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            for child in room.children:
                result += f'--- Child {room.children.index(child)+1} monthly cost: {child.cost*30:.2f}$\n'
            result += f'--- Appliances monthly cost: {(room.expenses - self.calculate_children_costs(room)):.2f}$\n'
        return result
