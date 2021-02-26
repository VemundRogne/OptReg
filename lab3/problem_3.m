init05; % Change this to the init file corresponding to your helicopter

% Continous time model
Ac = [0, 1,       0,       0;
      0, 0,     -K_2,       0;
      0, 0,       0,       1;
      0, 0, -K_1*K_pp, -K_1*K_pd];

Bc = [     0;
           0;
           0;
      K_1*K_pp];

% Discrete time system model. x = [lambda r p p_dot]'
delta_t	= 0.25; % sampling time
Ad = eye(4) + (delta_t.*Ac);
Bd = (delta_t.*Bc);

Q = diag([1, 1, 1, 1]);
R = diag([1, 1, 1, 1]);

[K, S, e] = dlqr(Ad, Bd, Q, R)