# Proper lower cofactors at the odd endpoint are not stable

This is the odd-level companion to
`md-even-cofactor-unbounded-nonreal-root-obstruction.md`. It concerns
the actual cofactors at spectral value \(-2\), not a spectral
perturbation or a numerical root plot. It does not assert instability
of a full spectral derivative after its different path terms have
been combined.

Let \(N=2m+1\), \(\theta=\pi/N\), and use the original recurrence

\[
R_j(b)=b^j\prod_{r<j}a_r+s_j^2(x+y)R_{j-1}(b)
       +s_js_{j-1}a_{j-1}xyR_{j-2}(b),
\quad
a_r=2+2\cos((2r+1)\theta),\quad s_r=2\sin(r\theta).
\tag{1}
\]

The visited central cofactor is \(G=R_m\). Its complete-node
identification with the positive q-Hahn determinant remains valid.
The central-skipping term of the actual odd source instead contains
\(D=R_{m-1}\):

\[
P_C(u)=G_b(u)G_c(u)+u s_m^2xyD_b(u)D_c(u).
\tag{2}
\]

**Theorem.** For each fixed integer \(s\ge1\) and each fixed \(L\),
the polynomial \(R_{m-s}(b;1,1)\) has at least \(2L\) nonreal zeros
at every sufficiently large odd level. In particular the individual
endpoint skipping cofactor \(D\) is not real stable at all large
levels. No Hermitian generalized pencil of uniformly bounded negative
index can represent it.

Here is the complete change to the even argument. Put \(j=m-s\),
\(A_j=\prod_{r<j}a_r\), \(B_N=2N^2/\pi^2\), and

\[
F_{N,s}(t)=\frac{t^jR_j(B_N/t;1,1)}{A_jB_N^j}.
\tag{3}
\]

For a fixed reversed coefficient of order \(r\), the unused rows
have \(k=m-\ell\in\{s+1,\ldots,s+r\}\) and
\(a_\ell=4\sin^2(k\theta)\). The monomer path weight tends to
\(8^r\), while every dimer weight tends to zero. Hence the
coefficient tends to \(1/(s+1)_r^2\). The same uniform bound as in
the even proof gives

\[
0\le[t^r]F_{N,s}(t)\le
\frac{(5\pi^2/16)^r}{(s+1)_r^2}.
\tag{4}
\]

Indeed \(K_{i,i+r}\le10^r\) and
\(a_\ell\ge16k^2/N^2\). Therefore

\[
F_{N,s}(t)\longrightarrow f_{s+1}(t)
:=\sum_{r=0}^{\infty}\frac{t^r}{(s+1)_r^2}
\quad\text{locally uniformly on }\mathbb C.
\tag{5}
\]

The proper lower cofactor has \(s=1\), so its limit is

\[
f_2(t)=\frac{f_1(t)-1}{t},\qquad
f_1(t)=\sum_{r\ge0}\frac{t^r}{(r!)^2}.
\tag{6}
\]

For every real \(x>0\), expansion of cosine and the elementary even
cosine moments on \([0,\pi]\) give

\[
f_1(-x^2/4)=\frac1\pi\int_0^\pi\cos(x\cos\varphi)\,d\varphi<1.
\tag{7}
\]

The strict inequality holds because the integrand is at most one
and is not identically one on an interval. Thus \(f_2(t)>0\) for
\(t<0\), while its positive coefficients give the same conclusion
for \(t\ge0\). For \(a>2\), independent beta variables with
parameters \((2,a-2)\) give
\(f_a(t)=\mathbb E f_2(tUV)\), so every \(f_{s+1}\), \(s\ge1\),
is strictly positive on the real axis.

Each such entire function is nonpolynomial and obeys
\(|f_a(t)|\le e^{2\sqrt{|t|}}\). The elementary finite-zero argument
in Section 4 of the even companion therefore proves infinitely many
zeros, all nonreal. Applying Rouché's theorem on any finite collection
of nonreal zero disks in (5), then reverting \(b=B_N/t\), proves the
claim. The bounded-negative-index consequence is exactly the
isotropic-eigenspace argument in Section 5 of that companion.

The distinct case \(s=0\) has limit \(f_1\), not \(f_2\). Nothing
in this proof contradicts the actual stable determinant for the
visited cofactor \(G=R_m\). Likewise, the first spectral derivative
of (2) contains the two derivatives of the visited product in
addition to the skipping product. The present result does not decide
the stability or the size of their combined sum.

As in the even theorem, each fixed limiting zero produces roots of
size \(N^2\); no positive fraction of nonreal roots or exponential
spectral cost follows. The obstruction rules out treating every
proper endpoint cofactor as a stable minor or as a Hermitian
extension with bounded negative index. A coherent sum, or a defect
whose effective cost is subexponential, remains possible.

The only source identities used are (1)–(2), from
`actual_cross_cofactor_factorization.md` Sections 1–2, with the hash
already recorded in the even companion. All limiting and zero-count
steps are explicitly proved above or in that unchanged companion.
