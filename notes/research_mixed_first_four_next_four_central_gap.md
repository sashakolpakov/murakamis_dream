# The first selected coordinate followed by a four-twist block

Research theorem, 6 November 2026.

For every actual mixed open critical reference of length at least three
whose first two types are four, both central Fourier phase functions
have a strict real-phase gap greater than \(1/500\) at height
\(H=1/100\). All later types may independently be three or four.
The comparison retains the original logarithmic branches, other
imaginary coordinates, and outgoing affine term.

The proof combines the frozen static endpoint estimates with a complete
interval cover of the correlated scalar budget. Its conclusion concerns
the two central phases. Estimates for the other finite rows and contour
currents remain separate; no complete finite-source or filling-volume
theorem is asserted here.

## 1. Actual references and the central alternatives

Fix \(m\ge3\) and types \(n_1,\ldots,n_m\in\{3,4\}\)
with \(n_1=n_2=4\). Use the actual open critical point from the
[original endpoint and ordinary equations](research_mixed_open_word_critical_localization.md).
Write \(e_*\) for the first private coordinate, \(z_*\) for its
attached coordinate, and \(s_*,b_*\) for the next ordinary block.
These four quantities belong to the same coupled reference. Put
\[
 x_*=(\Re e_*,\Re s_*,\Re z_*,\Re b_*),\qquad
 c=\Im z_*,\qquad H=1/100.
 \tag{1}
\]
The reference enclosures are
\[
\begin{array}{c|c|c}
 &\text{real part}&\text{imaginary part}\\ \hline
 e_*&(.333,.363)&(-.051,-.019)\\
 z_*&(.246,.350)&(-.078,-.020)\\
 s_*,b_*&(.24,.36)&(-.102,-.001).
\end{array}
\tag{2}
\]
Their sources and the coupled bound \(\Re(s_*+z_*)>.545\)
are recorded in Section 1 of the
[frozen next-four endpoint proof](research_mixed_first_four_next_four_endpoint_budget.md).

Let \(S_{\rm cap}\) denote the original calibrated private cap
action. The joint holomorphic phase is
\[
\begin{split}
 \mathcal F_4(e,s;z,b)={}&S_{\rm cap}(e)+g(e+z)+g(s+z)+g(s+b)
       -3g(s)-3g(z)-\tfrac32g(b)-g(e)\\
 &-\tfrac{i\pi}{2}(e-e^2)+2\pi izs.
\end{split}
\tag{3}
\]
All branches and additive calibrations are the original ones. In
particular \(g'(z)=\log(1-e^{-2\pi iz})\), and its real
part on the real interval is
\(J(x)=\int_0^x\log(2\sin\pi t)\,dt\).
Set \(p=\partial_b\mathcal F_4(e_*,s_*;z_*,b_*)\). For
\(x=(e_R,s_R,z_R,b_R)\), define
\[
 f(x,k)=\Re\mathcal F_4(e,s;z,b)-\Re p\,(b_R-\Re b_*),
 \quad \Im z=k,
 \tag{4}
\]
with \(\Im e,\Im s,\Im b\) fixed at their actual reference
values. The original domain and unselected maximum are
\[
\begin{gathered}
 K=[.27,.49]\times[.125,.5]\times[.22,.45]^2,\\
 G(k)=\max_{x\in K}f(x,k),\qquad M=f(x_*,c).
\end{gathered}
\tag{5}
\]
The original critical equations and supporting-plane comparison give
\(G(c)=M\) and \(f_k(x_*,c)=0\). The two central selected
alternatives are
\[
 f_{\rm fac}(x)=f(x,H)-2\pi H,\qquad
 f_{\rm force}(x)=f(x,H)+\Re g(z_R+iH).
 \tag{6}
\]

**Theorem 1.** For every reference specified above,
\[
 \boxed{\quad
 \max_{x\in K}f_{\rm fac}(x)<M-\frac1{500},\qquad
 \max_{x\in K}f_{\rm force}(x)<M-\frac1{500}.
 \quad}
 \tag{7}
\]
The constants do not depend on the word length or its later types.
The outgoing tangent in (4), including the allocated outgoing
halfweight in (3), is unchanged.

## 2. The correlated scalar bound and its implication

Use the same actual reference to define
\[
\begin{gathered}
 E=e^{-2\pi i e_*},\quad Z=e^{-2\pi i z_*},\quad
 S=e^{-2\pi i s_*},\quad
 \lambda=e^{2\pi H}/|Z|,\quad\ell=\log\lambda,\\
 A=\log\left|\frac{1-\lambda EZ}{1-EZ}\right|,\quad
 B=\log\left|\frac{1-\lambda SZ}{1-SZ}\right|,\quad
 C=\log\left|\frac{1-\lambda Z}{1-Z}\right|,\\
 d=\ell-B>0,\quad q=\Re(s_*+z_*)-1/2\in(.045,.21),\\
 a_*=\Re\cot(\pi s_*)>2/5,\qquad
 \gamma_*=[2\{2a_*+\min(a_*,7/16)\}]^{-1}.
\end{gathered}
\tag{8}
\]
Put \(\kappa=10\pi^2/11\), \(\eta=11\pi^2/10\),
\(\rho=3/50\), and
\[
\begin{split}
 T_q(a)=\max\big\{&aq-\kappa q^3/3
                 +(\kappa/3)(q^2-2a/\kappa)_+^{3/2},\\
                 &a(q+\rho)-\kappa q^3/3
                    -\kappa\rho q^2/2+\eta\rho^3/6\big\}.
\end{split}
\tag{9}
\]
For \(\theta\in\Theta=\{0,1/4,1/2,3/4,1\}\), define
\[
\begin{split}
 h_\theta&=3C-B-\theta d,\qquad
 m_\theta=A-\frac{163}{298}h_\theta,\\
 \widehat{\mathcal N}_\theta
 &=\gamma_*(1-\theta)^2d^2+\frac{45}{298}h_\theta^2
                      +\frac12m_\theta^2+\pi T_q(\theta d).
\end{split}
\tag{10}
\]
The [correlated endpoint deduction](research_mixed_next_four_correlated_endpoint_budget.md)
proves
\[
 \pi\{G(H)-M\}
 <V(c)+\min_{\theta\in\Theta}\widehat{\mathcal N}_\theta,
 \qquad V(c)=\frac{19\pi^2}{10}(H-c)^2.
 \tag{11}
\]
The vertical term comes from the fixed-reference curvature
\(f_{kk}<19\pi/5\) and its vanishing initial derivative.
The horizontal bound retains the complete outgoing ordinary pair,
the centered private-edge cost and the incoming-edge cost across
summed real part one half. It bounds the movement of all four real
coordinates, including boundary maxima.

For the forced alternative set \(R=e^{2\pi H}\),
\(T=e^{-2\pi\Im s_*}\), \(r_e=8/9\), and
\[
\begin{gathered}
 \mathcal T=\{2/5,81/200,41/100,83/200,21/50\},\\
 a_e(t)=-\cos2\pi(.306+t),\quad
 a_s(t)=-\cos2\pi(.22+t),\quad a_z(t)=-\cos2\pi t,\\
 P_t=(1+2r_ea_e(t)R+r_e^2R^2)
                            (T^2+2Ta_s(t)R+R^2),\\
 Q_t=(1+2a_z(t)R+R^2)^2,\qquad
 \mathcal T_* =\{t\in\mathcal T:P_t<Q_t\},\\
 \mathcal C(t)=\frac{.5-t}{2}
       \{\log(2\sin\pi t)+\log2\}+\pi H(.5-t).
\end{gathered}
\tag{12}
\]
The same deduction proves that \(\mathcal T_*\) is nonempty,
that every forced maximum satisfies \(z_R<t\) for any
\(t\in\mathcal T_*\), and consequently
\[
 \max_K f_{\rm force}<G(H)-\mathcal C(t).
 \tag{13}
\]

**Lemma 2.** At every actual reference in Theorem 1 there are
\(\theta\in\Theta\) and \(t\in\mathcal T_*\) such that
\[
 V(c)+\widehat{\mathcal N}_\theta
 <\min\{2\pi^2H,\pi\mathcal C(t)\}-\frac\pi{500}.
 \tag{14}
\]
Section 3 proves this statement by a complete interval cover. It
discharges equation (15) of the correlated deduction; the earlier
fixed-threshold scalar test in the frozen endpoint note is a separate
assertion and is not used.

Combining (11) with the factorial credit in (14) gives the first
inequality of (7). Combining (11), (13) and the forced credit in
(14) gives the second. Throughout, \(G(H)\) is the maximum over
the original \(K\). The factorial face exclusions used to compute
that maximum do not restrict the forced maximizer: at every point
of \(K\), its unselected phase is still at most \(G(H)\).
This proves Theorem 1 once Lemma 2 is established.

## 3. A complete cover of the actual-reference superset

The original endpoint auxiliary coordinate lies in
\[
 u_*\in[217/1000,234/1000]+i[27/1000,45/1000].
 \tag{15}
\]
For \(U=e^{2\pi i u_*}\), the
[rational endpoint equations](research_mixed_rational_critical_transport.md)
give
\[
\begin{split}
 E&=\frac{(U+1)^2}{5U^2-2U+1},\\
 Z&=\frac{29U^4-36U^3+38U^2-20U+5}
               {(U+1)^2(5U^2-2U+1)},\\
 S&=\frac{(U-1)(U+1)^6}
 {(17U^3-21U^2+19U-7)(41U^4-34U^3+36U^2-14U+3)}.
\end{split}
\tag{16}
\]
The next ordinary type-four equations then give
\[
 T_b=\frac{1-Z(1-S)^3/(1-ZS)}S,\qquad
 V_{\rm next}=\frac{1-ST_b}{T_b(1-ST_b)+(1-T_b)^3}.
 \tag{17}
\]
Here \(T_b=e^{-2\pi i b_*}\); it is distinct from the inverse
radius \(T\) in (12). The frozen map implementation evaluates
the factored expansion of \(T_b(U)\) directly.

Every actual reference obeys the following necessary restrictions.

1. The logarithmic coordinates of \(E,Z,S,T_b\) lie in (2).
2. Each of \(z_*,s_*,b_*\) lies in the closed disk of radius
   \(.060\) about \(.30-.052i\).
3. The coupled real sums lie in
   \(\Re(z_*+s_*)\in[.545,.77]\) and
   \(\Re(s_*+b_*)\in[.527,.77]\).
4. The coordinate of \(V_{\rm next}\) belongs to
   \(K_3\cup K_4\), where
\[
\begin{split}
 K_3={}&\{|w-(.35-.01i)|\le.083,\quad
          -.072\le\Im w\le.068,\quad\Re w-3\Im w\le.608\},\\
 K_4={}&\{|w-(.30-.052i)|\le.060,\quad
          -.108\le\Im w\le-.001\}.
\end{split}
\tag{18}
\]

The sources are the reference bounds cited above, the
[nonprivate-leg inclusion](research_mixed_open_local_factor_coverage.md),
the type-four rows with a type-four external input in the
[reduced-disk pair-sum theorem](research_mixed_reduced_disk_pair_sums.md),
and the [typed-domain inclusion](research_mixed_typed_last_row_envelopes.md).
The next external coordinate may have either type. It is attached
when \(m=3\), a case included in those domain theorems. Every
actual real part lies between zero and one half, so the principal
logarithm recovers its original coordinate. In particular
\(\Im V_{\rm next}<0\), which is also a necessary filter.

The [adaptive driver](../experiments/certify_mixed_next_four_adaptive_budget.py)
uses the original rational maps and outward interval arithmetic at
160 bits. It evaluates each rational function on a whole complex
rectangle by its midpoint value plus a whole-rectangle derivative
enclosure times the displacement. Horner value/derivative jets and
finite interval denominators justify this mean-value enclosure on
the convex rectangle. Exponential, logarithm, modulus, trigonometric
and square-root operations also use outward enclosures.

Subdivision alternates the real and imaginary auxiliary axes, starting
with the real axis. A box is excluded only when a whole enclosure
contradicts a necessary reference restriction. The proved ranges
\(0<d<1\), \(.045<q<.21\), and \(a_*>2/5\) may also
be intersected. Nonfinite or inconclusive estimates cause subdivision.

For the first scalar range, the actual summed real part lies in
\((.545,.71)\), so \(\Re(SZ)<0\). Since \(\lambda>1\),
the elementary squared-modulus comparisons give
\(1<|1-\lambda SZ|/|1-SZ|<\lambda\). Thus
\(0<B<\ell\), and
\[
 0<d<\ell=2\pi(H-c)<.176\pi<1.
 \tag{19}
\]

On each remaining box, \(c,\Im s_*\), all three logarithmic
increments and \(a_*\) come from that same box. The identity
\(\cot(\pi s_*)=i(1+S)/(1-S)\) evaluates the latter directly.
Since \(\gamma_*\) decreases with \(a_*\), its lower
curvature endpoint gives an upper bound for the coefficient in (10).
Every proposed ceiling must pass the whole-box strict test \(P_t<Q_t\).
The driver also permits the established uniform \(.42\) ceiling
with its coarse credit \(27/500+\pi/1250\) as a fallback.
All accepted leaves in the completed record in fact have a strict
test from (12). A box is accepted only if one of the five trials
has a rigorous upper budget below both credits in (14). The same
trial must pass both comparisons.

The first bounded run inspected 6,000 nodes and saved 2,997 terminal
leaves: 660 accepted and 2,337 excluded. Seven pending boxes remained.
The [continuation wrapper](../experiments/resume_mixed_next_four_adaptive_budget.py)
verified the original record and dependency hashes, its prefix-free
unit-mass partition, and the exact address-to-box correspondence. It
called the unchanged interval routine only on those seven boxes and
their descendants. All 2,997 prior leaves were copied unchanged.
After 581 additional visits, the remaining partition was complete.

The combined cover has exactly 6,581 visited nodes and 3,291 terminal
leaves, comprising 678 accepted and 2,613 excluded leaves. There are
no unresolved boxes. Their binary addresses are prefix-free with
exact dyadic mass one. The maximal terminal depth is 19, below the
unchanged depth limit 20. Thus every actual reference belongs to an
accepted box and satisfies (14), proving Lemma 2.

A separate read-only check at 192 bits of every saved acceptance
inequality used
the serialized budget upper endpoints and credit lower endpoints.
All 678 comparisons passed, with smallest saved combined slack greater
than \(1.51189367576\times10^{-5}\). The enclosing ball strings may
be displayed more coarsely than those endpoint strings, so the endpoints
are the appropriate data for this check. This verification evaluated no
reference map and reran no interval-cover cell.

## 4. Frozen records and scope

The [first adaptive record](../repro/results/research-mixed-next-four-adaptive-budget-attempt01.json)
and [completed continuation record](../repro/results/research-mixed-next-four-adaptive-budget-attempt02.json)
retain every leaf, ceiling witness, trial bound and input hash. The
completed record binds the original driver and continuation wrapper
and certifies preservation of the original terminal leaves. The
[assembly record](../repro/results/research-mixed-first-four-next-four-central-gap-assembly.json)
binds this note to those exact inputs and the frozen analytic proofs.

| Input | SHA256 |
|---|---|
| Frozen endpoint proof | `9a4e089fe3d69f746465ef366eb86ac086272d007d0e669aecc8bfc1340e8903` |
| Correlated deduction | `97ccec16443ba7a3015c19a3bfc05a67493049efc4924834997e40e01dca8269` |
| Adaptive driver | `e97474c4a7cdcaf43fe691a8c2f6083f7c0bec2f0df745d1f97ce886f274281d` |
| First adaptive record | `e7af3ac81f917fc97393e7711989eafbe1f020a0e7695c51565380b66c735faf` |
| Continuation wrapper | `42038957f58c03896ee4e2af3cad1101427150bff85f291619057a56b23e764f` |
| Completed record | `6e3520360bf93d779c359f39f33e479cf422ef2fa7eadbfe23ce0b5383af7d27` |

The scalar cover evaluates rational reference maps and elementary
costs; it performs no root solve or finite quantum-source evaluation.
Theorem 1 establishes both central phase comparisons with the original
outgoing tangent. It supplies no estimate for the remaining boundary
profiles, complete selected finite source, global open-word dominance,
or the cofinite hyperbolic filling-volume theorem.
