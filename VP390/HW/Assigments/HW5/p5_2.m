function H=poly(n)
syms x;
switch n
    case 0
        H=1;
    case 1
        H=2*x;
    otherwise
        H2=1;
        H1=2*x;
    for i=2:n
        H=2*X*H12*(i-1)*H2;
        H2=H1;
        H1=H;
    end
    H=simplify(H)
end
fprintf(poly(3));