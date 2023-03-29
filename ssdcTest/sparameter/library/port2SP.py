import cmath
import math

def calculateSparameter(request):
    pi = 3.141592653589791
    z01 = request["z01"]
    z02 = request["z02"]
    l = request["l"]
    f = request["f"]
    R = request["r"]
    Lt = request["lt"]
    G = request["g"]
    c = request["c"]
    z = complex(R,2*pi*f*Lt)
    y = complex(G,2*pi*0.001*f*c)
    gamma = cmath.sqrt(z*y)
    Zo = cmath.sqrt(z/y)
    
    A = cmath.cosh(gamma*l)
    B = Zo*cmath.sinh(gamma*l)
    C = cmath.sinh(gamma*l)/Zo
    D = cmath.cosh(gamma*l)
    
    s11 = ((A*z02)+B-(C*z01*z02)-(D*z01))/((A*z02)+B+(C*z01*z02)+(D*z01))
    s12 = 2*cmath.sqrt(z01*z02)/((A*z02)+B+(C*z01*z02)+(D*z01))
    s21 = 2*cmath.sqrt(z01*z02)/((A*z02)+B+(C*z01*z02)+(D*z01))
    s22 = (-(A*z02)+B-(C*z01*z02)+(D*z01))/((A*z02)+B+(C*z01*z02)+(D*z01))

    # s11 = complex(round(s11.real,4),round(s11.imag,4))
    # s12 = complex(round(s12.real,4),round(s12.imag,4))
    # s21 = complex(round(s21.real,4),round(s21.imag,4))
    # s22 = complex(round(s22.real,4),round(s22.imag,4))

    s11 = (str(round(20*math.log10(abs(s11)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s11)),4)))
    s12 = (str(round(20*math.log10(abs(s12)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s12)),4)))
    s21 = (str(round(20*math.log10(abs(s21)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s21)),4)))
    s22 = (str(round(20*math.log10(abs(s22)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s22)),4)))
    
    request["s11"] = str(s11)
    request["s12"] = str(s12)
    request["s21"] = str(s21)
    request["s22"] = str(s22)
    
    return request