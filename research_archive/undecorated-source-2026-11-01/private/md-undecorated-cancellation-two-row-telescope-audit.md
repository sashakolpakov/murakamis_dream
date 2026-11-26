# Exact two-row telescope and cyclic grading

The finite identities in §4 of `md-undecorated-bipyramid-exact-cyclic-transfer.md` have the stated signs and normalization. The two endpoints are both necessary. The cyclic trace in §2 is also exact with its stated degree states; no congruence or extra multiplicity is needed. This calculation gives no bound for the full cyclic source.

## 1. Recovering the two factors from the original matrix entries

Use \(N\ge3\), \(d=N-1\), \(m=\lfloor N/2\rfloor\), \(M=m-1\), and \(c_j=2\cos((2j+1)\pi/N)\), \(s_j=2\sin(j\pi/N)\). At \(x=0\), the original face Casimir is bidiagonal:
\[
 \Omega z^j=c_jz^j-s_j^2y z^{j-1}.
 \tag{1}
\]
Thus the raw resolvent numerator entry from column \(j\) to row \(i\le j\) is
\[
 V_{ij}(\sigma)=(-1)^{j-i}y^{j-i}
    \prod_{r=i+1}^{j}s_r^2
    \prod_{r\notin\{i,\ldots,j\}}(\sigma-c_r).
 \tag{2}
\]
No quantum denominator has been removed in (2).

The top factor \(H_{V,\mathrm L}(0,0,c,y;\sigma)\) sets its input-middle exponent to zero, so \(i=0\), \(j=k\le M\), and its contribution is \((-1)^kb_k(\sigma)c^{d-k}y^k\), with \(b_k\) as in the draft. The bottom factor \(H_{V,\mathrm C}(0,c,0,y;-2)\) sets its output-middle exponent to zero, so \(j=d\). To reach the prescribed total \(c\)-degree, its row is \(i=k\). This lies in the literal CROSS range at both parities. Its path sign is \((-1)^{d-k}\), while its \(k\) unused diagonal factors each contribute a minus sign at \(-2\). Therefore its coefficient is exactly \((-1)^dB_k c^ky^{d-k}\). The shared \(y^d\) target is then satisfied, without an independent choice of the two \(y\)-loads. This proves the draft's formula (13) and its overall sign from the raw source.

## 2. Both endpoint terms

The sine product identity \(\prod_{r=1}^{d}s_r^2=N^2\) cancels the two complementary step products. Set
\[
 C_k=\prod_{r=0}^{k-1}(2+c_r),\qquad
 T_k=N^2C_k\prod_{r=k+1}^{d}(\sigma-c_r),\qquad
 D_k=(\sigma-c_k)T_k.
 \tag{3}
\]
All three expressions are polynomials, including at every root. Directly,
\[
 (\sigma-c_{k+1})T_{k+1}=(2+c_k)T_k,
 \qquad D_k+D_{k+1}=(\sigma+2)T_k.
 \tag{4}
\]
Alternating (4) for \(0\le k\le m-1\) leaves
\[
 (\sigma+2)(-1)^d\mathcal B_N(\sigma)
       =D_0+(-1)^{m-1}D_m,
 \qquad D_0=N^2\chi_N(\sigma).
 \tag{5}
\]
There are no omitted internal terms or division assumptions.

For \(N=2m\), take \(P_m=2T_m(\sigma/2)\). The node lists give \(\chi_N=P_m^2\), \(C_m=2\), and \(\prod_{r=m}^{d}(\sigma-c_r)=P_m\). Hence
\[
 D_m=2N^2P_m,\qquad
 \mathcal B_N=-N^2\frac{P_m(P_m+2(-1)^{m-1})}{\sigma+2}.
 \tag{6}
\]
The quotient is a polynomial because \(P_m(-2)=2(-1)^m\). Its actual endpoint values are
\[
 \mathcal B_N(2)=-N^2(1-(-1)^m),\qquad
 \mathcal B_N(-2)=2N^2m^2=\frac{N^4}{2}.
 \tag{7}
\]
The second follows from \(P_m'(-2)=(-1)^{m-1}m^2\); it is not zero.

For \(N=2m+1\), take \(P_m=U_m(\sigma/2)-U_{m-1}(\sigma/2)\). Here \(\chi_N=(\sigma+2)P_m^2\), \(C_m=N\), and the remaining product is \((\sigma+2)P_m\). Therefore
\[
 D_m=N^3(\sigma+2)P_m,\qquad
 \mathcal B_N=N^2P_m(P_m+(-1)^{m-1}N),
 \tag{8}
\]
and
\[
 \mathcal B_N(2)=N^2(1+(-1)^{m-1}N),\qquad
 \mathcal B_N(-2)=0.
 \tag{9}
\]
The central odd factor has been retained; (8) does not use a regularized replacement of the raw bottom numerator.

In particular the smallest levels give
\[
 \mathcal B_3(\sigma)=9(\sigma-1)(\sigma+2),\qquad
 \mathcal B_4(\sigma)=-16(\sigma^2-2)(\sigma-2).
 \tag{10}
\]
For even \(N\), the difference quotient in (6) has magnitude at most \(m^2\) on \([-2,2]\), while \(|P_m|\le2\). This gives the stronger even bound \(N^4/2\). For odd \(N\), \(|P_m|\le N\) gives \(2N^4\). The uniform bound stated in the draft is consequently valid.

## 3. What the cyclic trace grading retains

Use the draft's notation here: the bipyramid has an even number of equatorial faces, and \(d\) is the quantum degree. For one transfer step,
\[
 a=t_{j-1}-u,\quad b=u'-v,\quad c=v',\quad
 p=d-a-b-c.
 \tag{11}
\]
The final quantity is exactly the south-pole degree of the local homogeneous coefficient. Thus, without any parity restriction on \(d\),
\[
 \ell(u',v')=\ell(u,v)+d-t_{j-1}-p,
                   \qquad\ell(u,v)=u+v.
 \tag{12}
\]
At each ordinary target, \(t_{j-1}=d\), this is the stated lowering by \(p\). Odd rows have \(p=0\). At the unique protected-target row \(j=1\), \(t_0=0\); nonnegative \(a=-u\) forces \(u=0\), and this odd row has \(p=0\), giving the increase by \(d\).

On a closed state path, summing (12) forces total south-pole degree \(d\). This proves the claimed identity \(\operatorname{tr}\prod_j\mathsf T_j(S)=S^d\operatorname{tr}\prod_j\mathsf T_j(1)\). Conversely the face monomials uniquely specify the pending states, so this specialization introduces neither a trace multiplicity nor an alias. The exact degree is the integer degree, not a residue modulo the quantum level.

There is no missing grading hypothesis in §2. The limitation is in a subsequent estimate: after cutting the cycle into blocks, both pending degrees and the net south-pole degree must still be matched. An operator norm for an unrestricted block or independently optimized south-pole gauges would discard information that the trace identity itself retains. The aligned specialization in §4 must not be substituted for the opposite-offset cyclic transfer in §2 without a further source identity.

## 4. Finite exact reproduction

`md-undecorated-cancellation-audit-two-row-telescope.py` constructs the original bidiagonal Casimir at \(x=0,y=1\), forms all coefficients of its resolvent numerator by Chebyshev polynomial division, and then takes exactly the rows and columns dictated by the two original face targets. It compares the resulting polynomial, coefficient by coefficient, with (6) or (8) in the rational cyclotomic field. Levels 3–12 give 75 checked polynomial coefficients, including both smallest levels. The script also checks 1300 finite admissible degree states against (12). The JSON output is `md-undecorated-cancellation-two-row-telescope-results.json`.

These finite identities corroborate the exact derivation; they do not estimate a full bipyramidal source or identify a contributing filling charge.
