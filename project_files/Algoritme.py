class Algoritme():
    from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from matplotlib.pyplot import plot, title, show, legend

agents_thuis = [1,1,1,1,1]
agents_uit = [1,1,1,11,1]
sonic_thuis = [1,3,2,7,4]
sonic_uit = [3,5,2,1,0]
n=10 # aantal uitslagen
t = linspace(0,9,n) # aantal uitslagen om er een lijn van te maken
xn = agents_uit + agents_thuis

# Linear regressison -polyfit - polyfit can be used other orders polys
(ar, br) = polyfit(t, xn, 1)
xr = polyval([ar, br], t)
# compute the mean square error
err = sqrt(sum((xr - xn)**2)/n)
print('Linear regression using polyfit')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, ms error= %.3f' % (a, b, ar, br, err))
print('\n')


# Linear regression using stats.linregress
(a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
print('Linear regression using stats.linregress')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, std error= %.3f' % (a,b,a_s,b_s,stderr))
print('\n')

# matplotlib ploting
title('Linear Regression Example')
# plot(t, x,'g.--')
plot(t, xn, 'k.')
plot(t, xr, 'r.-')
legend(['scores','regression'])
show();