# The fixed-polynomial turn is an even, uniformly weighted reversal

Private proof, 1 November 2026. No repository file is changed.

The sine-binomial turn matrix has a simpler form when the input is written in the fixed complete polynomial basis. The moving Newton connection cancels its triangular part exactly. In these coordinates the physical turn is a weighted reversal, with weights bounded above and below independently of the level before the first ordinary-color resonance. This controls every diagonal weighted Newton norm relative to the original reversal. It does not assert equivalence with the full spectral-jet norm.

## 1. Fixed input polynomials

Retain
\[
N\ge2,\quad d=N-1,\quad \theta=\pi/N,\quad q=e^{i\theta},
\quad M=q^s,\quad |s|\le R<1.
\]
Let \(e_n^0\) be the complete Newton basis, and define
\[
P_n(s)=\prod_{r=1}^n\frac{\sin((r-s)\theta)}{\sin(r\theta)},
\qquad
H_N(s)=P_d(s)=\frac{\sin(\pi s)}{N\sin(\pi s/N)}.
\tag{1}
\]
The function \(H_N\) is the previous boundary factor \(H_N(z)\) with \(z=2\pi i s\). Its value at \(s=0\) is one.

Define the paired weight
\[
W_n(s)=P_n(s)P_n(-s)
=\prod_{r=1}^n
 \left(1-\frac{\sin^2(s\theta)}{\sin^2(r\theta)}\right).
\tag{2}
\]
The empty product is one.

A fixed polynomial \(f\) means its canonical degree-\(<N\) polynomial representative, written
\[
f(z)=\sum_{n=0}^d\alpha_n e_n^0(z).
\tag{3}
\]
When used as input at color \(s\), it is evaluated in the actual moving equal-color Casimir. The coefficients \(\alpha_n\) in (3) are not the moving Newton coefficients. No equality of the moving and constant multiplication algebras is being assumed.

Let \(J\) reverse the \(N\) coordinates. The same-color-to-mixed turn uses the physical currying and the normalized carrier
\(\check R_{x,y}r_0^{-1}\) from [the typed-turn calculation](/private/tmp/md-main-meridian-typed-turn-newton-coefficients.md). Its output is expanded in the opposite-color complete Newton basis.

**Theorem.** In the fixed polynomial coordinates (3), this actual turn is
\[
\boxed{\quad
\mathscr T_s^{\mathrm{fix}}\alpha
=\frac{q^{-s^2/2}}{H_N(s)}
       J\operatorname{diag}(W_n(s))\,\alpha.
\quad}
\tag{4}
\]
In particular it is exactly even in \(s\), including the retained Gaussian scalar.

## 2. Proof from the physical source matrix

The physical highest-vector and cup-slide calculation gives
\[
\operatorname{coeff}\mathscr T_s^{\mathrm{fix}}(f)
=\frac{\kappa_{xy}}{H_N(s)}
       S_s f(A_s)e_0,\qquad
S_s=J R_0^{-1}D_s,
\tag{5}
\]
where \(D_s=\operatorname{diag}P_n(s)\),
\(\kappa_{xy}=q^{(d^2-s^2)/2}\), and
\(R_0e_0=\kappa_0e_0\), \(\kappa_0=q^{d^2/2}\).
The same source calculation proves \(S_sA_sS_s^{-1}=L_s\), with
\[
\begin{aligned}
(L_s)_{kk}&=c_k(0),\\
(L_s)_{k-1,k}&=-4\sin((k-s)\theta)\sin((k+s)\theta),\\
(L_s)_{d,0}&=(-1)^{N+1}4\sin^2(s\theta).
\end{aligned}
\tag{6}
\]
No other entries are nonzero. Since \(S_se_0=\kappa_0^{-1}e_d\), equation (5) becomes
\[
\operatorname{coeff}\mathscr T_s^{\mathrm{fix}}(f)
=\frac{q^{-s^2/2}}{H_N(s)}f(L_s)e_d.
\tag{7}
\]

For \(0\le n<N\), direct induction gives
\[
e_n^0(L_s)e_d=W_n(s)e_{d-n}.
\tag{8}
\]
For \(n=0\) this is the initial vector. At the next step use
\[
e_{n+1}^0(L_s)
=\frac{c_n(0)-L_s}{4\sin^2((n+1)\theta)}e_n^0(L_s).
\]
The diagonal vanishes on \(e_{d-n}\), because \(c_{d-n}(0)=c_n(0)\). Its upper neighbor contributes the factor
\[
\frac{\sin((d-n-s)\theta)\sin((d-n+s)\theta)}
     {\sin^2((n+1)\theta)}
=1-\frac{\sin^2(s\theta)}{\sin^2((n+1)\theta)}.
\]
This is precisely the next factor in (2). The wrap entry cannot contribute: the input vector reaches \(e_0\) only after \(d\) steps, and all canonical input polynomials have degree at most \(d\). Thus no wrap has been omitted from the matrix identity; it is merely unreachable in this particular degree-\(<N\) evaluation. Substitution of (8) in (7) proves (4).

Equivalently, if \(C_s\) is the row-convention connection
\(e_n^s=\sum_k(C_s)_{nk}e_k^0\), the previously proved moving-frame turn satisfies the exact identity
\[
T_s C_s^{-T}
=\frac{q^{-s^2/2}}{H_N(s)}
           J\operatorname{diag}(W_n(s)).
\tag{9}
\]
This proves that the cancellation of its triangular factor is an exact coordinate calculation. Its moving-frame entries with \(k+n>d\) have not been discarded.

The alternative form proposed from the physical matrix perturbation is also immediate:
\[
\operatorname{coeff}\mathscr T_s^{\mathrm{fix}}(f)
=\frac{\kappa_{xy}}{H_N(s)}
 J R_0^{-1} f(A_0+\rho^2[s]^2K)e_0.
\tag{10}
\]
Indeed \(D_sA_sD_s^{-1}=A_0+\rho^2[s]^2K\) and \(D_se_0=e_0\). Formula (8) evaluates this structured functional calculus in the fixed Newton basis.

## 3. Uniform bounds from the paired sine product

The following constants work at every level:
\[
\left(\frac{\sin(\pi R)}{\pi R}\right)^2
\le |W_n(s)|
\le
\left(\frac{\sinh(\pi R)}{\pi R}\right)^2
\qquad(0\le n<N,\ |s|\le R<1).
\tag{11}
\]
At \(R=0\), the quotients have their limiting value one.

To prove (11), the Euler sine product gives the exact absolutely convergent identity
\[
\frac{\sin((r-s)\pi/N)\sin((r+s)\pi/N)}
     {\sin^2(r\pi/N)}
=\prod_{k\in\mathbb Z}
       \left(1-\frac{s^2}{(r+kN)^2}\right).
\tag{12}
\]
It can be obtained by pairing the shifted sine products at \(s\) and \(-s\); the linear exponential factors cancel and the value at zero is one. Multiplying over \(1\le r\le n<N\), the integers \(r+kN\) are distinct and nonzero. Each factor obeys
\[
1-\frac{R^2}{m^2}
\le\left|1-\frac{s^2}{m^2}\right|
\le1+\frac{R^2}{m^2}.
\]
The product over this subset is bounded below by the product of the lower factors over all nonzero integers, and above by the product of the upper factors over all nonzero integers. The Euler sine and hyperbolic-sine products evaluate those two products as the sides of (11). This also proves the nonvanishing assertion without a choice of logarithm.

Reflection gives
\[
W_n(s)W_{d-n}(s)=H_N(s)^2.
\tag{13}
\]
In particular \(W_d=H_N^2\), so (11) supplies level-independent upper and lower bounds for \(H_N\) as well. The Gaussian \(q^{\pm s^2/2}\) and its inverse are bounded on the same disk because \(N\ge2\).

It follows from (4) that the turn and its inverse have level-independent operator bounds in the unweighted Newton coefficient \(\ell^p\) norms, \(1\le p\le\infty\). More generally, the comparison holds pointwise:
\[
C_R^{-1}|\alpha_{d-k}|
\le |(\mathscr T_s^{\mathrm{fix}}\alpha)_k|
\le C_R|\alpha_{d-k}|.
\tag{14}
\]
Thus every diagonal weighted Newton norm inherits precisely the weight transfer of the complete reversal, with the same level-independent extra constant. The diagonal weights may themselves depend exponentially on the level: no comparison of those weights is needed for the relative estimate (14). Fixed derivatives in \(s\) have uniform bounds on smaller disks, by Cauchy's formula applied to the individual diagonal entries.

## 4. All six orientation types in the same fixed frame

Define
\[
\mathcal M_s=H_N(s)^{-1}J\operatorname{diag}(W_n(s)).
\tag{15}
\]
Equation (13) implies the exact involution identity
\[
\mathcal M_s^2=I.
\tag{16}
\]

For the orientation conventions of the typed-turn report, the four-cycle of forward turns is
\[
++\longrightarrow(-+\to+-)\longrightarrow--
 \longrightarrow(+-\to-+)\longrightarrow++.
\]
Their fixed-polynomial coefficient matrices, in that order, are
\[
q^{-s^2/2}\mathcal M_s,\qquad
q^{s^2/2}\mathcal M_s,\qquad
q^{s^2/2}\mathcal M_s,\qquad
q^{-s^2/2}\mathcal M_s.
\tag{17}
\]
The first is (4). Two physical turns dualize \(f(\Omega)\) and leave its polynomial unchanged because the antipode fixes the Casimir. In fixed polynomial coordinates there is no intervening basis connection, so the next turn is the inverse of the first. The carrier obtained when the zero-charge reference order is swapped obeys
\(G'G=q^{-s^2}I\), by the full Hermite monodromy identity proved in the typed-turn report. This gives the third scalar in (17), and duality gives the fourth.

The remaining two types, the turns between the opposite-color endomorphism spaces, have matrix exactly \(\mathcal M_s\). Indeed their proved scalar reversal is
\[
\frac{P_n(-s)}{P_{d-n}(-s)}
=\frac{W_n(s)}{H_N(s)}.
\tag{18}
\]
Consequently the relative estimate (14), and its inverse, applies to every actual orientation type with its original duality, pivotal conventions and normalized carrier.

## 5. Uniform bulk comparison and its first correction

For every fixed \(\delta>0\), uniformly on
\(\delta N\le n\le(1-\delta)N\) and \(|s|\le R<1\),
\[
\log\frac{W_n(s)}{H_N(s)}
=\frac{\pi s^2}{N}\cot(\pi n/N)
       +O_{R,\delta}(N^{-2}).
\tag{19}
\]
The logarithm is the holomorphic branch equal to zero at \(s=0\). All fixed \(s\)-derivatives have the same uniform error on smaller disks.

To prove this without expanding an endpoint factor, use the symmetry of the factors in (2) under \(r\mapsto N-r\). If \(N=2M+1\), then \(H_N=W_M\). If \(N=2M+2\), then \(H_N=W_M\cos(s\theta)\). These identities follow from \(W_d=H_N^2\), their values at \(s=0\), and the symmetric middle factor. Thus \(\log(W_n/H_N)\) is a signed sum of factors whose indices lie between \(n\) and the midpoint, with the stated possible half-weight middle term.

On this interval every sine denominator stays uniformly away from zero. Each logarithm is
\[
\log\left(1-\frac{\sin^2(s\theta)}{\sin^2(r\theta)}\right)
=-\frac{\pi^2s^2}{N^2}\csc^2(\pi r/N)+O_{R,\delta}(N^{-4}).
\]
The finite sum of the errors is \(O(N^{-3})\). A Riemann sum from the midpoint to \(n/N\), with the endpoint correction of size \(O(N^{-2})\), gives
\[
-\frac{\pi^2s^2}{N}\int_{1/2}^{n/N}\csc^2(\pi t)\,dt
=\frac{\pi s^2}{N}\cot(\pi n/N).
\]
This proves (19); the bounds are holomorphic on a slightly larger \(s\)-disk, so Cauchy's formula gives the derivative statement.

For the specified same-color-to-mixed turn, its entry on the reversed \(n\)-th coefficient is consequently
\[
\exp\left[
\frac{\pi s^2}{N}
 \left(\cot(\pi n/N)-\frac{i}{2}\right)
 +O_{R,\delta}(N^{-2})
\right].
\tag{20}
\]
The sign-reversed fixed-reference type changes the Gaussian term to \(+i/2\); the opposite-color endomorphism turn has no Gaussian term. In particular every fixed bulk coefficient and jet approaches its complete reversed value. Equation (19) makes no such \(1+O(N^{-1})\) claim at the boundary indices; those retain the uniform estimate (14).


## 6. What this comparison retains

The fixed polynomial frame is legitimate for both the constant opposite-color and moving same-color algebras: each canonical representative has degree less than \(N\). Their multiplication laws still differ. The latter has the actual moving relation
\(\mathcal T_N+2\cos(2\pi s)\); the wrap in (6) records that change. Nothing in (8) or (14) deletes the corresponding newly opened multiplication sectors.

The full spectral-jet and Chebyshev norms are also distinct from a diagonal Newton coefficient norm. A uniformly bounded diagonal sequence in an exponentially conditioned basis need not define a uniformly bounded spectral operator. This report therefore proves the sharp fixed-frame Newton comparison and exact evenness, while leaving spectral control of the paired multiplier (2) as a separate analytic question.

The separately proved spectral unit
\(D_s^{-1}B_sD_{-s}=\operatorname{Mult}(a_s)\)
remains valid and polynomially controlled on the full confluent algebra. In fixed input coordinates, (9) makes the stronger cancellation explicit; it does not require estimating the unpaired diagonal \(P_n(s)^2\) by itself. No whole-knot estimate or identification of the regular microscopic limit is inferred here.

