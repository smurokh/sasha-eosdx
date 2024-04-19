AN=readmatrix("BN.txt")
YN=fft2(AN)
ZN=abs(YN)
writematrix(ZN)