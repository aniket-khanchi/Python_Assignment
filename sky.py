# import plotly_express as px
# import pandas as pd
# list=[];
# for rec in range(120,240):
#  list_rec = rec/60;
#  list.append(list_rec)
# x = []; pdf_list = []
# exp_const, f_exp_pwr, s_exp_pwr, F, G, H , I = 2.718281828, 3, 7, 0, 0, 0, 0
# for i in list:
#     lwr_lim = i; upr_lim = i+1/60
#     F = -abs(lwr_lim*f_exp_pwr); G = -abs(upr_lim*f_exp_pwr)
#     H = -abs(lwr_lim*s_exp_pwr); I = -abs(upr_lim*s_exp_pwr)
#     num1 = -abs(0.3131); num2 = -abs(0.0952)
#     eqn1 = exp_const**G - exp_const**F; eqn2 = exp_const**I - exp_const**H
#     eqn3 = num1*eqn1; eqn4 = num2*eqn2; pdf_eqn = eqn3 + eqn4
#     x.append(lwr_lim*60)
#     pdf_list.append(pdf_eqn*60) 
# #Label the axes and show the plot
# pdf_df = pd.DataFrame(data=pdf_list, index=x)
# pdf_fig = px.line(pdf_df, x=x, y=pdf_list, title='Probability Density Function',labels=dict(x="minutes", y="y") )
# mean = 125; q1 = 147; q2 = 143; q3 = 188;
# pdf_fig.add_vline(x=mean, line_width=1, line_color="green")
# pdf_fig.add_vline(x=q1, line_width=1, line_color="red")
# pdf_fig.add_vline(x=q2, line_width=1, line_color="red")
# pdf_fig.add_vline(x=q3, line_width=1, line_color="red")
# pdf_fig.show()
# #show the histogram
# hist_df = pd.DataFrame(data=pdf_list, index=x)
# hist_fig = px.histogram(hist_df, x=pdf_list, title='Histogram')
# hist_fig.show()


import matplotlib.pyplot as plt
import numpy as np

# import pandas as pd

pdf = lambda y: (((328/99)*y*np.exp(-2*y**2)) + ((204/99)*y*np.exp(-6*y**2))) 

time_list = [] #in minutes
pdf_out = []
# def pdf_out(p):
for i in range(120,240): #starting from 120 mins -2hr to 240 mins - 4hr
    hour = i/60
    time_list.append(i)
    pdf_out.append(pdf(hour)*60)
#computing mean, variance & Standard deviation
m = np.mean(pdf_out)
print(m)
v = np.var(pdf_out)
print(v)
quartiles = np.percentile(pdf_out,[25,50,75])


print(quartiles)

fig = plt.figure(figsize=(12, 6))

ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax.set_title('Full view')

ax.axhline(m, 0, 1, label='mean',color="green",linestyle="--")
ax.axhline(v, 0, 1, label='variance',color="purple",linestyle="-.")
ax.axhline(quartiles[0], 0, 1, label='25%',color="black")
ax.axhline(quartiles[1], 0, 1, label='50%',color="blue")
ax.axhline(quartiles[2], 0, 1, label='75%',color="orange")
ax.plot(time_list, pdf_out)  # Plot the chart

ax2.set_title('Truncated view')
ax2.axhline(m, 0, 1, label='mean',color="green",linestyle="--")
ax2.axhline(v, 0, 1, label='variance',color="purple",linestyle="-.")
ax2.axhline(quartiles[0], 0, 1, label='25%',color="black")
ax2.axhline(quartiles[1], 0, 1, label='50%',color="blue")
ax2.axhline(quartiles[2], 0, 1, label='75%',color="orange")
ax2.plot(time_list, pdf_out)  # Plot the chart
ax2.set_ylim([-0.0025, 0.01])



# plt.hist(pdf_out,bins =10)
ax.set_xlabel("Time in minutes")
ax.set_ylabel("PDF")

plt.show()  # display




