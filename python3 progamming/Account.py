#-*-coding:utf-8-*-
#__author__ = Leo Luo

import pickle

class SaveError(Exception):pass
class LoadError(Exception):pass

class Transaction:
    def __init__(self, amount, date, currency="USD", rate=1, description=None):
        """
        >>>t = Transaction(100, "2008-12-09")
        >>>t.amount, t.currency, t.usd_conversion_rate, t.usd
        (100, 'USD', 1, 100)
        >>>t = Transaction(250, "2009-03-12", "EUR", 1.53)
        >>>t.amount, t.currency, t.usd_conversion_rate, t.usd
        (250, 'EUR', 1.53, 382.5)
        """
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = rate
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def date(self):
        return self.__date

    @property
    def description(self):
        return self.__description

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate

class Account(object):
    def __init__(self, account_id, account_name):
        self.__account_id = account_id
        self.__account_name = account_name
        self.__t_list = []

    @property
    def account_id(self):
        return self.__account_id

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, value):
        assert len(value) >= 4, "account_name at least be 4 chracters"
        self.__account_name = value

    def __len__(self):
        "Returns the number of Transactions"
        return len(self.__t_list)


    def apply(self, transaction):
        "Applies (adds) the given transaction to the account"
        self.__t_list.append(transaction)

    @property
    def balance(self):
        "Returns the balance in USD"
        total = 0.0
        for transaction in self.__t_list:
            total += transaction.usd
        return total

    @property
    def all_usd(self):
        "Returns True if all transactions are in USD"
        for transaction in self.__t_list:
            if transaction.currency != "USD":
                return False
        return True

    def save(self):
        "Save the account's data in file number.acc"
        fh = None
        try:
            data = [self.account_id, self.account_name, self.__t_list]
            fh = open(self.account_name + ".acc", "wb")
            pickle.dump(data,fh,pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def load(self):
        """Loads the account's data from file number.acc

        All previous data is lost
        """
        fh =None
        try:
            fh = open(self.account_id + ".acc", "rb")
            data = pickle.load(fh)
            assert self.account_id == data[0], "account id doesn't match"
            self.__account_name, self.__t_list = data[1:]
        except (EnvironmentError,pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()





if __name__ == "__main__":
    import doctest
    doctest.testmod()
