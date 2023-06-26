clear
clc
%Parametros do sistema
tal=8e-5;
R=2.8614;
L=R*tal;
tal_m=3;
b=0.00071;
J=tal_m*b;
Ke=0.0921;
Kt=0.0921;

Ta=L/R;
Tb=J/b;
Tm=R*J/(Ke*Kt);
%Funcoes de transferencia
s=tf('s');
%Primeira Ordem
tf1 = tf(1/(Ke*Tm),[1,(1/Tm)+(1/Tb)]);
%Segunda Ordem
tf2 = tf(1/(Ke*Tm*Ta),[1,(1/Tm)+(1/Tb),((1/Tm)+(1/Tb))/Ta]);

%Função da fonte
N=1000;
tf=3.26;
t = linspace(0,tf,N)';
v_ref=11.58;
v = (v_ref*(1-exp(-5.8819*t)));

subplot(2,2,1)
y_1=lsim(tf1,v,t);
y_2=lsim(tf2,v,t);
plot(t,y_1,'b-',t,y_2,'g-')
title('Velocidade [rad/s]')
subplot(2,2,2)
ktaco=0.0208;
y_1_taco=lsim(tf1,v,t)*ktaco;
y_2_taco=lsim(tf2,v,t)*ktaco;
plot(t,y_1,'b-',t,y_2,'g-')
title('Vtaco [V]')
subplot(2,2,3)
y_1=lsim(tf1,v,t)*30/pi;
y_2=lsim(tf2,v,t)*30/pi;
plot(t,y_1,'b-',t,y_2,'g-')
title('Velocidade [RPM]')
subplot(2,2,4)
plot(t,v)
title('Tensão na Fonte [V]')

%Tabela
T = table(t,y_1_taco, y_2_taco);
writetable(T, 'vtaco_matlab.txt','Delimiter','\t');
