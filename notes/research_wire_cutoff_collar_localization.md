# Tracing a fixed collar of wire cutoffs

Research note, 3 November 2026.

The exact midpoint cutoff can be replaced by a fixed-width collar in
the original Newton index. After the original crossing traces, the
cost of this replacement tends to zero with the width of the collar.
This permits a smooth **discrete** taper, with its full
Askey--Wilson forcing retained. It does not assert that the taper has
a holomorphic continuation or that arbitrary factorial-divisor
currents are cutoff forcings.

The earlier
[midpoint contraction](research_radical_path_sector_gap.md#8-contracting-several-cutoff-forcings-before-estimating-them)
is the zero-width antecedent. The new estimate allows an
\(N\)-independent interval of possible cutoff locations, uniformly in
the real charge coupons of
[the exact charge family](research_dominant_saddle_transport.md#9-an-exact-analytic-coupon-family-and-the-proved-initializer).

## 1. A vanishing real-period cost near the midpoint

Use the original definitions
\[
 D=N-1,\quad m=\lfloor N/2\rfloor,\quad L=D-m,\quad
 \eta=(-1)^D,\quad
 s_j=2\sin(\pi j/N),\quad S_j=\prod_{h=1}^j s_h,
\]
\[
 c_j=2\cos((2j+1)\pi/N),\qquad
 e_j(z)=S_j^{-2}\prod_{h<j}(c_h-z),\qquad
 P_N(z)=2T_N(z/2)+2.
 \tag{1}
\]
Fix \(0<\epsilon\le1/8\), and set
\[
 \omega(\epsilon)
   =-2\int_0^\epsilon\log(\tan\pi r)\,dr
   \le 2\epsilon\{1-\log(3\epsilon)\}.
 \tag{2}
\]
In particular \(\omega(\epsilon)>0\) and
\(\omega(\epsilon)\longrightarrow0\).

**Lemma 1.** There are constants \(C_\epsilon,A\), independent of
\(N\) and \(j\), such that
\[
 \sup_{z\in[-2,2]}|e_j(z)|
 \le C_\epsilon N^A e^{N\omega(\epsilon)}
 \quad\hbox{if}\quad
 \frac jN\ge\frac12-\epsilon-\frac1N.
 \tag{3}
\]
Every fixed ordinary derivative has the same exponential bound.
For \(j>L\), the stronger bound
\(\|e_j\|_{[-2,2]}\le\sqrt{N-1}\) holds.

**Proof.** The last assertion is the
[original radical Fourier bound](research_high_newton_radical_contraction.md#7-fourier-bounds-for-the-original-radical-polynomials);
it applies to every index \(j>L\), including both level parities.
Thus the high part in (3) is the entire original radical, not just
a fixed number of top modes.

For \(j\le L\), the
[real Newton entropy estimate](research_three_crossing_real_period_newton_bound.md)
gives, uniformly in real \(u\),
\[
 |e_j(-2\cos u)|\le CN^A e^{NV_u(j/N)},\qquad
 0\le V_u(y)\le V_0(y)\quad(0\le y\le1/2).
 \tag{4}
\]
This estimate follows directly from the defining cosine product in
(1), with a uniform \(O(\log N)\) error for its logarithmic midpoint
sums, and the corresponding sine-factorial estimate. It includes
zero product factors.
The complete-boundary entropy satisfies
\[
 V_0(1/2)=0,\qquad V_0'(y)=2\log(\cot\pi y),\qquad
 V_0(1/2-r)=\omega(r).
 \tag{5}
\]
On \(0<r\le1/4\), \(\omega\) is increasing and concave. For
\(N^{-1}\le\epsilon\),
\[
 N\omega(\epsilon+N^{-1})
 \le N\omega(\epsilon)+\omega'(\epsilon).
 \tag{6}
\]
Equations (4)--(6) prove (3). The finitely many remaining levels
are absorbed into \(C_\epsilon\). Markov's inequality on
\([-2,2]\), applied to the actual degree-\(j\) polynomial, proves
the derivative assertion without division by \(\sin u\).
Finally \(\tan(\pi r)\ge\pi r>3r\); integrating its logarithm proves
(2). \(\square\)

## 2. The exact tapered kernel and its current

For each internal edge choose real weights
\[
 0\le\vartheta_j\le1,\qquad
 \vartheta_j=1\ \hbox{if }j/N\le1/2-\epsilon,\qquad
 \vartheta_j=0\ \hbox{if }j/N\ge1/2+\epsilon,\qquad
 \vartheta_D=0.
 \tag{7}
\]
For all sufficiently large levels these can be samples of one
fixed smooth function. No smoothness is needed for the estimates.
Put
\[
 K_N^\vartheta(z,w)=\sum_{j=0}^D
          \vartheta_j e_j(z)e_j(w),\qquad
 E_N^\vartheta=K_N-K_N^\vartheta.
 \tag{8}
\]
Thus \(E_N^\vartheta\) retains every original index whose weight
was removed. It includes the full radical above the collar.

Let \(\mathscr L_N e_j=c_j e_j-s_j^2e_{j-1}\) be the original
Askey--Wilson operator, as in
[the exact cutoff identity](research_bare_kernel_power_three_obstruction.md).
For arbitrary weights the complete ordinary-polynomial identity is
\[
 \begin{split}
 (w-\mathscr L_N^{(z)})K_N^\vartheta(z,w)
 &=\sum_{j=0}^{D-1}s_{j+1}^2
       (\vartheta_{j+1}-\vartheta_j)e_j(z)e_{j+1}(w)\\
 &\quad+\frac{\eta\vartheta_D}{N^2}P_N(w)e_D(z).
 \end{split}
 \tag{9}
\]
Indeed use the Newton multiplication recurrence through \(j<D\);
at the last index it is
\[
       we_D(w)=c_De_D(w)+\eta P_N(w)/N^2.
 \tag{10}
\]
The intermediate terms telescope to (9). For (7) the final term
vanishes because its coefficient is exactly zero. For the full
kernel it remains an ordinary free-boundary polynomial and
vanishes only after reduction in a selected variable. It has not
been discarded as a value-only identity.

Denote the first line of (9) by \(J_N^\vartheta\).
Whenever its coefficient at \(j\) is nonzero, both \(j/N\) and
\((j+1)/N\) lie in the collar enlarged by \(1/N\). Therefore all
its Newton factors satisfy (3). The same is true of the factors
in \(E_N^\vartheta\). Their coefficients have modulus at most
one for \(E_N^\vartheta\) and four for \(J_N^\vartheta\).
If the samples come from a fixed
smooth taper, the coefficients of \(J_N^\vartheta\) are in fact
\(O_\epsilon(N^{-1})\), but this improvement is not needed below.

## 3. Contract first, uniformly in the real charges

Let the selected vertices form a finite simple path, with original
degrees at most two. Only edges with two distinct selected
endpoints may be replaced by (8) or (9). All original outside
edges remain the full kernel.
The crossing powers \(n_v\) are fixed signed integers.
At vertex \(v\), allow the original real charge coupon
\(\mathcal C_{N,\chi_v}\), \(0\le\chi_v\le1\), as defined by its
full physical Hermite jets in Section 9 of the charge-family note.

For a nonempty internal-edge set \(F\), put \(S=V(F)\).
On every edge of \(F\), insert either \(E_N^\vartheta\) or the
oriented \(J_N^\vartheta\), and leave every other edge full.
Call the resulting original traced source \(T_{F,N}\).
Delete the edges in \(F\), then make the vertices in \(S\) free
physical boundary variables and omit their crossings and coupons.
Let \(Z_{C,N}\) be the remaining original component sources.
An uncut edge joining two vertices of \(S\) remains a bare edge;
it is not replaced by a polynomial-size constant.

**Theorem 2.** Uniformly for all real outside angles and all
\(\boldsymbol\chi\in[0,1]^I\),
\[
 |T_{F,N}|
 \le C_{\Gamma,\mathbf n,\epsilon}N^{A_{\Gamma,\epsilon}}\,
       e^{\,2|F|N\omega(\epsilon)}
       \prod_C\|Z_{C,N}\|_{\rm real}.
 \tag{11}
\]
Here the norm takes the supremum over every original and newly
created real boundary variable. Every fixed collection of ordinary
outside derivatives satisfies the same estimate at polynomial
additional cost. Every component has at most \(|I|-2\) selected
vertices.

**Proof.** Expand the at most \(N\) summands on each replaced
edge. At a vertex \(v\in S\), their Newton factors form a
polynomial \(Q_v\) of degree at most \(2D\). If \(d_F(v)\) is
the number of incident edges in \(F\), Lemma 1 and Markov's
inequality give
\[
 \|Q_v\|_{[-2,2]}+\|Q_v'\|_{[-2,2]}
 \le C_\epsilon N^A
                    e^{\,Nd_F(v)\omega(\epsilon)}.
 \tag{12}
\]
At a double physical node \(c=-2\cos\tau\), choose
\(0<\tau<\pi\). The exact coupon has value
\(\cos(N(1-\chi)\tau)\) and derivative
\[
 -\frac{N(1-\chi)\sin(N(1-\chi)\tau)}{2\sin\tau}.
 \tag{13}
\]
Consequently its physical values have modulus at most one and its
first normals are bounded by \(N^2/4\), since
\(\sin\tau\ge\sin(\pi/N)\ge2/N\).
The odd simple node has its original value and requires no
derivative. Similarly the original crossing has unit-modulus
physical values and first normals \(O_{\mathbf n}(N^2)\).
These statements retain the exact crossing scalars; they are
bounds on the actual jets, not replacements of the crossing.

For \(g_v=R^{n_v}\mathcal C_{N,\chi_v}Q_v\), the original residue
at a double node is
\[
 \eta\{[(4-c^2)g_v'(c)-cg_v(c)]f(c)
                          +(4-c^2)g_v(c)f'(c)\}.
 \tag{14}
\]
At the odd simple node it is the value of \(g_vf\). Equations
(12)--(14) bound the total absolute value of these coefficients
by a polynomial times \(e^{Nd_F(v)\omega(\epsilon)}\).

Each vertex in \(S\) has at most one uncut incidence, because
the original degree is at most two. Thus the surviving first
normals differentiate an actual boundary variable of a remaining
component. Its degree in that variable is at most \(D\).
Successive Markov inequalities bound all these mixed derivatives
by the whole-real-boundary norms in (11), at polynomial cost.
Summing the finitely many physical-node and Newton-index choices
adds only another power of \(N\), for this fixed path. Finally
\(\sum_{v\in S}d_F(v)=2|F|\), which proves (11).

Ordinary derivatives at the original outside boundaries commute
with the finite identities and have the same polynomial degree
bounds. A nonempty \(F\) removes at least two distinct selected
vertices; hence the asserted decrease in component size.
\(\square\)

## 4. What a deletion gap now permits

Let \(Z_{\Gamma,N}^\vartheta\) taper all selected--selected edges
and keep every outside edge full. Finite expansion gives exactly
\[
 Z_{\Gamma,N}-Z_{\Gamma,N}^\vartheta
   =\sum_{\varnothing\ne F\subseteq E_I}
                    (-1)^{|F|+1}T_{F,N},
 \tag{15}
\]
where every replacement in this formula is \(E_N^\vartheta\).
The sum is over all edge subsets, not only matchings. Products
of collar factors are not assumed square-zero.

Suppose, on a specified charge set, the shorter components have
their whole-real-boundary upper bounds at rates \(\mu_C\), and
their rates obey the actual geometric deletion comparison
\[
              \sum_C\mu_C\le M_\Gamma-g|F|,
                      \qquad g>0.
 \tag{16}
\]
These are explicit hypotheses. In particular the general path
comparison in
[the pair-activation note](research_positive_path_pair_activation_gap.md)
must not be used without its stated support certificates, and
geometry alone does not prove the component source bounds.
If \(2\omega(\epsilon)<g\), Theorem 2 proves
\[
 \|Z_{\Gamma,N}-Z_{\Gamma,N}^\vartheta\|_{\rm real}
 \le CN^A e^{N\{M_\Gamma-g+2\omega(\epsilon)\}}.
 \tag{17}
\]
Every nonempty product of the literal tapered currents (9), with
other edges full, satisfies the same strict rate comparison.
The estimate is uniform over all choices of weights (7).
For example, if \(g=1/1000\), choosing
\(\epsilon=2^{-18}\) gives
\[
 2\omega(\epsilon)
 <4\,2^{-18}(1+18\log2)
 <\frac{17}{81920}<\frac1{4000}.
 \tag{18}
\]
The middle inequality uses \(\log2<7/10\). Thus at least
\(3/4000\) of the rate gap remains.

The error in (17) is still an ordinary polynomial of degree at
most \(D\) in each original outside variable. Chebyshev expansion
extends it to complex outside angles with added rate
\(\sum|\Im u_j|\) and polynomial prefactor. Fixed ordinary
normals cost further powers of \(N\). A sufficiently small fixed
outside neighborhood therefore preserves the strict gap.

This is a source-level localization, not a proof of the remaining
dominant-cycle statement. The tapered finite sum may be used in
place of the full source once (16) and the component bounds are
available. Its cutoff location and its discrete transition can
then be chosen throughout a fixed collar, with the exact current
(9) controlled after tracing. A smooth discrete cutoff is not
holomorphic; moving its sampled formula into a complex wire
contour would require an additional exact construction. Nor has
every factorial-divisor face or distant alias been identified
with (9). Those are the remaining distinctions between this
localization and a global one-dimensional top relative quotient.
