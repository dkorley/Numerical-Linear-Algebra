function [L, U] = cholesky(A)
    n = size(A, 1);
    L = zeros(n);
    U = zeros(n);
    for j = 1:n
        U(j, j) = sqrt(A(j, j));
        L(j, j) = U(j, j);
        for i = j + 1:n
            L(i, j) = A(i, j) / U(j, j);
            U(j, i) = L(i, j);
        end
        for k = j + 1:n
            for i = k:n
                A(i, k) = A(i, k) - L(i, j) * U(j, k);
            end
        end
    end
end

