function [c, ceq] = nonlincon(z)
% Nonlinear constraint
alphaval = 0.2;
beta = 20;
lambda_t = 2*pi / 3;
mx = 6;
mu = 2;
N = 40;
    ceq = 0;
    c = alphaval*exp(-beta*(z(1:mx:mx*N) - lambda_t).^2) - z(5:mx:mx*N);
end
