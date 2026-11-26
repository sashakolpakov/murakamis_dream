# The cap-selected scalar period of an original two-run knot

Research note, 3 November 2026.

The actual two-run source probes a specified tensor eigenline of
the full auxiliary monodromy. Restricting the original marked
affine equation to that line gives a scalar cyclic equation, with
its entire forcing and cap normalization retained. Its denominator
contains only the two selected classical branches. Every other
tensor resonance is removable after this restriction.

This is an exact cancellation statement for the original prepared
source. Section 6 additionally proves a positive, quantitatively
observed numerator at selected resonances of every equal reflected
even pair. These facts do not determine the geometric leading term
of its physical value.

## 1. The actual sections and their domains

Fix nonzero signed powers
\[
 k=\lceil|a|/2\rceil,\qquad l=\lceil|b|/2\rceil,\qquad
 \sigma_a,\sigma_b\in\{1,-1\},\qquad k,l\ge1.
 \tag{1}
\]
Here \(\sigma_p=\operatorname{sgn}p\). Let \(e_p=1\) for
even \(p\), and \(e_p=0\) for odd \(p\), and assume
\(s=e_a+e_b\ge1\). This is exactly the one-component
condition for the literal two-run cylindrical closure, as
proved by the three endpoint pairings in
[the original source-jet theorem](research_two_run_monodromy_source_jets.md).
No such parity test is asserted for longer words.
At level \(N\ge2\), put
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad X=x^N,\quad
 \epsilon=(-1)^N,\quad
 \kappa=\exp\!\left(\frac{\pi i(N-1)^2}{2N}\right).
 \tag{2}
\]
For each even power use the zero-free function \(\psi\), its
normalized root \(a_{k,N}\), and the explicitly normalized section
from [the even-run cyclic descent](research_even_run_cyclic_descent.md).
For each odd power use the explicit polynomial section obtained
by multiplying the Reynolds sum by \(k-(k-1)y^N\), in equation
(38) of [the odd-run descent](research_odd_run_simple_spectrum_and_marked_kernel.md).
Its primitive polynomial normalization may be used instead;
the invariant-gauge qualification below applies.
Denote these actual normalized sections by \(f_{p,N}\).
In their own signed clocks they satisfy
\[
 \begin{split}
 \mathcal T_p(0;y)f_{p,N}(y)
   &=\gamma_{p,N}(y)
                         f_{p,N}(Q^{\sigma_p}y),\\
 \gamma_{p,N}(y)&=
 \begin{cases}
 q^{\sigma_p}(y-1)a_{|p|/2,N}(y^N),&p\text{ even},\\
 -q^{\sigma_p},&p\text{ odd},
 \end{cases}\\
 f_{p,N}(Q^{\sigma_p})&=v_p,\qquad
 (v_p)_r=q^{\sigma_p(\lceil|p|/2\rceil-r)}.
 \end{split}                                                    \tag{3}
\]
For an even power the root is fixed by
\[
 a_{s,N}(Y)^N=\psi_s(Y)^{-1},\quad a_{s,N}(0)=1,
 \qquad a_{s,N}(1)=s^{1/N}>0 .
 \tag{4}
\]
No additional unit scalar is chosen in (3)--(4).

Use the natural common clock, so that \(x\mapsto Qx\) advances
both physical color sequences. Define
\[
 \begin{split}
 \mathbf f_N(x)&=
       f_{a,N}(x^{\sigma_a})\otimes f_{b,N}(x^{\sigma_b}),\\
 c^T&=e_k^T\otimes e_l^T,\qquad
 \varphi_N(x)=c^T\mathbf f_N(x),\\
 A_N(x)&=\mathcal T_a(0;x^{\sigma_a})
                        \otimes\mathcal T_b(0;x^{\sigma_b}),\\
 \tau_N(x)&=\gamma_{a,N}(x^{\sigma_a})
                              \gamma_{b,N}(x^{\sigma_b}).
 \end{split}                                                    \tag{5}
\]
Use the connected domain
\[
 \Omega_N=\left\{x\ne0:
 \begin{array}{ll}
 |x|<R_{|p|/2}^{1/N}&\text{for each positive even }p\in\{a,b\},\\
 |x|>R_{|p|/2}^{-1/N}&\text{for each negative even }p\in\{a,b\}
 \end{array}\right\}.
 \tag{6}
\]
Only even powers impose a finite radius in (6), since the chosen
odd sections are polynomials. The functions in (5) are holomorphic
on \(\Omega_N\), which contains the entire unit circle.
With two even powers of opposite signs this is an annulus;
with just one even power it is a punctured disk or an exterior
domain. When both signs are positive the puncture is removable
for the sections and forcing; when both are negative the analogous
statement holds at infinity in the coordinate \(x^{-1}\).
The algebraic branches are those inherited from the separate
even disks, including after inversion. No continuation of an
even section beyond its proved disk is used.

The exact horizontal equation and the original cap give
\[
 A_N(x)\mathbf f_N(x)=\tau_N(x)\mathbf f_N(Qx),\qquad
 \mathbf f_N(Q)=w_0=v_a\otimes v_b,\qquad c^Tw_0=1.
 \tag{7}
\]

## 2. Restricting the original marked affine row

The original augmented transfer and its full ordered period are
\[
 \mathcal F_N(x)=
 \begin{pmatrix}A_N(x)&0\\c^TA_N(x)&1\end{pmatrix},\qquad
 \mathcal F_N(Q^{N-1}x)\cdots\mathcal F_N(x)
       =\begin{pmatrix}U_N(x)&0\\r_N(x)&1\end{pmatrix}.
 \tag{8}
\]
Thus \(r_N\) is the original color accumulator, not an arbitrary
co-source. On the regular set define its marked affine row
\[
                      h_N(x)=r_N(x)(I-U_N(x))^{-1}.
 \tag{9}
\]
The [marked numerator theorem](research_two_run_marked_laurent_numerator.md)
proves the exact intertwining
\[
 h_N(Qx)A_N(x)=h_N(x)-c^TA_N(x)
 \tag{10}
\]
and identifies the original source through the cap at \(x=Q\).
At least one run is even, so \(U_N(Q)=0\); there is no
invertibility qualification at this physical clock.

Put
\[
 \chi_{a,b}(X)=
       \prod_{\substack{p\in\{a,b\}\\p\ {\rm even}}}
           \frac{1-X^{\sigma_p}}{\psi_{|p|/2}(X^{\sigma_p})},
 \qquad d_{\rm sel}(X)=1-\chi_{a,b}(X).
 \tag{11}
\]
The product is over the two run positions, retaining multiplicity
when \(a=b\).
This is a specified classical algebraic function. It is independent
of \(N\), except that the quantum clock uses \(X=x^N\).
It satisfies \(\chi(1)=0\), \(d_{\rm sel}(1)=1\).

**Theorem 1.** The actual marked scalar
\[
                     \mathcal H_N(x)=h_N(x)\mathbf f_N(x)
 \tag{12}
\]
extends meromorphically to \(\Omega_N\) and is the unique
meromorphic solution there of
\[
 \boxed{\quad
 \mathcal H_N(x)-\tau_N(x)\mathcal H_N(Qx)
                  =\tau_N(x)\varphi_N(Qx).
 \quad}                                                        \tag{13}
\]
Its exact finite Green formula is
\[
 \boxed{\quad
 \mathcal H_N(x)=\frac{\mathcal R_N(x)}{d_{\rm sel}(x^N)},\qquad
 \mathcal R_N(x)=
   \sum_{j=1}^N
      \left[\prod_{m=0}^{j-1}\tau_N(Q^m x)\right]
                         \varphi_N(Q^j x).
 \quad}                                                        \tag{14}
\]
The numerator \(\mathcal R_N\) is holomorphic on \(\Omega_N\).
All products in (14) retain their original color order and
the complete physical color range.

*Proof.* Pair (10) with \(\mathbf f_N(x)\) and use (7).
This gives (13) on the original regular set. The product of its
scalar multipliers over one cycle is
\[
 \prod_{m=0}^{N-1}\tau_N(Q^m x)=
                                      \chi_{a,b}(X).
 \tag{15}
\]
For an even run, use
\(\prod_m[(Q^mx)^\sigma-1]=\epsilon(1-X^\sigma)\)
and the central scalar's \(N\)-th power
\(-\psi_{|p|/2}(X^\sigma)^{-1}\).
For an odd run, \((-q^\sigma)^N=-\epsilon\).
Thus every selected individual period carries the same
factor \(-\epsilon\); those two factors cancel, leaving
exactly (11).

Iteration of (7) also gives
\[
 U_N(x)\mathbf f_N(x)=\chi(X)\mathbf f_N(x),\qquad
 r_N(x)\mathbf f_N(x)=\mathcal R_N(x).
 \tag{16}
\]
The second equality follows directly by expanding the original
accumulator in (8): its \(j\)-th prefix is precisely the
\(j\)-th summand in (14). Therefore
\(h_N(I-U_N)\mathbf f_N=r_N\mathbf f_N\) gives
\(d_{\rm sel}\mathcal H_N=\mathcal R_N\).
This proves the meromorphic continuation and its formula,
including points where the full matrix inverse in (9) fails.

Conversely, (14) satisfies (13) by shifting its finite sum.
If two meromorphic solutions existed, their difference \(b\)
would satisfy \(b(x)=\tau_N(x)b(Qx)\); after \(N\) iterations,
\(d_{\rm sel}(x^N)b(x)=0\). Since
\(d_{\rm sel}(1)=1\), it is not identically zero on the
connected domain. Thus \(b=0\). \(\square\)

## 3. Exact cancellation of the nonselected resonances

The full determinant of \(I-U_N\) includes all \(kl\) pairs
of one-run monodromy eigenvalues. These are the factors of the
previously proved classical tensor determinant
\(\mathcal D_{a,b}(X)\). Formula (14) has a sharper conclusion
for the original prepared cap.

**Corollary 2.** At any \(x_0\in\Omega_N\) with
\[
 \mathcal D_{a,b}(x_0^N)=0,\qquad
                   d_{\rm sel}(x_0^N)\ne0,
 \tag{17}
\]
the marked projection \(h_N(x)\mathbf f_N(x)\) is holomorphic.
All apparent poles from those nonselected tensor resonances
cancel, regardless of their multiplicity or the corank of
\(I-U_N(x_0)\).

*Proof.* The numerator and denominator in (14) are holomorphic,
and the latter is nonzero at \(x_0\). \(\square\)

For a mixed even/odd pair, the odd magnitude disappears from
\(d_{\rm sel}\), but it remains in its actual polynomial section
and hence in \(\mathcal R_N\). This explicitly prevents reading
the original source or its volume from the selected denominator
alone. No identification of (11) with a full A-polynomial is made.

The statement is about the actual scalar restriction, not
the entire affine row \(h_N\). That row can have genuine
poles at other eigenmodes. At a selected zero of
\(d_{\rm sel}\), the scalar numerator in (14) may still
vanish; no nonexcitation condition is discarded.

The normalized horizontal sections retain an invariant gauge:
replacing their tensor by \(b(X)\mathbf f_N(x)\), with
\(b(1)=1\), multiplies both \(\mathcal H_N\) and
\(\mathcal R_N\) by \(b(X)\). The prescribed sections (3)
fix that choice. The physical source below is unchanged
by any such gauge regular at \(X=1\).

## 4. The original scalar and its exact reset coefficient

The actual two-run closing scalar is
\[
 \mathcal Z_{a,b,N}
      =\phi_N(R^bT(R^a))
      =\sum_{j=0}^{N-1}(M^be_0)_j(M^ae_0)_j .
 \tag{18}
\]
This is a bilinear pairing, with conjugation supplied only by
actual opposite powers.

**Theorem 3.** With the original carrier and both parity sequences,
\[
 \boxed{\quad
 \mathcal Z_{a,b,N}
                =\kappa^{a+b}\,[1+\mathcal H_N(Q)].
 \quad}                                                        \tag{19}
\]
Moreover \(\mathcal H_N\) has a zero of order at least \(s=e_a+e_b\)
at \(x=1\), and
\[
 \boxed{\quad
 \lim_{x\to1}\frac{\mathcal H_N(x)}{(x-1)^s}
  =\rho_{a,b,N}\kappa^{-a-b}\mathcal Z_{a,b,N},\qquad
 \rho_{a,b,N}=(-1)^{2-s}q^{\sigma_a+\sigma_b}
       \prod_{\substack{p\in\{a,b\}\\p\ {\rm even}}}
                    \sigma_p(|p|/2)^{1/N}.
 \quad}                                                        \tag{20}
\]

*Proof.* At \(x=Q\), the \(j\)-th prefix in (8) consists of
physical colors \(1,\ldots,j\). Applied to \(w_0\), it gives
the exact source channels at color \(j\), with only the
two factors \(\kappa^a,\kappa^b\) removed. For \(j=N\),
the reset at color zero annihilates the prefix.
Thus \(r_N(Q)w_0\) is the entire sum (18) except its
color-zero term \(\kappa^{a+b}\).
Since \(U_N(Q)=0\) and \(\mathbf f_N(Q)=w_0\), this is
\(\mathcal H_N(Q)\), proving (19).

The scalar denominator is one at \(x^N=1\), so
\(\mathcal H_N\) is holomorphic near the physical orbit.
Rewrite (13) as
\[
 \mathcal H_N(x)=
       \tau_N(x)\,[\mathcal H_N(Qx)+\varphi_N(Qx)].
 \tag{21}
\]
Here \(\varphi_N(Q)=1\), while (4)--(5) give
\[
 \lim_{x\to1}\frac{\tau_N(x)}{(x-1)^s}
                                      =\rho_{a,b,N}.
 \tag{22}
\]
Equations (19) and (21)--(22) prove (20). For two even
runs this is
\(\rho=\sigma_a\sigma_bq^{\sigma_a+\sigma_b}(kl)^{1/N}\);
for one odd run its constant factor \(-q^\sigma\) is
also retained. \(\square\)

This reduction keeps the source's scalar and its marked
first or second reset coefficient. It does not imply a lower bound
for \(1+\mathcal H_N(Q)\): the remaining scalar finite sum
is coherent and may have substantial cancellation.
For equal reflected runs it reproduces the known positive
norm identity. For different runs, neither a positive inner
product nor a nonzero geometric coefficient follows from
the scalar denominator reduction.

If both powers are odd, the selected period is identically one.
Then (14) cannot be divided by \(d_{\rm sel}\), and the
uniqueness argument fails. Those are exactly the two-component
closures excluded at the outset. This is a structural domain
restriction, not a vanishing claim for their original sources.

The result concerns two original prepared run columns and
their literal closing pairing. It is not an arbitrary-input
turn theorem, nor a full free-boundary packet for an
unresolved connected component. The underlying sections
still reconstruct every Newton coefficient and normal,
but extending the scalar projection to other inputs
requires their own marked source lines.

## 5. Finite normalization checks

The [focused checker](../experiments/check_two_run_selected_scalar_period.py)
constructs the specified horizontal sections on complete physical
and complex auxiliary orbits. It independently forms the full
tensor affine row from the original transfer matrices and compares
its marked projection with (14), including the scalar cyclic
equation and the full first or second reset coefficient.
The physical value is then compared with powers of the original
\(N\times N\) crossing matrix.

The [120-digit record](../repro/results/research-two-run-selected-scalar-period.json)
passed 72 signed level/pair cases and 216 complete cyclic orbits,
with 36 first-reset cases and 36 second-reset cases. It includes
different even powers, both signs, and mixed even/odd powers.
Its largest relative identity residual is
\(1.529387029871538\cdot10^{-113}\).
For odd powers it uses the explicit unshortened polynomial
section specified in Section 1.
The removability at other tensor resonances follows from the
holomorphic proof of Corollary 2; it is not inferred from
sampling near a numerical pole. No growth estimate is tested.

## 6. Selected reflected poles and their intrinsic scale

Here take \((a,b)=(2k,-2k)\), \(k\ge1\). Use the nowhere-zero
horizontal frame \(\widehat f_{2k,N}\) supplied by Corollary 4 of
[the even descent](research_even_run_cyclic_descent.md), and choose
the negative frame by conjugate reflection:
\[
 f(x)=\widehat f_{2k,N}(x),\qquad
 \widehat f_{-2k,N}(y)=\overline{f(\bar y)}.
 \tag{23}
\]
Both retain exactly the original physical samples. In this section
\(\mathcal H_N,\mathcal R_N\) mean (12)--(14) with these frames.
They are defined on the proved annulus
\(R_k^{-1/N}<|x|<R_k^{1/N}\). On its unit circle,
\(\mathbf f_N(x)=f(x)\otimes\overline{f(x)}\).

Put
\[
 \chi_k(X)=
 \frac{(1-X)(1-X^{-1})}{\psi_k(X)\psi_k(X^{-1})},
 \qquad d_k(X)=1-\chi_k(X),\qquad
 c_k=\frac{48}{49^k-1}.
 \tag{24}
\]
The functions in (24) are holomorphic on
\(R_k^{-1}<|X|<R_k\). The notation \(d_k\) here denotes the
selected scalar denominator, not the full tensor determinant.

**Theorem 4.** For each fixed \(k\), there is
\(X_k=e^{i\theta_k}\), \(0<\theta_k<\pi\), such that
\(\chi_k(X_k)=1\). Let \(m_k\ge1\) be the multiplicity of this
zero of \(d_k\), and put \(x_N=e^{i\theta_k/N}\).
For every \(N\ge2\), with both parity sequences retained,
\[
 \boxed{\quad
 \mathcal R_N(x_N)\ge c_k\|f(x_N)\|_2^2>0.
 \quad}                                                        \tag{25}
\]
Consequently \(\mathcal H_N\) has a pole of exactly order \(m_k\)
at \(x_N\). If \(C_{-m_k,N}\) is its leading Laurent coefficient,
then
\[
 \boxed{\quad
 \frac{|C_{-m_k,N}|}{\|f(x_N)\|_2^2}
 \ge
 \frac{m_k!\,c_k}
      {|d_k^{(m_k)}(X_k)|\,N^{m_k}} .
 \quad}                                                        \tag{26}
\]
There is no simple-root or corank-one assumption. The same
nonremovability holds on the entire \(Q\)-orbit of \(x_N\)
and on the conjugate orbit. The representatives \(x_N,\bar x_N\)
are at distance at most \(\theta_k/N\) from the reset \(1\);
each rotated pole is that close to its corresponding physical
clock \(Q^j\).

*Proof.* Schwarz reflection for the real-coefficient selected
branch gives, on \(|X|=1\),
\[
 \chi_k(X)=\frac{|1-X|^2}{|\psi_k(X)|^2}\ge0,\qquad
 \chi_k(1)=0.
 \tag{27}
\]
At \(X=-1\), the real Jacobi eigenvalues remain in their original
order. The selected eigenvalue is the largest one, namely
\(\mu_0(-1)=2\cos(\pi/(2k))\). Indeed the characteristic polynomial
there is \(P_k+P_{k-1}=2T_k(\mu/2)\), directly from the two
Chebyshev recurrences. This includes \(k=1\). Thus
\[
 \psi_k(-1)=1+\cos\!\left(\frac{\pi}{2k}\right)<2,\qquad
 \chi_k(-1)=\frac4{\psi_k(-1)^2}>1 .
 \tag{28}
\]
Continuity proves a crossing strictly between \(1\) and \(-1\)
on the upper semicircle. Choose, for example, the first crossing.
Since \(d_k(1)=1\), the analytic function \(d_k\) is not
identically zero; its zero at \(X_k\) has finite multiplicity.

Let \(v_0=f(x_N)\ne0\), and propagate the complete original run,
\[
 v_{j+1}=\mathcal T_{2k}(0;Q^jx_N)v_j,\qquad 0\le j<N.
 \tag{29}
\]
Every color in this orbit avoids the physical reset, because
\(x_N^N=X_k\ne1\). Equation (3) expresses (29) through \(f\).
Its full scalar multiplier is the selected one-run period
\(-\epsilon(1-X_k)/\psi_k(X_k)\), whose modulus is one by
(27). Hence \(v_N=\lambda v_0\), \(|\lambda|=1\).
The negative run is the exact conjugate, so the numerator (14)
is literally
\[
       \mathcal R_N(x_N)=\sum_{j=1}^N |e_k^Tv_j|^2.
 \tag{30}
\]
No phase or color is removed in this identity.

Apply the full cyclic observation estimate, Theorem 1 of
[the reflected marked-period note](research_reflected_run_marked_period.md):
\[
 \sum_{j=1}^N|e_k^Tv_j|^2
   \ge c_k\sum_{j=1}^N\|v_j\|_2^2
   \ge c_k\|v_N\|_2^2=c_k\|v_0\|_2^2.
 \tag{31}
\]
For clarity, that estimate needs neither \(N\ge k\) nor distinct
color observations. The preceding-color shift is unitary on the
cyclic trajectory because \(|\lambda|=1\). The last tridiagonal
row bounds the preceding channel's cyclic norm by seven times
the last, and each further row gives the recurrence
\(\|V_{h-1}\|\le6\|V_h\|+\|V_{h+1}\|\).
Summing the resulting bounds
\(\|V_h\|\le7^{k-h}\|V_k\|\) gives precisely (31).
This retains all original normal terms and also proves (25)
at the small levels \(N<k\).

Now expand the exact denominator:
\[
 d_k(x^N)=
 \frac{d_k^{(m_k)}(X_k)}{m_k!}
       (N x_N^{N-1})^{m_k}(x-x_N)^{m_k}
       +O((x-x_N)^{m_k+1}).
 \tag{32}
\]
The numerator is positive at the center by (25). Formula (14)
therefore gives the exact pole order and
\[
 C_{-m_k,N}=
 \frac{m_k!\,\mathcal R_N(x_N)}
      {d_k^{(m_k)}(X_k)(N x_N^{N-1})^{m_k}}.
 \tag{33}
\]
Since \(|x_N|=1\), this proves (26).
At all rotated clocks the individual scalar multipliers are
nonzero. Equation (13), whose forcing is holomorphic, propagates
the pole without a cancellation. Conjugation supplies the other
orbit. Finally
\(|x_N-1|=2\sin(\theta_k/(2N))\le\theta_k/N\).
\(\square\)

The normalized coefficient in (26) is unchanged by a zero-free
invariant change of frame. Its scale does not hide a possibly
exponential size of \(f(x_N)\). The normalization is essential:
even among algebraic nowhere-zero frames with the identical cap
and every identical physical coefficient, absolute residue sizes
can change exponentially.

More explicitly, fix any real \(r>R_k\) and use either of the
holomorphic, zero-free invariant gauges
\[
 b_N^\pm(X)=
       \left(\frac{r-X}{r-1}\right)^{\pm N},
                    \qquad b_N^\pm(1)=1 .
 \tag{34}
\]
Replace the positive frame by \(b_N^\pm(x^N)f(x)\), and the
negative frame by its conjugate reflection as in (23).
Every physical sample is unchanged. At \(X_k\ne1\) on the
unit circle, however, \(|r-X_k|>r-1\). The numerator,
the absolute leading Laurent coefficient, and
\(\|f(x_N)\|^2\) are all multiplied by
\[
       \left(\frac{|r-X_k|}{r-1}\right)^{\pm2N}.
 \tag{35}
\]
Thus (26) gives a nonzero selected period with polynomial
normalized loss, while preserving its true gauge dependence.
It does not compare that period to
\(\mathcal Z_{2k,-2k,N}=1+\mathcal H_N(Q)\).
A sharp physical growth theorem still needs control of a specified
horizontal section, or a gauge-invariant estimate linking its
resonant vector to the prepared physical cap. These auxiliary
clock poles are not singularities of a geometric boundary packet.
