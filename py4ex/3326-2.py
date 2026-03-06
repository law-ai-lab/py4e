def grade(score) :
    
     if score >= 0.9 :
       return "A"
     elif score >= 0.8 :
       return "B"
     elif score >= 0.7 :
       return "C"
     elif score >= 0.6 :
      return "D"
     else :
      return "F"
    
print(grade(0.85))
    