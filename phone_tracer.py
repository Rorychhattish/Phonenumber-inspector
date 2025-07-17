import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_number_info(phone):
    try:
        parsed = phonenumbers.parse(phone)
        location = geocoder.description_for_number(parsed, "en")
        sim_carrier = carrier.name_for_number(parsed, "en")
        tz = timezone.time_zones_for_number(parsed)

        print(" Phone Number Details:")
        print(f"   ➤ Number   : {phone}")
        print(f"   ➤ Location : {location}")
        print(f"   ➤ Carrier  : {sim_carrier}")
        print(f"   ➤ Timezone : {', '.join(tz)}")

    except Exception as e:
        print(f"[!] Error: {e}")

get_number_info("Your Phone Number")
