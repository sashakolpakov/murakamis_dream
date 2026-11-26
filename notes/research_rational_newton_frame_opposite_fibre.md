# A rational Newton frame and its opposite-fibre period

21 November 2026. Research note; previous finals and public manuscripts
remain unchanged.

The canonical positive and negative crossing polynomials both contain
the same large Chebyshev factor on a fixed outer spectral chart. A
rational change of representatives removes that factor while preserving
every physical Hermite jet. The denominator has poles only on the
opposite Chebyshev fibre. Those poles carry an exact compensating
period; they cannot be omitted when a contour is moved.

This gives a better rational frame for outer evaluation. It does not
turn multiplication of representatives into the physical quotient
product, remove the marked cycle, or establish a knot volume limit.

## 1. The physical algebra and a unit on its neighbourhood

Fix \(N\ge2\), \(d=N-1\), \(q=e^{\pi i/N}\), and write
\[
 P(z)=P_N(z)=2T_N(z/2)+2,\qquad
 c_j=2\cos((2j+1)\pi/N).
 \tag{1}
\]
Here \(T_N\) is the Chebyshev polynomial of the first kind. The original
physical algebra is
\[
 \mathcal A_N=\mathbb C[z]/(P),\qquad
 e_r(z)=\frac{\prod_{h=0}^{r-1}(c_h-z)}{S_r^2},
 \quad
 S_r=\prod_{h=1}^r2\sin(\pi h/N),\quad S_0=1.
 \tag{2}
\]
It retains the value and first derivative at every double root.
At odd \(N\), the simple root \(-2\) has only its value coordinate.
The original source and turn obey
\[
 \phi_N(f)=(-1)^dN^2[z^d]\operatorname{rem}_{P}f,\qquad
 \phi_N(e_i e_j)=\delta_{i+j,d},\qquad Je_r=e_{d-r}.
 \tag{3}
\]
The other original closing row is
\(\lambda_0(f)=f(c_0)\); it too is retained below.

Consider the rational function
\[
              u_N(z)=\frac4{4-P(z)}.
 \tag{4}
\]
Its pole set is the opposite fibre \(D_4=\{P=4\}\), disjoint from
the physical fibre \(D_0=\{P=0\}\). Moreover
\[
                 u_N-1=\frac{P}{4-P}.
 \tag{5}
\]
Thus \(u_N\) is a unit on a neighbourhood of the entire physical
divisor, and its class in \(\mathcal A_N\) is exactly one.

For every polynomial \(f\), the rational representative \(u_Nf\)
therefore has the same full physical Hermite data as \(f\). At a double
root, both its value and its first spectral derivative agree; at the
odd simple root its value agrees. This is equality in the full algebra,
not merely at the distinct roots.

These assertions concern the fixed root and spectral variable \(z\).
They do not identify a moving-\(q\) normal with a spectral derivative.
A moving-parameter application must retain its genuine full family
and its corresponding physical relation.

## 2. Exact finite operations in the rational frame

Let \(\mathscr O_0\) be the ring of rational functions regular at every
point of \(D_0\), and let
\(\pi_0:\mathscr O_0\to\mathcal A_N\) be its Hermite restriction.
The rational frame space is
\[
 \mathcal V_N^{\rm rat}
       =\{u_N f:\deg f<N\},\qquad
 s_u(a)=u_N\widetilde a,
 \tag{6}
\]
where \(\widetilde a\) is the canonical polynomial of degree below \(N\).
Equation (5) gives \(\pi_0s_u=I\). In particular \(s_u\) is a
linear isomorphism onto this \(N\)-dimensional rational space.

Transport the original operations by this isomorphism:
\[
 F\star G=s_u(\pi_0F\,\pi_0G),\qquad
 J_uF=s_u(J\pi_0F),\qquad
 \phi_u(F)=\phi_N(\pi_0F).
 \tag{7}
\]
Also put \(\lambda_{0,u}(F)=\lambda_0(\pi_0F)\).
The unit for \(\star\) is \(u_N\), the frame vectors are \(u_Ne_j\),
and their product and turn matrices are exactly the original matrices.
Every finite original Conway word has precisely the same two closing
values after this transport. No boundary direction is deleted.

Ordinary rational multiplication is different from \(\star\).
It has the same physical class, but can leave the finite frame space.
Thus one may multiply rational functions before Hermite restriction,
but an assertion about their values away from \(D_0\) must retain
the actual reduction or carry. Equations (6)--(7) are a change of
representatives, not a multiplicative splitting of the quotient.

## 3. The whole frame has a uniform outer bound

**Theorem.** For every compact
\(K\subset\{z:\operatorname{Re}z<-6\}\), there is a constant \(C_K\)
independent of \(N\ge2\) such that
\[
 \boxed{\quad
       \sup_{z\in K}\sum_{r=0}^{d}|u_N(z)e_r(z)|
                                      \le\frac{C_K}{N^2}.
 \quad}
 \tag{8}
\]
Consequently, if \(f=\sum_{r=0}^da_re_r\), then
\[
          \sup_K|u_Nf|\le C_KN^{-2}\max_r|a_r|.
 \tag{9}
\]
Every fixed spectral derivative has the same type of bound, with a
constant also depending on the derivative order.

**Proof.** The exact endpoint ratios from the
[outer crossing theorem](research_canonical_crossing_outer_chart_carry.md)
are
\[
 e_d=\frac{(-1)^dP}{N^2(z-c_0)},\qquad
 \frac{e_{d-j}}{e_d}
       =\frac{S_j^2}{\prod_{h=1}^j(c_h-z)}.
 \tag{10}
\]
Choose \(\delta>0\) so that
\(\operatorname{Re}z\le-6-\delta\) on a neighbourhood of \(K\).
Since \(c_h\in[-2,2]\), each factor in the second expression has
modulus at most
\[
                            \rho_K=\frac4{4+\delta}<1.
 \tag{11}
\]
Hence the sum of these ratios is at most \(1/(1-\rho_K)\).

There are no opposite-fibre poles on the outer half-plane. To see
this with a bound uniform in \(N\), choose \(w\) with
\(w+w^{-1}=z\) and \(|w|>1\). On \(K\), \(|w|\) is bounded below
by some \(r_0>5\), because \(|z|>6\) and
\(|z|\le|w|+|w|^{-1}\). Thus
\[
 |P(z)|=|w^N+2+w^{-N}|
             \ge r_0^N-2-r_0^{-N}
             \ge r_0^2-2-r_0^{-2}>4.
 \tag{12}
\]
In particular \(P/(4-P)\) is uniformly bounded there. Equation (10)
gives
\[
 u_Ne_d=\frac{(-1)^d4P}{N^2(z-c_0)(4-P)}
                                      =O_K(N^{-2}).
 \tag{13}
\]
Combine this with (11) to obtain (8), and then (9).
The same estimates hold on a slightly larger compact neighbourhood.
Cauchy's integral formula gives the fixed derivative bounds.
\(\square\)

This bound measures the coefficient norm in the full actual Newton
frame. It is not a bound for the coefficients \(a_r\) of an arbitrary
completed knot packet, which may themselves have substantial growth.

For the original signed crossings, the outer theorem gives the more
precise consequence
\[
 u_NR_N^\epsilon(z)
   =-\frac{4\kappa^\epsilon q^{\epsilon d}}
                  {N^2(z-c_0)}(1+O_K(N^{-2})),
 \qquad \epsilon=\pm1,\quad \kappa=q^{d^2/2}.
 \tag{14}
\]
Indeed \(P/(4-P)=-1+O_K(e^{-a_KN})\) for some \(a_K>0\).
Thus the common variable outer exponential has disappeared from both
rational crossing representatives. All original unit phases remain.

## 4. The physical period transfers to the opposite fibre

Let \(f\) be canonical, so \(\deg f<N\). All residues below are residues
of ordinary meromorphic one-forms; a repeated root uses its full pole,
not a semisimple value substitution. The original closing is
\[
 \phi_N(f)=(-1)^dN^2
                  \sum_{P(a)=0}\operatorname{Res}_{z=a}
                                             \frac{f(z)}{P(z)}\,dz.
 \tag{15}
\]
For example, the finite sum in (15) equals \([z^d]f\), by expanding
at infinity. Equation (5) preserves every residue at the physical
divisor. The relevant global identity is exactly
\[
 \frac{u_Nf}{P}\,dz
               =\frac fP\,dz+\frac f{4-P}\,dz.
 \tag{16}
\]
The left side is \(O(z^{-N-1})\,dz\) at infinity, so has zero residue
there. Its only finite poles are in \(D_0\cup D_4\). Therefore
\[
 \boxed{\quad
 \phi_N(f)
   =(-1)^dN^2\sum_{P(a)=0}
                      \operatorname{Res}_{a}\frac{u_Nf}{P}\,dz
   =-(-1)^dN^2\sum_{P(b)=4}
                      \operatorname{Res}_{b}\frac f{4-P}\,dz.
 \quad}
 \tag{17}
\]
The minus sign is essential. With both sets of small circles oriented
counterclockwise, their integrals of the left side of (16) sum to zero.
Replacing the physical contour by a contour around \(D_4\) reverses
its orientation.

The condition on the representative in (17) is also essential.
An unreduced polynomial of larger degree can leave a residue at
infinity, and a rational inserted coupon can have further poles.
Their contributions must be retained. Formula (16) remains an identity,
but its total residue relation then includes every such term.

The rational frame has consequently moved the large polynomial sector
into explicit opposite-fibre poles. It has not made the source disappear.
For instance
\[
                     \phi_N(e_d)=1,\qquad Je_d=1.
 \tag{18}
\]
The leading endpoint polynomial is a genuine physical socle class.
The rational representative in (13) retains that same class and period.

## 5. The inverse-word carry is still present

Let the exact polynomial carry of the two canonical inverse crossings
be
\[
        C_N=\frac{R_N^+R_N^--1}{P},
        \qquad R_N^+R_N^-=1+PC_N.
 \tag{19}
\]
For \(\overline R^\epsilon=u_NR_N^\epsilon\), ordinary rational
multiplication gives
\[
 \overline R^+\overline R^-=1+P\overline C_N,\qquad
            \overline C_N=
                  \frac{16C_N+8-P}{(4-P)^2}.
 \tag{20}
\]
This is direct algebra, with the opposite-fibre poles displayed.
It does not assert \(\overline R^+\overline R^-=1\) as a rational
function. In the transported finite algebra its inverse identity
is instead
\[
                      \overline R^+\star\overline R^-=u_N,
 \tag{21}
\]
where \(u_N\) is the transported unit.

On the outer chart, (14) makes the ordinary product
\(O_K(N^{-4})\). Hence the ordinary defect in (20) approaches \(-1\);
it cannot be dropped even though it no longer has the original large
Chebyshev exponential. The original product is recovered by the
physical restriction and carry, not by multiplying scalar outer
principal terms.

There is a local algebraic reason no general choice of representatives
removes all carries. Consider the square-zero extension
\[
       \mathbb C[z]/(P^2)\longrightarrow\mathbb C[z]/(P).
 \tag{22}
\]
Any unital algebra section sends the class of \(z\) to
\(z+Ph(z)\) modulo \(P^2\). The relation \(P=0\) would require
\[
 P(z+Ph)=P(1+hP')=0\pmod{P^2}.
 \tag{23}
\]
This is possible only if \(P'\) is invertible modulo \(P\), and is
possible when that condition holds by choosing \(h=-(P')^{-1}\).
The actual \(P_N\) has double roots at every \(N\ge2\), so (22)
does not split. The rational frame (4) does not change this extension.

## 6. Why this normalization singles out one fibre

Put \(v=P_N(z)\). Every rational unit on
\(\mathbb A^1\setminus\{0,4\}\) has the form
\[
                     c\,v^a(v-4)^b,\qquad
           c\in\mathbb C^\times,\quad a,b\in\mathbb Z.
 \tag{24}
\]
Indeed a rational function and its inverse can have finite poles only
at \(0,4\), so unique factorization gives (24). A unit which extends
regularly and nonvanishingly across both removed fibres must have
\(a=b=0\). If it is normalized to one at \(v=0\), it is the constant one.
Thus a rational base unit cancelling a power of \(v\) at infinity
cannot simultaneously be a regular unit at both ramified fibres.

Our choice \(u(v)=4/(4-v)\) is normalized at the physical fibre and
has its pole at the opposite one. On the Laurent cover
\(z=w+w^{-1}\),
\[
 P_N(z)=\frac{(w^N+1)^2}{w^N},\qquad
                  u_N=-\frac{4w^N}{(w^N-1)^2}.
 \tag{25}
\]
It introduces no branch-value divisor beyond the two already present
in this Chebyshev geometry.

The spectral half-step \(w\mapsto qw\) exchanges the fibres:
\[
       P_N(qw+q^{-1}w^{-1})=4-P_N(w+w^{-1}).
 \tag{26}
\]
It sends \(u(v)\) to \(4/v\), which is singular at the physical fibre.
The existing
[doubled-grid theorem](research_mixed_next_outer_doubled_grid_half_step.md)
already retains these two fibres and their Hermite multiplicities.
Equation (26) is not an identification of that half-step with the
physical Newton turn \(J\).

The improvement here is the rational frame estimate (8) and its exact
period/carry bookkeeping. It does not define a knot-dependent
A-polynomial torsor: \(P_N\), \(u_N\) and the two fibres are universal.
The actual knot data are its packet, the transported operations and
the marked period. A global geometric contour argument must still
carry the opposite-fibre residues and prove the required coherent
lower estimate.

## Complete proof and coverage sources

All three complete matching texts were read. The first supplies the
actual outer ratios and inverse carry, the second the full Newton
algebra and marked source, and the third the existing opposite-fibre
coverage. The rational normalization, frame bound, residue transfer
and limitations are proved above.

| Source | SHA-256 |
|---|---|
| [Canonical outer crossing and carry](research_canonical_crossing_outer_chart_carry.md) | f26d45f356e1efeb209bf59a556c1ce17eb54aca4e170d3e02b4b38fa50945be |
| [Actual Newton source and turn](actual_newton_turn_positive_gram.md) | d8b21fa8db909120035e86e997a0e02cb84f8dce2dcf6fb244bb5c85c17e28a3 |
| [Doubled spectral grid](research_mixed_next_outer_doubled_grid_half_step.md) | 0cc541295d0562af9d235e4d27f7e1cb329a2fdc14569629ef76b3b0cccbaa37 |

Only written mathematics and text/hash operations were used. No
mathematical program, test, numerical iteration, build, git operation,
previous-final edit or public-document change was performed.
