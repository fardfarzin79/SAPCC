

Ex_1 = ex_1*m_1
Ex_2 = ex_2*m_2
Ex_2_1 = ex_2_1*m_2_1
Ex_3= ex_3*m_3
Ex_4 = ex_4*m_4
Ex_5 = ex_5*m_5
Ex_6 = ex_6*m_6
Ex_7 = ex_7*m_7
Ex_8 = ex_8*m_8
Ex_8_1 = ex_8_1*m_8_1
Ex_9 = ex_9*m_9
Ex_10 = ex_10*m_10
Ex_11 = ex_11*m_11

#Fuel, Product, and Destruction of Exergy in KW

#Absorber
Ex_F_abs = Ex_1+Ex_2+Ex_2_1
Ex_p_abs = Ex_4
Ex_loss_abs = Ex_3
Ex_D_abs = Ex_F_abs-Ex_p_abs
psi_abs = Ex_p_abs/Ex_F_abs

#pump
Ex_F_pump = Ex_4+w_pump
Ex_P_pump = Ex_5
Ex_D_pump = Ex_F_pump-Ex_P_pump
psi_pump = Ex_P_pump/Ex_F_pump

#Heat exchanger
Ex_F_HX = Ex_7-Ex_9
Ex_P_HX = Ex_6-Ex_5
Ex_D_HX = Ex_F_HX-Ex_P_HX
psi_HX = Ex_P_HX/Ex_F_HX


Ex_F_ST = Ex_6+W_reb+W_cond
Ex_P_ST = Ex_8+Ex_7+Ex_8_1
Ex_D_ST = Ex_F_ST-Ex_P_ST
psi_ST = Ex_P_ST/Ex_F_ST

#cooler
Ex_F_CO = Ex_10+W_CO
Ex_P_CO = Ex_11
Ex_D_CO = Ex_F_CO-Ex_P_CO
psi_CO = Ex_P_CO/Ex_F_CO



psi_plant = (Ex_p_abs+Ex_P_pump+Ex_P_HX+Ex_P_ST+Ex_P_CO)/(Ex_F_abs+Ex_F_pump+Ex_F_HX+Ex_F_ST+Ex_F_CO)


##########ECONOMIC



C_captotal = Z_absorber_capital+Z_pump_capital+Z_HX_capital+Z_stripper_capital+Z_cooler_capital 
h = 8000
Z_dot_absorber = ((Z_absorber_capital+Z_absorber_op)/h)*(Z_absorber_capital/C_captotal)

Z_dot_pump = ((Z_pump_capital+Z_pump_op)/h)*(Z_pump_capital/C_captotal)

Z_dot_HX = ((Z_HX_capital+Z_HX_op)/h)*(Z_HX_capital/C_captotal)

Z_dot_stripper = ((Z_stripper_capital+Z_stripper_op)/h)*(Z_stripper_capital/C_captotal)

Z_dot_cooler = ((Z_cooler_capital+Z_cooler_op)/h)*(Z_cooler_capital/C_captotal)


c_4 = (Z_dot_absorber+(c_2*Ex_2*0.0036+c_1*Ex_1*0.0036-c_3*Ex_3*0.0036))/(Ex_4*0.0036)
       
C_D_absorber = (c_1+c_2)*(Ex_D_abs+Ex_loss_abs)*0.0036
r_abs = c_4-c_2/c_2

f_abs = (Z_absorber_capital/h)/((Z_absorber_capital/h)+C_D_absorber)

#cooler

c_10 =  c_2
#((c_2*Ex_2*0.0036)+Z_dot_cooler+(c_power_cooler*W_CO*0.0036))/(Ex_10*0.0036)
C_D_cooler = (c_power_cooler+c_10)*(Ex_D_CO)*0.0036
r_cooler = (c_2-c_10)/c_10
f_cooler = (Z_cooler_capital/h)/((Z_cooler_capital/h)+C_D_cooler)

#pump
c_5 = c_power_pump+(((c_4*Ex_4*0.0036)+Z_dot_pump+(c_power_pump*w_pump*0.0036))/(Ex_5*0.0036))
C_D_pump = (c_4+c_power_pump)*(Ex_D_pump)*0.0036
r_pump = (c_5-c_4-c_power_pump)/(c_4+c_power_pump)
f_pump = (Z_pump_capital/h)/((Z_pump_capital/h)+C_D_pump)

#HX

c_9 = (c_10*Ex_10)/Ex_9

c_6 = c_5 #p role
c_7 = (((c_6*Ex_6*0.0036)-c_5*Ex_5*0.0036)+(c_9*Ex_9*0.0036)-Z_dot_HX)/(Ex_7*0.0036)
C_D_HX = (c_7)*Ex_D_HX*0.0036
r_HX = (c_6-(c_7-c_9))/(c_7-c_9)
f_HX = (Z_HX_capital/h)/((Z_HX_capital/h)+C_D_HX)

#STRIPPER

c_8 = c_heat+c_power_cooler+((Z_dot_stripper+(c_6*Ex_6*0.0036)+(c_heat*W_reb*0.0036)+(c_power_cooler*W_cond*0.0036)-(c_7*Ex_7*0.0036))/(Ex_8*0.0036))
C_D_stripper = (c_6+(c_heat)+(c_power_cooler))*Ex_D_ST*0.0036
r_stripper = ((c_8+c_7)-c_6-(c_heat)-c_power_cooler)/(c_6+(c_heat)+c_power_cooler)
f_stripper = (Z_stripper_capital/h)/((Z_stripper_capital/h)+C_D_stripper)

#total
c_fuel = c_2+c_heat+c_power_pump+c_power_cooler
c_product = c_7+c_8
r_plant = (c_product-c_fuel)/c_fuel
C_D_plant = c_fuel*(Ex_D_ST+Ex_D_abs+Ex_D_pump+Ex_D_HX+Ex_D_CO)*0.0036
f_plant = (C_captotal/h)/((C_captotal/h)+C_D_plant)