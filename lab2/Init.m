%%% Physical constants of the helicopter %%%
la = 0.63;  % Distance from elevation axis to helicopter body [m]
lh = 0.18;  % Distance from pitch axis to motor [m]
Kf = 0.25;  % Force constant, motor [N/V]
Je = 0.83;  % Moment of inertia for elevation [kg m^2]
Jt = 0.83;  % Moment of inertia for travel [kg m^2]
Jp = 0.034; % Moment of inertia for pitch [kg m^2]
mh = 1.05;  % Mass of helicopter [kg]
mw = 1.87;  % Balance weight [kg]
mg = 0.05;  % Effective mass of helicopter [kg]
Kp = 0.49;  % Force to lift the helicopter form the ground [N]

K1 = Kf*lh / Jp;
K2 = Kp*la / Jt;

%%% CONTROLLER VARIABLES %%%
Kpp = 0.1;
Kpd = 0.4;

%%% CONTINOUS TIME MODEL %%%
% x_dot = A_c*x + B_c * u
% x = [travel, 
%      travelrate,
%      pitch,
%      pitchrate]
% u = pitch_setpoint
Ac = [0, 1,       0,       0;
      0, 0,     -K2,       0;
      0, 0,       0,       1;
      0, 0, -K1*Kpp, -K1*Kpd];

Bc = [     0;
           0;
           0;
      K1*Kpp];

Cc = eye(4);
continous_heli_model = ss(Ac, Bc, Cc, 0);

%%% DISCRETE TIME MODEL %%%
Ts = 0.1;
discrete_heli_model = c2d(continous_heli_model, Ts, 'foh');

%%% PLOT STEP RESPONSE OF CONTINOUS TIME MODEL %%%
figure(1);
step(continous_heli_model, 50);
title(sprintf('Step-response (continous model) with Kpp = %-5.2f, Kpd = %-5.2f', Kpp, Kpd));

%%% PLOT STEP RESPONSE OF DISCRETE TIME MODEL %%%
figure(2);
step(discrete_heli_model, 50);
title(sprintf('Step-response (discrete model) with Kpp = %-5.2f, Kpd = %-5.2f', Kpp, Kpd));


%%% OPTIMAL TRAJECTORY %%%
travel_startpoint = pi;
travel_endpoint = 0;