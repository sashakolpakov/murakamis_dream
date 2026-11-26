# Algebraic transport detected by neighboring boundary values

Research deduction, 7 November 2026. The nonzero holomorphic
asymptotic of the original Fourier boundary sum determines the
ratios of its neighboring boundary values. Their limits satisfy
explicit polynomial equations obtained from the original critical
equations. The finite ratios also obey an exact compatibility
identity before taking a limit.

The variables below are the boundary variables of this finite
expression. They are not identified here with a knot's meridian
and longitude. The resulting polynomial equations describe this
boundary correspondence; they are not an asserted finite-level
quantum A-polynomial annihilator.

The later [exact boundary difference system](research_mixed_fourier_exact_boundary_difference_system.md)
does supply two finite-level annihilating operators for this same
function. Their joint finite-band kernel is a line, and their
commuting symbols are the polynomials below. The present argument
independently identifies the branch selected by its proved asymptotic;
neither result identifies a closed knot's peripheral A-polynomial.

## 1. The original nonzero function and its two shifts

For each integer level \(N\), use exactly the finite function
from
[the complete Fourier-cap theorem](research_mixed_fourier_right_cap_full_asymptotic.md):
\[
 Z_N(a,y)=V_N^{\rm F}(y,e^{-2\pi ia}).
 \tag{1}
\]
Fix one of its actual reference pairs \((a_0,x_0)\).
The
[holomorphic packet theorem](research_mixed_fourier_right_cap_holomorphic_packet.md)
supplies a complex neighborhood on which
\[
 Z_N(a,y)=N^{-3/2}\mathcal A(a,y)e^{N\Phi(a,y)}
                                (1+\epsilon_N(a,y)),
 \qquad \mathcal A\ne0,\qquad \epsilon_N=O(N^{-1}),
 \tag{2}
\]
uniformly, with every fixed derivative of the normalized error
on smaller neighborhoods. The original stationary pair
\((s(a,y),q(a,y))\), phase \(\Phi\), and coefficient
\(\mathcal A\) use the continued original logarithmic branches.
In particular \(Z_N\ne0\) on a common smaller neighborhood
for every sufficiently large integer \(N\).

Let \(U'\) be a relatively compact polydisc in that neighborhood.
For sufficiently large \(N\), the shifted points below stay
inside the neighborhood. Define
\[
 \lambda_N(a,y)=\frac{Z_N(a+1/N,y)}{Z_N(a,y)},\qquad
 \upsilon_N(a,y)=\frac{Z_N(a,y+1/N)}{Z_N(a,y)}.
 \tag{3}
\]
These are ratios of the exact original finite sum, not of an
independently chosen stationary approximation.
With
\[
 X=e^{-2\pi ia},\qquad Y=e^{2\pi iy},\qquad
 r=e^{-2\pi i/N},
 \tag{4}
\]
the first shift sends \(X\) to \(rX\), and the second
sends \(Y\) to \(r^{-1}Y\). The opposite signs follow
from the original incoming and outgoing conventions.

**Proposition 1.** Uniformly on \(U'\), at both parities,
\[
 \lambda_N=e^{\Phi_a}(1+O(N^{-1})),\qquad
 \upsilon_N=e^{\Phi_y}(1+O(N^{-1})).
 \tag{5}
\]
The error estimates hold with every fixed parameter derivative.
More precisely, on smaller polydiscs,
\[
 \begin{split}
 \lambda_N&=e^{\Phi_a}
  \exp\left\{\frac{\Phi_{aa}/2+\partial_a\log\mathcal A}{N}
                                         +O(N^{-2})\right\},\\
 \upsilon_N&=e^{\Phi_y}
  \exp\left\{\frac{\Phi_{yy}/2+\partial_y\log\mathcal A}{N}
                                         +O(N^{-2})\right\}.
 \end{split}
 \tag{6}
\]

*Proof.* Substitute (2) in (3). Taylor's theorem gives
\(N[\Phi(a+1/N,y)-\Phi(a,y)]
=\Phi_a+\Phi_{aa}/(2N)+O(N^{-2})\), and the analogous
formula for the other variable. The nonzero coefficient
has a local logarithm; its corresponding increment is
\(N^{-1}\partial_a\log\mathcal A+O(N^{-2})\).
Finally \(\partial_a\epsilon_N=O(N^{-1})\), so
\[
 \frac{1+\epsilon_N(a+1/N,y)}{1+\epsilon_N(a,y)}
                                      =1+O(N^{-2}).
\]
This uses the normalized holomorphic error, rather than
an unnormalized derivative of an exponentially large sum.
The same argument applies to \(y\); Cauchy's estimates
on nested polydiscs give the fixed derivative assertions.
This proves (5)--(6). \(\square\)

## 2. Explicit limits from the original critical equations

Put
\[
 S=e^{-2\pi i s(a,y)},\qquad Q=e^{-2\pi i q(a,y)},
 \qquad L=e^{\Phi_a},\qquad U=e^{\Phi_y}.
 \tag{7}
\]
The unallocated phase is
\[
 F_0(s,a,q;y)=g(s+a)+g(s+q)-3g(s)-g(a)-g(q)
                                      +2\pi ias+\ell_q(y),
 \tag{8}
\]
with \(\ell_q\) defined in the full-source theorem.
The actual logarithmic equations are \(F_{0,s}=F_{0,q}=0\).
Exponentiating them, without changing their chosen lifts,
gives
\[
 \boxed{\quad
 (1-XS)(1-SQ)=X(1-S)^3,\qquad
 Y(1-SQ)=(1-Q)(1-YQ).
 \quad}
 \tag{9}
\]

At the stationary pair, the chain-rule terms in
\(d\Phi=dF_0(s(a,y),a,q(a,y);y)\) containing \(ds,dq\)
vanish. Hence
\[
 \begin{split}
 \Phi_a&=\Log(1-XS)-\Log(1-X)+2\pi is,\\
 \Phi_y&=2\pi i(q-1/2)
                          +\Log(1-YQ)-\Log(1-Y).
 \end{split}
 \tag{10}
\]
Every logarithm has its original continuation. In particular,
the \(-1/2\) in the outgoing linear term has not been removed.
It follows that the actual shift limits are
\[
 \boxed{\quad
 L=\frac{1-XS}{S(1-X)},\qquad
 U=-\frac{1-YQ}{Q(1-Y)}.
 \quad}
 \tag{11}
\]
The minus sign in \(U\) comes from \(e^{-\pi i}\).
The factors \(1-X\) and \(1-Y\) are part of the original
normalization and are retained. All the displayed denominators
are nonzero on a sufficiently small neighborhood of the actual
reference. A specialization where they vanish would require
a separate limiting argument.

## 3. Polynomial relations without the internal variables

Define
\[
                      D=X+(1-X)L,\qquad E=Y-(1-Y)U.
 \tag{12}
\]
Equation (11) gives exactly \(D=1/S\), \(E=1/Q\).
Substituting these into (9), and multiplying by the
nonzero denominators, yields two explicit polynomials:
\[
 \begin{split}
 \mathcal P_1(X,Y,L,U)
   &:=D(D-X)(DE-1)-XE(D-1)^3=0,\\
 \mathcal P_2(X,Y,L,U)
   &:=YE(DE-1)-D(E-1)(E-Y)=0.
 \end{split}
 \tag{13}
\]
For example the first equation of (9) becomes
\((D-X)(DE-1)/(D^2E)=X(D-1)^3/D^3\),
which proves the first line with its exact powers.
The second becomes
\(Y(DE-1)/(DE)=(E-1)(E-Y)/E^2\), proving the other.

These equations are used on the open set retaining all original
nonvanishing factors. In these coordinates this includes
\[
 XY(1-X)(1-Y)DE(D-1)(E-1)(D-X)(E-Y)(DE-1)\ne0.
 \tag{14}
\]
It excludes components introduced solely by clearing a
denominator. Conversely, on (14), equations (13) recover
the exponentiated equations (9) by \(S=1/D,Q=1/E\).
The original logarithmic critical branch is still selected
by continuation from the prescribed reference; the polynomial
equations alone do not distinguish its logarithmic lifts.

Combining (5) and (13), the exact finite ratios satisfy the
polynomial limit identities
\[
 \mathcal P_j(X,Y,\lambda_N,\upsilon_N)=O(N^{-1})
                      \quad(j=1,2),
 \tag{15}
\]
uniformly on \(U'\), with fixed derivatives on smaller
polydiscs. This follows by polynomial substitution and
the uniform bounds on the limiting variables.
No finite-level annihilation assertion is used to prove (15).

## 4. Exact compatibility and the normalization it leaves free

Before taking any limit, the two original ratios obey
\[
 \lambda_N(a,y)\upsilon_N(a+1/N,y)
       =\upsilon_N(a,y)\lambda_N(a,y+1/N).
 \tag{16}
\]
Both sides are exactly \(Z_N(a+1/N,y+1/N)/Z_N(a,y)\).
Thus transport around every elementary square of the
boundary lattice is compatible. On a connected rectangular
portion of that lattice, any two nonzero functions with the
same ratios differ by one constant: their quotient is unchanged
on each edge, hence on every vertex. Multiplication by a nonzero
constant acts freely and transitively on these functions.
This is a concrete multiplicative torsor, with the original
finite sum specifying one of its sections.

On the selected analytic branch, (10) gives the continuous
compatibility relation
\[
 \partial_y\log L=\partial_a\log U.
 \tag{17}
\]
Equivalently, the graph in \((X,Y,L,U)\) has
\[
                  d\log X\wedge d\log L
                         -d\log Y\wedge d\log U=0.
 \tag{18}
\]
Indeed
\(2\pi i\,d\Phi=-\log L\,d\log X+\log U\,d\log Y\)
on the continued logarithmic branches; applying \(d\)
proves (18). The graph has two complex dimensions, so
it is locally Lagrangian for the displayed product symplectic
form. This conclusion concerns the branch selected by the
finite-source asymptotic, not every component of (13).

The ratios and the polynomial equations leave the absolute
normalization free. Multiplication of \(Z_N\) by \(e^{Nc}\),
with \(c\) independent of \(a,y\), preserves both ratios
and changes its logarithmic growth by \(\Re c\).
Here that freedom is fixed by the literal finite normalization
and the calibrated \(\Phi\) in the full-source theorem.
An identification of this normalized action with a marked
hyperbolic volume still requires its geometric argument.

The result provides algebraic boundary transport for the
original finite sum, together with a nonzero analytic section
near the actual references. Extending that section through
arbitrary short fillings requires control of the global
contributing contour, as in
[the controlled saddle-transport criterion](research_dominant_saddle_transport.md).
Local algebraicity and exact compatibility alone do not
supply that global continuation or an exact quantum
A-polynomial for a closed knot.
