function z = forwardSubstitution(L, b)
    n = size(L, 1);
    z = zeros(n, 1);
    z(1) = b(1) / L(1, 1);
    for i = 2:n
        totalsum = 0;
        for j = 1 : i - 1
            totalsum = totalsum + L(i, j) * z(j);
        end
        z(i) = (b(i) - totalsum) / L(i, i);
    end
end
