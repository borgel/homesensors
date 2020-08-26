def aqi_from_pm(pm):
   if pm > 1000:
      return 1000
   elif pm < 0:
      return 0

   if pm > 350.5:
      return calc_aqi(pm, 500, 401, 500, 350.5)
   elif pm > 250.5:
      return calc_aqi(pm, 400, 301, 350.4, 250.5)
   elif pm > 150.5:
      return calc_aqi(pm, 300, 201, 250.4, 150.5)
   elif pm > 55.5:
      return calc_aqi(pm, 200, 151, 150.4, 55.5)
   elif pm > 35.5:
      return calc_aqi(pm, 150, 101, 55.4, 35.5)
   elif pm > 12.1:
      return calc_aqi(pm, 100, 51, 35.4, 12.1)
   elif pm >= 0:
      return calc_aqi(pm, 50, 0, 12, 0)
   return 0

# range upper, range lower, concentration upper, cencentration lower
def calc_aqi(Cp, Ih, Il, BPh, BPl):
   a = Ih - Il
   b = BPh - BPl
   c = Cp - BPl
   return round((a/b) * c + Il)

