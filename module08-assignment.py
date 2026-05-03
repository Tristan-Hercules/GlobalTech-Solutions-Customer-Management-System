# module08-assignment.py
# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "IT Support": 95
}

# TODO 2: Create customer dictionaries
customer1 = {
    "company_name": "Alpha Corp",
    "contact_person": "John Smith",
    "email": "john@alphacorp.com",
    "phone": "555-1001"
}

customer2 = {
    "company_name": "Beta Industries",
    "contact_person": "Sarah Johnson",
    "email": "sarah@beta.com",
    "phone": "555-1002"
}

customer3 = {
    "company_name": "Gamma LLC",
    "contact_person": "Michael Brown",
    "email": "michael@gamma.com",
    "phone": "555-1003"
}

customer4 = {
    "company_name": "Delta Systems",
    "contact_person": "Emily Davis",
    "email": "emily@delta.com",
    "phone": "555-1004"
}

# TODO 3: Create a master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)

for cust_id, info in customers.items():
    print(cust_id, ":", info)

# TODO 5: Look up specific customers
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)

print("C002 Info:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer information
customers["C001"]["phone"] = "555-9999"
customers["C002"]["industry"] = "Manufacturing"

print("\n\nUpdating Customer Information:")
print("-" * 60)

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
projects = {
    "C001": [
        {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000},
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 60, "budget": 13200}
    ],
    "C002": [
        {"name": "Sales Dashboard", "service": "Data Analysis", "hours": 80, "budget": 14000}
    ],
    "C003": [
        {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 100, "budget": 20000}
    ],
    "C004": [
        {"name": "Help Desk Setup", "service": "IT Support", "hours": 75, "budget": 7125}
    ]
}

print("\n\nProject Information:")
print("-" * 60)

for cust_id, plist in projects.items():
    print(cust_id, "Projects:")
    for project in plist:
        print(" ", project)

# TODO 8: Calculate project costs
print("\n\nProject Cost Calculations:")
print("-" * 60)

for cust_id, plist in projects.items():
    for project in plist:
        rate = services[project["service"]]
        cost = rate * project["hours"]
        print(project["name"], "- Cost: $", cost)

# TODO 9: Customer statistics using dictionary methods
print("\n\nCustomer Statistics:")
print("-" * 60)

print("Customer IDs:", customers.keys())

company_names = [value["company_name"] for value in customers.values()]
print("Companies:", company_names)

print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
service_counts = {}

for plist in projects.values():
    for project in plist:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)

for service, count in service_counts.items():
    print(service, ":", count)

# TODO 11: Financial aggregations
all_projects = []

for plist in projects.values():
    all_projects.extend(plist)

total_hours = sum(project["hours"] for project in all_projects)
total_budget = sum(project["budget"] for project in all_projects)
avg_budget = total_budget / len(all_projects)

# Highest and lowest budget values only
max_budget = max(project["budget"] for project in all_projects)
min_budget = min(project["budget"] for project in all_projects)

print("\n\nFinancial Summary:")
print("-" * 60)

print("Total Hours:", total_hours)
print("Total Budget: $", total_budget)
print("Average Budget: $", round(avg_budget, 2))
print("Highest Project Budget: $", max_budget)
print("Lowest Project Budget: $", min_budget)

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)

for cust_id, info in customers.items():
    plist = projects.get(cust_id, [])
    num_projects = len(plist)
    cust_hours = sum(p["hours"] for p in plist)
    cust_budget = sum(p["budget"] for p in plist)

    print(cust_id, "-", info["company_name"])
    print("Projects:", num_projects)
    print("Hours:", cust_hours)
    print("Budget: $", cust_budget)
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
adjusted_rates = {
    service: rate * 1.10
    for service, rate in services.items()
}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)

for service, rate in adjusted_rates.items():
    print(service, ":", round(rate, 2))

# TODO 14: Filter customers using dictionary comprehension
active_customers = {
    cust_id: info
    for cust_id, info in customers.items()
    if cust_id in projects and len(projects[cust_id]) > 0
}

print("\n\nActive Customers (with projects):")
print("-" * 60)

print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
customer_budgets = {
    cust_id: sum(project["budget"] for project in plist)
    for cust_id, plist in projects.items()
}

print("\n\nCustomer Budget Totals:")
print("-" * 60)

print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
service_tiers = {
    service: (
        "Premium" if rate >= 200 else
        "Standard" if rate >= 100 else
        "Basic"
    )
    for service, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)

print(service_tiers)

# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]

    for field in required_fields:
        if field not in customer_dict or customer_dict[field] == "":
            return False

    return True

print("\n\nCustomer Validation:")
print("-" * 60)

for cust_id, info in customers.items():
    print(cust_id, "Valid:", validate_customer(info))

# TODO 18: Project status tracking with loops and conditionals
statuses = ["active", "completed", "pending"]
status_counts = {"active": 0, "completed": 0, "pending": 0}

index = 0

for plist in projects.values():
    for project in plist:
        project["status"] = statuses[index % 3]
        status_counts[project["status"]] += 1
        index += 1

print("\n\nProject Status Summary:")
print("-" * 60)

print(status_counts)

# TODO 19: Budget analysis function with aggregation
def analyze_customer_budgets(projects_dict):
    results = {}

    for cust_id, plist in projects_dict.items():
        total = sum(project["budget"] for project in plist)
        count = len(plist)
        average = total / count if count > 0 else 0

        results[cust_id] = {
            "total": total,
            "average": average,
            "count": count
        }

    return results

print("\n\nDetailed Budget Analysis:")
print("-" * 60)

budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):
    used_services = []

    if customer_id in projects:
        for project in projects[customer_id]:
            used_services.append(project["service"])

    total_budget = sum(
        project["budget"] for project in projects.get(customer_id, [])
    )

    recommendations = []

    for service, rate in services.items():
        if service not in used_services:
            if total_budget >= 15000 and rate >= 150:
                recommendations.append(service)
            elif total_budget < 15000:
                recommendations.append(service)

    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)

for cust_id in customers.keys():
    recs = recommend_services(cust_id, customers, projects, services)
    print(cust_id, ":", recs)