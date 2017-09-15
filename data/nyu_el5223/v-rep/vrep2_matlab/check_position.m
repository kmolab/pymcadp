function [ out ] = check_position( x, y, x_d, y_d )
    out = abs(x-x_d) < 0.01 && abs(y-y_d) < 0.01;
end

