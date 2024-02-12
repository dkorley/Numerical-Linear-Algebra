function x = backwardSubstitution(U, z)
    n = size(U, 1);
    x = zeros(n, 1);
    x(n) = z(n) / U(n, n);
    for i = n - 1:-1:1
        totalsum = 0;
        for j = i + 1:n
            totalsum = totalsum + U(i, j) * x(j);
        end
        x(i) = (z(i) - totalsum) / U(i, i);
    end
end
