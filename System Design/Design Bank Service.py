class Bank:
    def __init__(self, initialBalance) -> None:
        self.balance = initialBalance

    def withdraw(amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        return True

    def deposit(amount):
        self.balance += amount

    def getBalance():
        return self.balance


design a smart meter system that measures the electricity usage
and reports the measurement every minute to a central service.
tents and building managers should be able to view this data on a
website while being able to view it by hour, day, week, month,
and any interval in the past.


class SmartMeter:
    def __init__(self):
        self.data = {
            '2019': {
                'Jan': {
                    '1': {
                        '0': {

                        }
                        '24': {

                        }
                    }
                }
            }
        }

    def getData(newData):
        get self.data map where newData year, month, day, hour is the same and average that hour
