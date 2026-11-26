# The actual outgoing action in the Green insertion

Private finite-source deduction, 9 November 2026. The complete outgoing
ratio stays strictly inside the unit circle through the terminating
tail. The exact trailing Green column therefore gives an action-dependent
bound for every Chebyshev coefficient of its insertion, including the
last coefficient. A written action comparison enlarges its polynomially
bounded spectral ellipse to height \(1/8\). This retains the outgoing
attachment in applying the global analytic probe.

The inverse here is on \([M,D]\). It is not identified with the earlier
inverse on \([M,D-1]\). No mathematical numerical evaluation or
frozen-source edit is used. The resulting optimized probe criterion is
not claimed to satisfy the required volume budget.

## 1. A strict unweighted ratio bound through the tail

Use the notation and stable half-line inverse of the
[absolute anchor theorem](research_mixed_next_outgoing_absolute_anchor.md):
\[
\begin{gathered}
D=N-1,\quad M=\lceil N/2\rceil,\quad U=D-M,\quad
\theta=\pi/N,\quad q=e^{i\theta},\quad r=q^{-2},\\
\kappa_N=q^{D^2/2},\quad c_j=2\cos((2j+1)\theta),\\
s_j=2\sin(j\theta),\qquad S_b=\prod_{j=1}^b s_j,\qquad S_D=N,\\
t=(\pi a-\pi/2)/2,\quad \sigma=2\sin(\pi a),\quad
\tau=\sigma^{3/2},\quad
V=3e^{it}+2e^{-3it}+Ze^{5it},\\
Y=e^{-2\pi ia},\quad A=Y(Y-1),\quad w=-e^{5it},\quad
\mathcal L(a,Z)=-Aw\,m(a,Z).
\end{gathered}                                                     \tag{1}
\]
The full containing output region is
\[
\mathfrak Z=\{\rho e^{-i\alpha}:4/5\le\rho\le8/7,\ 
                              3\pi/5\le\alpha\le39\pi/50\}.
                                                                    \tag{2}
\]
For \(a<1\), set \(\xi=-\tau m\). Its exact frozen equations are
\[
\tau\xi^2+V\xi+\tau=0,\qquad |\xi|<1,\qquad
                  |\xi|=\sqrt{\sigma}\,|\mathcal L|.
                                                                    \tag{3}
\]
The absolute anchor supplies continuity through \(a=1\), where
\(\mathcal L(1,Z)=0\).

**Tail bound.** Uniformly on (2),
\[
             |\mathcal L(a,Z)|<\frac{97}{100},
                         \qquad 5/6\le a<1.                       \tag{4}
\]

Here is an explicit exclusion of the relevant circle. On this
interval \(0<\sigma\le1\), and the actual tail rotation from
[full-tail energy, (13)](research_mixed_next_outgoing_full_tail_weighted_energy.md)
gives
\[
                 \Re V+\Im V-2\tau>\frac8{25}.                    \tag{5}
\]
If \(|\mathcal L|=1\), then \(|\xi|=\sqrt{\sigma}\).
Writing \(\xi=\sqrt{\sigma}e^{i\varphi}\), the largest absolute
real part of the rotated off-diagonal term is
\[
\max_\varphi
\left|\Re\{(1-i)\tau(\xi+\xi^{-1})\}\right|
                  =\sigma\sqrt{2+2\sigma^2}.                     \tag{6}
\]
This follows by combining the cosine coefficient
\(\tau(\sqrt{\sigma}+\sigma^{-1/2})\) and the sine coefficient
\(\tau(\sqrt{\sigma}-\sigma^{-1/2})\).
Its excess over \(2\tau\) satisfies
\[
\begin{split}
0\le \sigma\sqrt{2+2\sigma^2}-2\sigma^{3/2}
&=\frac{2\sigma^2(1-\sigma)^2}
 {\sigma\sqrt{2+2\sigma^2}+2\sigma^{3/2}}\\
&\le\sqrt2\,\sigma(1-\sigma)^2
\le\frac{4\sqrt2}{27}<\frac29 .
\end{split}                                                       \tag{7}
\]
The maximum of \(\sigma(1-\sigma)^2\) on \([0,1]\) is \(4/27\),
as follows by differentiating; the last inequality uses
\(\sqrt2<3/2\).
Thus (5) leaves the strict margin
\[
\Re\{(1-i)[V+\tau(\xi+\xi^{-1})]\}>\frac{22}{225}
                                  \quad(|\xi|=\sqrt{\sigma}).       \tag{8}
\]

Put \(r_*=97/100\). At the same argument, replacing \(\xi\) by
\(r_*\xi\) changes the expression in (8) in absolute value by
at most
\[
\begin{split}
\sqrt2\{\sigma^2(1-r_*)+\sigma(r_*^{-1}-1)\}
&<3(1-r_*)/r_*\\
&=\frac9{97}<\frac{22}{225}.
\end{split}                                                       \tag{9}
\]
The final reserve is exactly \(109/21825>0\).
Consequently no characteristic root has
\(|\mathcal L|=r_*\) anywhere on the tail. The selected stable
root tends to zero as \(a\uparrow1\); continuity on each fixed
output fiber proves (4). This argument uses the original rotated
characteristic, including its complex off-diagonal phase. It is
not an unrotated absolute diagonal-dominance assertion.

By the uniform finite-ratio assertion of the absolute anchor,
after increasing the common level threshold,
\[
\left|\frac{C_{b,N}(Z)}{C_{b-1,N}(Z)}\right|
 \le\frac{49}{50},\qquad
                    5/6\le b/N<1,\quad Z\in\mathfrak Z.            \tag{10}
\]
The exact terminal row is included. No estimate at a nonphysical
index \(N\) is used.

## 2. Monotonicity of the original anchored action

From now on restrict the output to the actual closed parameter
rectangle
\[
z_*=u+ih,\qquad 3/10\le u\le39/100,\quad
-3/100\le h\le1/50,\qquad Z=e^{-2\pi iz_*}.                       \tag{11}
\]
Every actual-transfer assertion below concerns the original complete
words in powers three and four beginning \(343\), of length at least
five, at \(w=-2\) and \(Z=Z_*\), with their unchanged
\(\Lambda>419/200\).
The
[terminal normalization theorem](research_mixed_next_outgoing_action_terminal_normalization.md)
identifies
\[
\mathcal E(a,Z)=-\int_a^1\log|\mathcal L(x,Z)|\,dx
              =\Re\widetilde{\mathcal S}(a,z_*),
                    \qquad 1/2\le a\le1,                        \tag{12}
\]
where \(\mathcal E(1,Z)=0\). On the original middle interval this
is exactly the original zero-lift action, with no new additive
constant. Beyond that interval it is the explicitly continued
critical value, not a claimed finite saddle contour.

Set
\[
\gamma_0=\log(126/125),\qquad \gamma_1=\log(100/97)>\gamma_0.
                                                                    \tag{13}
\]
The adopted middle action inequality and (4) give
\[
\begin{split}
\partial_a\mathcal E(a,Z)
&<-\tfrac12\log(2\sin\pi a)-\gamma_0,
                                  &&1/2\le a\le5/6,\\
\partial_a\mathcal E(a,Z)
&<-\gamma_1,                   &&5/6\le a<1.
\end{split}                                                       \tag{14}
\]
On the middle interval \(2\sin\pi a\ge1\).
Thus \(\mathcal E\) is strictly decreasing on the whole half
interval and, uniformly on (11),
\[
0\le\mathcal E(a,Z)\le
\mathcal E(1/2,Z)-\gamma_0(a-1/2).
                                                                    \tag{15}
\]
The derivative's logarithmic singularity at \(1\) is integrable,
as proved in the terminal normalization theorem.

For any fixed \(h\ge0\), define the continuous maximum
\[
\mathcal P_Z(h)=
\max_{1/2\le a\le1}
       \{\mathcal E(a,Z)+h(a-1/2)\}.                              \tag{16}
\]
In fact the decrease is uniformly stronger than (15). Put
\[
                     c_*=\frac18+\frac{53}{37800}.
                                                                    \tag{16a}
\]
Then
\[
\boxed{\quad
\mathcal E(a,Z)-\mathcal E(1/2,Z)
                       \le-c_*(a-1/2),\qquad1/2\le a\le1.
\quad}                                                            \tag{16b}
\]
To prove this, write \(t=a-1/2\) and
\(J(a)=\int_0^a\log(2\sin\pi x)\,dx\), with \(J(1/2)=0\).
On \([1/2,5/6]\), the function
\(f(a)=\log(2\sin\pi a)\) is decreasing and concave, with
endpoint values \(\log2\) and zero. Its chord gives
\[
J(5/6)\ge\frac{\log2}{6}.
\]
The averages of a decreasing function are decreasing. Therefore
\[
\frac{J(1/2+t)}{t}\ge\frac{\log2}{2},
                             \qquad0<t\le1/3.
\]
Integrating the first line of (14) gives a middle action loss
at least \(t(\log2/4+\gamma_0)\).

For \(1/3\le t\le1/2\), the second line of (14) instead gives
the affine lower bound for the loss
\[
\mathcal E(1/2,Z)-\mathcal E(1/2+t,Z)
\ge\frac{\log2}{12}+\frac{\gamma_0}{3}
                         +\gamma_1(t-1/3).                      \tag{16c}
\]
All needed logarithm bounds are elementary:
\[
\log2>\frac23,\qquad
\gamma_0=\log(1+1/125)>\frac1{126},\qquad
\gamma_1=\log(1+3/97)>\frac3{100}.
\]
The first follows from
\(\log2=2\int_0^{1/3}(1-x^2)^{-1}\,dx\); the others follow
from \(\log(1+x)>x/(1+x)\).
The middle loss per \(t\) thus exceeds \(11/63\).
At \(t=1/2\), twice (16c) exceeds
\[
\frac19+\frac1{189}+\frac1{100}
                      =\frac18+\frac{53}{37800}=c_*.
\]
At \(t=1/3\), (16c) divided by \(t\) exceeds \(11/63>c_*\);
indeed \(11/63-1/8=25/504=1875/37800\).
The difference between (16c) and \(c_*t\) is affine.
Its two endpoint signs prove (16b) throughout the tail, and the
middle estimate proves it on the rest of the interval.

Consequently
\[
\mathcal P_Z(h)=\mathcal E(1/2,Z)
                  \qquad(0\le h\le1/8).                          \tag{17}
\]
The coefficient reserve \(c_*-1/8=53/37800\) remains positive.
For larger \(h\), (16) retains the actual outgoing action rather
than replacing its variation by a constant decay rate.

## 3. The complete trailing column and every coefficient

Keep the original complete signed outgoing polynomial
\[
\alpha_{b,N}(Z)=(-q)^bC_{b,N}(Z).
\]
Let
\[
I_N^+=[M,D]\cap\mathbb Z,\qquad
G_N^+=(\mathcal J_{I_N^+,N}-ZI)^{-1}.
                                                                    \tag{18}
\]
This is the natural-last-row inverse of the
[trailing determinant theorem](research_mixed_next_outgoing_trailing_determinants.md).
It differs from the inverse on \([M,D-1]\) used in the first
Green-ellipse theorem. Its exact column is
\[
(G_N^+)_{b,M}
 =\frac{\alpha_{b,N}}{qA_M\alpha_{M-1,N}},\qquad M\le b\le D.
                                                                    \tag{19}
\]
The complete lower boundary value is nonzero by that theorem.
Here \(A_M=Y_M(Y_M-1)\), \(Y_M=r^M\), and \(\mathcal J_N\)
is its original signed three-term operator, with the same row
order and terminating coefficient.

With the unchanged Newton quotient, define
\[
\begin{split}
P_b^{\rm rad}(\zeta)
 &=\frac{e_b(\zeta)}{e_M(\zeta)}
   =\prod_{h=M}^{b-1}\frac{c_h-\zeta}{s_{h+1}^2},\\
\nu_N^+(\zeta,Z)
 &=\sum_{b=M}^{D}(G_N^+)_{b,M}P_b^{\rm rad}(\zeta).
\end{split}                                                       \tag{20}
\]
Its degree is at most \(U\), not \(U-1\). There are exactly
\(U+1\) double nodes \(c_j\), so exact cardinal interpolation
still applies to this degree.

The two-sided absolute anchor, its uniform logarithmic error,
and \(|A_M|=s_M\) bounded away from zero imply
\[
|(G_N^+)_{b,M}|
\le C N^A
 \exp N\{\mathcal E(b/N,Z)-\mathcal E(1/2,Z)\}
                         \qquad(M\le b\le D).                    \tag{21}
\]
Here and below \(C,A\) are fixed, uniform over (11) and both
parities. Polynomial factors include the exact \(S_b/N\) and
the half-input \(N^{-1/2}\) normalization; they do not conceal
an exponential anchor.

For \(1\le k\le U\), put
\[
\nu_N^{+,<k}=\sum_{b=M}^{M+k-1}(G_N^+)_{b,M}P_b^{\rm rad}.
                                                                    \tag{22}
\]
Its degree is at most \(k-1\). The original physical quotient
bound, valid through \(D\), is
\[
 |P_b^{\rm rad}(c_j)|\le CN^2.
                                                                    \tag{23}
\]
It retains its literal zeros when \(j>D-b\); on the remaining
nodes the factors telescope to \(s_M^2/s_b^2\).
Monotonicity in (15), (21), and (23) therefore give
\[
\max_j|\nu_N^+(c_j,Z)-\nu_N^{+,<k}(c_j,Z)|
\le C N^A
 e^{N\{\mathcal E((M+k)/N,Z)-\mathcal E(1/2,Z)\}}.
                                                                    \tag{24}
\]
The sum contains at most \(N\) terms. The exact cardinal norms
are polynomial at both parities, as in
[finite Green localization, Section 4](research_mixed_next_outgoing_finite_green_localization.md).
Applying those norms to the degree-at-most-\(U\) difference
in (24) proves the same bound on the entire real interval
\([-2,2]\), with a larger fixed polynomial factor.

Write the exact Chebyshev expansion
\[
\nu_N^+(\zeta,Z)
     =\sum_{k=0}^{U}\widehat\nu^+_{k,N}(Z)T_k(\zeta/2).
                                                                    \tag{25}
\]
For \(k\ge1\), subtracting (22) does not change its \(k\)-th
coefficient. The elementary cosine-coefficient bound, and the
same real norm argument for \(k=0\), prove
\[
\boxed{\quad
|\widehat\nu^+_{k,N}(Z)|
\le CN^A
 \exp N\{\mathcal E(1/2+k/N,Z)-\mathcal E(1/2,Z)\},
                         \qquad0\le k\le U.
\quad}                                                            \tag{26}
\]
We used \((M+k)/N\ge1/2+k/N\) and the decreasing action.
Thus no parity-dependent argument just outside the endpoint is
introduced.
Combining (26) with (16b) yields the explicit stronger coefficient
bound
\[
                  |\widehat\nu^+_{k,N}(Z)|
                         \le CN^A e^{-c_*k},\qquad0\le k\le U.
                                                                    \tag{26a}
\]

The terminal coefficient in (26) has not been deleted. Indeed,
for \(U\ge1\) its exact expression is
\[
\widehat\nu^+_{U,N}
 =2(-1)^U\frac{S_M^2}{N^2}
       \frac{(-q)^D}{qA_M\alpha_{M-1,N}} .
                                                                    \tag{27}
\]
Only \(b=D\) contributes to the leading degree. Its Newton
leading coefficient is \((-1)^U S_M^2/N^2\), and
\(T_U(\zeta/2)\) has leading coefficient \(1/2\).
This also checks the original terminating value \(C_{D,N}=1\).

Let \(\mathcal E_h\) be the filled spectral ellipse with boundary
\(\zeta=2\cos(\vartheta+ih)\). Summing (26), using
\(|T_k(\zeta/2)|\le e^{kh}\), and then the maximum principle,
gives the action-dependent ceiling
\[
\boxed{\quad
\|\nu_N^+(\cdot,Z)\|_{\mathcal E_h}
\le CN^A
 e^{N\{\mathcal P_Z(h)-\mathcal E(1/2,Z)\}},
                                      \qquad h\ge0.
\quad}                                                            \tag{28}
\]
The same fixed polynomial exponent works for each fixed height.
For \(0\le h\le1/8\), this is a polynomial ceiling for the
new degree-\(U\) insertion. In particular it holds on the closed
ellipse of height \(1/8\), without an exponential tolerance.
For larger heights it records the full actual rate cost.

## 4. Attach before applying the global probe

Define the exact attached polynomial
\[
\begin{split}
F_N^+(\zeta,Z)
 &=qA_M\alpha_{M-1,N}(Z)\nu_N^+(\zeta,Z)\\
 &=\sum_{b=M}^{D}\alpha_{b,N}(Z)P_b^{\rm rad}(\zeta).
\end{split}                                                       \tag{29}
\]
Equations (28) and the absolute half-input anchor imply
\[
                  \|F_N^+(\cdot,Z)\|_{\mathcal E_h}
                       \le CN^A e^{N\mathcal P_Z(h)}.
                                                                    \tag{30}
\]
All phases remain in (29). The common outgoing factor has
been attached before any probe estimate, so no separate
exponential cost for \(\alpha_{M-1,N}\) is added to (30).

Use the original full observation
\[
\mathcal L_N(F)=\phi_N[R_N^3e_MQ_N^{\rm full}F].
                                                                    \tag{31}
\]
Then the exact trailing reduction, with its already paid forcing
and cutoff replacement, reads
\[
\mathcal T_0[F_{\rm in,N}](-2,Z_*)
 = I_{{\rm geom},N}
   +\frac{1}{\kappa_N^2N}\mathcal L_N(F_N^+(\cdot,Z_*))
   +O(e^{N(\Lambda-\epsilon_0)}).
                                                                    \tag{32}
\]
The symbol \(F_{\rm in,N}\) here is the original incoming source,
not the attached polynomial in (29).
The exact identity behind (32) is
\[
\mathcal L_N(F_N^+)
       =\sum_{b=M}^{D}(-q)^b
                    \phi_N(R_N^3e_bQ_N^{\rm full})C_{b,N}.
                                                                    \tag{33}
\]
Neither the entire transformed cutoff forcing nor a last-row
boundary value has been silently dropped.

For fixed \(0<r<R<R_*\), let \(c(r,R)>0\) be the finite Neumann
constant of the adopted
[global analytic probe](research_mixed_next_outer_global_analytic_probe.md).
The input \(F_N^+(-2\cos u,Z)\) is even and periodic and is
holomorphic on every fixed strip. Applying that theorem to
(30) gives, for every \(\tau>0\),
\[
\boxed{\quad
|\mathcal L_N(F_N^+(\cdot,Z))|
\le C_\tau N^{A_\tau} e^{N\mathcal P_Z(R)}
 \left\{N^{-1}
       +e^{N(\mathfrak M_3+\tau-c(r,R))}\right\}.
\quad}                                                            \tag{34}
\]
Its exact full-Hermite identity still has the original even
forcing \(4\kappa_N^3/N^2\), zero odd forcing, and all three
test zeros. The global probe introduces no artificial matching
endpoints. Equation (34) uses the exact finite source and does
not insert a pointwise relative packet error into a cancelling
sum.

Thus a sufficient uniform strict budget, on any specified actual
family, is
\[
\mathcal P_{Z_*}(R)+
              \max\{0,\mathfrak M_3-c(r,R)\}<\Lambda .
                                                                    \tag{35}
\]
When \(R\le1/8\), (17) gives the earlier anchored criterion
on this larger input strip. At larger allowed heights, (16)
gives the actual cost to optimize against a possibly stronger
probe gain.
No repetition of Neumann cycles is treated as free: the input
norm on the wider strip is precisely the cost in (30).

The estimates (4), (26), and (28)--(34) are proved on the
original source. The inequality (35) has not been verified.
In particular this note does not close the remaining coherent
boundary product or prove stability under arbitrary fixed short
fillings.

## Source versions

- Absolute outgoing anchor:
  51c9e5f1a47be3d9f3e1fa756e390a98c07f84c33f1aa0ad5ee5b948771229ab.
- Original action terminal normalization:
  5b46b329c54cf252fc9d52f91e546fda47eadcfb2a0b62b842881c1bd2d87ce4.
- Middle selected-action inequality:
  77ffb14e6f3a3408b4aee3594d1c205b9db61fccdbf011181de9f86c26e9dbd5.
- Full-tail energy:
  0037a31d5f2a8cedea53d70bf1f0434f906668fe0934e5ee303890a8b3eceee7.
- Natural trailing determinants and complete-source reduction:
  8564c705a0c8cd96cb7211c10166a522dde511bda27a94ac18a7cdafccf0b47f.
- Finite Green interpolation and exact node polynomials:
  b0cc349962797f5ef5afb3d4aec87fd2caf5a3740bb0041a0c6a8ae4d48e4492.
- Global analytic probe:
  cb47c9d87949e276615443150b2da2260fec5bb09d3780039b90b322cd14eeb8.
