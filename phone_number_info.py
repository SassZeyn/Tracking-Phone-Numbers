
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type, format_number, PhoneNumberFormat

# Example phone number with international dialing format
phone_number = '+14155552671'  # Example: US number

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number)

# Get various details
country = geocoder.description_for_number(parsed_number, "en")
phone_carrier = carrier.name_for_number(parsed_number, "en")
time_zones = timezone.time_zones_for_number(parsed_number)
num_type = number_type(parsed_number)  # This returns an enum value
formatted_number = format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
is_valid = phonenumbers.is_valid_number(parsed_number)
is_possible = phonenumbers.is_possible_number(parsed_number)

# Output all information
print("Country:", country)
print("Carrier:", phone_carrier)
print("Time Zones:", ', '.join(time_zones))
print("Formatted Number:", formatted_number)
print("Is Valid Number:", is_valid)
print("Is Possible Number:", is_possible)
