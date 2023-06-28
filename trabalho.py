def calc_conceito(nota11,nota22,nota33):
  
  #nota1=int(input(" digite sua primeira nota:"))
  if nota11 <0 or nota11 >100:
        return 'NULO'
  

  #nota2=int(input(" digite sua segunda nota:"))
  if nota22 <0 or nota22 >100:
      return 'NULO'
  

  #nota3=int(input(" digite sua terceira nota:"))
  if nota33 <0 or nota33 >100:
      return 'NULO'
  

  media=((nota11+nota22+nota33)/3)
  #print((nota11+nota22+nota33)/3)

  if media >=0 and media<50:
    return 'D'
  elif media>=50 and media<70:
    return 'C'
  elif media>=70 and media<90:
    return 'B'
  elif media >=90 and media<=100:
    return 'A'
  else:
    return 'NULO'