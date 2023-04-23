#!/usr/bin/env python3

import sys
import roman
import dateparser


def main():
   if len(sys.argv) == 1:
    date = "today"
   else:
        date = " ".join(sys.argv[1:])
   # převedeme datum na řetězec ve formátu "dd.mm.yyyy"
   try:
      date_obj = dateparser.parse(date)
      date = date_obj.strftime("%d.%m.%Y")
   except:
      print(f"Time `{date}' not recognized.", file=sys.stderr)
      sys.exit(1)
   try:
      # převedení na římské číslice
      day, month, year = date.split(".")
      day_roman = roman.toRoman(int(day))
      month_roman = roman.toRoman(int(month))
      year_roman = roman.toRoman(int(year))
   except:
      print(f"Time `{date}' not recognized.", file=sys.stderr)
      sys.exit(1)

   print(f"{day_roman}.{month_roman}.{year_roman}")
 
if __name__ == "__main__":
    main()
