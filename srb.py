import math
import time,sys
 
def Print(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def Input(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value
  
def round_to_even(n):
    # round off to the nearest integer
    rounded = round(n)
    # if the rounded number is odd, add 1
    if rounded % 2 != 0:
        rounded += 1
    return rounded

#CREDITS
Print("\033[33mCredits:\n        Syed Shahid \033[0m")
print("\n")

#Input Data
l= int(Input("Enter the length of clear span(l) in mm ==> l = "))
Print("\n")

LL=int(Input("Enter the live load in kN/m acting on beam in service condition ==> LL = "))
Print("\n")

DL = int(Input("Enter the Dead load (Not self wt) or UDL in kN/m==> DL = "))
Print("\n")
b= int(Input("Enter the width of beam (b)in mm ==> b = "))
Print("\n")

fy= int(Input("Enter the yield strength of steel used in N/mm**2= "))
Print ("The steel used is Fe " + str(fy))
print("\n")

fck=int(Input("Enter the grade of concrete in N/mm**2= "))
Print("M" + str(fck)+ "grade concrete is used.")
Print("\n\n")

cc=int(Input("Enter the clear cover in mm: "))
Print("\n")

Print ("\033[33mSTEP1: Effective depth of beam (d)\033[0m")
Print("\n")

Print ("\t From cl:23.2.1 IS 456:2000 \n")
if l >= 3000 and l <= 4000:
    a = 15
elif l >= 5000 and l <= 10000:
    a = 12
else:
    a = 10

d = l / a
Print ("\t Effective depth provided (d_pro) = " +str(l) + "/" + str(a) + "\n")
rounded_d = round(d,2)
d=rounded_d
d = round_to_even(d)
Print("\t \033[31mEffective dept provided (d_pro) = " + str(d) + "mm\033[0m \n")
Print("\n")

Print("\033[33mSTEP 2: Overall Depth of beam (D)\033[0m \n")
Print("\n")

D=d+cc
Print("\t D = d + cc \n")
Print("\t D =" + str(d) + "+" + str(cc) + "\n")
Print("\t D= " + str(D) + "\n")
D= round_to_even(D)
Print("\t The Overall Depth of beam = " + str(D) + "mm")
Print("\n")
Print(" \033[31m The Size of Beam ( bXD ) = " +str(b) + "mm X " + str(D) + "mm\033[0m")
Print("\n\n")

Print("\033[33mSTEP 3: Calculation of Effective Span (L)\033[0m \n")
Print("\n")

C1= l+b
C2= l+d

Print("\t L should be least of\n")
Print("\t\t L= clear span + width of beam = " + str(l) + "+" + str(b) + "="+ str(C1) + "mm\n")
Print("\t\t L = clear span + effective depth = " + str(l) + "+"+ str(d) + "=" + str(C2) + "mm \n")
Print("\n")
L= min(C1,C2)
L = round_to_even(L)

Print("\t \033[31mThe Effective Span L = " + str(L) +"mm\033[0m \n")
Print("\n")

Print("\033[33mSTEP 4: LOAD CALCULATION \033[0m \n")
Print("\n")

Dc= 25 #Density of Concrete
W1 = b*D*Dc/1000000
W1 = round(W1,2)
Print("\t 1. The self weight of beam W1= b*D*Dc \n")
Print("\t    Self weight of Beam W1 ="+ str(b/1000)+ "*"+ str(D/1000) + "*"+str(Dc) + "="+str(W1) + "kN/m\n")

W2= LL
Print("\t 2. Enter the Live Load W2 = "+ str(W2) +"kN/m\n")
W3 = DL
Print("\t 3.Enter the Dead load or UDL W3 = " + str(W3) + "kN/m\n")

W=W1+W2+W3
W = round (W,2)
Print( "\t \033[31m Total Service Load W = "+ str(W) + "kN/m \033[0m\n")
Print("\n")
Wu= 1.5*W
Wu= round(Wu,2)
Print("\t \033[31m Factored load Wu = "+ str(Wu) + "kN/m\033[0m\n")
print("\n")

Print("\033[33m STEP 5: CALCULATION OF MAXIMUM ULTIMATE BENDING MOMENT (Mu) \033[0m\n")
Print("\n")

Mu=Wu*((L/1000)**2)/8
Mu=round(Mu,2)
Print("\t For Simply Supported Beam \n\t Mu= Wu*L**2/8 \n")

Print ("\t\033[31m Bending Moment Mu = "+ str(Mu) + "kNm\033[0m \n")
Print("")

Print("\033[33m STEP 6: CHECK FOR EFFECTIVE DEPTH \033[0m\n")
Print("\n")

Es = 2*10**5 # Modulus of Elasticity of steel
fy = fy
Esu= (0.87*fy/Es)+0.002
Xu_max = (0.0035/(Esu+0.0035))*d
Print("\t\033[31m Since Fe"+str(fy) + "gradr steel is used;\n\t Hence Limiting depth of Neutral Axis = Xu_max/d = "+ str(round(Xu_max/d,2)) +".\33[0m\n")
Print("")

Mu_lim= Mu *10**6
Print("\t Now; \n")
Print("\t From cl:G1.1C IS 456:2000 \n")

Print("\t Mu_lim=0.36*(Xu_max/d)*(1-0.42*(Xu_max/d))*b*d_req**2*fck \n")
Print("")
d_req = math.sqrt(Mu_lim/((0.36*(Xu_max/d)*(1-0.42*(Xu_max/d))*b*fck)))
d_req = round(d_req,2)

DNA= round(Xu_max/d,2) #it is Xu_max/d

Print ("\t .: d_req = √((Mu_lim / ( 0.36*(Xu_max/d)*(1-0.42*(Xu_max/d))*b*fck))")

print("")
print("\t .: d_req = √((" + str(Mu_lim/1000000) + "*10**6/ (0.36*(" + str(DNA) + ")*(1-0.42*(" + str(DNA) + "))*" + str(b) + "*" + str(fck) + ")))")
print("")


Print("\t Effective depth required d_req= " + str(d_req)+ "mm \n")
print("")
if d_req<d:
    Print("\t\033[34m d_req < d_pro Hence Design is safe\033[0m\n")
else:
    Print("\t\033[34m d_req > d_pro: Design is NOT SAFE,Revise Effective depth provided\033[0m\n")
    raise SystemExit
print("")

Print("\033[33m STEP 7: DETERMINATION OF TYPE OF BEAM \033[0m\n ")

Mu_lim=(0.36*(Xu_max/d)*(1-0.42*(Xu_max/d))*b*d**2*fck)


Mu_lim = Mu_lim/1000000
Mu_lim = round(Mu_lim,2)

Print("\t From Cl:G1.1C IS 456:2000 \n")
Print("\t Mu_lim=(0.36*(Xu_max/d)*(1-0.42*(Xu_max/d))*b*d**2*fck)\n")


Print("\t .: Mu_lim = 0.36*"+ str(DNA) + "*(1-0.42*"+ str(DNA) + ")*"+ str(b) + "*" + str(d) +  "**2*"+ str(fck))

print("")

Print("\t Limiting Moment Mu_lim = "+ str(Mu_lim) + "kNm \n")
if Mu < Mu_lim:
    Print("\t\033[34m Mu < Mu_lim: Hence the Beam is Singly Reinforced Beam\033[0m\n")
else:
    Print("\t\033[34m Mu > Mu_lim: Hence the Beam is Doubly Reinforced Beam\033[0m\n")
    raise SystemExit
    
#Print("")

Print("\n\033[33m STEP 8: DESIGN OF REINFORCEMENTS \033[0m\n")
print("")

Print("\t From Cl: G1.1b IS 456:2000 \n")
Print("\t Mu= 0.87*fy*Ast_req*d*(1-(fy*Ast/(b*d*fck))) \n")
Print("\t"+str(Mu)+ "*10**6=0.87*"+ str(fy)+ "*Ast_req*d*(1-("+ str(fy) + "Ast_req/(b*d*"+ str(fck) + "))\n")
print("")

# Calculate the coefficients of the quadratic equation
Mu = Mu * 10**6
a = 0.87*fy*fy*d/(b*d*fck)
b1 = -0.87*fy*d
c = Mu
AA1 = round(a,2)
BB1 = round(b1,2)
CC1 = round(c,2)
import math
Print("\t"+ str(AA1) + "Ast_req**2-"+ str(BB1)+ "Ast_req +"+str(CC1) + "=0 \n")

def quadratic_solver(a, b1, c):
    discriminant = b1**2 - 4*a*c
    if discriminant < 0:
        print("No real roots")
    elif discriminant == 0:
        x = -b1 / (2*a)
        print("One real root: x = ", x)
    else:
        x1 = round((-b1 + math.sqrt(discriminant)) / (2*a),2)
        x2 = round((-b1 - math.sqrt(discriminant)) / (2*a),2)
        Ast_req = min (x1,x2)
        print("")
        Print("\t\033[31m.: Ast_req = "+str(Ast_req) + "mm**2\033[0m\n")
        return Ast_req
Ast_req=quadratic_solver(a, b1, c)

print("")

Print("\033[33m Now: Check for Minimum Reinforcements.\033[0m\n")
print("")
Print("\t From Cl:26.5.1.1 a\n")
Print("\t (Ast_min/(b*d))= 0.87/fy\n")
Print("\t Ast_min = (0.87*b*d)/fy \n")
Ast_min = 0.87*b*d/fy
Ast_min = round(Ast_min,2)
Print("\t Ast_min =0.87*"+ str(b) + "*"+ str(d) + "/fy\n")
Print("\n")
Print("\t\033[31m Minimum Reinforcements Ast_min ="+ str(Ast_min)+ "mm**2\033[0m\n")

Ast_req = max (Ast_min,Ast_req)
Print ("\t\033[31m .: Ast_req = " + str(Ast_req) + "mm**2\033[0m \n")
print("\n")

Print("\t Now assume diameter of bars\n")
phi = int(Input("\t Enter the diamer of bars: "))
ast = math.pi*phi**2/4
ast = round(ast,2)
N= (Ast_req/ast)
N = round_to_even(N)
Ast_pro = N*math.pi*phi**2/4
Ast_pro = round(Ast_pro,2)
Print("\n")
Print ("\t ast = Area of 1 bar \n")
Print ("\t ast = math.pi*phi**2/4 \n")
Print ("\t ast = π*"+ str(phi**2) + "/4")
Print ("\t ast = "+ str(ast)+ "mm**2\n")
Print ("\t Number of bars N= Ast_req/ast\n")
Print ("\t Number of bars N = "+  str(Ast_req)+ "/"+str(ast))
Print("\n")
Print ("\t\033[34m Provide "+ str(N) + "bars of"+ str(phi)+ "mm dia \033[0m\n")
Print("")
Print ("\t Ast_pro = N*math.pi*phi**2/4 \n")
Print ("\t Ast_pro = "+ str(N) + "* π *"+ str(phi**2) + "/4 \n")
Print("")
Print ("\t\033[031m Area of steel provided: Ast_pro ="+ str(Ast_pro) + "mm**2\033[0m \n")
Print ("")

print("\n\033[33m STEP 9: Design of Shear Reinforcements\033[0m\n")
Vu= (Wu*L)/2
Vu = round(Vu/1000,2)
Tv = Vu*1000/(b*d)
Tv= round(Tv,3)
Pt = 100*Ast_pro/(b*d)
Pt= round(Pt,3)


def calculate(Pt, fck):
    numerator = 0.85 * math.sqrt(0.8 * fck) * ((math.sqrt(1 + 5 * max(0.8 * fck / (6.89 * Pt), 1))) - 1)
    denominator = 6 * max(0.8 * fck / (6.89 * Pt), 1)
    result = round(numerator / denominator, 2)
    return result
result = calculate(Pt, fck)
Tc = result

Print("\t For Simply supported: \n")
Print("\t Shear force Vu = (Wu*L)/2  \n" )
Print("\t Shear force Vu = "+ str(Wu)+ "*" + str(L) + "*/2 \n")
Print("\t \033[31mShear force Vu= "+ str(Vu) + "kN\n\033[0m\n\n")
Print("\t Now:\n ")
Print("\t From cl:40.1 IS 456:2000 \n \t Nominal Shear Stress Tv = (Vu*1000)/(b*d) \n")
Print("\t Tv = ("+ str(Vu)+ "*1000)/("+ str(b)+ "*"+ str(d)+")\n")
Print ("\t \033[31mTv = "+ str(Tv)+ "N/mm**2")
print("\n\033[0m")
Print ("\t Pt = (100*Ast_pro)/(b*d)\n")
Print("\t Percentage of Steel in Tension Pt = (100*"+str(Ast_pro)+ ")/("+ str(b)+"*"+str(d)+ ")")
Print("\n\t \033[31mPercentage of Steel in Tension Pt = "+ str(Pt)+ "%\n\033[0m\n")
Print("\t From Table 19 IS 456:2000\n")
Print(" \t\033[31m Shear Strength of Concrete Tc = "+str(Tc)+ "N/mm**2\033[0m")
print("\n")

if Tv<0.5*Tc:
    Print("Since, Tv < 0.5*Tc \n \t.: No Shear Reinforcements are required; \033[34mDesign is Safe\033[0m")
    
elif Tv == Tc:
    Print("\n Since Tv <= Tc \n \t.: Minimum Shear Reinforcements are required")
    
    #Calculation of Area of Verticle Stirrups
    Print("\n\t From cl 26.5.1.6 IS 456:2000")
    d_1=int(Input("\n \t Enter the diameter of Verticle Stirrups d_1in mm: "))
    Asv = 2*(math.pi/4)*d_1**2
    Asv = round(Asv,2)
    Print("\n \t Area of 2 Legged Vertical Stirrups Asv = 2*(π/4)*d_1**2")
    Print("\n \t Asv = 2*(π/4)*"+str(d_1)+"**2")
    Print("\n \t Asv = "+ str(Asv)+ "mm**2")
    
    #Calculation of Spacing
    Sv = 0.87*fy*Asv/(0.4*b)
    Sv = round(Sv,2)
    Print("\n \t Spacing of Stirrups Sv = 0.87*fy*Asv/(0.4b)")
    Print("\n \t Sv = 0.87*"+str(fy)+"*"+str(Asv)+"/(0.4*"+str(b)+")")
    Print("\n \t Sv = "+str(Sv)+ "mm\n")
    Print(" \n\t From cl 26.5.1.5 IS 456:2000\n")
    Print(" \t Sv is least of Sv, 0.75d, 300mm ")
    
    Sv1 = 0.75*d
    Sv = min(Sv,Sv1,300)
    Print("\n\t .: Spacing Sv = "+ str(Sv)+" mm")
    
    Print("\n \t\033[31m Provide 2L "+str(d_1)+"mm Verticle Stirrups @ "+ str(Sv)+ "mm c/c \033[0m ")
    
else:
    Print("\n \t Since Tv > Tc;  Shear Reinforcements are required\n ")
    Vuc = Tc*b*d
    Vuc = Vuc/1000
    Vus = Vu - Vuc
    
    d_1=int(Input("\n \t Enter the diameter of Verticle Stirrups d_1in mm: "))
    Asv = 2*(math.pi/4)*d_1**2
    Asv = round(Asv,2)
    Sv = (0.87*fy*Asv*d)/(Vus*1000)
    Sv = round(Sv,2)
    
    Print("\n\n \t Shear Carried by Concrete Vuc = Tc*b*d ")
    Print("\n\t Shear Carried by Concrete Vuc = "+str(Tc)+ "*"+ str(b)+ "*"+str(d))
    Print("\n\n\033[31m\t Shear Carried by Concrete Vuc = "+str(Vuc)+ "kN\033[0m \n")
    Print("\n \t Shear Carried by stirrups Vus = Vu -Vuc ")
    Print("\n\t Shear Carried by stirrups Vus = "+str(Vu)+ "-"+str(Vuc)+"kN")
    Print("\n\n\t \033[31m Shear Carried by Stirrups Vus = "+str(Vus)+"kN\033[0m\n")
    
    Print("\n \t Area of 2 Legged Vertical Stirrups Asv = 2*(π/4)*d_1**2 ")
    Print("\n \t Asv = 2*(π/4)*"+str(d_1)+"**2 ")
    Print("\n \t Asv = "+ str(Asv)+ "mm**2 \n")
    
    Print("\n\t From cl. 40.4 aIS 456:2000\n")
    Print("\n\t Spacing of stirrups Sv= (0.87*fy*Asv*d_1)/(Vus*1000) ")
    Print("\n \t Sv = 0.87*"+str(fy)+ "*"+ str(Asv)+ "*" +str(d)+ "/"+ str(Vus*1000))
    Print ("\n \tSv = "+str(Sv)+ "mm\n")
    Print(" \n\n\t From cl 26.5.1.5 IS 456:2000\n")
    Print(" \t Sv is least of Sv, 0.75d, 300mm ")
    Sv = min (0.7*d,Sv,300)
    Sv = round(Sv,2)
    Print("\n \t\033[31m Provide 2L "+str(d_1)+"mm Verticle Stirrups @ "+ str(Sv)+ "mm c/c \033[0m \n")

Print("\n\033[33m STEP 10: CHECK FOR DEFLECTION CONTROL \033[0m\n")

Print("\n \t From Fig 4 IS 456:2000 ")
Print("\n \t Stress in Steel fs = 0.58*fy*Ast_req/Ast_pro\n")
fs= 0.58*fy*Ast_req/Ast_pro
fs = round(fs,2)
Print("\n \t Stress in steel fs = 0.58*"+str(fy)+"*"+ str(Ast_req)+"/"+str(Ast_pro)+"\n")
Print("\n \t \033[31m Stress in steel fs = "+str(fs)+"N/mm**2\n \033[0m")

Kf = 1
Kc = 1
Print("\n \tKf=1 , No Compression Steel ")
Print("\n \tKc =1 ,No Flanged Section \n")

#Kt Calculation
Kt=1/(0.225+0.00322*fs-0.625*math.log10(1/Pt))
Kt = round(Kt,2)
Print ("\n \tFrom Fig 4 IS 456:2000 ")
Print ("\n \t Kt = "+ str(Kt)+".\n")

Print("\n \t \033[33m NOW; \n\033[0m")
aa1= 20*Kt*Kf*Kc
aa1 = round(aa1,2)
bb1= L/d
bb1= round(bb1,2)
Print("\n \t (L/d)max = 20*Kt*Kf*Kc")
Print("\n \t (L/d)max =20*"+str(Kt)+"*"+str(Kf)+"*"+str(Kc))
Print("\n \t (L/d)max= "+str(aa1)+" \n")
Print("\n \t (L/d)pro = "+str(bb1))
Print("\n")
if aa1<bb1:
    Print("\n Since (L/d)max < (L/d)pro \n BEAM IS NOT SAFE IN DEFLECTION\n \033[34m HENCE THE DESIGN IS NOT SAFE \n INCREASE THE EFFECTIVE DEPTH AND REDESIGN THE BEAM\033[0m ")
else:
    Print("\n \033[034m Since (L/d)max > (L/d)pro \n DEFLECTION CONTROL IS SATISFACTORY: HENCE SAFE\033[0m ")

