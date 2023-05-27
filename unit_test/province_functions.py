def get_formatted_province(province='', country='', population=''):
    if not(province) and not(country) and not(population):
        return "no inputs given"
    else:
        if population:
            full_info = f"{province}, {country} - {population}"
        else:
            full_info = f"{province}, {country}"
    return full_info.title()

