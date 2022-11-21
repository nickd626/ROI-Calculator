class ROICalculator():
    def __init__(self):
        pass

    def income(self):
        self.rentalIncome = int(
            input('What is your total monthly rental income?\n'))
        self.laundryIncome = int(
            input('What is your total monthly laundry income?\n'))
        self.storageIncome = int(
            input('What is your total monthly storage income?\n'))
        self.miscIncome = int(
            input('What is your total monthly miscellaneous income?\n'))
        self.totalIncome = (
            self.rentalIncome + self.laundryIncome + self.storageIncome + self.miscIncome)
        print(f'Your total monthly income is ${self.totalIncome}.\n')
        return self.totalIncome

    def expenses(self):
        self.tax = int(input('What is your total monthly tax expense?\n'))
        self.insurance = int(
            input('What is your total monthly insurance expense?\n'))
        self.utilities = int(
            input('What is your total monthly utilities expense?\n'))
        self.HOA = int(
            input('What is your total monthly Home Owners Association (HOA) expense?\n'))
        self.lawnCare = int(
            input('What is your total monthly lawn care expense?\n'))
        self.vacancy = int(
            input('What is your total monthly vacancy expense?\n'))
        self.repairs = int(
            input('What is your total monthly repair expense?\n'))
        self.capEX = int(
            input('What is your total monthly capital expenditure (CapEX) expense?\n'))
        self.propertyManagement = int(
            input('What is your total monthly property management expense?\n'))
        self.mortgage = int(
            input('What is your total monthly mortgage expense?\n'))
        self.totalExpenses = (
            self.tax + self.insurance + self.utilities + self.HOA + self.lawnCare +
            self.vacancy + self.repairs + self.capEX + self.propertyManagement + self.mortgage)
        print(f'Your total monthly expenses are ${self.totalExpenses}.\n')
        return self.totalExpenses

    def cash_flow(self):
        self.totalCashFlow = self.totalIncome - self.totalExpenses
        print(f'Your total monthly cash flow is ${self.totalCashFlow}.\n')
        return self.totalCashFlow

    def cash_on_cash_ROI(self):
        self.downPayment = int(
            input('What was the cost of the down payment?\n'))
        self.closingCost = int(
            input('What was the closing cost?\n'))
        self.rehabBudget = int(
            input('What did you pay for any initial repairs/rehab?\n'))
        self.miscInvestments = int(
            input('What was the total of any miscellaneous costs when acquiring the property?\n'))
        self.totalInvestment = (
            self.downPayment + self.closingCost + self.rehabBudget + self.miscInvestments)
        self.annualCashFlow = (self.totalCashFlow * 12)
        self.cashOnCashROI = (
            (self.annualCashFlow / self.totalInvestment) * 100)
        print(f'Your total investment was ${self.totalInvestment}.\n')
        return self.cashOnCashROI

    def runner(self):
        self.income()
        self.expenses()
        self.cash_flow()
        self.cash_on_cash_ROI()
        print(f'-------------------------\nYour total annual income is ${self.totalIncome * 12}.00\nYour total annual expenses are ${self.totalExpenses * 12}.00\nYour total annual cash flow is ${self.totalCashFlow * 12}.00\nYour cash on cash return on investment is {self.cashOnCashROI}%')

a = ROICalculator()

a.runner()