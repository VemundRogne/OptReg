clc
clear all 

init06;
T = 0.25;
Ad = [1 T 0 0;
    0 1 -T*K_2 0;
    0 0 1 T;
    0 0 -T*K_1*K_pp 1-T*K_1*K_pd];
e = eig(Ad)