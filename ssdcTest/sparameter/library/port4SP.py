import cmath
import math

def calculateSparameter(request):
    pi = 3.141592653589791
    z01 = request["z01"]
    z02 = request["z02"]
    l = request["l"]
    f = request["f"] 
    Rodd = request["rodd"]
    Lodd = request["lodd"]
    Godd = request["godd"]
    codd = request["codd"]
    Reven = request["reven"]
    Leven = request["leven"]
    Geven = request["geven"]
    ceven = request["ceven"]
    
    z_e = complex(Reven,2*pi*f*Leven)
    z_o = complex(Rodd,2*pi*f*Lodd)
    y_e = complex(Geven,2*pi*0.001*f*ceven)
    y_o = complex(Godd,2*pi*0.001*f*codd)
    gamma_e = cmath.sqrt(z_e*y_e)
    Zo_e = cmath.sqrt(z_e/y_e)
    gamma_o = cmath.sqrt(z_o*y_o)
    Zo_o = cmath.sqrt(z_o/y_o)

    A_e = cmath.cosh(gamma_e*l)
    B_e = Zo_e*cmath.sinh(gamma_e*l)
    C_e = cmath.sinh(gamma_e*l)/Zo_e
    D_e = cmath.cosh(gamma_e*l)
    A_o = cmath.cosh(gamma_o*l)
    B_o = Zo_o*cmath.sinh(gamma_o*l)
    C_o = cmath.sinh(gamma_o*l)/Zo_o
    D_o = cmath.cosh(gamma_o*l)

    s11= s33 = (((A_e*z02)+B_e-(C_e*z01*z02)-(D_e*z01))/(2*((A_e*z02)+B_e+(C_e*z01*z02)+(D_e*z01))))+(((A_o*z02)+B_o-(C_o*z01*z02)-(D_o*z01))/(2*((A_o*z02)+B_o+(C_o*z01*z02)+(D_o*z01))))
    s22 = s44 = (((-A_e*z02)+B_e-(C_e*z01*z02)+(D_e*z01))/(2*((A_e*z02)+B_e+(C_e*z01*z02)+(D_e*z01))))+(((-A_o*z02)+B_o-(C_o*z01*z02)+(D_o*z01))/(2*((A_o*z02)+B_o+(C_o*z01*z02)+(D_o*z01))))
    s13 = s31 = (((A_e*z02)+B_e-(C_e*z01*z02)-(D_e*z01))/(2*((A_e*z02)+B_e+(C_e*z01*z02)+(D_e*z01))))-(((A_o*z02)+B_o-(C_o*z01*z02)-(D_o*z01))/(2*((A_o*z02)+B_o+(C_o*z01*z02)+(D_o*z01))))
    s24 = s42 = (((-A_e*z02)+B_e-(C_e*z01*z02)+(D_e*z01))/(2*((A_e*z02)+B_e+(C_e*z01*z02)+(D_e*z01))))-(((-A_o*z02)+B_o-(C_o*z01*z02)+(D_o*z01))/(2*((A_o*z02)+B_o+(C_o*z01*z02)+(D_o*z01))))
    s12 = s21 = s34 = s43 = (cmath.sqrt(z01*z02)/((A_e*z02)+B_e+(C_e*z01*z02)+(D_e*z01)))+(cmath.sqrt(z01*z02)/((A_o*z02)+B_o+(C_o*z01*z02)+(D_o*z01)))
    s14 = s41 = s23 = s32 = (cmath.sqrt(z01*z02)/((A_e*z02)+B_e+(C_e*z01*z02)+(D_e*z01)))-(cmath.sqrt(z01*z02)/((A_o*z02)+B_o+(C_o*z01*z02)+(D_o*z01)))

    sdd11 = (s11-s13-s31+s33)/2
    sdd12 = (s12-s14-s32+s34)/2
    sdd21 = (s21-s23-s41+s43)/2
    sdd22 = (s22-s24-s42+s44)/2
    sdc11 = (s11+s13-s31-s33)/2
    sdc12 = (s12+s14-s32-s34)/2
    sdc21 = (s21+s23-s41-s43)/2
    sdc22 = (s22+s24-s42-s44)/2
    scd11 = (s11-s13+s31-s33)/2
    scd12 = (s12-s14+s32-s34)/2
    scd21 = (s21-s23+s41-s43)/2
    scd22 = (s22-s24+s42-s44)/2
    scc11 = (s11+s13+s31+s33)/2
    scc12 = (s12+s14+s32+s34)/2
    scc21 = (s21+s23+s41+s43)/2
    scc22 = (s22+s24+s42+s44)/2

    # s11 = complex(round(s11.real,4),round(s11.imag,4))
    # s12 = complex(round(s12.real,4),round(s12.imag,4))
    # s13 = complex(round(s13.real,4),round(s13.imag,4))
    # s14 = complex(round(s14.real,4),round(s14.imag,4))
    # s21 = complex(round(s21.real,4),round(s21.imag,4))
    # s22 = complex(round(s22.real,4),round(s22.imag,4))
    # s23 = complex(round(s23.real,4),round(s23.imag,4))
    # s24 = complex(round(s24.real,4),round(s24.imag,4))
    # s31 = complex(round(s31.real,4),round(s31.imag,4))
    # s32 = complex(round(s32.real,4),round(s32.imag,4))
    # s33 = complex(round(s33.real,4),round(s33.imag,4))
    # s34 = complex(round(s34.real,4),round(s34.imag,4))
    # s41 = complex(round(s41.real,4),round(s41.imag,4))
    # s42 = complex(round(s42.real,4),round(s42.imag,4))
    # s43 = complex(round(s43.real,4),round(s43.imag,4))
    # s44 = complex(round(s44.real,4),round(s44.imag,4))

    # sdd11 = complex(round(sdd11.real,4),round(sdd11.imag,4))
    # sdd12 = complex(round(sdd12.real,4),round(sdd12.imag,4))
    # sdd21 = complex(round(sdd21.real,4),round(sdd21.imag,4))
    # sdd22 = complex(round(sdd22.real,4),round(sdd22.imag,4))
    # sdc11 = complex(round(sdc11.real,4),round(sdc11.imag,4))
    # sdc12 = complex(round(sdc12.real,4),round(sdc12.imag,4))
    # sdc21 = complex(round(sdc21.real,4),round(sdc21.imag,4))
    # sdc22 = complex(round(sdc22.real,4),round(sdc22.imag,4))
    # scd11 = complex(round(scd11.real,4),round(scd11.imag,4))
    # scd12 = complex(round(scd12.real,4),round(scd12.imag,4))
    # scd21 = complex(round(scd21.real,4),round(scd21.imag,4))
    # scd22 = complex(round(scd22.real,4),round(scd22.imag,4))
    # scc11 = complex(round(scc11.real,4),round(scc11.imag,4))
    # scc12 = complex(round(scc12.real,4),round(scc12.imag,4))
    # scc21 = complex(round(scc21.real,4),round(scc21.imag,4))
    # scc22 = complex(round(scc22.real,4),round(scc22.imag,4))

    s11 = (str(round(20*math.log10(abs(s11)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s11)),4)))
    s12 = (str(round(20*math.log10(abs(s12)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s12)),4)))
    s13 = (str(round(20*math.log10(abs(s13)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s13)),4)))
    s14 = (str(round(20*math.log10(abs(s14)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s14)),4)))
    s21 = (str(round(20*math.log10(abs(s21)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s21)),4)))
    s22 = (str(round(20*math.log10(abs(s22)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s22)),4)))
    s23 = (str(round(20*math.log10(abs(s23)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s23)),4)))
    s24 = (str(round(20*math.log10(abs(s24)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s24)),4)))
    s31 = (str(round(20*math.log10(abs(s31)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s31)),4)))
    s32 = (str(round(20*math.log10(abs(s32)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s32)),4)))
    s33 = (str(round(20*math.log10(abs(s33)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s33)),4)))
    s34 = (str(round(20*math.log10(abs(s34)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s34)),4)))
    s41 = (str(round(20*math.log10(abs(s41)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s41)),4)))
    s42 = (str(round(20*math.log10(abs(s42)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s42)),4)))
    s43 = (str(round(20*math.log10(abs(s43)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s43)),4)))
    s44 = (str(round(20*math.log10(abs(s44)),4))+' ∠ '+str(round(math.degrees(cmath.phase(s44)),4)))

    sdd11 = (str(round(20*math.log10(abs(sdd11)),4))+' ∠ '+str(round(math.degrees(cmath.phase(sdd11)),4)))
    sdd12 = (str(round(20*math.log10(abs(sdd12)),4))+' ∠ '+str(round(math.degrees(cmath.phase(sdd12)),4)))
    sdd21 = (str(round(20*math.log10(abs(sdd21)),4))+' ∠ '+str(round(math.degrees(cmath.phase(sdd21)),4)))
    sdd22 = (str(round(20*math.log10(abs(sdd22)),4))+' ∠ '+str(round(math.degrees(cmath.phase(sdd22)),4)))
    sdc11 = (str(round((abs(sdc11)),4))+' ∠ '+str(round(math.degrees(cmath.phase(sdc11)),4)))
    sdc12 = (str(round((abs(sdc12)),4))+' ∠ '+str(round(math.degrees(cmath.phase(sdc12)),4)))
    sdc21 = (str(round((abs(sdc21)),4))+' ∠ '+str(round(math.degrees(cmath.phase(sdc21)),4)))
    sdc22 = (str(round((abs(sdc22)),4))+' ∠ '+str(round(math.degrees(cmath.phase(sdc22)),4)))
    scd11 = (str(round((abs(scd11)),4))+' ∠ '+str(round(math.degrees(cmath.phase(scd11)),4)))
    scd12 = (str(round((abs(scd12)),4))+' ∠ '+str(round(math.degrees(cmath.phase(scd12)),4)))
    scd21 = (str(round((abs(scd21)),4))+' ∠ '+str(round(math.degrees(cmath.phase(scd21)),4)))
    scd22 = (str(round((abs(scd22)),4))+' ∠ '+str(round(math.degrees(cmath.phase(scd22)),4)))
    scc11 = (str(round(20*math.log10(abs(scc11)),4))+' ∠ '+str(round(math.degrees(cmath.phase(scc11)),4)))
    scc12 = (str(round(20*math.log10(abs(scc12)),4))+' ∠ '+str(round(math.degrees(cmath.phase(scc12)),4)))
    scc21 = (str(round(20*math.log10(abs(scc21)),4))+' ∠ '+str(round(math.degrees(cmath.phase(scc21)),4)))
    scc22 = (str(round(20*math.log10(abs(scc22)),4))+' ∠ '+str(round(math.degrees(cmath.phase(scc22)),4)))

    request["s11"] = str(s11)
    request["s12"] = str(s12)
    request["s13"] = str(s13)
    request["s14"] = str(s14)
    request["s21"] = str(s21)
    request["s22"] = str(s22)
    request["s23"] = str(s23)
    request["s24"] = str(s24)
    request["s31"] = str(s31)
    request["s32"] = str(s32)
    request["s33"] = str(s33)
    request["s34"] = str(s34)
    request["s41"] = str(s41)
    request["s42"] = str(s42)
    request["s43"] = str(s43)
    request["s44"] = str(s44)

    request["sdd11"] = str(sdd11)
    request["sdd12"] = str(sdd12)
    request["sdd21"] = str(sdd21)
    request["sdd22"] = str(sdd22)
    request["sdc11"] = str(sdc11)
    request["sdc12"] = str(sdc12)
    request["sdc21"] = str(sdc21)
    request["sdc22"] = str(sdc22)
    request["scd11"] = str(scd11)
    request["scd12"] = str(scd12)
    request["scd21"] = str(scd21)
    request["scd22"] = str(scd22)
    request["scc11"] = str(scc11)
    request["scc12"] = str(scc12)
    request["scc21"] = str(scc21)
    request["scc22"] = str(scc22)

    return request