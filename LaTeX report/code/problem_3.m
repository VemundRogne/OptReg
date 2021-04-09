clc
clear all
%% Initialization and model definition
init06; % Change this to the init file corresponding to your helicopter

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
A1 = eye(4) + (delta_t.*Ac);
B1 = (delta_t.*Bc);

% Number of states and inputs
mx = size(A1,2); % Number of states (number of columns in A)
mu = size(B1,2); % Number of inputs(number of columns in B)

% Trajectory start and end values
lambda_0 = pi;
lambda_f = 0;
% Initial values
x1_0 = lambda_0;                        % Lambda
x2_0 = 0;                               % r
x3_0 = 0;                               % p
x4_0 = 0;                               % p_dot
x0 = [x1_0 x2_0 x3_0 x4_0]';            % Initial values

% Time horizon and initialization
N  = 100;                               % Time horizon for states
M  = N;                                 % Time horizon for inputs
z  = zeros(N*mx+M*mu,1);                % Initialize z for the whole horizon
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

% Generate the matrix Q and the vector c (objecitve function weights in the QP problem) 
Q1 = zeros(mx,mx);
Q1(1,1) = 1;                            % Weight on state x1
Q1(2,2) = 0;                            % Weight on state x2
Q1(3,3) = 0;                            % Weight on state x3
Q1(4,4) = 0;                            % Weight on state x4
P1 = 1;                                % Weight on input
Q = gen_q(Q1,P1,N,M);                  % Generate Q, hint: gen_q
% The constant linear term is zero in our case
c = zeros(size(Q, 2), 1);              % Generate c, this is the linear constant term in the QP

%% Generate system matrixes for linear model
Aeq = gen_aeq(A1,B1,N,mx,mu);          % Generate A, hint: gen_aeq
beq = zeros(size(Aeq, 1), mu);             % Generate b
A0x0 = A1*x0;
beq(1:size(A0x0,1), :) = A0x0;

%% Solve QP problem with linear model
tic
% x = quadprog(H,f,A,b,Aeq,beq,lb,ub);
[z,lambda] = quadprog(2*Q, c,[],[], Aeq, beq, vlb, vub);% hint: quadprog. Type 'doc quadprog' for more info 
t1=toc;

% Calculate objective value
phi1 = 0.0;
PhiOut = zeros(N*mx+M*mu,1);
for i=1:N*mx+M*mu
  phi1=phi1+Q(i,i)*z(i)*z(i);
  PhiOut(i) = phi1;
end

%% Extract control inputs and states
u  = [z(N*mx+1:N*mx+M*mu);z(N*mx+M*mu)]; % Control input from solution

x1 = [x0(1);z(1:mx:N*mx)];              % State x1 from solution
x2 = [x0(2);z(2:mx:N*mx)];              % State x2 from solution
x3 = [x0(3);z(3:mx:N*mx)];              % State x3 from solution
x4 = [x0(4);z(4:mx:N*mx)];              % State x4 from solution

num_variables = 5/delta_t;
zero_padding = zeros(num_variables,1);
unit_padding  = ones(num_variables,1);

u   = [zero_padding; u; zero_padding];
x1  = [pi*unit_padding; x1; zero_padding];
x2  = [zero_padding; x2; zero_padding];
x3  = [zero_padding; x3; zero_padding];
x4  = [zero_padding; x4; zero_padding];
x = [x1 x2 x3 x4];

timesteps = 0:delta_t:delta_t*(length(u)-1);
u_opt = timeseries(u, timesteps);
x_opt = timeseries(x, timesteps);
%% Calculating feedback gain
% This is a simple setup for effective testing of different Q and R values. 
% It builds and start the simulink model automatically
R_values = [0.01, 0.1, 1, 10];
Q_values = {
    diag([0.1, 1, 1 1]),
    diag([10, 1, 1, 1]),
    diag([100, 1, 1, 1]),
    diag([1, 0.1, 1, 1]),
    diag([1, 10, 1, 1]),
    diag([1, 100, 1, 1]),
    diag([1, 1, 0.1, 1]),
    diag([1, 1, 10, 1]),
    diag([1, 1, 100, 1]),
    diag([1, 1, 1, 0.1]),
    diag([1, 1, 1, 10]),
    diag([1, 1, 1, 100])
};

isR = false; %If true: Test different R values, else test Q values
if (isR == true)
    l = length(R_values)
else
    l = length(Q_values)
end
    
modelname = 'helicopter'
for i = 1:l
    if (isR == true)
        Q = diag([1, 1, 1, 1]);
        R = R_values(i);
    else
        Q = Q_values{i, 1};
        R = 1;
    end
    [K, S, e] = dlqr(A1, B1, Q, R);
    if (isR == true)
        filename = sprintf('data/data_R%.3f.mat', R);
    else
        filename = sprintf('data/Q_test_%d', i);
    end
        
    set_param(strcat(modelname,'/To File'), 'Filename', filename);
    
    set_param(gcs, 'SimulationCommand', 'connect');
    set_param(gcs', 'SimulationCommand', 'start');
    
    pause(40);
    set_param(gcs', 'SimulationCommand', 'stop');
    set_param(gcs, 'SimulationCommand', 'disconnect');
    
    input('Press ENTER when you are ready for new test: ')
end