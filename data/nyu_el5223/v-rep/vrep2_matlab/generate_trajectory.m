function [ z ] = generate_trajectory( m, c, x )
    for i=1:length(x)
        z(i) = m*x(i)+c;
    end
end

