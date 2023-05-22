%Variáveis extraidas do simulink
t = out.tout(2:end);
cos_int = out.simout(2:end,1);
cos_ddt = out.simout(2:end,2);
sin = out.simout(2:end,3);


plot(t,sin,'r',t,cos_int,'b',t,cos_ddt,'g--','LineWidth',2)
legend(' Seno',' Cosseno-Integral',' Cosseno-Derivada','FontSize',25)
xlabel('Tempo [s]','FontSize',30)
ylabel('Amplitude','FontSize',30)
ax = gca;
ax.FontSize = 30;
grid on
