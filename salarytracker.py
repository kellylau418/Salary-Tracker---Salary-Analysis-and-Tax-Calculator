import csv

class Country:
    def salary(self):
        return self._salary

    def job(self):
        return self._job

    def experience(self):
        return self._experience
    
    def size(self):
        return self._size

    def __str__(self):
        return (f'Job Title: {self._job}, Salary(before tax): {float(self._salary):.2f}, Experience Level: {self._experience}, Company Size: {self._size}')

    def __add__(self, n):
        s = float(self._salary)
        s += n
        self._salary = f'{s:.2f}'

    def __sub__(self, n):
        s = float(self._salary)
        s -= n
        self._salary = f'{s:.2f}'

    def __eq__(self, other):
        return float(self._salary) == float(other.salary())

    def __lt__(self, other):
        return float(self._salary) < float(other.salary())

    def __gt__(self, other):
        return float(self._salary) > float(other.salary())


class Gb(Country):
    def __init__(self, job, salary, experience, size):
        self._job = job
        self._salary = salary
        self._experience = experience
        self._size = size

    def __generate_total_tax(self):
        s = float(self._salary)
        if s <= 13577.30:
            return s*0.045
        
        elif s <= 54298.39:
            return (s-13578.38)*0.2 + s*0.045
        
        elif s <= 162020.25:
            return 8144.00 + (s-54298.39)*0.4 + s*0.045

        else:
            return 51232.32 + (s - 162022.41)*0.45 + s*0.045
        
    def tax_owed(self):
        return f'{self.__generate_total_tax():.2f}'

    def income_after_tax(self):
        i = float(self._salary) - self.__generate_total_tax()
        return f'{i:.2f}'

    def __repr__(self):
        return (f'GB(Job Title: {self._job}, Salary(before tax): {float(self._salary):.2f}, Experience Level: {self._experience}, Company Size: {self._size})')

    

class Ca(Country):
    def __init__(self, job, salary, experience, size):
        self._job = job
        self._salary = salary
        self._experience = experience
        self._size = size

    def __generate_federal_tax(self):
        s = float(self._salary)
        
        if s <= 37390.99:
            return s*0.15
        
        elif s <= 74780.49:
            return (s-37390.99)*0.205 + 5608.64 
        
        elif s <= 115922.73:
            return 13286.86 + (s-74780.49)*0.26

        elif s <= 165441.84:
            return 23970.47 + (s - 115922.73)*0.29 

        else:
            return 38331.02 + (s-165441.84)*0.33

    def __generate_provincial_tax(self):
        s = float(self._salary)
        
        if s <= 34494.53:
            return s * 0.0505
        
        elif s <= 68990.56:
            return 1741.97 + (s-34494.53)*0.0915

        elif s <= 111932.25:
            return 4898.36 + (s-68990.56)*0.1116

        elif s <= 164167.30:
            return 9690.65 + (s-111932.25)*0.1216

        else:
            return 16042.43 + (s-164167.30)*0.1316

    def tax_owed(self):
        ccp_ei = (float(self._salary) - self.__generate_provincial_tax() - self.__generate_federal_tax())*0.057
        tax = ccp_ei + self.__generate_provincial_tax() + self.__generate_federal_tax()
        return f'{tax:.2f}'
        
    def income_after_tax(self):
        
        ccp_ei = (float(self._salary) - self.__generate_provincial_tax() - self.__generate_federal_tax())*0.057
        gross = float(self._salary) - (ccp_ei + self.__generate_provincial_tax() + self.__generate_federal_tax())
        return f'{gross:.2f}'

    def __repr__(self):
        return (f'CA(Job Title: {self._job}, Salary(before tax): {float(self._salary):.2f}, Experience Level: {self._experience}, Company Size: {self._size}')
    
    
class Collection:
    

    def __init__(self):
        self._gb_list = []
        self._ca_list = []

    def append_gb(self, o):
        self._gb_list.append(o)

    def append_ca(self, o):
        self._ca_list.append(o)

    def access_gb(self, i):
        return self._gb_list[i]

    def access_ca(self, i):
        return self._ca_list[i]

    def search_by_job_gb(self, j):
        t = ''
        for i in self._gb_list:
            if i.job() == j:
                t += f'{self._gb_list.index(i)}   '

        if t == '':
            print(None)

        else:

            print(f'List of item indexes with job title : {j}')
            print(t)

    def search_by_job_ca(self, j):
        t = ''
        for i in self._ca_list:
            if i.job() == j:
                t += f'{self._ca_list.index(i)}   '

        if t == '':
            print(None)

        else:

            print(f'List of item indexes with job title : {j}')
            print(t)

    def search_by_experience_gb(self, e):
        t = ''
        for i in self._gb_list:
            if i.experience() == e:
                t += f'{self._gb_list.index(i)}   '

        if t == '':
            print(None)

        else:
            print(f'List of item indexes with experience level : {e}')
            print(t)

    def search_by_experience_ca(self, e):
        t = ''
        for i in self._ca_list:
            if i.experience() == e:
                t += f'{self._ca_list.index(i)}   '

        if t == '':
            print(None)

        else:
            print(f'List of item indexes with experience level : {e}')
            print(t)
        

    def __str__(self):
        return (f'GB list: {self._gb_list}\n CA list:{self._ca_list}')

    def __repr__(self):
        return (f'Collection(GB list: {self._gb_list}\n CA list:{self._ca_list})')
        

with open('ds_salaries.csv') as file_in:
    file_in.readline()

    reader = csv.reader(file_in)
    all_data = Collection()

    for line in reader:
        country = line[10]
        salary = line[7]
        job_title = line[4]
        experience_level = line[2]
        company_size = line[11]
        

        if country == 'GB':
            i = Gb(job_title, salary, experience_level, company_size)
            all_data.append_gb(i)

        elif country == 'CA':
            i = Ca(job_title, salary, experience_level, company_size)
            all_data.append_ca(i)


for gb_instance in all_data._gb_list:
    print(gb_instance)
##print(all_data)
##a = all_data.access_ca(2)
##print(a)
##print(a.income_after_tax())
##print(a.tax_owed())
##a + 1000
##print(a)
##all_data.search_by_experience_ca('MI')


        
