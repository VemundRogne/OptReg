clc
clear all
%% Initialization and model definition
init06;

Ac = [0, 1,       0,       0,       0,        0 ;
      0, 0,     -K_2,      0,       0,        0 ;
      0, 0,       0,       1,       0,        0 ;
      0, 0, -K_1*K_pp, -K_1*K_pd,   0,        0 ;
      0, 0,       0,       0,       0,        1 ;
      0, 0,       0,       0,    -K_3*K_ep, -K_3*K_ed; ];

Bc = [     0,     0;
           0,     0;
           0,     0;
      K_1*K_pp,   0;
           0,     0;
           0,   K_3*K_ep];

% Discrete time system model.
delta_t	= 0.25; % sampling time
Ad = eye(6) + (delta_t.*Ac);
Bd = (delta_t.*Bc);

%% Initial values and constraints
% Number of states and inputs
mx = size(Ad,2); % Number of states (number of columns in A)
mu = size(Bd,2); % Number of inputs(number of columns in B)

% Trajectory start and end values
lambda_0 = pi;
lambda_f = 0;
% Initial values
x1_0 = lambda_0;                        % Lambda
x2_0 = 0;                               % r
x3_0 = 0;                               % p
x4_0 = 0;                               % p_dot
x5_0 = 0;                               % e
x6_0 = 0;                               % e_dot
x0 = [x1_0 x2_0 x3_0 x4_0 x5_0 x6_0]';            % Initial values


% Time horizon and initialization
N  = 40;                               % Time horizon for states
M  = N;                                 % Time horizon for inputs
z  = zeros(N*mx+N*mu,1);                % Initialize z for the whole horizon
z0 = z;                                 % Initial value for optimization

% Bounds
ul 	    = -30*pi/180;                   % Lower bound on control
uu 	    = -ul;                          % Upper bound on control

xl      = -Inf*ones(mx,1);              % Lower bound on states (no bound)
xu      = Inf*ones(mx,1);               % Upper bound on states (no bound)
xl(3)   = ul;                           % Lower bound on state x3
xu(3)   = uu;                           % Upper bound on state x3
% Generate constraints on measurements and inputs
[vlb,vub]       = gen_constraints(N,M,xl,xu,ul,uu); % hint: gen_constraints
vlb(N*mx+M*mu)  = 0;                    % We want the last input to be zero
vub(N*mx+M*mu)  = 0;                    % We want the last input to be zero

% We also have a nonlinear constraint as a function: nonlincon
Aeq = gen_aeq(Ad,Bd,N,mx,mu);          % Generate A, hint: gen_aeq
beq = zeros(size(Aeq, 1), 1);             % Generate b
A0x0 = Ad*x0;
beq(1:size(A0x0,1), :) = A0x0;
%% Cost function
q_1 = 1;
q_2 = 10;
cost_func = @(x) sum((x(1:mx:mx*N) - lambda_f).^2) + sum(q_1*x(N*mx+1:mu:N*mu+N*mx).^2) + sum(q_2*x(N*mx+2:mu:N*mu+N*mx).^2);
nonlcon = @nonlincon;

[z, fval] = fmincon(cost_func, z0, [], [], Aeq, beq, [], [], nonlcon);

%% Extract control inputs and states
u1  = [z(N*mx+1:2:N*mx+M*mu)]; % Control input from solution
u2  = [z(N*mx+2:2:N*mx+M*mu)];

x1 = [x0(1);z(1:mx:N*mx)];              % State x1 from solution
x2 = [x0(2);z(2:mx:N*mx)];              % State x2 from solution
x3 = [x0(3);z(3:mx:N*mx)];              % State x3 from solution
x4 = [x0(4);z(4:mx:N*mx)];              % State x4 from solution
x5 = [x0(5);z(5:mx:N*mx)];
x6 = [x0(6);z(6:mx:N*mx)];

num_variables = 5/delta_t;
zero_padding = zeros(num_variables,1);
unit_padding  = ones(num_variables,1);

u1   = [zero_padding; u1; zero_padding];
u2   = [zero_padding; u2; zero_padding];
x1  = [pi*unit_padding; x1; zero_padding];
x2  = [zero_padding; x2; zero_padding];
x3  = [zero_padding; x3; zero_padding];
x4  = [zero_padding; x4; zero_padding];
x5  = [zero_padding; x5; zero_padding];
x6  = [zero_padding; x6; zero_padding];
x = [x1 x2 x3 x4 x5 x6];

timesteps = 0:delta_t:delta_t*(length(x1)-1);
%u_opt = timeseries(u, timesteps);
%x_opt = timeseries(x, timesteps);

plot(timesteps, x)
legend('Travel', 'travelrate', 'pich', 'pitchrate', 'elevation', 'elevationrate')
