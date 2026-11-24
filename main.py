from models.Incident import Incident
from models.InfrastructureIncident import InfrastructureIncident
from models.SecurityIncident import SecurityIncident
from models.Engineer import Engineer
from storage.json_repository import JsonRepository
import numpy as np

from services.incident_service import incident_service

# repository = JsonRepository()
# service = incident_service(repository)
#
# engineer = Engineer(199, "Ankit Soni", "Implementation")
#
# incident = Incident(
#     201,
#     "Payment gateway unavailable",
#     "Critical",
#     engineer
# )
#
# service.add_incident(incident)
#
# print("\nAll incidents:")
#
# for item in service.list_incidents():
#     item.display()
#
# print("\nUpdating incident status:")
#
# success = service.update_incident_status(201, "In Progress")
#
# print("Update successful:", success)


# salaries = np.array([35000, 45000, 55000, 65000, 75000, 85000])
#
# print("Average salary:", np.mean(salaries))
# print("Highest salary:", np.max(salaries))
# print("Lowest salary:", np.min(salaries))
# print("Salary increased by 10 percent:", salaries * 1.10)
# print("Salary greater than 60000:", salaries[salaries > 60000])
# print("Count of employees with salary greater than 60000:", np.sum(salaries > 60000))

employees = np.array([
    [35000, 2],
    [45000, 4],
    [55000, 5],
    [65000, 7],
    [75000, 9],
    [85000, 12]
])

# print(employees)
# print(employees.shape)
# print(employees.ndim)
#
# print(employees[0])       # First employee
# print(employees[:, 0])    # All salaries
# print(employees[:, 1])    # All experience values
# print(employees[0, 0])    # First employee's salary
#
# print(np.sum(employees, axis=0))
# print(np.sum(employees, axis=1))

# print("Average salary of employees:", np.mean(employees[:, 0]))
# print("Average experience of employees:", np.mean(employees[:, 1]))
# print("Count of Employees with more than 5 years of experience:", np.sum(employees[:, 1] > 5))
# print("Highest salary:", np.max(employees[:, 0]))
# print(" Total salary of each employee using axis=1:", np.sum(employees, axis=1))

print(np.sum(employees[:,0]))
print(np.sum(employees[:,1]))
print(employees[employees[:,0] > 50000])
print("Average salary of employeese having more than 5 years of experience:", np.mean(employees[employees[:,1] > 5][:,0]))
