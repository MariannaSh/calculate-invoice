input_items = [
    {"nazwa": "Clean Code, Robert C. Martin", "netto": 100.00, "vat": 8},
    {"nazwa": "Applying UML and Patterns, C. Larman", "netto": 300.00, "vat": 8},
    {"nazwa": "Shipping", "netto": 50.00, "vat": 23}
]


print("| VAT [%] | Netto [zł] | VAT [zł] |")
print("|---------|------------|----------|")


unikalne_vat = []
for item in input_items:
    if item["vat"] not in unikalne_vat:
        unikalne_vat.append(item["vat"])

for vat in unikalne_vat:
    sum_netto = sum(item["netto"] for item in input_items if item["vat"] == vat)
    sum_vat = sum(item["netto"] * (vat / 100) for item in input_items if item["vat"] == vat)
    print(f"| {vat}%     |  {sum_netto:.2f}     | {sum_vat:.2f}    |")


