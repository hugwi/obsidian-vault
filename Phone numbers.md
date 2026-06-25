---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
phone_patterns[0] = (
    (^\+[0-9]{2}|^\+[0-9]{2}\(0\)|^\(\+[0-9]{2}\)\(0\)|^00[1-9]{2}|^0)([1-9]{9}$|[0-9\-\s]{10}$)
)

Can be converted to one capturing group by adding ?: two the both groups.
((?:^\+[0-9]{2}|^\+[0-9]{2}\(0\)|^\(\+[0-9]{2}\)\(0\)|^00[1-9]{2}|^0)(?:[1-9]{9}$|[0-9\-\s]{10}$))

Comment: Don't need to match [1-9] and [0-9\-s] . Can just match both with the latter on. 1-9 also ignores patterns with 0? Also should make the length a bit more permissisve. 

Matches: +442345678900', '00442345678900

phone_patterns[1] = (
    (^(([\+]\d{2}[ ][1-9]\d{0,2}[ ])|([0]\d{1,3}[-]))((\d{2}([ ]\d{2}){2})|(\d{3}([ ]\d{3})*([ ]\d{2})+))$)
)
	
Matches: 0770-77 87 99

^(([\+]\d{2}[ ][1-9]\d{0,2}[ ])|([0]\d{1,3}[-]))((\d{2}([ ]\d{2}){2})|(\d{3}([ ]\d{3})*([ ]\d{2})+))$ 
matches +45 12 111 111 11 11 11 Length: 16 

phone_patterns[2] = (
    (^(?!\(0{4,}\d+\))\(?[0|\+][1-9]([\d \-\)\–\/\(]+){6,}\)?([ .\-–\/]?)([\d]+)$)
		
Matches: +1 234 567 8900', '+41 22 730 5989', '(+41) 22 730 5989', '+49 (0)22 730 5989', '+442345678900', '042345678900', '011 123-456-7890', 01234 567 8900
Shouldn't match
(00009)+1 234 567 8900


phone_patterns[3] = (
    (^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$)
)


Matches: 0486 176629, 0763314736, 0770-77 87 87



Missing following patterns
0711/48932-0 - german local number 
01 69907 0
900 205 000 what kind of phone number is this? 

- 078 714 35 39
- +34 650 95 49 36
- + 32 51 25 91 10

(?:^\+[0-9]{2}|^\+[0-9]{2}\(0\)|^\(\+[0-9]{2}\)\(0\)|^00[1-9]{2}|^0)(?:[1-9]{9}$|[0-9\-\s]{10}$))
^(([\+]\d{2}[ ][1-9]\d{0,2}[ ])|([0]\d{1,3}[-]))((\d{2}([ ]\d{2}){2})|(\d{3}([ ]\d{3})*([ ]\d{2})+))$


#### Phone format 

https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s03.html
This regular expression follows the international phone number notation specified by the Extensible Provisioning Protocol (EPP). EPP is a relatively recent protocol (finalized in 2004), designed for communication between domain name registries and registrars. It is used by a growing number of domain name registries, including .com, .info, .net, .org, and .us. The significance of this is that EPP-style international phone numbers are increasingly used and recognized, and therefore provide a good alternative format for storing (and validating) international phone numbers.

EPP-style phone numbers use the format ``+_`CCC`_._`NNNNNNNNNN`_x_`EEEE`_``, where _`C`_ is the 1–3 digit country code, _`N`_ is up to 14 digits, and _`E`_ is the (optional) extension. The leading plus sign and the dot following the country code are required. The literal “x” character is required only if an extension is provided.


Fax? How to handlle?
deliveryDetails.outletAddress.faxNumber


contractual_partner.address.address_components[].phone_number -  0231 94188-0
INVC_CUST_CELLPHONE - 015254614891 Valid phone number???
mms_order.requested_fulfillments[].pickup_location.outlet.address.address_components[].phone_number - 0224884111

Incorrect matched:
brand_category_data[].product_info[].ean (international article number) - 0745883795239
search_query - 0194735030408 
article_number - 0000000
gtin (global trade number) - 0045496335281 valid phone number

Should we remove fax_id and, ean, article 

Missed phones: 
48 (12) 255 51 90
+32 (3) 740 74 60

This is not matched as phone? CUST_PHONE_INVOICE
exlcude our tables
Remove ean if there are the same length 
mpn is (manufucturer part number) - 0878615097520
UUID - 032124057021
PAYER - 0003005910
INVOICE_NO - 012304407
FINANCE_NO - 05355555555
PAYER_PARTY - 0001990020
VOUCHER_NO - 032685413001838
name_basic - 033214 33214
BILLTOPARTY - 0003008199
review_title - 07777777777
search_query - 0702534640690 <- valid phone number 
soh_order_no - 071877707583
product.title - 09.4765.2000
CUST_FIRSTNAME_DLVRY - 036023-50422 < - Probably right? 
PackageReferenceNumber - 41125845+41125844, +190641346 

Can we remove the name query? std_query

Valid phone number: 
contractual_partner.address.address_components[].phone_number - 0224884111


TODO: 
- Remove ean and other columns and see how many match we have
- Look into the distribution of length change from eans and rest of phones
- Extend regex to remove incorrect matches and false negatives


(^\(?:[0|\+][1-9](?:[\d \-\)\-\/\(]+){6,}\)?(?:[ .\-\/]?)(?:[\d]+)$)
(^\(?[0|\+][1-9]([\d \-\)\–\/\(]+){6,}\)?([ .\-–\/]?)([\d]+)$)


Next steps: 
Check landline number, spain doesn't have leading zero 
Note: We don't capture digits without leading zeros for now. 
Check how to lower case
Rename email to have extracted_content and not extracted_emails
Move email pii_field_keywords to after aggregation on field level


