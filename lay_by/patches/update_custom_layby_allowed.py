import frappe

def execute():
    customers = frappe.get_all("Customer", fields=["name"])
    for cust in customers:
        customer = frappe.get_doc("Customer", cust.name)
        if (
            (customer.custom_id_number or (customer.custom_passport_number and customer.custom_passport_country))
            and customer.mobile_no
            and customer.custom_identification_type != "None"
        ):
            customer.custom_layby_allowed = 1
        else:
            customer.custom_layby_allowed = 0
        customer.db_update()

        # To execute the patch run the following command: "bench update --patch"
