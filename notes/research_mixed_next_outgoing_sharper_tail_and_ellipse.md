# A sharper outgoing tail circle and a larger Green ellipse

Private exact-source deduction, 9 November 2026. The complete outgoing
ratio lies inside the circle of radius \(4/5\) throughout the terminating
tail. Together with the original middle action inequality, this gives
a uniform action slope exceeding \(205/1134\). The actual degree-\(U\)
Green insertion is consequently polynomially bounded on the closed
spectral ellipse of height \(9/50\).

This is a separate strengthening of the
[action-weighted Green theorem](research_mixed_next_outgoing_action_weighted_green_ellipse.md).
That frozen theorem and its source normalization are unchanged.
The inverse remains the one on \([M,D]\), including the last physical
row. No mathematical numerical evaluation is used. No coherent
attachment budget is claimed.

## 1. The original tail characteristic

Use
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\quad
q=e^{i\pi/N},\quad r=q^{-2},\quad \kappa_N=q^{D^2/2},\\
\mathfrak Z=\{\rho e^{-i\alpha}:4/5\le\rho\le8/7,\ 
                              3\pi/5\le\alpha\le39\pi/50\},\\
t=(\pi a-\pi/2)/2,\quad \sigma=2\sin(\pi a),\quad
\tau=\sigma^{3/2},\\
V=3e^{it}+2e^{-3it}+Ze^{5it},\quad
Y=e^{-2\pi ia},\quad A=Y(Y-1),\quad w=-e^{5it}.
\end{gathered}                                                     \tag{1}
\]
Let \(m(a,Z)\) be the original half-line inverse diagonal of the
[absolute anchor theorem](research_mixed_next_outgoing_absolute_anchor.md),
and put
\[
\mathcal L=-Aw\,m,\qquad \xi=-\tau m.
\]
For \(a<1\), these satisfy
\[
V+\tau(\xi+\xi^{-1})=0,\qquad
|\xi|<1,\qquad |\xi|=\sqrt{\sigma}\,|\mathcal L|.                 \tag{2}
\]
The selected \(\mathcal L\) is continuous through \(a=1\), with
\(\mathcal L(1,Z)=0\). These facts include the actual phases, rather
than an unsigned diagonal-dominance replacement.

On \(5/6\le a\le1\), the original
[tail rotation, equation (13)](research_mixed_next_outgoing_full_tail_weighted_energy.md)
gives
\[
                 \Re V+\Im V-2\tau>\frac8{25}.                  \tag{3}
\]
Here \(0\le\sigma\le1\).

**Tail-circle theorem.** Uniformly for \(Z\in\mathfrak Z\),
\[
                  |\mathcal L(a,Z)|<\frac45,
                                  \qquad5/6\le a<1.             \tag{4}
\]

To prove it, suppose \(|\mathcal L|=4/5\) and write
\(\xi=(4/5)\sqrt{\sigma}\,e^{i\varphi}\). Combining the cosine
and sine coefficients gives the exact maximum
\[
\max_\varphi
 \left|\Re\{(1-i)\tau(\xi+\xi^{-1})\}\right|
 =\sigma\sqrt{\frac{32}{25}\sigma^2+\frac{25}{8}}.                \tag{5}
\]
In general, for \(|\xi|=\varrho\sqrt{\sigma}\), its squared
value is \(2\varrho^2\sigma^4+2\varrho^{-2}\sigma^2\);
(5) follows by setting \(\varrho=4/5\).

The excess of (5) over \(2\tau\) admits a uniform rational bound.
The concavity inequality \(\sqrt{1+x}\le1+x/2\), together with
\(\sqrt2<10/7\) and \(\sigma^3\le\sigma^{3/2}\), gives
\[
\begin{split}
\sigma\sqrt{\frac{32}{25}\sigma^2+\frac{25}{8}}
                         -2\sigma^{3/2}
&\le \frac{5\sqrt2}{4}\sigma
       +\frac{32\sqrt2}{125}\sigma^3-2\sigma^{3/2}\\
&\le \frac{25}{14}\sigma-\frac{286}{175}\sigma^{3/2}\\
&\le \frac{25}{14}\sigma-\frac{13}{8}\sigma^{3/2}.
\end{split}                                                       \tag{6}
\]
The last comparison uses \(286\cdot8>13\cdot175\).
For positive constants \(A_0,B_0\), differentiation on
\([0,\infty)\) gives
\[
\sup_{\sigma\ge0}(A_0\sigma-B_0\sigma^{3/2})
                         =\frac{4A_0^3}{27B_0^2}.
\]
Consequently (6) is at most
\[
\frac{4\,000\,000}{12\,520\,872}<\frac8{25},                     \tag{7}
\]
where the exact positive cross-multiplication difference is
\[
8\cdot12\,520\,872-25\cdot4\,000\,000=166\,976.
\]
Equations (3), (5), and (7) show
\[
\Re\{(1-i)[V+\tau(\xi+\xi^{-1})]\}
 >
\frac8{25}-\frac{4\,000\,000}{12\,520\,872}>0
\]
on the proposed circle. It therefore contains no characteristic
root. Continuity from the selected value \(\mathcal L(1,Z)=0\)
proves (4) on each output fiber. All comparisons are uniform on
the closed containing region.

For the exact original complete polynomial
\[
C_{b,N}(Z)=
\sum_{k=0}^{D}
 \frac{(r^b)^{-k}(r^{b+1};r)_k(rZ;r)_k}{(r;r)_k^2},
\]
the absolute anchor gives
\(C_{b,N}/C_{b-1,N}=\mathcal L(b/N,Z)(1+O(N^{-1}))\)
uniformly through \(D\). Hence, for all sufficiently large levels
and both parities,
\[
\left|\frac{C_{b,N}(Z)}{C_{b-1,N}(Z)}\right|
 \le\frac{81}{100},
 \qquad 5/6\le b/N<1,\quad b\le D,\quad Z\in\mathfrak Z.          \tag{8}
\]
The literal stop \(k\le D-b\), all numerator zeros, and the exact
terminal value \(C_{D,N}=1\) are retained. There is no row at
index \(N\) in this assertion.

## 2. The original action and a uniform slope

Restrict the action interpretation to the original actual output
rectangle
\[
z_*=u+ih,\quad 3/10\le u\le39/100,\quad
             -3/100\le h\le1/50,\qquad Z=e^{-2\pi iz_*}.          \tag{9}
\]
The adopted terminal normalization identifies
\[
\mathcal E(a,Z)=-\int_a^1\log|\mathcal L(x,Z)|\,dx
              =\Re\widetilde{\mathcal S}(a,z_*),\qquad
                                  1/2\le a\le1.                \tag{10}
\]
This is the original zero-lift action on the middle interval,
with its specified continuation and zero value at \(a=1\).
No new saddle-contour claim beyond the middle is needed.

Put
\[
\gamma_0=\log(126/125),\qquad
\gamma_1^\sharp=\log(5/4),\qquad
c_0=\frac{\log2}{4}+\gamma_0,\qquad
c_\diamond=\frac{205}{1134}.
                                                                    \tag{11}
\]
The original middle inequality and (4) give
\[
\partial_a\mathcal E(a,Z)<
\begin{cases}
-\tfrac12\log(2\sin\pi a)-\gamma_0,&1/2\le a\le5/6,\\
-\gamma_1^\sharp,&5/6\le a<1.
\end{cases}                                                       \tag{12}
\]
The endpoint logarithmic singularity remains integrable.

For completeness, the needed comparisons of constants are
written directly. The positive logarithm series gives
\[
\log2
 =2\int_0^{1/3}\frac{dx}{1-x^2}
 >2\left(\frac13+\frac1{81}\right)=\frac{56}{81},
 \qquad \gamma_0>\frac1{126}.
\]
Thus
\[
c_0>\frac{14}{81}+\frac1{126}
        =\frac{205}{1134}=c_\diamond
        =\frac9{50}+\frac{11}{14175}.                            \tag{13}
\]
Also
\[
\gamma_1^\sharp
 =2\int_0^{1/9}\frac{dx}{1-x^2}>\frac29,
 \qquad \gamma_0<\frac1{125},\qquad \log2<\frac7{10}.
\]
For the last upper bound the first four nonnegative exponential
terms suffice:
\[
e^{7/10}>
 1+\frac7{10}+\frac{49}{200}+\frac{343}{6000}
 =\frac{12013}{6000}>2.
\]
In particular
\[
\gamma_1^\sharp-c_0
 >\frac29-\frac7{40}-\frac1{125}
 =\frac{353}{9000}>0.                                           \tag{14}
\]

Let \(J(a)=\int_0^a\log(2\sin\pi x)\,dx\), with \(J(1/2)=0\),
and write \(t=a-1/2\). On \([1/2,5/6]\), the integrand is
decreasing and concave. Its chord gives \(J(5/6)\ge\log2/6\),
and its decreasing averages give
\[
                    J(1/2+t)\ge t\log2/2,\qquad0\le t\le1/3.
\]
Integrating (12) therefore gives
\[
\mathcal E(1/2,Z)-\mathcal E(1/2+t,Z)\ge
\begin{cases}
\tfrac12J(1/2+t)+\gamma_0t,&0\le t\le1/3,\\
\tfrac12J(5/6)+\gamma_0/3+
             \gamma_1^\sharp(t-1/3),&1/3\le t\le1/2.
\end{cases}                                                       \tag{15}
\]
These two expressions keep a stronger piecewise profile if useful.
The first is at least \(c_0t\); the second is at least
\(c_0/3+\gamma_1^\sharp(t-1/3)\ge c_0t\), by (14).
Consequently
\[
\boxed{\quad
\mathcal E(a,Z)-\mathcal E(1/2,Z)
 \le-c_0(a-1/2)\le-c_\diamond(a-1/2),\qquad1/2\le a\le1 .
\quad}                                                            \tag{16}
\]

## 3. Every coefficient of the actual attached source

Use the exact natural trailing inverse and insertion of the
action-weighted Green theorem:
\[
\begin{gathered}
G_N^+=(\mathcal J_{[M,D],N}-ZI)^{-1},\qquad
\alpha_{b,N}=(-q)^bC_{b,N},\\
(G_N^+)_{b,M}=\frac{\alpha_{b,N}}{qA_M\alpha_{M-1,N}},\\
P_b^{\rm rad}(\zeta)=e_b(\zeta)/e_M(\zeta),\qquad
\nu_N^+(\zeta,Z)=\sum_{b=M}^D(G_N^+)_{b,M}P_b^{\rm rad}(\zeta),\\
F_N^+(\zeta,Z)=qA_M\alpha_{M-1,N}\nu_N^+(\zeta,Z)
             =\sum_{b=M}^D\alpha_{b,N}P_b^{\rm rad}(\zeta).
\end{gathered}                                                     \tag{17}
\]
The degree is \(U\), not \(U-1\), and the \(U+1\) original
double nodes are the same ones used in its exact cardinal proof.

The proved action-dependent coefficient estimate is
\[
\nu_N^+(\zeta,Z)=\sum_{k=0}^U\widehat\nu_{k,N}^+(Z)T_k(\zeta/2),
\qquad
|\widehat\nu_{k,N}^+|
 \le CN^A e^{N[\mathcal E(1/2+k/N,Z)-\mathcal E(1/2,Z)]}.
                                                                    \tag{18}
\]
Substituting (16), without changing any source row, proves
\[
                  |\widehat\nu_{k,N}^+|
                          \le CN^A e^{-c_\diamond k},
                                      \qquad0\le k\le U.         \tag{19}
\]
In particular the exact terminal coefficient in the source theorem
is included; no top-degree truncation is made.

Let \(\mathscr E_h\) denote the filled spectral ellipse with
boundary \(\zeta=2\cos(\vartheta+ih)\). Since
\(|T_k(\zeta/2)|\le e^{kh}\), (13), (19), and the maximum
principle give the uniform closed-ellipse estimate
\[
\boxed{\quad
\|\nu_N^+(\cdot,Z)\|_{\mathscr E_h}\le CN^A,\qquad
\|F_N^+(\cdot,Z)\|_{\mathscr E_h}
       \le CN^A e^{N\mathcal E(1/2,Z)},\qquad0\le h\le9/50 .
\quad}                                                            \tag{20}
\]
The second assertion uses the original absolute half-input
anchor in (17). It does not add its exponential rate twice.
The coefficient reserve at \(h=9/50\) is explicitly
\(11/14175>0\). Equivalently the source maximum satisfies
\[
\max_{1/2\le a\le1}
 \{\mathcal E(a,Z)+h(a-1/2)\}=\mathcal E(1/2,Z),
                                             \quad0\le h\le9/50.
                                                                    \tag{21}
\]

All transfer applications keep exactly the complete observation
\(\mathcal L_N(F)=\phi_N[R_N^3e_MQ_N^{\rm full}F]\) and the original
scalar \((\kappa_N^2N)^{-1}\mathcal L_N(F_N^+)\), with the already
paid forcing and cutoff errors of the trailing reduction.
The inverse in (17) is never identified with the earlier one on
\([M,D-1]\). Both parities and all original Hermite normal terms
remain unchanged.

The enlargement (20) supplies a stronger actual input norm for
the global and Fourier probes. Their inverse or conjugation
conditions must still be proved at the chosen width. A larger
input ellipse does not itself provide a larger admissible
inverse weight, and it does not verify the remaining coherent
volume budget or the general short-filling theorem.

## Source versions

- Action-weighted Green interpolation and full attachment:
  e39abb76185b6969901b6ee4c95a4f947bdda5f74d8ff57062ed4b6591a0c029.
- Original full-tail rotation:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Complete outgoing absolute anchor:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Original action terminal normalization:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
- Middle selected-action inequality:
  77ffb14e6f3a3408b4aee3594d1c205b9db61fccdbf011181de9f86c26e9dbd5.
- Natural trailing determinants and exact last row:
  8564c705a0c8cd96cb7211c10166a522dde511bda27a94ac18a7cdafccf0b47f.

