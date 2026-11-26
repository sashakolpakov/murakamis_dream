# From a radial contour bound to physical summation nodes

Private research deduction, 8 November 2026. This note proves a
finite-polynomial continuation lemma for the original observation.
Its hypothesis is a bound for the complete source on a radial
segment, with the outgoing factor already attached. It gives a
fixed interval of physical summation nodes with an exponential gap.
No mathematical numerical evaluation is used.

The complete vertical source theorem supplies this hypothesis
for both the original polynomial and its unchanged filtered version.
The application in Section 4 retains every outgoing summation index.

## 1. Finite functions and the required radial bound

Put
\[
D=N-1,\quad r=e^{-2\pi i/N},\quad
P_j=(r;r)_j,\quad p_j(V)=(rV;r)_j,
\]
and retain the original next conditional kernel
\[
C_{0,N}(Y,Z)=
\sum_{j=0}^{D}\frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^2}.
\tag{1}
\]
Its powers of \(Y\) lie between \(-D\) and zero. Let \(G_N(w,Y)\)
be a polynomial in \(Y\) of degree at most \(D\), and let \(d_N\)
be the original degree-at-most-\(D\) polynomial with
\(d_N(r^b)=P_b^{-1}\). Set
\[
\begin{split}
T_N(Y)&=G_N(w,Y)d_N(Y)C_{0,N}(Y,Z),\\
K_N(y)&=\frac{N T_N(e^{-2\pi iy})}{1-e^{-2\pi iNy}},\\
M_N&=\lceil N/2\rceil,\qquad L_N=(M_N-\tfrac12)/N,\qquad
\zeta_N=e^{-2\pi iL_N}.
\end{split}
\tag{2}
\]
The parameters \(w,Z\) are fixed during continuation in \(Y\).

Suppose there is a fixed \(\gamma>0\) and a real comparison rate
\(\Lambda\) such that
\[
|K_N(L_N+ih)|\le CN^A e^{N(\Lambda-\gamma)}
\quad\text{for}\quad
\frac{\log(9/10)}{2\pi}\le h\le0.
\tag{3}
\]
The constants are uniform over any parameter family for which
the conclusion is desired. The denominator in (2) has no zero
on this segment: exactly
\[
(e^{-2\pi i(L_N+ih)})^N=-e^{2\pi Nh}.
\tag{4}
\]

**Proposition.** Under (3), there is a fixed \(\delta>0\),
depending only on \(\gamma\), such that
\[
\left|\frac{G_N(w,r^b)}{P_b}C_{0,N}(r^b,Z)\right|
\le C'N^{A'}e^{N(\Lambda-\gamma/2)}
\tag{5}
\]
for every integer
\[
\lceil N/2\rceil\le b\le\lfloor N(1/2+\delta)\rfloor,
\tag{6}
\]
at all sufficiently large levels of either parity.
The sum of the absolute values in (5) over any subset of (6)
satisfies the same exponential estimate with polynomial cost.
The width \(\delta\) is independent of \(N,w,Z\).

## 2. Polynomial continuation with an explicit exponential cost

Set
\[
Q_N(t)=(\zeta_Nt)^D T_N(\zeta_Nt).
\tag{7}
\]
This is a polynomial of degree at most \(3D\): multiplication
by \(Y^D\) removes every negative power in (1).
For real \(9/10\le t\le1\), put \(h=\log t/(2\pi)\).
Then (2)--(4) imply
\[
|T_N(\zeta_Nt)|
 =\frac{1+t^N}{N}|K_N(L_N+ih)|
 \le2CN^{A-1}e^{N(\Lambda-\gamma)}.
\]
Since \(|\zeta_Nt|^D\le1\), the same estimate holds for
\(Q_N(t)\). There is no additional exponential cost from
removing the Laurent powers.

We give the polynomial estimate used for continuation.
If a complex polynomial \(Q\) of degree \(m\) has modulus
at most \(B\) on \([9/10,1]\), write
\[
Q((x+19)/20)=\sum_{\nu=0}^m a_\nu T_\nu(x),
\tag{8}
\]
where \(T_\nu(\cos\theta)=\cos(\nu\theta)\).
Cosine orthogonality gives \(|a_0|\le B\) and
\(|a_\nu|\le2B\) for \(\nu\ge1\), also for complex coefficients.
For \(\rho>1\), the ellipse
\[
\mathcal E_\rho=
\{x\in\mathbb C:|x-1|+|x+1|\le\rho+\rho^{-1}\}
\]
has boundary \(x=(v+v^{-1})/2\), \(|v|=\rho\).
There
\[
T_\nu(x)=\tfrac12(v^\nu+v^{-\nu}),\qquad
|T_\nu(x)|\le\rho^\nu.
\]
The maximum principle extends the inequality to the filled ellipse.
Thus
\[
|Q((x+19)/20)|\le(2m+1)B\rho^m
\qquad (x\in\mathcal E_\rho).
\tag{9}
\]
This elementary proof supplies the needed continuation for the
complete polynomial, without estimates for its individual coefficients
in the original quantum basis.

Choose
\[
\rho=e^{\gamma/12},\qquad
a_\rho=\tfrac12(\rho+\rho^{-1}),\qquad
d_\rho=(a_\rho-1)/20.
\tag{10}
\]
The disk \(|x-1|\le a_\rho-1\) lies in \(\mathcal E_\rho\):
the sum of distances to its two foci is at most
\(2+2|x-1|\le2a_\rho\).
Therefore \(|t-1|\le d_\rho\) is a permitted disk in (9).
For \(m\le3D<3N\), its cost satisfies
\[
\rho^m\le e^{\gamma N/4}.
\]
Equations (7)--(10) now give
\[
|Q_N(t)|\le C''N^{A''}
       e^{N(\Lambda-3\gamma/4)}
\qquad (|t-1|\le d_\rho).
\tag{11}
\]

## 3. The actual physical nodes

Take
\[
\delta=\min\{1/100,\ d_\rho/(8\pi)\}>0.
\tag{12}
\]
For \(b\) in (6), the number
\[
t_b=\zeta_N^{-1}r^b=e^{-2\pi i(b/N-L_N)}
\]
satisfies
\[
|t_b-1|\le2\pi|b/N-L_N|
 \le2\pi\left(\delta+\frac1{2N}\right)
 \le4\pi\delta\le d_\rho/2
\tag{13}
\]
once \(N\ge1/(2\delta)\). This is the same calculation at
even and odd levels; \(L_N\) differs from \(1/2\) by at most
\(1/(2N)\).

At these nodes \(|r^b|=1\), so the multiplier in (7) has
modulus one and \(|T_N(r^b)|=|Q_N(t_b)|\). The defining
interpolation values of \(d_N\) give
\[
T_N(r^b)=\frac{G_N(w,r^b)}{P_b}C_{0,N}(r^b,Z).
\tag{14}
\]
Equations (11)--(14), weakened to the gap \(\gamma/2\),
prove (5). There are at most \(N\) physical indices; taking
their absolute sum changes only the polynomial prefactor.

The construction extends a bound for the full observation,
including the outgoing factor. It does not extend an estimate
for the inner kernel alone. It also keeps the prescribed
physical values and the original closing normalization.
No positivity or phase coherence is assumed.

## 4. The complete original observation near the half-period

Use the actual complete words in powers three and four beginning
\(343\), of length at least five, with their original coupled
reference, fixed contour heights and affine rate
\(\Lambda_{123}(z)\). Let
\[
w\in[-2,2],\qquad z=u+ih_z,\quad 3/10\le u\le39/100,\qquad
Z=e^{-2\pi iz},\qquad c=\Im y_* .
\tag{15}
\]
Every height and reference correlation is exactly that of
[the complete vertical assembly](research_mixed_next_three_half_grid_and_near_half_complete_source.md).
The notation \(F_N\) in that theorem denotes the original
\(F_{34,N}\). Its conclusion supplies (3), for both
\[
G_N=F_{34,N},\qquad G_N=F_{34,N}^{\mathrm{mid}},
\]
with
\[
\Lambda=\Lambda_{123}(z),\qquad \gamma=10^{-13}.
\tag{16}
\]
Indeed its bound holds on the whole half-grid vertical
\(c\le h\le1/100\), and the actual lower radius satisfies
\(e^{2\pi c}<41/50<9/10\). Thus it includes the entire
radial segment required in (3).

The degree assumption also holds. The original finite incoming
formula for \(F_{34,N}\) uses outgoing factors \(p_j(Y)\)
of degree \(j\le D\), so the entire polynomial has degree
at most \(D\). The complete correction
\(F_{34,N}-F_{34,N}^{\mathrm{mid}}\) has degree at most \(D\)
as well, by the unchanged filter theorem used in that assembly.
No contour contribution is filtered separately.

**Corollary.** Take the fixed positive \(\delta\) in (10),(12),
with \(\gamma=10^{-13}\). For either choice of \(G_N\) above,
every subset
\[
\mathcal B_N\subseteq
\{\lceil N/2\rceil,\ldots,\lfloor N(1/2+\delta)\rfloor\}
\]
satisfies
\[
\sum_{b\in\mathcal B_N}
\left|\frac{G_N(w,r^b)}{P_b}C_{0,N}(r^b,Z)\right|
\le C N^B
\exp N\left\{\Lambda_{123}(z)-\frac1{2\cdot10^{13}}\right\}.
\tag{17}
\]
This is uniform on the actual parameter family (15), at all
sufficiently large levels of both parities.
It follows directly from the proposition and (16).

For comparison with the original radical formula, put
\(q_N=e^{\pi i/N}\) and \(\kappa_N=q_N^{D^2/2}\). The exact
unfiltered identity is
\[
\frac{F_{34,N}(w,r^b)}{P_b}C_{0,N}(r^b,Z)
 =\frac{(-q_N)^b}{\kappa_N^2N}
       \ell_b(w)C_{0,N}(r^b,Z).
\tag{18}
\]
Thus (17) estimates the original summand with its outgoing
factor and its original \(1/N\), without inserting another
closing scalar. In particular it is not the inner-kernel bound
followed by a positive outgoing estimate.

For the original middle band, \(\delta\le1/100<1/3\) implies
that the entire interval in (17) lies below its upper end
\(\lceil5N/6\rceil\), for sufficiently large \(N\). Subtracting
this completely bounded contribution leaves only the physical
indices
\[
\lfloor N(1/2+\delta)\rfloor+1
       \le b<\lceil5N/6\rceil .
\tag{19}
\]
The constant width is independent of \(N\); no numerical value
or optimality of that width is asserted. The remaining sum (19),
the survival of the geometric contribution in the full transfer,
and stability under arbitrary short partial fillings are not
proved here.

