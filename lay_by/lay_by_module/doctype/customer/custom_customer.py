from erpnext.selling.doctype.customer.customer import Customer
import frappe

class CustomCustomer(Customer):
    def validate(self):
        super(CustomCustomer, self).validate()
        self.validate_identification()
        self.check_lay_by_allowed()

    def validate_identification(self):
        if self.custom_identification_type == "ID" and not self.custom_id_number:
            frappe.throw("ID Number is required if Identification Type is ID")
        elif self.custom_identification_type == "Passport":
            if not self.custom_passport_number:
                frappe.throw("Passport Number is required if Identification Type is Passport")
            if not self.custom_country_of_origin:
                frappe.throw("Passport Country of Origin is required if Identification Type is Passport")

    def check_lay_by_allowed(self):
        if ((self.custom_id_number or (self.custom_passport_number and self.custom_country_of_origin)) 
            and self.mobile_no 
            and self.custom_identification_type != "None"
            ):
            self.custom_layby_allowed = 1
        else:
            self.custom_layby_allowed = 0