# Even crossing representatives on the full cover and their left-cut current

Written research proof, 23 November 2026.

The entire microscopic crossing function has an explicit partial-fraction
expansion. It gives uniform bounds on the full physical logarithmic cover,
an exact finite-level left-cut jump, and a uniform integrable bound at the
cut endpoint. The original polynomial spectator and genuine turn kernel
remain in the resulting finite-contour identity. No bound for the rest of
that contour or for a general short-component closing is inferred.

## 1. Original source and the even representative

Put \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), \(\eta=(-1)^d\), and
\[
 P_N(z)=2T_N(z/2)+2,\quad \kappa=e^{\pi i d^2/(2N)},\quad
 c_j=2\cos((2j+1)\pi/N),\quad w_N(\alpha)=2\cosh(\alpha/N).
 \tag{1}
\]
All algebra classes are in the full \(\mathbb C[z]/P_N\). The original
functional and genuine turn satisfy
\[
 \phi_N=\eta N^2[z^d]\operatorname{rem}_{P_N},\quad
 \phi_N(e_i e_j)=\delta_{i+j,d},\quad \mathsf T e_i=e_{d-i},
 \quad K_N(z,w)=\sum_{i=0}^d e_i(z)e_i(w).
 \tag{2}
\]
In particular \((\mathsf T f)(w)=\phi_{N,z}(f(z)K_N(z,w))\).
Let \(r_{n,N}=\kappa^{-n}R^n\) denote the canonical normalized power.
For \(m=\lfloor N/2\rfloor\), its distinct double-node data are
\[
 r_{n,N}(c_j)=\nu_j^n,\quad r_{n,N}'(c_j)=in\gamma_j\nu_j^n,\quad
 \nu_j=(-1)^jq^{j(j+1)},\quad
 \gamma_j=\frac{N-1-2j}{4\sin((2j+1)\pi/N)}\quad(0\le j<m).
 \tag{3}
\]
At odd \(N=2m+1\) only the value \(\nu_m^n\) at \(-2\) is prescribed.
These include all original first spectral normals, not just values.

Use the entire even functions of [M]:
\[
 c(\alpha)=\cosh(\alpha/2),\quad P(\alpha)=4c(\alpha)^2,\quad
 D(\alpha)=1+\sum_{k\ge1}(\mathsf E_k(\alpha)-\mathsf H_k(\alpha)).
 \tag{4}
\]
That note proves \(r_{1,N}(w_N(\alpha))\to D(\alpha)+ic(\alpha)\)
uniformly on compact complex disks with every fixed derivative. Define
\[
 U_n=\begin{cases}D+inc,&n\text{ odd},\\1+incD,&n\text{ even},\end{cases}
 \qquad G_{n,N}(\alpha)=
 e^{-in(\alpha^2+\pi^2)/(4\pi N)}U_n(\alpha),\qquad n\in\mathbb Z.
 \tag{5}
\]
The construction includes negative powers and zero.

## 2. A source derivation of the partial fractions

Write \(\beta_j=(2j+1)\pi\). We prove
\[
 \boxed{\quad
 D(\alpha)=-4c(\alpha)^2\sum_{j\ge0}(-1)^j
 \left\{\frac1{(\alpha-i\beta_j)^2}
                  +\frac1{(\alpha+i\beta_j)^2}\right\}.
 \quad} \tag{6}
\]
Each apparent pole is removable after multiplication by \(c^2\).
The proof below retains the finite oscillating normal contribution.

At a double root write \(P_N=(z-c_j)^2Q_j\). Direct Chebyshev
differentiation gives
\[
 Q_j(c_j)=N^2/(4-c_j^2),\qquad Q_j'(c_j)/Q_j(c_j)=c_j/(4-c_j^2).
\]
Indeed \((4-z^2)P_N''-zP_N'+N^2(P_N-2)=0\), and its derivative
at the double root determine \(P_N''(c_j)\) and \(P_N'''(c_j)\).
Partial fractions of the canonical polynomial divided by \(P_N\),
using (3), are therefore exactly
\[
 \frac{r_{1,N}(z)}{P_N(z)}
 =\frac1{N^2}\sum_{j<m}\nu_j
 \left\{\frac{4-c_j^2}{(z-c_j)^2}
       +\frac{i\gamma_j(4-c_j^2)-c_j}{z-c_j}\right\}
 +\mathbf1_{N\text{ odd}}\frac{\nu_m}{N^2(z+2)}.
 \tag{7}
\]
There is no polynomial part. Fix a circle \(|\alpha|=A\) with radius
different from every \(\beta_j\), and set \(z=w_N(\alpha)\). Since
\(P_N(w_N(\alpha))=P(\alpha)\), the summand in braces divided by \(N^2\)
is \(A_{j,N}+iB_{j,N}\), where, with
\(\theta_j=\beta_j/N\) and \(\delta_j=w_N(\alpha)-2\cos\theta_j\),
\[
 A_{j,N}=\frac{4\sin^2\theta_j}{N^2\delta_j^2}
                    -\frac{2\cos\theta_j}{N^2\delta_j},\qquad
 B_{j,N}=\frac{(N-2j-1)\sin\theta_j}{N^2\delta_j}.
 \tag{8}
\]
For each fixed \(j\), uniformly on this circle,
\[
 A_{j,N}\to\frac{2(\beta_j^2-\alpha^2)}{(\alpha^2+\beta_j^2)^2},
 \qquad B_{j,N}\to\frac{\beta_j}{\alpha^2+\beta_j^2},\qquad
 \nu_j\to(-1)^j.
 \tag{9}
\]

Here is the uniform finite-tail estimate needed to pass to these limits.
For \(j\ge J_A\), put \(u=\pi(j+\tfrac12)/N\) and
\(\zeta=\sinh(\alpha/(2N))\). Then
\(\delta_j=4(\sin^2u+\zeta^2)\), and \(J_A\) can be fixed so that
\[
 |\sin^2u+\zeta^2|\ge\tfrac12\sin^2u,\qquad
 |A_{j,N}|\le C_A/(j+1)^2 .
 \tag{10}
\]
Indeed \(|\zeta|=O_A(N^{-1})\) and
\(\sin u\ge2u/\pi\) for \(0\le u\le\pi/2\).
Thus the \(A\)-tail is absolutely \(O_A(J^{-1})\).

The \(B\)-tail requires its phase. Exactly
\(\nu_{j+1}=-q^{2j+2}\nu_j\). Remove the last index \(j=m-1\);
its \(B\) is \(O_A(N^{-3})\), at either parity. For \(j\le m-2\) put
\[
 a_j=\frac{B_{j,N}}{1+q^{2j+2}},\quad h=\frac{\pi}{2N},\quad
 v=\frac\pi2-u.
\]
Here \(v\ge3h\), so the denominator is nonzero. Direct substitution gives
\[
 a_j=\frac{e^{-i(u+h)}}{2\pi N}
       \frac{v\sin v}{\sin(v-h)}
       \frac{\sin u}{\sin^2u+\zeta^2}.
 \tag{11}
\]
The first real quotient in (11) and its \(u\)-derivative are bounded
uniformly. To see this, \(\sin v/\sin(v-h)=O(1)\) for \(v\ge3h\), and
\[
 \frac d{dv}\frac{\sin v}{\sin(v-h)}
                       =-\frac{\sin h}{\sin^2(v-h)}.
\]
Multiplication by \(v\) leaves a bounded derivative, since \(h/v\le1/3\).
The last quotient in (11) and its derivative have bounds
\(C_A\csc u\) and \(C_A\cos u\,\csc^2u\), by (10). For
\(J_A\le J\le m-2\), consequently
\[
 |a_J|+\sum_{j=J}^{m-3}|a_{j+1}-a_j|+|a_{m-2}|\le C_A/J.
 \tag{12}
\]
For completeness, integrate
\(C_A N^{-1}(\csc u+\cos u\,\csc^2u)\) from \(u_J\) to \(\pi/2\).
It is \(O_A(J^{-1})\); the logarithmic term is bounded using
\(\log(N/J)/N\le C/J\). The endpoint values obey the same bound.
If \(J>m-2\), the tail contains only the removed last term or is empty.

Now \(\nu_jB_{j,N}=a_j(\nu_j-\nu_{j+1})\). Summation by parts,
\(|\nu_j|=1\), (12), and the removed last term prove
\[
 \left|\sum_{j=J}^{m-1}\nu_j B_{j,N}\right|\le C_A/J .
 \tag{13}
\]
This estimate includes the near-midpoint normal sector; its small
phase denominator was canceled explicitly in (11).
The odd simple term in (7) is \(O_A(N^{-2})\).
Taking \(N\to\infty\), then \(J\to\infty\), in (7) gives
\[
 D+ic=P\sum_{j\ge0}(-1)^j
 \left\{\frac{2(\beta_j^2-\alpha^2)}{(\alpha^2+\beta_j^2)^2}
                         +\frac{i\beta_j}{\alpha^2+\beta_j^2}\right\}.
 \tag{14}
\]
The limiting second series has uniform \(O_A(J^{-1})\) tails away
from its poles, by elementary alternating summation.

We evaluate it without importing a summation formula. For real \(\alpha\),
integrate \(e^{-\beta_jt}\cos(\alpha t)\) on \([0,\infty)\) and sum.
The finite alternating exponential sums are dominated by \(2e^{-\pi t}\).
Dominated convergence gives
\[
 \sum_{j\ge0}\frac{(-1)^j\beta_j}{\alpha^2+\beta_j^2}
                  =\int_0^\infty\frac{\cos(\alpha t)}{2\cosh\pi t}\,dt
                  =\frac1{4c(\alpha)}.
 \tag{15}
\]
For the last equality integrate \(e^{i\alpha t}/\cosh\pi t\) around
a rectangle of height \(i\). The sole pole is \(i/2\), with residue
\(e^{-\alpha/2}/(\pi i)\); the vertical sides vanish. The two horizontal
integrals give \((1+e^{-\alpha})I=2e^{-\alpha/2}\), so \(I=1/c\).
Evenness handles negative real \(\alpha\); meromorphic continuation
gives (15) elsewhere. Equation (14) now proves (6). Its normally
convergent squared-pole series times \(c^2\) is entire, so the identity
extends through all removed poles.

## 3. A one-sided formula and bounds on the full physical cover

Differentiating (15) and separating its two squared-pole sums gives
\[
 D(\alpha)=-i\sinh(\alpha/2)
       -8c(\alpha)^2 S_+(\alpha),\qquad
 S_+(\alpha)=\sum_{j\ge0}\frac{(-1)^j}{(\alpha+i\beta_j)^2}.
 \tag{16}
\]
For \(y=\Im\alpha\ge0\), this series has no poles. Abel summation gives
\[
 |S_+(x+iy)|\le\frac3{x^2+(y+\pi)^2}.
\]
Indeed the initial term is the reciprocal of that denominator and
the total variation is at most
\(2\int_{y+\pi}^{\infty}(x^2+t^2)^{-3/2}dt
\le2/(x^2+(y+\pi)^2)\).
Evenness then proves the global bound
\[
 |D(x+iy)|\le\cosh(x/2)+
       \frac{24\cosh^2(x/2)}{x^2+(|y|+\pi)^2}.
 \tag{17}
\]
In particular all fixed derivatives of \(D\) are uniformly bounded on
each vertical strip, by buffered Cauchy estimates.

For fixed \(r,L>0\), (5) and (17) imply, uniformly for \(N\ge2\),
\[
 |G_{n,N}(\alpha)|\le C_r(1+|n|)e^{|n|rL/(2\pi)}
 \quad (|\Re\alpha|\le r,\ |\Im\alpha|\le LN).
 \tag{18}
\]
The exponential's modulus is
\(\exp(n\Re\alpha\,\Im\alpha/(2\pi N))\). Fixed derivatives follow
by enlarging \(r\) to \(r+1\) and \(L\) to \(L+1/2\).
This includes the entire physical logarithmic window, not arbitrary
unbounded imaginary height at a fixed level.

At \(\alpha_j=i\beta_j\), (16) directly gives
\(D(\alpha_j)=(-1)^j,\ D'(\alpha_j)=0\).
Thus (5) has exactly
\[
 G_{n,N}(\alpha_j)=\nu_j^n,\qquad
 G_{n,N}'(\alpha_j)=-\frac{n(N-1-2j)}{2N}\nu_j^n .
 \tag{19}
\]
The value also agrees at the odd simple node \(j=(N-1)/2\), where
the displayed derivative is zero. Hermite projection at the chosen
distinct physical lifts therefore gives \(r_{n,N}\) exactly.

## 4. Exact finite-contour source and genuine turn

Evenness permits the definition
\[
 g_{n,N}(z)=G_{n,N}\!\left(N\operatorname{arccosh}(z/2)\right)
 \quad\hbox{on }\Omega=\mathbb C\setminus(-\infty,-2].
 \tag{20}
\]
The square of \(\operatorname{arccosh}(z/2)\) is holomorphic on
\(\Omega\), with its removable value at \(2\); hence (20) is holomorphic
there. On \((-2,2)\) take the positive lift
\(\alpha=iN\arccos(z/2)\). No holomorphy through \(-2\) is asserted.
For any polynomial spectator \(h\), small positive circles
\(\gamma_j\subset\Omega\) around the distinct double nodes give exactly
\[
 \phi_N(R^nh)=\kappa^n\left\{
 \frac{\eta N^2}{2\pi i}\sum_{j<m}
      \oint_{\gamma_j}\frac{g_{n,N}(z)h(z)}{P_N(z)}\,dz
 +\mathbf1_{N\text{ odd}}\nu_m^n h(-2)\right\}.
 \tag{21}
\]
This follows from (3),(19) and the original double-root residues.
It is coefficientwise valid with polynomial boundary spectators.

There is also an exact finite slit-circle formula. Fix \(R>2\).
Let \(\Gamma_R\) be the positively oriented outer circle with its two
limits at \(-R\), using the continued branches in \(\Omega\). Write
\(z(a)=-2\cosh(a/N)\), \(r_R=N\operatorname{arccosh}(R/2)\), and
\[
 J_{n,N}(a)=G_{n,N}(a+i\pi N)-G_{n,N}(-a+i\pi N).
\]
Then
\[
 \boxed{\quad
 \phi_N(R^nh)=\frac{\kappa^n\eta N^2}{2\pi i}
 \left\{\int_{\Gamma_R}\frac{g_{n,N}h}{P_N}\,dz
       -\int_0^{r_R}\frac{J_{n,N}(a)h(z(a))}{P_N(z(a))}
                                                    z'(a)\,da\right\}.
 \quad} \tag{22}
\]
The upper cut bank runs from \(-R\) to \(-2\), giving precisely this
minus sign after substitution by \(a\).
To prove (22), apply the residue theorem to the finite slit disk,
retaining a small endpoint excision until the limit is taken.
For even \(N\) its endpoint contribution vanishes. For odd \(N\),
(19) gives \(G'_{n,N}(i\pi N)=0\); locally
\[
 g_{n,N}(z)=G_{n,N}(i\pi N)+O(z+2)+O((z+2)^{3/2}),\quad
 P_N(z)=N^2(z+2)+O((z+2)^2).
\]
Its positive local residue is \(G_{n,N}(i\pi N)h(-2)/N^2\), not half
of it. Moving the clockwise endpoint excision to the source side gives
this full contribution in (22); the odd term of (21) must not be added
a second time.

Taking \(h(z)=f(z)K_N(z,w)\) in (21) or (22) gives the exact genuine
turn of the canonical product \(R^nf\), for every \(w\), including its
boundary derivatives. All original external scalar factors remain.
Neither a contour at infinity nor an exchange with a limiting kernel
integral has been used.

## 5. Exact reflection and the full finite-level left-cut jump

Reindexing the normally convergent series (6) gives
\[
 D(\alpha+2\pi i)=-D(\alpha)-\frac{8c(\alpha)^2}{(\alpha+i\pi)^2}.
 \tag{23}
\]
Iteration and evenness give, with
\(S_N(\alpha)=\sum_{k=0}^{N-1}(-1)^k/(\alpha-i\pi(2k+1))^2\),
\[
 D(2\pi iN-\alpha)=(-1)^N[D(\alpha)+8c(\alpha)^2S_N(\alpha)].
 \tag{24}
\]
All displayed apparent poles are removable in these identities.
Put \(E_{n,N}(\alpha)=e^{-in(\alpha^2+\pi^2)/(4\pi N)}\).
For \(\alpha=a+i\pi N\), reflection is \(\alpha^*=-a+i\pi N\), and
\[
 c(\alpha^*)=(-1)^Nc(\alpha),\qquad
 E_{n,N}(\alpha^*)/E_{n,N}(\alpha)=(-1)^{nN}e^{-n\alpha}.
\]
Thus the exact full bank jump is
\[
 \boxed{\quad
 J_{n,N}(a)=E_{n,N}(\alpha)
 \begin{cases}
 (1-e^{-n\alpha})U_n(\alpha)-8e^{-n\alpha}c(\alpha)^2S_N(\alpha),
                                                     &n\text{ odd},\\
 (1-e^{-n\alpha})U_n(\alpha)-8in e^{-n\alpha}c(\alpha)^3S_N(\alpha),
                                                     &n\text{ even}.
 \end{cases}
 \quad} \tag{25}
\]
This includes zero and negative \(n\). It is a finite-\(N\) equality on
the whole finite cut in (22), not just its endpoint expansion.

## 6. Uniform endpoint density with the actual spectator retained

Fix \(r>0\) and an integer \(n\). On \(|\xi|\le r+1\), exactly
\[
 E_{n,N}(i\pi N+\xi)=
 e^{in\pi(N^2-1)/(4N)}
                e^{n\xi/2-in\xi^2/(4\pi N)}.
 \tag{26}
\]
By (17), \(U_n\) and every fixed derivative are bounded there uniformly
in \(N\), with constants depending on \(n,r\). More quantitatively,
Cauchy gives
\[
 \sup_{|\xi|\le r}|\partial_\xi^kG_{n,N}(i\pi N+\xi)|
 \le k!C_{r+1}(1+|n|)
   e^{|n|((r+1)/2+(r+1)^2/(8\pi))}.
 \tag{27}
\]
The jump is odd in \(a\). Taylor's theorem and (19) therefore give
\[
 |J_{n,N}(a)|\le C_{n,r}
 \begin{cases}a,&N\text{ even},\\a^3,&N\text{ odd},\end{cases}
 \qquad0\le a\le r .
 \tag{28}
\]
For the cubic estimate the exact first derivative at \(i\pi N\)
vanishes; oddness cancels the even Taylor coefficients.

The left-cut denominator and its differential are exactly
\[
 P_N(z(a))=\begin{cases}4\cosh^2(a/2),&N\text{ even},\\
                         -4\sinh^2(a/2),&N\text{ odd},\end{cases}
 \qquad z'(a)=-2\sinh(a/N)/N.
 \tag{29}
\]
Since \(|P_N|\ge4\) at even levels and \(|P_N|\ge a^2\) at odd
levels, and \(N^2|z'(a)|\le2a\cosh(r/2)\), (28) proves
\[
 \boxed{\quad
 N^2\left|\frac{J_{n,N}(a)}{P_N(z(a))}z'(a)\right|
                                  \le C_{n,r}a^2 .
 \quad} \tag{30}
\]
At \(a=0\) use the removable limit. For every actual scalar or normed
polynomial spectator, the portion \(0\le a\le r\le r_R\) of its endpoint
bank contribution in (22) consequently has norm at most
\[
 C_{n,r}\int_0^r a^2\|h(-2\cosh(a/N))\|\,da .
 \tag{31}
\]
In particular this is at most
\(C_{n,r}r^3\sup_{0\le a\le r}\|h(z(a))\|\), after enlarging the
constant. No degree restriction or reset of \(h\) is made. For a genuine
turn \(h=fK_N\), that entire original spectator remains on the right.

The estimate controls this endpoint's co-source density. It does not
bound the remaining interval up to \(r_R\), which can grow with \(N\),
or the outer contour, the spectator's norm, or its coherent closing.
Local nonzero crossing factors and (30) do not establish a geometric
lower bound after an arbitrary fixed short component.

## Complete proof inputs and closest coverage

All listed complete matching texts were read. [M] identifies the
entire function \(D\) from the actual full crossing. [W] supplies its
original signed-power data, and [N] the Frobenius normalization/turn.
The finite Abel estimate, global bounds, reflection, slit formula and
endpoint bound are proved above.

| Role | Complete text | SHA-256 |
| --- | --- | --- |
| M, input | [Microscopic crossing, 353 lines](research_microscopic_original_crossing_multiplier.md) | 9304576cb69c56a9ced9e4c85dcaf21164b9168c090284e3570751e122f85caf |
| W, input | [Signed Ward normals, 503 lines](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_signed_gaussian_ward_endpoint_packet.md) | 6bdced1b01917e41631386a24b337b60dfe5b04d35d70007cb56badc511a0191 |
| N, input | [Original Newton turn, 434 lines](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| Coverage | [Even Ward source, 430 lines](research_even_twist_ward_source_reduction.md) | 7cd055df1b070ecc8a5f4a4b62e821e37c616e1bbb935aa274939cf44e8e0b18 |
| Coverage | [Germ/turn remainder, 185 lines](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/research_source_germ_truncation_and_turn_remainders.md) | ed1390c5c2e2bf3dddd29f5b161c4cbfcec9ba4e9c7a22ab0d446ea40d14330b |
| Coverage | [Analytic/slit Hermite coupons, 369 lines](research_analytic_hermite_coupon_trace.md) | 6a3f0f290f9ec9e99d9a56fc0350379ef1f68f8e329ad116d5c4e2fabd786447 |

The prior slit-coupon theorem already retains general cut banks, poles
and endpoint arcs. The additions here are the actual even crossing
representative, its explicit whole-cover continuation and jump, and its
uniform endpoint density, with the genuine original turn and spectators.
No claim about a whole short-component period or volume is made.
Only written mathematics and text/hash operations were used. Earlier
finals, frozen manuscripts and public files were not changed.
