# A low-frequency inverse retaining every leading adjoint shift

Private finite-source theorem, 9 November 2026. Keep the complete
leading finite-shift operator instead of replacing it by a scalar
multiplier. Its compression to frequencies \(|k|\le\alpha N\),
for any fixed \(\alpha<1/2\), is uniformly accretive. A weighted
Fourier inverse and an exact coefficient comparison then give
an inverse for the same compression of the original grouped
operator. The remaining modes, including eleven boundary output
modes, are retained.

This is not positivity or surjectivity of the full constrained
operator. It gives a new finite probe with its original Hermite
conditions and parity forcing. No sufficient volume budget or
short-filling theorem is asserted. No numerical evaluation or
frozen-source edit is used.

## 1. Exact source and full leading-shift operator

Use the adopted
[global grouped operator](research_mixed_next_outer_global_analytic_probe.md),
with
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\quad
q=e^{i\pi/N},\quad\kappa_N=q^{D^2/2},\\
z(u)=-2\cos u,\quad
Q_{3,N}^{\rm rev}(z)=\prod_{\nu=0}^2(z-c_{U-\nu}),\\
\mathcal C_Ng=e_M^{-1}\mathcal B_N(e_MQ_{3,N}^{\rm rev}g),\\
\mathcal B_N=q^{-2}\mathcal L_2(\mathcal L_3^2-I)
 +q^{-3}Z_{\rm mult}\mathcal L_3
 -8q^{-2}\mathcal L_3+(8q^{-1}+2)I.
\end{gathered}                                                     \tag{1}
\]
Here \(Z_{\rm mult}\) is spectral multiplication. The exact
radical shift ratios give, on nonreal horizontal lines,
\[
(\mathcal C_Ng)(u)=
 \sum_{j=-3}^3a_{j,p}(u,N^{-1})g(u+2\pi j/N),                     \tag{2}
\]
where \(p\) records parity. The whole expression is removable
at every real pole on even periodic analytic inputs.

Let \(a_j^0(u)=a_{j,p}(u,0)\), common to both parities. Keep
all its shifts in the operator
\[
(\mathcal P_Ng)(u)=
 \sum_{j=-3}^3 a_j^0(u)g(u+2\pi j/N).                            \tag{3}
\]
The leading coefficient convention is exactly
\[
\sum_{j=-3}^3a_j^0(u)v^j
 =Q(u)^3d(u,-e^{3iu}v),\qquad Q(u)=2-2\cos u,                     \tag{4}
\]
\[
\begin{split}
d(u,\zeta)&=(\ell^2-1)m-(8+2\cos u)\ell+10,\\
\ell&=2+2a-a(\zeta+\zeta^{-1}),\\
m&=2+2a-a(e^{-iu}\zeta+e^{iu}\zeta^{-1}),\qquad a=\cot^2(u/2).
\end{split}                                                       \tag{5}
\]
This follows by using
\(2+2a+a e^{-inu}v^{-1}+a e^{inu}v\) for the original
radical-conjugated \(\mathcal L_n\), with \(n=3,2\).
No first-order expansion of the character \(v\) is made.

Each \(a_j^0\) is an entire trigonometric polynomial of degree
at most eleven. Indeed \(Q^3a^h=Q^{3-h}(2+2\cos u)^h\),
\(0\le h\le3\), is a trigonometric polynomial of degree at most
three. In the leading triple product the largest phase exponent
is \(3+3+2=8\); the remaining terms have smaller total degree.
Thus the possible pole at \(u=0\) is removed coefficientwise
in (4). This assertion concerns the leading coefficients only,
not the separated finite coefficients in (2).

Also
\[
                         a_j^0(-u)=a_{-j}^0(u).                  \tag{6}
\]
It follows directly from (4)--(5) by replacing \((u,v)\) with
\((-u,v^{-1})\). Consequently \(\mathcal P_N\), like
\(\mathcal C_N\), preserves the even subspace.

## 2. Positive frozen symbols on a fixed low-frequency band

Fix once
\[
                       0<\alpha<1/2.
\]
For real \(|\nu|\le\alpha\), define
\[
p(u,\nu)=\sum_j a_j^0(u)e^{2\pi ij\nu}
             =Q(u)^3d(u,-e^{3iu+2\pi i\nu}).                     \tag{7}
\]
The adopted all-character theorem gives \(d\ge4\) whenever
\(u\) is real and not an endpoint of its cotangent chart.
Thus \(p(u,\nu)>0\) except that the central limit needs to be
checked. The explicit endpoint values are
\[
p(0,\nu)=4096\cos^6(\pi\nu)>0,\qquad p(\pi,\nu)=256.
                                                                    \tag{8}
\]
For the first, \(a=4u^{-2}+O(1)\), and both \(\ell\) and \(m\)
have leading term \(16u^{-2}\cos^2(\pi\nu)\). Multiplication
by \(Q^3=u^6+O(u^8)\) gives (8); all lower-order terms vanish
in that limit. At \(\pi\), substitute \(a=0\), \(\ell=m=2\)
directly into (5). The symmetry
\(p(-u,-\nu)=p(u,\nu)\), together with periodicity and the
symmetric range of \(\nu\), covers the full circle.
Compactness proves
\[
 \mu_\alpha=\min_{\substack{-\pi\le u\le\pi\\|\nu|\le\alpha}}
                           p(u,\nu)>0.                          \tag{9}
\]
The reality in this statement follows from (5) on unit
characters. It is not a claim that a variable-coefficient
finite matrix is self-adjoint.

Write the finite Fourier expansion
\[
p(u,\nu)=\sum_{\ell=-11}^{11}p_\ell(\nu)e^{i\ell u}.
\]
Set
\[
\begin{split}
C_\ell&=\sup_{|\nu|\le\alpha}|p_\ell(\nu)|,\qquad
D_\ell=\sup_{|\nu|\le\alpha}|p_\ell'(\nu)|,\\
C_0^{\rm sum}&=\sum_\ell C_\ell,\qquad
C_1^{\rm sum}=\sum_\ell D_\ell,\qquad
C_{\rm ov}=\sum_\ell|\ell|C_\ell .
\end{split}                                                       \tag{10}
\]
All these constants are finite and specified by (4).
For real \(\nu\),
\(p_{-\ell}(\nu)=\overline{p_\ell(\nu)}\).

Let \(K_N=\lfloor\alpha N\rfloor\), and let \(\Pi_N\) project
onto Fourier indices \(-K_N,\ldots,K_N\). In Fourier coordinates,
the exact leading operator has matrix
\[
(\mathcal P_N)_{n,k}=p_{n-k}(k/N),\qquad
                       (\mathcal P_N)_{n,k}=0\quad(|n-k|>11).
                                                                    \tag{11}
\]
This follows by applying (3) to \(e^{iku}\).
Its finite compression is
\[
                  P_{I,N}=\Pi_N\mathcal P_N\Pi_N.                \tag{12}
\]
For example its Hermitian defect is explicitly
\[
(P_{I,N}-P_{I,N}^*)_{n,k}
      =p_{n-k}(k/N)-p_{n-k}(n/N),                                \tag{13}
\]
so its norm is at most
\(N^{-1}\sum_\ell|\ell|D_\ell\) by row and column sums.
We will prove coercivity directly, without omitting this defect.

## 3. Fourier-index freezing proves actual compression coercivity

Extend every vector \(f\) in the compressed index set by zero.
For \(L=\lfloor\sqrt N\rfloor>11\), use the real windows
\[
\chi_j(k)=L^{-1/2}{\bf1}_{\{j\le k<j+L\}},\qquad f^{(j)}=\chi_jf.
\]
Their exact overlaps are
\[
\sum_j\chi_j(k)^2=1,\qquad
\sum_j\chi_j(n)\chi_j(k)=1-\frac{|n-k|}{L}
                                      \quad(|n-k|\le11).         \tag{14}
\]
Therefore
\[
\left|\langle f,P_{I,N}f\rangle
 -\sum_j\langle f^{(j)},P_{I,N}f^{(j)}\rangle\right|
                   \le\frac{C_{\rm ov}}{L}\|f\|_2^2.             \tag{15}
\]

For each nonzero window choose a reference index \(k_j\) in
its intersection with the compressed set. Freeze the matrix
coefficients at \(\nu_j=k_j/N\):
\[
(P_j^0v)_n=\sum_{\ell=-11}^{11}p_\ell(\nu_j)v_{n-\ell}.
\]
Fourier orthogonality and (9) give
\[
             \langle v,P_j^0v\rangle
                       \ge\mu_\alpha\|v\|_2^2.                  \tag{16}
\]
This frozen quadratic form is real. Within the window,
\(|k-k_j|\le L\), so the error in its quadratic form is at
most \(C_1^{\rm sum}L/N\) times the squared norm.
Summing and using (14)--(15) gives the fully finite bound
\[
\Re\langle f,P_{I,N}f\rangle
 \ge\left(\mu_\alpha-\frac{C_1^{\rm sum}L}{N}
                       -\frac{C_{\rm ov}}L\right)\|f\|_2^2.
                                                                    \tag{17}
\]
Hence, for all sufficiently large \(N\),
\[
            \Re\langle f,P_{I,N}f\rangle
                         \ge\frac{3\mu_\alpha}{4}\|f\|_2^2 .
                                                                    \tag{18}
\]
The indices \(\pm K_N\) and both signs of every carrier are
included by zero extension. No coalescing physical endpoint
has been removed from the angular domain.

## 4. A fixed weighted inverse and the exact finite operator

Choose a fixed \(\rho>0\) such that
\[
\mathcal B_\alpha(\rho):=
 \sum_{\ell=-11}^{11}C_\ell(e^{\rho|\ell|}-1)
                       <\frac{\mu_\alpha}{4}.                  \tag{19}
\]
Such a choice exists because the left side is continuous and
zero at \(\rho=0\). For zero exponential cost on the actual
Green input one may additionally require \(\rho\le1/8\).

Let \(E_\rho\) be diagonal multiplication by \(e^{\rho|k|}\)
in Fourier coordinates. Since
\(\big||n|-|k|\big|\le|n-k|\), row and column sums give
\[
\|E_\rho P_{I,N}E_\rho^{-1}-P_{I,N}\|
                         \le\mathcal B_\alpha(\rho).             \tag{20}
\]
Together with (18), this proves that the weighted leading
compression is accretive with lower bound \(\mu_\alpha/2\),
and its inverse norm is at most \(2/\mu_\alpha\).

The passage to the original operator costs \(O(N^{-1})\), with
no derivative or strip loss. To see it rigorously, use the Hardy
strip norm
\[
\|f\|_{\rho,2}^2
 =\frac1{4\pi}\int_{-\pi}^{\pi}
       \{|f(u+i\rho)|^2+|f(u-i\rho)|^2\}\,du
 =\sum_k|\widehat f_k|^2\cosh(2k\rho).
                                                                    \tag{21}
\]
It is equivalent to the weighted Fourier norm:
\[
 \tfrac12\|E_\rho\widehat f\|_2^2
       \le\|f\|_{\rho,2}^2\le\|E_\rho\widehat f\|_2^2.             \tag{22}
\]
On these two nonreal lines, the exact coefficient charts from
the global grouped source give
\[
\sup_{u,\ p}|a_{j,p}(u,N^{-1})-a_j^0(u)|\le C_\rho/N .
\]
Real shifts are isometries in each boundary \(L^2\) norm.
Thus for every even trigonometric polynomial,
\[
       \|(\mathcal C_N-\mathcal P_N)f\|_{\rho,2}
                          \le C_\rho' N^{-1}\|f\|_{\rho,2}.      \tag{23}
\]
The exact grouped removal ensures that the left side is the
Hardy norm of the actual analytic output. Its finite coefficients
may have individual real poles; no bound through those individual
poles was assumed. Their values on the two nonreal lines suffice.

Projection onto \(|k|\le K_N\) is a contraction in (21) and
in the weighted Fourier norm. By (22)--(23), the actual even
compression
\[
 A_{I,N}^{\rm ev}
   =\Pi_N\mathcal C_N\big|_{\{\text{even polynomials of degree }
                                            \le K_N\}}
                                                                    \tag{24}
\]
is an \(O(N^{-1})\) perturbation, in weighted coordinates, of
the even restriction of \(P_{I,N}\).
The even restrictions are legitimate: (6) proves even closure
for \(\mathcal P_N\), the exact source proves it for
\(\mathcal C_N\), and \(E_\rho,\Pi_N\) preserve that subspace.
After increasing the common threshold,
\[
\boxed{\quad
\Re\langle f,E_\rho A_{I,N}^{\rm ev}E_\rho^{-1}f\rangle
            \ge\frac{\mu_\alpha}{4}\|f\|_2^2,\qquad
\|(A_{I,N}^{\rm ev})^{-1}\|_{\rho\to\rho}
                              \le\frac4{\mu_\alpha}.
\quad}                                                            \tag{25}
\]
The norm on the right is the weighted Fourier norm.
This is an inverse on a finite square low-frequency compression,
not on all even analytic functions.

## 5. Exact residual modes and the original full trace

Let \(F_N\) be even and holomorphic near the closed strip of
height \(\rho\), and solve the finite system
\[
                  g_N=(A_{I,N}^{\rm ev})^{-1}\Pi_NF_N.
\]
It is an even trigonometric polynomial of degree at most \(K_N\).
Define the exact residual
\[
                         \rho_N=F_N-\mathcal C_Ng_N.             \tag{26}
\]
Then
\[
\Pi_N\rho_N=0,\qquad
\|g_N\|_{\rho,\mathrm F}\le C\|F_N\|_{\rho,\mathrm F},\qquad
\|\rho_N\|_{\rho,\mathrm F}\le C\|F_N\|_{\rho,\mathrm F}.           \tag{27}
\]
Here \(\|\cdot\|_{\rho,\mathrm F}=\|E_\rho\widehat{\cdot}\|_2\).
For the last bound, (11),(19) bound
\(\mathcal P_N\) from compressed inputs to all Fourier outputs
by a fixed constant; (22)--(23) do the same for \(\mathcal C_N\).

The high-frequency support in (27) gives
\[
\boxed{\quad
\|\rho_N\|_{\mathbb R}
 \le C_\rho e^{-\rho K_N}\|F_N\|_{\rho,\mathrm F}
 \le C_\rho' e^{-\alpha\rho N}\|F_N\|_{\rho,\mathrm F}.
\quad}                                                            \tag{28}
\]
Indeed Cauchy--Schwarz uses
\(\sum_{|k|>K_N}e^{-2\rho|k|}
 =2e^{-2\rho(K_N+1)}/(1-e^{-2\rho})\).
No algebraic relative error has been discarded.

There is also an exact description of the residual when \(F_N\)
is an ordinary spectral polynomial. The ordinary divisibility
and leading-degree theorem gives
\[
                    \deg\mathcal C_Ng_N\le K_N+11.              \tag{29}
\]
Thus its only possible contribution above the solved band is
in the eleven pairs of modes
\[
                  K_N<|k|\le K_N+11.                            \tag{30}
\]
For larger modes the residual equals the original input
coefficient. The coefficients in (30) are retained boundary
outputs of the solved system, not presumed equal to coefficients
of \(F_N\).

Put \(h_N=Q_{3,N}^{\rm rev}g_N\). It satisfies the exact three
central test zeros and is an ordinary spectral polynomial.
The original full Hermite transpose therefore gives directly
\[
\boxed{\quad
\mathcal L_N(F_N)
 =\mathfrak f_N\ell_N(h_N)+\mathcal L_N(\rho_N),\qquad
\mathfrak f_N=
 \begin{cases}
 4\kappa_N^3/N^2,&N\ {\rm even},\\
 0,&N\ {\rm odd},
 \end{cases}
\quad}                                                            \tag{31}
\]
where
\[
\mathcal L_N(F)=\phi_N[R_N^3e_MQ_N^{\rm full}F],\qquad
\ell_N(h)=\phi_N[R_N^3e_Mh].
\]
For analytic \(F_N\), these functionals use its full Hermite
class; the test and its operator image are already polynomials.
Every first normal and the odd simple node is retained.

The original consumed-normal formula, \(|\mu_{j,N}|\le2\),
and \(|Q_{3,N}^{\rm rev}|\le64\) on the real interval give
\[
|\mathfrak f_N\ell_N(h_N)|
       \le C N^{-1}\|F_N\|_{\rho,\mathrm F}.
\]
It is zero at odd levels. Using the adopted complete physical
bound for \(Q_N^{\rm full}\), equation (28) gives, for every
\(\tau>0\),
\[
\boxed{\quad
|\mathcal L_N(F_N)|
 \le C_\tau N^{A_\tau}\|F_N\|_{\rho,\mathrm F}
 \{N^{-1}+e^{N(\mathfrak M_3+\tau-\alpha\rho)}\}.
\quad}                                                            \tag{32}
\]

## 6. Actual attachment and unproved adequacy

For the actual natural-last-row polynomial
\(F_N^+=qA_M\alpha_{M-1,N}\nu_N^+\), the adopted
[action-weighted ellipse theorem](research_mixed_next_outgoing_action_weighted_green_ellipse.md)
gives
\[
\|F_N^+(-2\cos u,Z)\|_{\rho,\mathrm F}
              \le CN^A e^{N\mathcal P_Z(\rho)}.                  \tag{33}
\]
One may pass from its closed-strip supremum to this norm by
(21)--(22). Its top degree \(U\) is included. The exact degree
profile from that source remains available to sharpen (28)
or the boundary modes (30), but no such sharpening is assumed.

For any fixed \(\alpha,\rho\) satisfying (9),(19), a sufficient
strict budget for the original complete transfer is
\[
\boxed{\qquad
\mathcal P_{Z_*}(\rho)+
             \max\{0,\mathfrak M_3-\alpha\rho\}<\Lambda .
\qquad}                                                           \tag{34}
\]
The original scalar \((\kappa_N^2N)^{-1}\), paid cutoff/forcing
errors and nonzero geometric term are unchanged.
When \(\rho\le1/8\), \(\mathcal P_{Z_*}(\rho)\) is exactly
\(\Re\mathcal S(1/2,z_*)\).

The finite coercivity and contraction estimates above are
proved. A choice meeting (34) is not proved. In particular
\(\rho\) must obey the actual finite coefficient condition
(19); it cannot be replaced by \(1/8\) merely because the
input is analytic that far. At \(\alpha=1/2\), the central
value in (8) degenerates. This proof makes no assertion there,
does not solve away the codimension-three obstruction of the
full operator, and does not suppress its retained high-frequency
residual without the explicit estimate (28).

## Source versions

- Exact grouped global operator and full Hermite pairing:
  cb47c9d87949e276615443150b2da2260fec5bb09d3780039b90b322cd14eeb8.
- All-unit-character positivity:
  c88ba98093fc147f5acfcf1790aa5b6f0f26edda6d741d2efc7c55315942e55e.
- Original ordinary divisibility and exact degree increase:
  c5cb10096ed4c6aafefdc957958ddaf392ad17c81cab5e7e99dbbe026fc1aed3.
- Source sliding-window proof pattern, retaining finite boundaries:
  e1b713461bacdf263c07c3baa21de67960fae5e5e2735e5c400c009c987afddf.
- Actual Green action/degree profile and complete attachment:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.

