# Certified endpoint support grids and geometric decoupling

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

This note separates the original source optimization from its geometric
reference parameters. It gives certified source upper values on a slope grid,
with convex interpolation between values, and a subharmonic principle for
the actual support defect. It does not yet compare those upper values with
every geometric intercept.

The 192-bit author and independent 256-bit positive-frequency replay pass.
The author checks 18,513 source cells and 14,232 reference-slope cells; the
independent replay checks 18,545 and 16,033 cells after exact refinements.

## 1. The original (4,3) right endpoint

The notation \((4,3)\) means that the left leg has type four and the own
block has type three.
At the right period endpoint \(Y=1\), retain every finite row:
\[
 |C_{0,N}(X,1)|\,|d_N(X)X^{-N\sigma}|^{1/2}
 \le \sum_{j=0}^{N-1}
       \frac{|X^{-j}p_j(X)|}{S_j}
                 |d_N(X)X^{-N\sigma}|^{1/2}.
 \tag{1}
\]
The half weight is only a nonnegative modulus; no holomorphic square
root is selected. Write \(X=e^{-2\pi i(x+ih)}\). With the notation of
[the angular candidate theorem](research_mixed_angular_support_candidates.md),
the row's full upper exponent is
\[
 E_h(u,x)=I_h(u,x)-J(u)-2\pi hu
       +\tfrac12\{\max(\nu_h(x),2\pi h_+)-2\pi\sigma h\}.
 \tag{2}
\]
Here \(u\in[0,1]\), \(x\in[0,1]\), and \(h_+=\max(h,0)\).
The actual cases certified below are
\[
 (h,\sigma)=(-.057,0),\quad(-.02,0),\quad(0,0),\quad(.014,1).
 \tag{3}
\]
Define the compact source support function
\[
 S_h(\kappa)=\max_{0\le u,x\le1}
                       \{E_h(u,x)-\kappa x\}.
 \tag{4}
\]
It is continuous and convex in \(\kappa\), since it is a maximum of
affine functions, and is 1-Lipschitz. Thus certified upper values
\(S_h(\kappa_j)<U_{h,j}\) give the rigorous chord bound
\[
 S_h(\kappa)<
 \frac{\kappa_{j+1}-\kappa}{\kappa_{j+1}-\kappa_j}U_{h,j}
 +\frac{\kappa-\kappa_j}{\kappa_{j+1}-\kappa_j}U_{h,j+1},
 \quad \kappa_j\le\kappa\le\kappa_{j+1}.
 \tag{5}
\]
These are upper chords, not tangent approximations or extrapolated lines.

## 2. A global two-variable interval proof of each source value

There is no missing row or Fourier switch in (4). Put \(H=|h|\),
\(G_H(v)=\Re g(v-iH)\), and \(c_h=2\pi\max(-h,0)\).
For \(q=0,1\), define
\[
 \begin{split}
 F_q(u,x;h,\kappa)={}&G_H(x+u)-(1+q/2)G_H(x)-J(u)+c_hu\\
 &+\pi h_+(1-q/2)-\pi\sigma h
                      -(\kappa+q\pi h_+)x .
 \end{split}
 \tag{6}
\]
The original reflection identity gives exactly
\[
            E_h(u,x)-\kappa x=\max(F_0,F_1).
 \tag{7}
\]
In particular the positive selected height in (3) retains its
normalization and both Fourier alternatives. The lower-half-plane
primitive in (6), when \(h\ne0\), is regular for the entire row and angular period,
including \(x+u>1\); its real part is periodic.

**Proposition 1.** The canonical record supplies strict rational upper
values \(U_{h,j}\) for all 60 pairs
\[
          h\in\{-.057,-.02,0,.014\},\qquad
          \kappa_j=-2/5+j/20,\quad j=0,\ldots,14.
 \tag{8}
\]
Every value bounds the whole square in (4), including its closed boundary.
For example, at \(\kappa=1/4\) the certified upper values at the four
heights in (8), in order, are
\[
 \frac{390319}{10^6},\quad \frac{343479}{10^6},\quad
 \frac{81373}{250000},\quad \frac{271577}{10^6}.
\]
The canonical record contains all 60 exact rational upper values.

Here is the acceptance proof. On each exact dyadic square, both
functions (6) are bounded by their value and gradient at the midpoint
plus the complete second-order Taylor remainder. For radii \(r_u,r_x\),
this is
\[
 F_q(v)\le F_q(p)+|F_{q,u}(p)|r_u+|F_{q,x}(p)|r_x
 +\tfrac12 M_{uu}r_u^2+M_{ux}r_ur_x+\tfrac12 M_{xx}r_x^2.
 \tag{9}
\]
Each \(M\) bounds the corresponding real Hessian entry throughout
the whole square. The exact derivatives used are
\[
 \begin{split}
 F_{q,u}&=G_H'(x+u)-J'(u)+c_h,\\
 F_{q,x}&=G_H'(x+u)-(1+q/2)G_H'(x)-\kappa-q\pi h_+,\\
 F_{q,uu}&=G_H''(x+u)-\pi\cot(\pi u),\\
 F_{q,ux}&=G_H''(x+u),\\
 F_{q,xx}&=G_H''(x+u)-(1+q/2)G_H''(x).
 \end{split}
 \tag{10}
\]
All quantities are evaluated outward. On a square meeting \(u=0\)
or \(u=1\), apply (9) to the smooth part \(F_q+J\), then subtract
the exact minimum of \(J\) on the row interval. That minimum is
among the two interval endpoints and \(1/6\), when included.
This follows from \(J'(u)=\log(2\sin\pi u)\); the other critical
point \(5/6\) is a maximum. Endpoint values \(J(0)=J(1)=0\) are
used exactly, rather than differentiating the logarithmic zeros.

At \(h=0\), a square meeting \(x=0,1\) or \(u+x=1\) is instead bounded
by the exact separate ranges of the three real \(J\) terms in (6).
On any interval in \([0,2]\), those ranges are attained at its endpoints
or the included integer translates of \(1/6,5/6\); use the continuous
periodic extension and exact integer values zero. Every other square
uses (9). Thus zero-height factor zeros and the diagonal support wall
are included without differentiating a singular logarithm.

The proof accepts a square only if both outward upper bounds are
strictly below the prescribed rational \(U_{h,j}\). A floating optimizer
may propose that rational number, but it supplies no acceptance premise.
The exact prefix-free binary covers have Kraft mass one. Consequently
every row and angle, every Fourier branch, and all removable endpoints
are included. A finite positive minimum certificate reserve absorbs
the arbitrary small Fourier-comparison tolerance from the preceding note.
The original finite source in (1) therefore has the stated upper rate,
with only polynomial prefactors.

## 3. The actual reference slope range

For reference legs
\[
 a\in[.27,.33]+i[-.057,-.02],\qquad
 b\in[.30,.39]+i[-.03,.02],
 \tag{11}
\]
let \(s=s(a,b)\) be the original selected conditional root, and define
\[
 \begin{split}
 \Phi(a,b)={}&g(s+a)+g(s+b)-2g(s)+2\pi ias
                         -\tfrac32g(a)-g(b),\\
 \Phi_a={}&g'(s+a)+2\pi is-\tfrac32g'(a).
 \end{split}
 \tag{12}
\]
The [full central conditional theorem](research_mixed_central_conditional_rectangles.md)
establishes this holomorphic branch on a neighborhood of the full reference
product before any boundary reduction is made.

**Proposition 2.** Throughout (11),
\[
                        -2/5<\Re\Phi_a<3/10.
 \tag{13}
\]
The separate harmonic maximum and minimum principles reduce this to
the sixteen products of reference rectangle edges. The focused checker
covers them by exact dyadic parameter rectangles. It uses the original
quadratic identity
\[
 A(B-1)U^2+(A-B)U+1-A=0,\quad
 A=e^{-2\pi ia},\ B=e^{-2\pi ib},\quad
 s=\frac{i}{2\pi}\Log U.
 \tag{14}
\]
On every accepted cell, the selected root enclosure lies in
\(.2<\Re s<.44,\ |\Im s|<.15\), all original logarithms remain on
their regular strips, and the original logarithmic residual has modulus
less than one. Since exponentiating (14) makes that residual an integer
multiple of \(2\pi i\), its lift is exactly zero. The established central
uniqueness identifies the root with (12). Its entire derivative enclosure
satisfies (13). Thus the certified grid (8) covers every actual reference
slope, not merely the diagnostic examples that proposed it.

## 4. Why local slope chords suffice on the distinguished boundary

Let the target endpoint coordinate be \(e\in\{0,1\}\), preserving both
possible geometric supporting planes even though they have the same
physical value \(Y=1\). Put
\[
 C_e(a,b;h)=\Phi(a,b)-a\Phi_a(a,b)
                         +(e-b)\Phi_b(a,b)+ih\Phi_a(a,b).
 \tag{15}
\]
The original complex supporting plane at target \((x+ih,e)\) is
\[
                       \Re C_e+\kappa x,\qquad\kappa=\Re\Phi_a.
 \tag{16}
\]
The imaginary tangent contribution is retained in (15).

The actual optimized support defect is
\[
                 D_h(a,b)=S_h(\Re\Phi_a)-\Re C_e.
 \tag{17}
\]
It is separately subharmonic in the two reference variables.
Indeed it is the supremum, over the fixed compact source square,
of the harmonic functions
\[
       E_h(u,x)-\Re\{C_e+x\Phi_a\}.
\]
This family is locally bounded and continuous jointly in source and
reference variables, so the supremum is continuous and subharmonic.
Successive maximum principles therefore extend a bound for the actual
defect (17) on the distinguished boundary to the full reference product.

On each boundary cell one may choose any chord (5) whose slope interval
contains that cell's certified range of \(\kappa\), subdividing or using
several adjacent slope intervals if needed. Subtracting \(\Re C_e\) yields
a rigorous upper bound for the actual defect there. The maximum principle
is applied only after the true defect has been bounded on the entire
boundary. It is not applied to a slope-restricted subdomain, and no chord
is extrapolated beyond its certified interval.

Thus source optimization and reference geometry require separate
two-real-variable certificates, rather than one blind joint
high-dimensional cover. The source values and slope range are supplied
here. A negative reference-intercept comparison has not yet been supplied.

For unselected target heights in \([-.057,0]\), or selected heights in
\([0,.014]\), the source-point
defect is subharmonic in the target complex angle: the product entropy is
an integral of logarithms of moduli of holomorphic factors, the Fourier
envelope is a maximum of harmonic functions, and the other terms are
harmonic. Maximizing over the row preserves this property. Its maximum
on the target rectangle is therefore on the two horizontal height edges
or the two vertical period seams. The horizontal edges use the grids
above. The vertical seams require their own comparison; they are not
discarded by an unsupported claim of global height convexity.

## 5. Reproduction and scope

    python3 experiments/check_mixed_endpoint_support_grid.py --precision 192
    python3 experiments/replay_mixed_43_endpoint_support.py --precision 256

The result records every accepted dyadic source and reference cell, exact
rational grid values, and current dependency hashes. This is a source
upper-envelope and geometric-decoupling theorem. It is not the missing
full endpoint supporting-plane gap or the whole mixed-word source theorem.
