# Copyright (c) 2023, Mubashir Bashir and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import fmt_money
from frappe import _


class MedicalStores(Document):
    def validate(self):  
        for m in self.medicine_name:            
            # Check if a buying price document exists
            if frappe.db.exists("Item Price", {
                "item_code": m.item_code,
                "price_list": "Standard Buying",
                "medical_store": self.name
            }):
                if frappe.db.exists("Item Price", {
                    "item_code": m.item_code,
                    "price_list": "Standard Buying",
                    "medical_store": self.name,
                    "price_list_rate":['!=', m.purchasing]
                }):
                    frappe.db.set_value("Item Price", {
                        "item_code": m.item_code,
                        "price_list": "Standard Buying",
                        "medical_store": self.name
                    }, "price_list_rate", m.purchasing)
            else:
                frappe.get_doc({
                    "doctype": "Item Price",
                    "item_code": m.item_code,
                    "price_list": "Standard Buying",
                    "price_list_rate": m.purchasing,
                    "medical_store": self.name
                }).insert()

            # Check if a selling price document exists
            if frappe.db.exists("Item Price", {
                "item_code": m.item_code,
                "price_list": "Standard Selling",
                "medical_store": self.name
            }):
                if frappe.db.exists("Item Price", {
                    "item_code": m.item_code,
                    "price_list": "Standard Selling",
                    "medical_store": self.name,
                    "price_list_rate":['!=', m.selling]
                }):
                    frappe.db.set_value("Item Price", {
                        "item_code": m.item_code,
                        "price_list": "Standard Selling",
                        "medical_store": self.name
                    }, "price_list_rate", m.selling)
            else:
                frappe.get_doc({
                    "doctype": "Item Price",
                    "item_code": m.item_code,
                    "price_list": "Standard Selling",
                    "price_list_rate": m.selling,
                    "medical_store": self.name
                }).insert()
            
    # Create a user and user permission after the document has been inserted
    def after_insert(self):        
        # Create a user and user permission after the document has been inserted
        if not frappe.db.exists("User", {
            "first_name": self.name,
            "email": self.email,
        }):
            user_doc = frappe.get_doc({
                "doctype": "User",
                "first_name": self.name,
                "email": self.email,
                "email_signature": self.email,
                "send_welcome_email": '1',
                "role_profile_name": "Pharmacy",
                "module_profile": "MSP"
            })
            try:
                user_doc.insert()
            except frappe.exceptions.DuplicateEntryError:
                pass

        if not frappe.db.exists("User Permission", {
            "user": self.email,
            "allow": "Medical Stores"
        }):
            user_permission_doc = frappe.get_doc({
                "doctype": "User Permission",
                "user": self.email,
                "allow": "Medical Stores",
                "for_value": self.name,
            })
            try:
                user_permission_doc.insert()
            except frappe.exceptions.DuplicateEntryError:
                pass
    
# @frappe.whitelist()
# def delete_non_profit_module():            
#     try:
#         frappe.db.sql("DELETE FROM `tabModule Def` WHERE `module_name` = 'Non Profit'")
#         return "The 'Non Profit' module has been deleted successfully\nThe 'Non Profit' module has been deleted successfully\nThe 'Non Profit' module has been deleted successfully\nThe 'Non Profit' module has been deleted successfully\nThe 'Non Profit' module has been deleted successfully\nThe 'Non Profit' module has been deleted successfully\nThe 'Non Profit' module has been deleted successfully\n"
#     except Exception as e:
#         frappe.log_error(f"Error deleting 'Non Profit' module: {str(e)}")
#         frappe.throw("Error deleting 'Non Profit' module.")

# bench --site test execute  pharmacy.pharmacy.doctype.medical_stores.medical_stores.delete_non_profit_module