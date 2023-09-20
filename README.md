## Pharmacy

Pharmacy Store

#### License

MIT

This app is specifically made for a medical/pharmacy store user. 
The administrator will create a store using a webform and enter the details of the store like store_name, registration_no, email, phone, address etc.
When the admin will submit the form, a user will be created in the user list besed on the condition if it doesn't already exists and a welcome email will be sent 
to the provided email address of the store.
The store user will recieve the welcome email where'll he'll be asked to setup password for his newly created store account. 
After setting the passwork, he'll be directed to a specific workspace where he can see his store and after clicking on the store button, a single page will open where he can see 3 sections. Store info, Medicine info, and Search Medicine.
In the first section, he can see info related to his store where he can update few fields like adress, phone etc, but some specific fields like store name, email, registration are read-only.
In the second section, there's a table that has a link field medicine code which is linked with item list, and the user can add madicine through the link field and set purchasing and selling price in the table.      
When he save the document, all these changes will be saved in the medical store list and 2 new documents will be created in the item-price-list with the store name, purchasing price and selling price. 
In the third section, there's a search bar where the user can enter the medicine name and it will fetch the complete row from the medicine table against that name if it is present.
