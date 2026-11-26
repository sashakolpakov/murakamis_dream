# An exact finite Newton remainder for the outer adjoint

Private algebraic source deduction, 8 November 2026. The original
outgoing polynomial admits an exact adjoint reduction to at most
eleven fixed-degree observations and the original parity forcing.
The reduction uses tests satisfying the three endpoint conditions;
it does not infer membership in the adjoint image from three zeros
of the target.

The division below has a fixed finite band in the original normalized
Newton basis. We give a crude exponential coefficient bound, but it
does not meet the required action budget. No cancellation estimate,
bounded inverse, or full transfer asymptotic is asserted. No
mathematical numerical evaluation or frozen-source edit is used.

## 1. Original operator and the constrained ordinary map

Keep
\[
\begin{gathered}
N\ge6,\quad m=\lfloor N/2\rfloor\ge3,\quad D=N-1,\quad
M=\lceil N/2\rceil,\quad U=m-1,\\
q=e^{\pi i/N},\quad \theta=\pi/N,\quad
c_j=2\cos((2j+1)\theta),\quad
s_j=2\sin(j\theta),\quad S_j=\prod_{\nu=1}^j s_\nu,\\
e_j(z)=S_j^{-2}\prod_{a<j}(c_a-z),\quad
P_N(z)=2T_N(z/2)+2,\quad
\mathcal A_N=\mathbb C[z]/(P_N).
\end{gathered}                                                     \tag{1}
\]
The full original turn, crossing, and trace are denoted by
\(T,R,\phi_N\). Multiplication by \(z\) is \(Z\), and
\(\mathcal L_n=R^{-n}(TZT)R^n\) in the full algebra.
Throughout, \(\mathcal L_n\) also denotes its original ordinary
polynomial realization from
[current-free crossing transport, Theorem 1](research_current_free_aw_crossing_transport.md).
That realization preserves \((P_N)\), including all first normals.

The exact conjugated transpose is the ordinary polynomial operator
\[
\boxed{\quad
\mathcal B_N
 =q^{-2}\mathcal L_2(\mathcal L_3^2-I)
   +q^{-3}Z\mathcal L_3-8q^{-2}\mathcal L_3
                         +(8q^{-1}+2)I .
\quad}                                                            \tag{2}
\]
In the full quotient,
\[
\mathcal B_N=R^{-3}\mathcal D_{3,N}^{\mathrm t}R^3 .
                                                                    \tag{3}
\]
This follows by conjugating the ordered transpose in
[the endpoint theorem, equation (2)](research_mixed_next_outer_adjoint_radical_endpoint_conditions.md):
\(R^{-3}\mathcal L_{-1}R^3=\mathcal L_2\),
\(R^{-3}\mathcal LR^3=\mathcal L_3\), and \(Z\) commutes with \(R\).
Equation (3) is a full-algebra identity, not just an equality of
distinct physical values.

Define the monic three-node polynomial
\[
Q_{3,N}^{\rm rev}(z)
       =(z-c_U)(z-c_{U-1})(z-c_{U-2}).
                                                                    \tag{4}
\]
For every \(h\in Q_{3,N}^{\rm rev}\mathbb C[z]\), the endpoint
theorem gives
\(\mathcal D_{3,N}^{\mathrm t}(R^3e_Mh)\in e_M\mathcal A_N\).
By (3), \(\mathcal B_N(e_Mh)\) therefore vanishes at every
distinct physical node, including the odd simple node.
The ordinary polynomial \(e_M\) is a nonzero scalar times the
product of those distinct linear factors. Consequently
\[
\boxed{\quad
\mathfrak B_Nh:=\frac{\mathcal B_N(e_Mh)}{e_M}
       \ \in\mathbb C[z],
 \qquad h\in Q_{3,N}^{\rm rev}\mathbb C[z].
\quad}                                                            \tag{5}
\]
This is ordinary divisibility before any reduction modulo \(P_N\).
The quotient is evaluated at zeros by polynomial continuation.
No division by an outgoing coefficient is involved.

## 2. Exact leading term and the eleven-dimensional remainder

For \(n>0\), the original ordinary operator satisfies
\[
\mathcal L_n(z^k)
 =(-1)^nq^{n+1+2k}z^{k+n}
                         +\text{terms of degree at most }k+n-1.
                                                                    \tag{6}
\]
Here \(k\) is any nonnegative integer. To check the coefficient,
put \(X=e^{it}\), \(z=-X-X^{-1}\), in its exact angular formula
\[
\mathcal L_nf
 =(c_0+A+C)f-q^nAX^{-n}f(t-2\theta)
                         -q^nCX^nf(t+2\theta).
                                                                    \tag{7}
\]
As \(X\to\infty\),
\[
A\longrightarrow-q^{-1},\qquad C\longrightarrow-q,\qquad
c_0+A+C=O(X^{-1}).
\]
Only the last term in (7) reaches degree \(k+n\);
\(f(t+2\theta)\) supplies \(q^{2k}\).
This proves (6), with the sign coming from \(z\sim-X\).
The polynomial removability needed for this leading-term argument
is part of the cited current-free theorem.

In (2), only \(q^{-2}\mathcal L_2\mathcal L_3^2\) reaches
degree \(k+8\). Its leading coefficient is
\[
q^{-2}(-q^{4+2k})(-q^{10+2k})q^{15+2k}
                         =q^{27+6k}.
                                                                    \tag{8}
\]
Thus every nonzero \(h\) in the domain of (5), of degree \(r\)
and leading coefficient \(h_r\), obeys
\[
\deg\mathfrak B_Nh=r+8,\qquad
[z^{r+8}]\mathfrak B_Nh=q^{27+6(M+r)}h_r.
                                                                    \tag{9}
\]
In particular the multiplier is nonzero and has modulus one.

**Theorem 1.** Every ordinary polynomial \(H\) has a unique
decomposition
\[
\boxed{\quad
H=\mathfrak B_Nh+\mathcal R,\qquad
h\in Q_{3,N}^{\rm rev}\mathbb C[z],\qquad
\deg\mathcal R\le10.
\quad}                                                            \tag{10}
\]
If \(\deg H=d\ge11\), then \(\deg h\le d-8\).
If \(\deg H\le10\), then \(h=0\) and \(\mathcal R=H\).
Equivalently,
\[
\mathbb C[z]
 =\mathfrak B_N\!\left(Q_{3,N}^{\rm rev}\mathbb C[z]\right)
                       \mathbin{\oplus}\mathbb C[z]_{\le10}.
                                                                    \tag{11}
\]

*Proof.* For each \(r\ge3\), use the monic domain element
\(Q_{3,N}^{\rm rev}z^{r-3}\). By (9) its image has degree
\(r+8\) with known nonzero leading coefficient. Subtract a
multiple of that image to eliminate the highest remaining
degree whenever it is at least eleven. This procedure terminates
and gives (10). A nonzero difference of two domain tests has
image degree at least eleven by (9), so it cannot equal a
polynomial of degree at most ten. This proves uniqueness.
\(\square\)

All operations in this proof are linear over any spectator
polynomial ring, such as \(\mathbb C[Z]\). Thus the construction
preserves the ordinary outgoing variable and its zeros.

## 3. The original Newton basis gives a twelve-term reduction

For the actual finite degrees, there is a more explicit banded
form of Theorem 1. Besides the original actions
\[
Ze_j=c_je_j-s_{j+1}^2e_{j+1},\qquad
\mathcal Le_j=c_je_j-s_j^2e_{j-1},
                                                                    \tag{12}
\]
one has
\[
\boxed{\begin{split}
\mathcal L_1e_j={}&q^{2j}s_j^2e_{j-1}
 +(4q^{2j+1}-c_0q^{4j+2})e_j\\
 &+q^{2j+2}s_{j+1}^2e_{j+1}.
\end{split}}                                                      \tag{13}
\]
The \(j=0\) lower term is zero. We use (12)--(13) only when
all indicated upper indices are at most \(D\), so no singular
\(S_N\) normalization is introduced.

For completeness, (13) follows from the exact angular identity
\[
\mathcal L_1
 =\frac{q}{q^4-1}(Z\mathcal L-q^2\mathcal LZ)
                         +\frac8{c_0}I .
                                                                    \tag{14}
\]
Its two shifted coefficients agree with (7) at \(n=1\).
For its diagonal use
\(c_0+A+C=8/(c_0+z)\), from the original transport source.
This proves (14). Substitution of (12) gives the upper and
lower coefficients in (13), using respectively
\[
q^2c_{j+1}-c_j=(q^4-1)q^{2j+1},\qquad
q^2c_j-c_{j-1}=(q^4-1)q^{2j-1}.
                                                                    \tag{15}
\]
The diagonal simplifies to the displayed
\(4q^{2j+1}-c_0q^{4j+2}\).
Here \(q^4-1\) and \(c_0\) are nonzero for \(N\ge6\).

The exact operator recurrence
\[
\mathcal L_{n+1}=8qI-qZ\mathcal L_n-q^2\mathcal L_{n-1}
                                                                    \tag{16}
\]
shows from (12)--(13) that \(\mathcal L_2,\mathcal L_3\)
have Newton bands \([-1,2]\), \([-1,3]\).
Consequently, whenever \(j\ge3\) and \(j+8\le D\),
\[
\mathcal B_Ne_j=\sum_{\nu=-3}^{8}b_{j,\nu,N}e_{j+\nu},
\qquad
b_{j,8,N}
 =q^{27+6j}\frac{S_{j+8}^2}{S_j^2}.
                                                                    \tag{17}
\]
The top coefficient also follows directly from (8) and the
leading coefficient \((-1)^j/S_j^2\) of \(e_j\).
Every coefficient in (17) is specified by (2),(12),(13),(16);
these are finite ordinary polynomial identities.

To make the size of these coefficients explicit, use the
coefficient \(\ell^1\) norm in this normalized Newton basis.
On any index range where the displayed products are defined,
\[
\|Z\|_1,\|\mathcal L\|_1\le6,\qquad
\|\mathcal L_1\|_1\le14,\qquad
\|\mathcal L_2\|_1\le98,\qquad
\|\mathcal L_3\|_1\le610.
                                                                    \tag{18}
\]
These follow from \(|c_j|\le2\), \(s_j^2\le4\), and (16).
Therefore every eligible column of (17) has absolute sum at most
\[
C_B:=98(610^2+1)+14\cdot610+10.
                                                                    \tag{19}
\]
This fixed constant is independent of \(N\).

Now put \(L=\lfloor N/6\rfloor\), \(d=U-L\), and define
\[
Q_{\ell,N}^{\rm rev}(z)
       =\prod_{a=U-\ell+1}^{U}(z-c_a),\qquad 0\le\ell\le d.
                                                                    \tag{20}
\]
The original node reflection \(c_{M+a}=c_{U-a}\) gives
\[
\frac{e_{M+\ell}}{e_M}
       =(-1)^\ell\frac{S_M^2}{S_{M+\ell}^2}Q_{\ell,N}^{\rm rev}.
                                                                    \tag{21}
\]
Thus if \(3\le r\) and \(r+8\le d\), (17) gives the exact
reverse-Newton band \([r-3,r+8]\) for
\(\mathfrak B_NQ_{r,N}^{\rm rev}\).
Its twelve terms retain both endpoint conditions and all
ordinary factors.

For a target written as
\[
e_MH=\sum_{\ell=0}^{d}a_\ell e_{M+\ell},
                                                                    \tag{22}
\]
the following is the explicit version of (10).
Start at \(\ell=d\) and descend to eleven. Set \(r=\ell-8\),
\(j=M+r\), and divide the current coefficient of \(e_{M+\ell}\)
by \(b_{j,8,N}\). Subtract that multiple of
\(\mathcal B_Ne_j\), and add the same multiple of \(e_j\)
to a test polynomial \(v_N\).
Only indices from \(\ell-11\) through \(\ell\) are changed.
At termination,
\[
\boxed{\quad
e_MH=\mathcal B_Nv_N+
          \sum_{\ell=0}^{\min(10,d)}\rho_\ell e_{M+\ell},
\qquad
v_N=\sum_{r=3}^{d-8}\tau_r e_{M+r}=e_Mh.
\quad}                                                            \tag{23}
\]
Empty sums are zero. In particular \(h\) satisfies all three
endpoint conditions. The construction is unique by Theorem 1.
All intermediate degrees are at most
\[
M+d=D-L=\lceil5N/6\rceil-1<N.
                                                                    \tag{24}
\]
No wrapping or quotient reduction occurs in this construction.

In this actual range, each index in the top product obeys
\[
N/2<M+r+a\le D-L<5N/6\qquad(1\le a\le8),
\]
so \(s_{M+r+a}>1\) and \(|b_{M+r,8,N}|>1\).
Set \(n_*=\max(d-10,0)\). The elimination and (19) give
the fully explicit, but crude, bound
\[
\sum_\ell|\rho_\ell|+\sum_r|\tau_r|
 \le2(1+C_B)^{n_*}\sum_{\ell=0}^{d}|a_\ell|.
                                                                    \tag{25}
\]
Indeed each elimination multiplies the remaining coefficient
norm by at most \(1+C_B\); its added test coefficient is no
larger than that preceding norm. Summing the resulting geometric
bound proves (25). This estimate rules out an unstated
level-dependent denominator in the algorithm. It does not give
a small exponential cost.

## 4. The actual outgoing source and the exact forcing

Use the unchanged outgoing polynomial and row conventions of
[the exact Newton coefficient theorem](research_mixed_next_middle_exact_newton_coefficients.md).
In its notation, \(r=q^{-2}\), \(K=\lfloor N/4096\rfloor\),
and
\[
e_MH_N(\cdot,Z)
 =\sum_{\ell=0}^{d}(-q)^\ell
       C_{0,N}^{>K}(r^{M+\ell},Z)e_{M+\ell}.
                                                                    \tag{26}
\]
The physical conditional kernel in (26) has no extra \(+N\).
Apply (23) with
\(a_\ell=(-q)^\ell C_{0,N}^{>K}(r^{M+\ell},Z)\).
The coefficients \(\rho_\ell(Z),\tau_r(Z)\) remain ordinary
polynomials in \(Z\). Put
\[
\mathcal R_N(z,Z)
 =\sum_{\ell=0}^{\min(10,d)}
                \rho_\ell(Z)\frac{e_{M+\ell}(z)}{e_M(z)}.
                                                                    \tag{27}
\]
It has degree at most ten in \(z\), and
\(H_N=\mathfrak B_Nh_N+\mathcal R_N\) exactly.

Keep the full original output and observation
\[
Q_N^{\rm full}(z)=\mathcal K_{3,N}(-2,z),\qquad
\mathcal L_N(H)=\phi_N(R^3e_MQ_N^{\rm full}H).
                                                                    \tag{28}
\]
The original seven-term theorem gives
\[
\mathcal D_{3,N}Q_N^{\rm full}=\mathfrak f_N1,\qquad
\mathfrak f_N=
\begin{cases}
4\kappa^3/N^2,&N\text{ even},\\
0,&N\text{ odd}.
\end{cases}
                                                                    \tag{29}
\]
Pair (23) with \(R^3Q_N^{\rm full}\). By (3) and the
full bilinear transpose, this yields
\[
\boxed{\quad
\mathcal L_N(H_N)
 =\mathfrak f_N\,\phi_N(R^3v_N)
       +\sum_{\ell=0}^{\min(10,d)}
          \rho_\ell(Z)\,
            \phi_N(R^3e_{M+\ell}Q_N^{\rm full}).
\quad}                                                            \tag{30}
\]
Every additional endpoint term multiplying a full-output value
or first normal vanishes because the *test* \(v_N/e_M\) has
the three zeros. The radical's consumed normal is retained in
each observation. The inner factor is still the full original
output. No shortened first-normal or odd simple-value
identification is used.

Consequently [the exact outer-source reduction, equation
(13)](research_mixed_next_three_outer_casimir_observation.md) becomes
\[
\begin{split}
\mathcal T_0[F_N](-2,Z_*)
={}&I_{{\rm geom},N}
 +\frac{(-q)^M}{\kappa^2N}
  \left\{
   \mathfrak f_N\,\phi_N(R^3v_N(\cdot,Z_*))\right.\\
 &\left.\hspace{18mm}
   +\sum_{\ell=0}^{\min(10,d)}
       \rho_\ell(Z_*)\,
       \phi_N(R^3e_{M+\ell}Q_N^{\rm full})
  \right\}
 +O(e^{N(\Lambda-\epsilon_*)}).
\end{split}                                                       \tag{31}
\]
The original scalar, both Fourier sectors, the already paid
error, and the selected geometric integral are unchanged.
Odd levels have no forcing term in (30)--(31); even levels
retain exactly (29).

Although each original reverse-Newton summand with \(\ell\ge3\)
has the three zeros, this does not say that it is an image under
\(\mathfrak B_N\). The image begins in degree eleven. In
particular the remainder in (30) is generally a linear function
of *all* the outgoing coefficients in (26), not just the first
three or first eleven. Estimate (25) cannot be replaced by a
bounded-inverse assertion because its diagonal happens to be
nonzero. The action sizes of these remaining observations,
their exact outgoing coefficients, and the even forcing
observation remain to be controlled.
