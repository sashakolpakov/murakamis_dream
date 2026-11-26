# The Fourier right cap needs no outgoing halfweight in its inner contour

Research deduction, 7 November 2026. The old conditional-index contour
can be proved directly with the outgoing halfweight absent. Its whole
central sheet, both horizontal aliases, vertical aliases and zero-mode
joins reduce to three explicit bare real-row profiles after the cardinal
factor is included. The main sheet retains a joint quadratic loss.
This argument does not divide by a finite Fourier weight, does not use
the pending annulus test, and does not assert signs for the three rows.

The conclusion is an inner-index source estimate. The outer outgoing
index still has its original physical rows and its own contour terms.
The exact finite Fourier cap is not identified with just this inner
critical-height integral.

## 1. Original source, reference and allocation

Use the [correlated endpoint](research_mixed_fourier_right_cap_correlated_endpoint.md)
with incoming type \(3+\eta\), \(\eta=0,1\), incoming
\(a_*\in K_{3+\eta}\), and original critical pair
\((s_*,q_*)\in O_4^2\). This includes the last ordinary vertex
of every actual Fourier-ended prefix of length at least two.
The own type is four throughout. Fix \(y=x_0\), \(Y=e^{2\pi iy}\).
The inherited bounds are
\[
 3/5<|Y|<5/8,\qquad .18299<\Re y<.18301.
 \tag{1}
\]
All heights stay at these actual reference values. Write
\[
 \begin{split}
 P&=[.22,.45],\qquad a=x+i h_a,\quad q=z+i h_q,\quad x,z\in P,\\
 |h_a|&\le .108,\qquad -.102\le h_q\le-.001,\qquad
 -.102\le h_s=\Im s_*\le-.001.
 \end{split}
 \tag{2}
\]
If \(\eta=1\), the incoming height is negative. This is the original
unselected incoming halfweight regime, not an independently selected
or reset height.

The unallocated own-four phase and the cardinal phase are
\[
 \begin{split}
 Q_1(s;a,q)&=g(s+a)+g(s+q)-3g(s)-g(a)-g(q)+2\pi ias,\\
 \ell_q(y)&=2\pi iy(q-\tfrac12)
 -\frac{\operatorname{Li}_2(Ye^{-2\pi iq})-\operatorname{Li}_2(Y)}
                {2\pi i},\\
 \mathscr F_\eta(s,a,q)&=Q_1(s;a,q)-\frac\eta2g(a)+\ell_q(y).
 \end{split}
 \tag{3}
\]
The lifted \(y\), absolute constants and original branches are retained.
The actual equations are
\(\mathscr F_s(s_*,a_*,q_*)=\mathscr F_q(s_*,a_*,q_*)=0\).
Set
\[
 M_\eta=\Re\mathscr F_\eta(s_*,a_*,q_*),\quad
 p_\eta=\Re\mathscr F_{\eta,a}(s_*,a_*,q_*),\quad
 \mu=1/1250000,\quad \kappa=\mu/2.
 \tag{4}
\]
Thus \(M_\eta,p_\eta\) are precisely the action and incoming marginal
of the Fourier boundary allocation, including \(-\eta g(a)/2\).

There is an exact cardinal interpolation on the present strip:
\[
 f_N(q;y)=\frac{e^{-\pi i(N-1)y}}N(1-Y^N)
             \frac{e^{2\pi iNyq}}{\mathcal P_N(q+1/N,Y)} .
 \tag{5}
\]
Here \(\mathcal P_N\) is the particular interpolation in
[root-Pochhammer interpolation](research_root_pochhammer_interpolation.md),
not an interpolation chosen only by its lattice values. Since
\(|Ye^{-2\pi iq}|<5/8\), it has uniform exponential rate
\(\Re\ell_q(y)\), with its original polynomial prefactor.
At every physical \(q=l/N\), (5) equals the original \(f_l(y)\).
Consequently the actual cap remains exactly
\[
 V_N^{\rm F}(y,e^{-2\pi ia})
       =\sum_{l=0}^{N-1}C_{1,N}(e^{-2\pi ia},r^l)f_l(y).
 \tag{6}
\]
Equation (6) is not replaced by an off-grid summation identity.

## 2. Bare joint curvature on the complete old index interval

**Lemma 1.** On
\[
 s\in[1/8,1/2]+i[-.108,.068],\qquad
 a,q\in[.22,.45]+i[-.12,.12],
 \tag{7}
\]
the bare ordinary phase
\(Q_1(s;a,q)-\eta g(a)/2\) has
\[
       -\Re\partial^2_{s,a,q}(Q_1-\eta g(a)/2)\succ\mu I_3.
 \tag{8}
\]
This is a statement about the original uneliminated phase on a
convex product; it does not require a moving conditional root.

*Proof.* For \(s_R\in[.15,.5]\), write the phase as
\[
 V(s,a)+V(s,q)-g(s)-\frac\eta2g(a)+2\pi ias,\qquad
 V(v,w)=g(v+w)-g(v)-g(w).
 \tag{9}
\]
Both pair forms are positive with the common floor \(\mu\),
by the [zero-mode proof](research_mixed_horizontal_zero_mode_support.md),
Section 2, and its
[half-index extension](research_mixed_half_index_contour.md),
Section 1. The additional own costs have nonnegative negative-real
Hessians. The omitted outgoing term \(-g(q)/2\) is not needed.

For \(s_R\in[1/8,.15]\), use the exact quantities
\(u,p,v,C_a,C_q\) of the
[own-four left-cut proof](research_mixed_four_left_cut_extension.md),
with \(v=\Re\cot\pi q\). The bare matrix divided by \(\pi\) is
\[
 \begin{pmatrix}
 3u-C_a-C_q&-C_a&-C_q\\
 -C_a&(1+\eta/2)p-C_a&0\\
 -C_q&0&v-C_q
 \end{pmatrix}.
 \tag{10}
\]
The old diagonal and Schur arguments explicitly hold for every
outer coefficient \(\lambda\ge1\), rather than only for
\(\lambda=3/2\). In particular, each outer diagonal exceeds
\(9/70\); if \(C>0\), \(p-C>3/10\), and
\[
 C+\frac{C^2}{\lambda p-C}<187/120.
 \tag{11}
\]
For \(C\le0\) this expression is nonpositive. The index Schur
complement therefore exceeds
\[
       3(21/20)-2(187/120)=1/30 .
 \tag{12}
\]
The old determinant lower bound remains unchanged, and reducing the
outgoing coefficient only decreases the old trace upper bound
\(40/3\). Exactly its determinant/trace argument gives
\[
 -\Re\partial^2(Q_1-\eta g(a)/2)
       \succ\frac{729\pi}{58800000}I_3
       \succ\frac1{40000}I_3\succ\mu I_3.
 \tag{13}
\]
No scalar inequality is reevaluated. This proves (8). \(\square\)

For the actual \(q\)-heights in (2), the cardinal contribution has
strictly positive negative-real curvature:
\[
 -\Re\ell_{qq}(y)=
 \frac{-2\pi\Im(Ye^{-2\pi iq})}
                   {|1-Ye^{-2\pi iq}|^2}>0 .
 \tag{14}
\]
Indeed \(z-\Re y\in(.036,.268)\), so the imaginary part in
the numerator is negative. In fact (14) exceeds \(1/10\).
To see this without new evaluations, the old height estimate gives
\(e^{2\pi h_q}>1/2\), so \(r=|Ye^{-2\pi iq}|>3/10\),
while \(r<5/8\). The angle \(2\pi(z-\Re y)\) belongs to
\((1/5,\pi-1/5)\); its sine exceeds
\(1/5-(1/5)^3/6>19/100\). The denominator is less than
\((13/8)^2<3\). Thus (14) is greater than
\(2\pi(3/10)(19/100)/3>1/10\).

Combining (8) and (14), and integrating from the original stationary
pair, proves the bare main-sheet inequality
\[
 \begin{split}
 \Re\mathscr F_\eta(v+i h_s,a,q)
 \le{}&M_\eta+p_\eta(x-\Re a_*)\\
 &-\kappa\{(v-\Re s_*)^2+(x-\Re a_*)^2+(z-\Re q_*)^2\}
 \end{split}
 \tag{15}
\]
for every \(v\in[1/8,1/2]\) and \(x,z\in P\).
Denote its right side with the index square omitted by
\(\mathcal L_\eta(x,z)\).

## 3. Every inner contour current survives the change of allocation

Use the old own-four index contour with cuts \(1/8,1/2\), lower
height \(-1/5\) and upper height \(5/4\). Repeat its exact residue
calculation for the original conditional kernel before inserting
an outgoing \(d_N\) factor. The original row interpolation has
phase \(Q_1\); the retained incoming halfweight contributes only
\(-\eta g(a)/2\). Multiplication by (5) then adds \(\ell_q(y)\).
This reconstructs (3) from the literal source. It is not division
of a previously estimated finite product by \(d_N(q)^{1/2}\).

All index derivatives in the old alias comparisons are unchanged:
both the removed halfweight and the added cardinal phase are
independent of \(s\). Equations (19)--(20) of the own-four
left-cut proof consequently give the stronger pointwise statements
\[
 \begin{split}
 \Re\mathscr F_\eta(v-i/5,a,q)-2\pi/5
 &<\Re\mathscr F_\eta(v+i h_s,a,q)-1893\pi/25000,\\
 \Re\mathscr F_\eta(v+5i/4,a,q)-5\pi/2
 &<\Re\mathscr F_\eta(v+i h_s,a,q)-7/50.
 \end{split}
 \tag{16}
\]
They are therefore below the bare plane \(\mathcal L_\eta\)
by those same positive margins. Every vertical alias is bounded
by its corresponding real-cut value, because its original
index derivative and Fourier penalty are also unchanged.
For the unpenalized joins, (8) gives vertical convexity in the
index between \(0\) and \(h_s\), so each join is bounded by the
maximum of its real cut and (15). No convexity of a finite sum's
logarithmic modulus is used.

The exact factorial domains, full cotangent denominators, zero-mode
coefficient \(+N\), half-grid shifts and both parities are exactly
those of the old contour. Every polynomial prefactor and source
tolerance can be retained uniformly on the compact family (2).

## 4. The complete inner-source envelope and its three remaining defects

Define the bare real-row/cardinal rate on the **full** real row interval
\[
 \begin{split}
 \mathcal T_\eta(u;x,z)={}&
 \int_0^u\log|1-e^{-2\pi i(a+t)}|\,dt
 +\int_0^u\log|1-e^{-2\pi i(q+t)}|\,dt\\
 &-3J(u)-2\pi h_a u-\frac\eta2\Re g(a)+\Re\ell_q(y),
             \qquad 0\le u\le1 .
 \end{split}
 \tag{17}
\]
Integrable logarithmic zeros and revived rows are retained. The
left monotonicity and the
[right-tail endpoint comparison](research_mixed_right_tail_endpoint_bound.md)
apply unchanged: every term changed in the allocation is constant
in \(u\). Consequently its entire physical tail is controlled by
\[
     \mathcal T_\eta(1/8;x,z),\quad
     \mathcal T_\eta(1/2;x,z),\quad
     \mathcal T_\eta(1;x,z).
 \tag{18}
\]

**Theorem 2.** For every prescribed \(\tau>0\), the literal
conditional source and exact cardinal interpolation satisfy
\[
 \begin{split}
 &|C_{1,N}(e^{-2\pi ia},e^{-2\pi iq})|\,
       |d_N(e^{-2\pi ia})|^{\eta/2}|f_N(q;y)|\\
 &\quad\le C_\tau N^{A_\tau}
  \exp N\left\{\max\left(
      \mathcal L_\eta(x,z),
      \mathcal T_\eta(1/8;x,z),
      \mathcal T_\eta(1/2;x,z),
      \mathcal T_\eta(1;x,z)\right)+\tau\right\}.
 \end{split}
 \tag{19}
\]
It holds uniformly on the stated actual reference families and
independent horizontal targets \(P^2\), with all original physical
rows, inner aliases and joins. It uses the direct source estimates
and (8), not the old completed row signs. In particular it needs
no premise that \(\beta_Y(q_*)\in K_3\).

The three remaining comparisons can be made more precise without
choosing numerical trials. Put \(\widehat\kappa=\mu/4\) and
\[
 \begin{split}
 \widehat{\mathcal L}_\eta(x,z)
 &=M_\eta+p_\eta(x-\Re a_*)
   -\widehat\kappa\{(x-\Re a_*)^2+(z-\Re q_*)^2\},\\
 D_{\eta,c}
 &=\max_{x,z\in P}
       [\mathcal T_\eta(c;x,z)-\widehat{\mathcal L}_\eta(x,z)],
                   \qquad c\in\{1/8,1/2,1\}.
 \end{split}
 \tag{20}
\]
For \(c=1/8,1/2\), the difference in (20) is the sum of a
function of \(x\), a function of \(z\), and a constant. It is
strictly concave in each coordinate, with curvature floor
\(\mu/2\): at a real cut (17) equals
\(\Re\mathscr F_\eta(c,a,q)\), and Lemma 1 applies at height zero.
Thus each of its two one-dimensional maxima is at an endpoint or
its unique interior derivative zero. This is a genuine two-scalar
reduction, not a two-dimensional source grid.

The last row simplifies exactly, by the full-circle logarithmic
mean and \(J(1)=0\):
\[
 \mathcal T_\eta(1;x,z)
    =2\pi(-h_a)_+-\frac\eta2\Re g(a)+\Re\ell_q(y).
 \tag{21}
\]
For \(\eta=0\), its defect in (20) is convex in \(x\), so its
\(x\)-maximum is at one of the two plateau endpoints.
For \(\eta=1\), it is strictly concave in \(x\):
the old \(\Re\cot\pi a>9/70\) gives curvature
\(9\pi/140-\mu/2>0\). Its \(z\)-part is strictly concave
for either type by (14), with floor \(1/10-\mu/2\).
Those maxima again require only endpoints and at most one
interior stationary point per concave coordinate.

In particular the three inequalities
\[
                    D_{\eta,1/8}\le0,\qquad
                    D_{\eta,1/2}\le0,\qquad
                    D_{\eta,1}\le0
 \tag{22}
\]
are sufficient for the complete inner-source bound with
\(\widehat{\mathcal L}_\eta\). Uniform strict versions give a
uniform deficit for all its nonmain physical-row contributions.
No sign in (22), or value of these maxima, has been evaluated here.

This identifies the halfweight obligation more sharply than adding
the uncontrolled Bregman term of \(g(q)/2+\ell_q\) to an old
small-curvature plane: the whole bare main sheet and its inner
horizontal aliases are already paid analytically. Only the three
real-row defects remain for that operation. To obtain a whole
right-cap theorem for (6), one must additionally retain and control
the outgoing \(q\)-sum's physical complement, its contour aliases
and joins, or an exact coherent replacement that proves the same
whole-source statement. Equation (19) by itself supplies no such
outer deformation or noncancellation claim.
