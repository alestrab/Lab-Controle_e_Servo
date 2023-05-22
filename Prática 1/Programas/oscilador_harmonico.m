%Variáveis extraidas do simulink
t = out.tout;
u = out.simout(:,1);
x = out.simout(:,2);
v = out.simout(:,3);
k = out.simout(:,4);

%Energia em função do deslocamento
subplot(2,2,1)
plot(x,k,'r',x,u,'b','LineWidth',2)
legend(' Cinética',' Potencial','FontSize',15)
xlabel('Deslocamento [m]','FontSize',20)
ylabel('Energia [J]','FontSize',20)
ax = gca;
ax.FontSize = 15;
grid on

%Energia em função da velocidade
subplot(2,2,3)
plot(v,k,'r',v,u,'b','LineWidth',2)
legend(' Cinética',' Potencial','FontSize',15)
xlabel(' Velocidade [m/s]','FontSize',20)
ylabel('Energia [J]','FontSize',20)
ax = gca;
ax.FontSize = 15;
grid on

%Velocidade em função do deslocamento
subplot(1,2,2)
plot(x,v,'r','LineWidth',2)
xlabel('Deslocamento [m]','FontSize',20)
ylabel('Velocidade [m/s]','FontSize',20)
ax = gca;
ax.FontSize = 15;
grid on