

Ex_1  = ex_1*m_1
Ex_2 = ex_2*m_2
Ex_2_1 = ex_2_1*m_2_1
Ex_2_2 = ex_2_2*m_2_2
Ex_2_3 = ex_2_3*m_2_3
Ex_3 = ex_3*m_3
Ex_4 = ex_4*m_4
Ex_5 = ex_5*m_5
Ex_6 = ex_6*m_6
Ex_7 = ex_7*m_7
Ex_8 = ex_8*m_8
Ex_9 = ex_9*m_9
Ex_10 = ex_10*m_10
Ex_10_1 = ex_10_1*m_10_1
Ex_11 = ex_11*m_11
Ex_12  = ex_12*m_12
Ex_13 = ex_13*m_13
Ex_14 = ex_14*m_14
Ex_15 = ex_15*m_15
Ex_16 = ex_16*m_16
Ex_17 = ex_17*m_17
Ex_18 = ex_18*m_18
Ex_19 = ex_19*m_19
Ex_20 = ex_20*m_20
Ex_21  = ex_21*m_21
Ex_22 = ex_22*m_22
Ex_23 = ex_23*m_23
Ex_24 = ex_24*m_24
Ex_25 = ex_25*m_25
Ex_26 = ex_26*m_26


#Absorber
Ex_F_abs = Ex_1+Ex_2+Ex_2_1+Ex_2_2+Ex_2_3
Ex_p_abs = Ex_4
Ex_loss_abs = Ex_3
Ex_D_abs = Ex_F_abs-Ex_p_abs
psi_abs = Ex_p_abs/Ex_F_abs

#pump
Ex_F_pump = Ex_4+w_pump
Ex_P_pump = Ex_5
Ex_D_pump = Ex_F_pump-Ex_P_pump
psi_pump = Ex_P_pump/Ex_F_pump

#HX
Ex_F_HX = Ex_24-Ex_25
Ex_P_HX = Ex_8-Ex_6
Ex_D_HX = Ex_F_HX-Ex_P_HX
psi_HX = Ex_P_HX/Ex_F_HX

#SEPERATOR RVC
Ex_F_sep_R = Ex_9
Ex_P_sep_R = Ex_10+Ex_12
Ex_D_sep_R = Ex_F_sep_R-Ex_P_sep_R
psi_sep_R = Ex_P_sep_R/Ex_F_sep_R

#compressor
Ex_F_compr = w_compr+Ex_10
Ex_P_compr = Ex_11
Ex_D_compr = Ex_F_compr-Ex_P_compr
psi_compr = Ex_P_compr/Ex_F_compr

#cooler comp
Ex_F_cooler_2 = w_cooler_2+Ex_10_1
Ex_P_cooler_2 = Ex_11
Ex_D_cooler_2 = Ex_F_cooler_2-Ex_P_cooler_2
psi_cooler_2 = Ex_P_cooler_2/Ex_F_cooler_2

#solar section
#coolector
Ex_F_col = Ex_14+solar
Ex_P_col = Ex_15
Ex_D_col = Ex_F_col-Ex_P_col
psi_col = Ex_P_col/Ex_F_col

# solar separator
Ex_F_sep_solar = Ex_15
Ex_P_sep_solar = Ex_16+Ex_17
Ex_D_sep_solar = Ex_F_sep_solar-Ex_P_sep_solar
psi_sep_solar = Ex_P_sep_solar/Ex_F_sep_solar

#cooler solvent
Ex_F_cooler = w_cooler+Ex_25
Ex_P_cooler = Ex_26
Ex_D_cooler = Ex_F_cooler-Ex_P_cooler
psi_cooler = Ex_P_cooler/Ex_F_cooler

#sepertaor LVC
Ex_F_sepl = Ex_20
Ex_P_sepl = Ex_21+Ex_24
Ex_D_sepl = Ex_F_sepl-Ex_P_sepl
psi_sepl = Ex_P_sepl/Ex_F_sepl

#compressor
Ex_F_compl = w_compl+Ex_21
Ex_P_compl = Ex_22
Ex_D_compl = Ex_F_compl-Ex_P_compl
psi_compl = Ex_P_compl/Ex_F_compl

#cooler compr
Ex_F_cooler_2l = w_cooler_2l+Ex_22
Ex_P_cooler_2l = Ex_23
Ex_D_cooler_2l = Ex_F_cooler_2l-Ex_P_cooler_2l
psi_cooler_2l = Ex_P_cooler_2l/Ex_F_cooler_2l


#stripper
Ex_F_st = Ex_7+Ex_11+Ex_13+w_reboiler+w_cond+Ex_16+Ex_17+Ex_23
Ex_P_st = Ex_18+Ex_19
Ex_D_st = Ex_F_st-Ex_P_st
psi_st = Ex_P_st/Ex_F_st


psi_plant = (Ex_p_abs+Ex_P_pump+Ex_P_HX+Ex_P_sep_R+Ex_P_compr+Ex_P_cooler_2+Ex_P_col+Ex_P_sep_solar+Ex_P_cooler+Ex_P_sepl+Ex_P_compl+Ex_P_cooler_2l+Ex_P_st)/(Ex_F_abs+Ex_F_pump+Ex_F_HX+Ex_F_sep_R+Ex_F_compr+Ex_F_cooler_2+Ex_F_col+Ex_F_sep_solar+Ex_F_cooler+Ex_F_sepl+Ex_F_compl+Ex_F_cooler_2l+Ex_F_st)



C_captotal = Z_absorber_capital+Z_pump_capital+Z_HX_capital+Z_capital_solar+Z_stripper_capital+3*Z_cooler_capital+2*Z_capital_comp+3*Z_capital_seperator 
h = 8000

Z_dot_absorber = ((Z_absorber_capital+Z_absorber_op)/h)*(Z_absorber_capital/C_captotal)
Z_dot_pump = ((Z_pump_capital+Z_pump_op)/h)*(Z_pump_capital/C_captotal)

Z_dot_HX = ((Z_HX_capital+Z_HX_op)/h)*(Z_HX_capital/C_captotal)

Z_dot_stripper = ((Z_stripper_capital+Z_stripper_op)/h)*(Z_stripper_capital/C_captotal)

Z_dot_cooler = ((Z_cooler_capital+Z_cooler_op)/h)*(Z_cooler_capital/C_captotal)

Z_dot_sep = ((Z_capital_seperator+Z_seperator_op)/h)*(Z_capital_seperator/C_captotal)

Z_dot_comp_1 = ((Z_capital_comp+Z_comp_op)/h)*(Z_capital_comp/C_captotal)
Z_dot_comp_2 = ((Z_capital_comp+Z_comp_op)/h)*(Z_capital_comp/C_captotal)

#absorber
c_4 = (Z_dot_absorber+(1.5*Ex_2_3*0.0036+c_2*Ex_2_1*0.0036+c_2*Ex_2_1*0.0036+c_2*Ex_2*0.0036+c_1*Ex_1*0.0036-c_3*Ex_3*0.0036))/(Ex_4*0.0036)
       
C_D_absorber = (c_1+c_2+1.5)*(Ex_D_abs+Ex_loss_abs)*0.0036
r_abs = (c_4-c_2-1.5)/(c_2+1.5)

f_abs = (Z_absorber_capital/h)/((Z_absorber_capital/h)+C_D_absorber)

#pump
c_5 = c_power_pump+(((c_4*Ex_4*0.0036)+Z_dot_pump+(c_power_pump*w_pump*0.0036))/(Ex_5*0.0036))
C_D_pump = (c_4+c_power_pump)*(Ex_D_pump)*0.0036
r_pump = (c_5-c_4-c_power_pump)/(c_4+c_power_pump)
f_pump = (Z_pump_capital/h)/((Z_pump_capital/h)+C_D_pump)

#cooler

c_25 =  c_2

#((c_2*Ex_2*0.0036)+Z_dot_cooler+(c_power_cooler*W_CO*0.0036))/(Ex_10*0.0036)
C_D_cooler = (c_power_cooler+c_25)*(Ex_D_cooler)*0.0036
r_cooler = (c_2-c_25)/c_25
f_cooler = (Z_cooler_capital/h)/((Z_cooler_capital/h)+C_D_cooler)

#HX
c_6 = c_5 #p role
c_24 = (Z_dot_HX+((c_5*Ex_8*0.0036-c_6*Ex_6*0.0036))+(c_25*Ex_25*0.0036))/(Ex_24*0.0036)
C_D_HX = (c_24-c_25)*Ex_D_HX*0.0036
r_HX = (c_6-(c_24-c_25))/(c_24-c_25)
f_HX = (Z_HX_capital/h)/((Z_HX_capital/h)+C_D_HX)

#seperator


c_8 = c_6
c_9 = c_8
c_12 = c_9
c_10 = ((c_9*Ex_9*0.0036)-(c_9*Ex_10*0.0036)+Z_dot_sep)/(Ex_10*0.0036)
C_D_sepr = c_9*Ex_D_sep_R*0.0036
r_sepr = ((c_12+c_10)-c_9)/c_9
f_sepr = (Z_capital_seperator/h)/((Z_capital_seperator/h)+C_D_sepr)

#comp rvc
c_10_1 = c_power_pump+(((c_10*Ex_10*0.0036)+Z_dot_comp_1+(c_power_pump*w_compr*0.0036))/(Ex_10_1*0.0036))
C_D_compr = (c_10+c_power_pump)*Ex_D_compr*0.0036
r_compr = (c_10_1-c_power_pump-c_10)/(c_power_pump+c_10)
f_compr = (Z_capital_comp/h)/((Z_capital_comp/h)+C_D_compr)

#cooler comp
c_11= c_10_1
C_D_cooler_2 = (c_power_cooler+c_10_1)*(Ex_D_cooler_2)*0.0036
r_cooler_2 = (c_11-c_10_1)/c_10_1
f_cooler_2 = (Z_cooler_capital/h)/((Z_cooler_capital/h)+C_D_cooler_2)


#solar coolector
c_14 = c_10
c_15 = c_14

#sep solar 
c_17 = c_15
c_16 = ((c_15*Ex_15*0.0036)-(c_17*Ex_17*0.0036)+Z_dot_sep)/(Ex_16*0.0036)
C_D_sep_solar = c_15*Ex_D_sep_solar*0.0036
r_sep_solar = ((c_16+c_17)-c_15)/c_15
f_sep_solar = (Z_capital_seperator/h)/((Z_capital_seperator/h)+C_D_sep_solar)


#seperator lvc


c_21 = c_24
c_20 = ((c_21*Ex_21*0.0036)+(c_24*Ex_24*0.0036)-Z_dot_sep)/(Ex_20*0.0036)
C_D_sepl = c_20*Ex_D_sepl*0.0036
r_sepl = ((c_21+c_24)-c_20)/c_20
f_sepl = (Z_capital_seperator/h)/((Z_capital_seperator/h)+C_D_sepl)

#comp
c_22 = c_power_pump+(((c_21*Ex_21*0.0036)+Z_dot_comp_2+(c_power_pump*w_compl*0.0036))/(Ex_22*0.0036))
C_D_comp = (c_21+c_power_pump)*Ex_D_compl*0.0036
r_comp = (c_22-c_power_pump-c_21)/(c_power_pump+c_21)
f_comp = (Z_capital_comp/h)/((Z_capital_comp/h)+C_D_comp)

#cooler comp
c_23 = c_22
C_D_cooler_2l = (c_power_cooler+c_22)*(Ex_D_cooler_2l)*0.0036
r_cooler_2l = (c_23-c_22)/c_22
f_cooler_2l = (Z_cooler_capital/h)/((Z_cooler_capital/h)+C_D_cooler_2l)

#stripper
c_18 = c_heat+c_power_cooler+((Z_dot_stripper+(c_5*Ex_7*0.0036)+(c_11*Ex_11*0.0036)+(c_12*Ex_13*0.0036)+(c_16*Ex_16*0.0036)+(c_17*Ex_17*0.0036)+(c_23*Ex_23*0.0036)+(c_heat*w_reboiler*0.0036)+(c_power_cooler*w_cond*0.0036)-(c_20*Ex_19*0.0036))/(Ex_18*0.0036))
C_D_stripper = (c_5+c_11+c_12+c_16+c_17+c_23+(c_heat)+(c_power_cooler))*Ex_D_st*0.0036
r_stripper = ((c_18+c_20)-c_5-c_11-c_12-c_16-c_17-c_23-(c_heat)-c_power_cooler)/(c_5+c_11+c_12+c_16+c_17+c_23+(c_heat)+c_power_cooler)
f_stripper = (Z_stripper_capital/h)/((Z_stripper_capital/h)+C_D_stripper)

#total
c_fuel = c_2+c_heat+c_power_pump+c_power_cooler
c_product = c_18+c_20
r_plant = (c_product-c_fuel)/c_fuel
C_D_plant = c_fuel*(Ex_D_st+Ex_D_abs+Ex_D_pump+Ex_D_compr+Ex_D_HX+Ex_D_cooler_2+Ex_D_cooler+Ex_D_sep_R+Ex_D_sepl+Ex_D_cooler_2l+Ex_D_compl+Ex_D_col)*0.0036
f_plant = (C_captotal/h)/((C_captotal/h)+C_D_plant)