# Moving-height comparisons for the coupled first-cap envelope

Research deduction, 7 November 2026. On a nonpositive fixed ordinary
index height, the type-three true-end cap alternative has a strictly
positive derivative under the actual affine first-height change.
For the regular cap alternative, the same derivative is minimized
at zero ordinary index height and then at the original endpoint
values of both private real coordinates. The upper ordinary cut is
paid by the already proved cap half-stencils. This leaves only two
explicit lower-cut expressions for that regular comparison.

The neighboring retained height is held fixed in these comparisons.
Its additional term is recorded with both incidences in Section 4.
No sign of that term, of the two remaining lower-cut expressions,
or of the complete compensated boundary is asserted.

## 1. Original coupled derivative

Use the literal source, phases and allocations of the
[complete adjoining envelope](research_mixed_first_attached_complete_contour_envelope.md)
and [fixed-height comparison](research_mixed_first_attached_fixed_height_comparison.md).
The first target follows its actual affine early path
\[
 a=x+ih,\qquad h=c\frac{x-.1}{.12},\qquad
 .1\le x\le.22,\qquad
 \lambda=-\frac c{.12},\qquad r=e^{2\pi h}.
 \tag{1}
\]
Thus \(a'=1-i\lambda\). Retain the actual sign of \(c\):
own three has \(-.072<c<.021\), and own four has
\(-.108<c<-.020\). In particular
\[
 -\frac7{40}<\lambda<\frac9{10},\qquad
 \frac12<r<\frac{23}{20},\qquad
 \lambda\ge0\Longrightarrow r\le1,\quad
 \lambda\le0\Longrightarrow r\ge1.
 \tag{2}
\]
The same proofs apply after multiplying the original first height
by a fixed additional cutoff in \([0,1]\), using the resulting
effective \(c\) in both places in (1).

Keep the second target \(b\) fixed, and write
\[
 e\in[.27,.49]\ \hbox{real},\qquad
 s=v+i\eta,\quad v\in[.2,.49],\quad \eta\le0.
 \tag{3}
\]
The regular joint profile, with the shared first Fourier weight
allocated exactly once, is
\[
 \mathcal J=\Psi_\alpha(e,a)-\frac\alpha2g(a)
                                  +F_{\alpha\epsilon}(s;a,b).
 \tag{4}
\]
Its moving-height derivative is
\[
 \begin{split}
 \mathcal H_\alpha(e,v,\eta;x,c)
 &=\Re\{(1-i\lambda)D_\alpha\},\\
 D_\alpha&=g'(e+a)+g'(s+a)
                         -(2+\alpha)g'(a)+2\pi i s.
 \end{split}
 \tag{5}
\]
The last term is the original ordinary chirp. No imaginary gauge
is added to (5): the opposite gauges of the two half-stencils
cancel in this joint expression.

## 2. The ordinary-height and endpoint reductions

**Lemma 1.** For either \(\alpha\), the function in (5) strictly
decreases as \(\eta\) increases on \((-\infty,0]\). At \(\eta=0\)
its minimum over \(e,v\) is attained at
\[
                  e\in\{.27,.49\},\qquad v\in\{.2,.49\}.
 \tag{6}
\]

*Proof.* Put \(R=e^{2\pi\eta}\) and
\(\theta=2\pi(v+x)\). On the present real intervals,
\[
             .6\pi\le\theta\le1.42\pi,\qquad
                         \cos\theta<-6/25.
 \tag{7}
\]
Direct differentiation of the original logarithm and chirp gives
\[
 \partial_\eta\mathcal H_\alpha
  =-\frac{2\pi\{1-Rr\cos\theta-\lambda Rr\sin\theta\}}
                        {|1-Rr e^{-i\theta}|^2}<0.
 \tag{8}
\]
Indeed, if \(\lambda\ge0\), then \(Rr\le1\) and
\(\cos\theta+\lambda\sin\theta<9/10\). If \(\lambda<0\),
the same expression is less than
\(-6/25+7/40=-13/200<0\). This proves strictness in (8).

At \(\eta=0\), differentiating with respect to \(v\) gives
\[
 \partial_v\mathcal H_\alpha
  =\frac{2\pi\{\lambda(1-r\cos\theta)+r\sin\theta\}}
                             {|1-r e^{-i\theta}|^2}.
 \tag{9}
\]
Write its numerator without the constant \(2\pi\) as \(N(\theta)\).
At every zero,
\[
 \lambda=-\frac{r\sin\theta}{1-r\cos\theta},\qquad
 N'(\theta)=\frac{r(\cos\theta-r)}{1-r\cos\theta}<0.
 \tag{10}
\]
Every critical point is therefore a strict maximum. Two such
crossings would require an intervening crossing in the other
direction. Thus the minimum in \(v\) is at an endpoint.

The \(e\) derivative is the original cap half-stencil derivative:
with \(\theta_e=2\pi(e+x)\), its sign is the sign of
\[
                 \sin\theta_e+\lambda(\cos\theta_e-r).
 \tag{11}
\]
At a zero its derivative with respect to \(\theta_e\) equals
\((r\cos\theta_e-1)/(r-\cos\theta_e)<0\).
Here \(\cos\theta_e<0\). The same endpoint-minimum argument
therefore applies, exactly as in Lemma 2 of the
[real-private half-stencil](research_mixed_cap_real_private_half_stencil.md).
This proves (6). \(\square\)

The upper ordinary cut in (6) already has a uniform favorable sign.
Let
\[
 H^{\rm cap}_\alpha(e)
   =\Re\{(1-i\lambda)
       [g'(e+a)-(1+\alpha/2)g'(a)+3i/2]\}.
 \tag{12}
\]
The completed
[cap half-stencils](research_mixed_cap_early_taper_envelope_transport.md),
equation (14), give
\(H^{\rm cap}_0>1/20\) and \(H^{\rm cap}_1>1/600\).
At \(v=.49\) the exact identity is
\[
 \mathcal H_\alpha(e,.49,0)
   =H^{\rm cap}_\alpha(e)+H^{\rm cap}_\alpha(.49)
                              +\lambda(.98\pi-3).
 \tag{13}
\]
For \(\lambda\ge0\), the last term is nonnegative, since
\(.98\pi>3\). If \(\lambda<0\), only own three occurs;
\(.98\pi-3<2/25\) and \(\lambda>-7/40\). Hence
\[
 \mathcal H_0(e,.49,0)>\frac{43}{500},\qquad
 \mathcal H_1(e,.49,0)>\frac1{300}.
 \tag{14}
\]

Consequently, apart from these already paid endpoints, a uniform
regular-profile sign can depend only on the two explicit expressions
\[
 \Re\!\left[(1-i\lambda)
 \{g'(e+a)+g'(.2+a)-(2+\alpha)g'(a)+.4\pi i\}\right],
                  \qquad e=.27,\ .49.
 \tag{15}
\]
No favorable sign of (15) is asserted. In particular, failure of an
individual expression there would not by itself show failure of the
maximum finite-source envelope; its profile could be inactive.

## 3. The entire own-three true-end alternative is increasing

For \(\alpha=0\), keep the actual alternative
\[
        E_{\rm end}(h)+\Re F_{0\epsilon}(s;a,b),\qquad
 E_{\rm end}(h)=\frac35+2\pi h_++\frac1{100}\log4 .
 \tag{16}
\]
No assumption that it is dominated by a regular private profile
is made.

**Proposition 2.** Along (1), with \(b\) fixed and \(\eta\le0\),
the derivative of (16) is greater than \(21/242\), with one-sided
derivatives at the two real endpoints.

*Proof.* Its \(\eta\) derivative is precisely (8): the cap
endpoint term is independent of \(\eta\), and the only
\(\eta\)-dependent terms of its \(a\) derivative are the same
ordinary logarithm and chirp. It suffices to prove the assertion
at \(\eta=0\).

Put
\[
 p=g'(v+a)-g'(a),\qquad
 Z=\frac{1-r e^{-2\pi i(x+v)}}{1-r e^{-2\pi ix}} .
 \tag{17}
\]
The common-radius comparison already proved for the fixed-height
envelope gives
\[
                         \Re p>\frac{21}{242}.
 \tag{18}
\]
To retain the argument with its original lift, multiply the
numerator of \(Z\) times its conjugate denominator by \(e^{i\pi v}\).
Its real and imaginary parts are exactly
\[
 \begin{split}
 \Re&=(1+r^2)\cos\pi v-2r\cos(2\pi x+\pi v)>0,\\
 \Im&=(1-r^2)\sin\pi v.
 \end{split}
 \tag{19}
\]
Positivity in the first line follows from
\(0<\pi v<2\pi x+\pi v<\pi\), the decreasing cosine,
and \(1+r^2\ge2r\). Continuation from \(r=0\)
therefore fixes the original argument without an integer lift.
Equation (19) proves
\[
 r\le1\Longrightarrow\Im p\ge-\pi v,\qquad
 r\ge1\Longrightarrow\Im p\le-\pi v.
 \tag{20}
\]

If \(c\le0\), then \(\lambda\ge0\), \(r\le1\), and the
endpoint term in (16) has zero derivative. The joint derivative is
\[
                  \Re p+\lambda(\Im p+2\pi v)
                     \ge\Re p+\lambda\pi v>\frac{21}{242}.
 \tag{21}
\]
If \(c\ge0\), then \(\lambda\le0\), \(r\ge1\), and the
endpoint derivative is \(-2\pi\lambda\). The joint derivative is
\[
 \Re p+\lambda(\Im p+2\pi v-2\pi)
       \ge\Re p+\lambda(\pi v-2\pi)>\frac{21}{242}.
 \tag{22}
\]
The last added term is nonnegative because \(v<1/2\).
At \(c=0\) both formulas agree. This proves the proposition.
\(\square\)

Integration followed by the maximum over the unchanged ordinary
real interval preserves this bound. Thus the own-three true-end
alternative is fully paid for this moving-first-height comparison,
even when the maximizing ordinary real index changes. No smoothness
of that maximizer or phase root is needed.

## 4. The neighboring height and the unchanged boundary charges

The preceding statements hold \(b\) fixed. When the actual minimum
move also changes its neighbor's height, that contribution cannot
be dropped. If \(b=z+ih_b\) has
\(h_b'=\xi c_b R(z)/.12\), \(\xi\in\{0,1\}\), the exact extra
derivative of the full adjacent profile is
\[
 -\frac{\xi c_bR(z)}{.12}
       \Im\left\{
          \partial_b F_{\alpha\epsilon}(s;a,b)
                         +\partial_1\mathcal P_{\rm next}(b,d)
          \right\}.
 \tag{23}
\]
Here \(\mathcal P_{\rm next}\) denotes the actual next profile
with its existing allocation; one may use its coherent phase only
where its full finite-source theorem applies. The first marginal
in braces is explicitly
\[
              g'(s+b)-(1+\epsilon/2)g'(b).
 \tag{24}
\]
The two halves at \(b\) are thus retained, with the same switch
and original reference. No sign of (23) is inferred from the
root-eligibility theorem alone. Formula (23) is written on a
regular differentiable profile. A physical-tail alternative must
retain its own rate and derivative, including its zero walls;
it is not assigned a coherent derivative by this notation.

For a move confined to the first real coordinate with the second
real coordinate fixed, only the first two retained heights can
change. In the actual compensated left window with its protected
cut strip, the closing terms, synthetic extension and relative
pinning fee consequently remain unchanged. The exact cancellation
identity (4) of the
[shallow compensated comparison](research_mixed_left_boundary_shallow_taper.md)
still identifies the change of the calibrated boundary expression
with that of these literal local source factors. This observation
retains the charges; it does not pay (23) or substitute an
independently closed cap value.

The unresolved requirements are therefore concrete: regular
profile control at (15) or a proof that a failing profile is
inactive, the other physical-tail alternatives, and the actual
two-incidence neighbor term (23). No complete boundary inequality,
whole-source lower bound, or larger knot family follows from the
paid moving-height branch in Proposition 2.
