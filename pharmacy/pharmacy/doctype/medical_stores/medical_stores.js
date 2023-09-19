// Copyright (c) 2023, Mubashir Bashir and contributors
// For license information, please see license.txt

frappe.ui.form.on('Medical Stores', {
    search_medicine: function(frm) {
        const result = frm.doc.medicine_name.filter((medicine) => medicine.item_code == frm.doc.search_medicine);

        // Create an HTML table from the result
        const tableHTML = '<table class="table"><tr><th scope="col">No</th><th scope="col">Item Code</th><th scope="col">Item Name</th><th scope="col">Purchasing</th><th scope="col">Selling</th></tr>' +
            result.map((medicine) => {
                // Format purchasing and selling as PKR currency
                const formattedPurchasing = Number(medicine.purchasing).toLocaleString('en-PK', { style: 'currency', currency: 'PKR' });
                const formattedSelling = Number(medicine.selling).toLocaleString('en-PK', { style: 'currency', currency: 'PKR' });

                return `<tr><td>${medicine.idx}</td><td>${medicine.item_code}</td><td>${medicine.item_name}</td><td>${formattedPurchasing}</td><td>${formattedSelling}</td></tr>`;
            }).join('') + '</table>';

        // Set the HTML table as the value of the medicine_html field
        $(frm.fields_dict.medicine_html.wrapper).empty();
        $(tableHTML).appendTo(frm.fields_dict.medicine_html.wrapper);
    }
});

























// frappe.ui.form.on('Medical Stores', {
// 	search_medicine: function(frm) {
// 		// frappe.msgprint(__('Searched'));
// 		const result = frm.doc.medicine_name.filter((medicine) => medicine.item_code == frm.doc.search_medicine);
// 		console.log('Result',result)
// 		// frappe.msgprint(__(result));
// 	}
// });
