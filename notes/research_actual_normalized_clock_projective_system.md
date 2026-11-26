# The normalized joint clock system and its actual projective direction

Private written proof, 18 November 2026.

The unreduced boundary-exact source equations have balanced numbers
of factorial factors on their two sides. In the actual node scaling
one can divide their common scalar power of \(z\). What remains is
an exact analytic system of clock derivatives and bounded unit
factors on the original period quotient.

Its leading homogeneous equations contain the actual source direction
\([\mu]\). No rank or reducedness of that projective system is assumed
or concluded. In particular a simple Alexander determinant does not
by itself pay a local inverse for this presentation.

## 1. Source and the balanced scalar order

Use the fixed matching lattice, original highest cut, and the
unreduced coefficients \(\mathcal A_{j,v},\mathcal B_{j,v}\)
of [R]. At each crossing its inverse-factorial lengths are \(n,o\);
put \(M=n+o\). For a lattice step \(v\), write
\[
        \delta_n=n(v),\qquad\delta_o=o(v),\qquad
                       \delta_M=\delta_n+\delta_o .
 \tag{1}
\]
The notation \(a_+=\max(a,0)\) will be used for integers.
The Gaussian factors of \(\mathcal A_{j,v}\) number
\[
           (\delta_M)_++(-\delta_n)_++(-\delta_o)_+,
 \tag{2}
\]
and those of \(\mathcal B_{j,v}\) number
\[
           (-\delta_M)_++(\delta_n)_++(\delta_o)_+ .
 \tag{3}
\]
Their difference is
\(\delta_M-\delta_n-\delta_o=0\). Each is therefore
\[
            \frac{|\delta_M|+|\delta_n|+|\delta_o|}{2}.
 \tag{4}
\]
Summing over all crossings gives a nonnegative integer \(d_v\),
independent of the external shift \(j\).

All other factors of these coefficients are monomials or color
factors \(1-Q^rY^{\pm1}X^L\). Their limiting values at
\(Q=1,Y=\alpha,X=\mathbf1\), \(\alpha\ne0,1\), are units.
Every counted factorial factor has the form \(1-Q^rX^L\);
its lattice form \(L\) is one of \(n,o,M\). If \(L\) is identically
zero, its shift is zero and it contributes no factors in [R].
No extra boundary multiplier has been introduced.

The exact equation of [R], after grading completion, is
\[
 \left[
   \mathcal B_{j,v}(Q,Y,\mathsf E)\mathsf T^jM^v
                       -\mathcal A_{j,v}(Q,Y,\mathsf E)
 \right]\mathscr W_m=0,
 \quad
 \mathsf E_i:m\mapsto m+e_i,\quad M^v=e^{-h v\cdot m}.
 \tag{5}
\]
All its natural factors and their left ordering remain in (5).

## 2. Exact normalization in the actual Borel variables

Use the source and simple-node chart of [A]:
\[
 Y=\alpha+z,\qquad h=z^2\epsilon,\qquad m=\nu/z,\qquad
 F(z,\eta,\nu)
       =z\,\mathcal B_h\mathscr W_{\nu/z}(\alpha+z,z^2\eta).
 \tag{6}
\]
Let \(I\) be the primitive in \(\eta\) from the original origin,
with all continuation history retained. For a lattice form \(L\)
write \(D_L=L\cdot\partial_\nu\). The exact dictionary is
\[
                    Q^r\mathsf E^L
                       \longmapsto e^{r z^2 I+zD_L}.
 \tag{7}
\]
The two operators in this exponent commute. With
\(\psi(t)=(e^t-1)/t\), \(\psi(0)=1\), each factorial factor is
exactly
\[
 \boxed{\quad
 1-e^{r z^2I+zD_L}
    =-z\,(D_L+r zI)\,\psi(zD_L+r z^2I).
 \quad}
 \tag{8}
\]
This is a convergent power-series identity wherever the displayed
operators are bounded, and a formal identity independently of that.
No division by \(D_L\) is involved.

Replace every counted factor using (8), and remove only the
common scalar \((-z)^{d_v}\) from the two sides of (5).
Denote the remaining coefficient operators by
\(\widetilde{\mathcal A}_{j,v}\) and
\(\widetilde{\mathcal B}_{j,v}\).
Their definition keeps every factor \(D_L+r zI\), every \(\psi\),
and all original color, monomial, framing and pivot factors.
The normalized row is
\[
 \left[
   \widetilde{\mathcal B}_{j,v}\,
                  \widehat{\mathsf T}^{\,j}\widehat M^{\,v}
                       -\widetilde{\mathcal A}_{j,v}
 \right]F=0,\qquad
               \widehat M^{\,v}=e^{-z(v\cdot\nu)I}.
 \tag{9}
\]
It holds formally by scalar division in (5). Its analytic version
on the actual continued charts will be proved next. The coefficients
stand to the left of both source actions; they have not been
commuted through \(\widehat M^{\,v}\).

## 3. Bounded units on the full period quotient

Fix a finite continued \(\eta\)-path supplied by [A], including
its initial segment from zero, and a smaller compact neighborhood.
Let its length be at most \(L_0\). On a smaller \(z\)-disk the
actual family is entire of uniform exponential type in all clocks.
By [E, Section 3] it has a Cauchy representation on one product
spectral torus \(|\theta_i|=R_0\), with a bounded density.
The period kernel is preserved by every multiplier holomorphic
on a neighborhood of the full closed spectral polydisk.

On continuous density families along this path, the spectral
realization of \(D_L\) is multiplication by \(L\cdot\theta\);
hence
\[
             \|D_L\|\le\|L\|_1R_0,\qquad \|I\|\le L_0 .
 \tag{10}
\]
For the finite collection of rows under consideration, shrink \(z\)
so that every operator
\[
                  K_{r,L}=zD_L+r z^2I
 \tag{11}
\]
has norm at most \(1/4\). The elementary series gives
\[
 \|\psi(K_{r,L})-1\|
 \le\sum_{a\ge1}\frac{\|K_{r,L}\|^a}{(a+1)!}
 \le\frac{\|K_{r,L}\|e^{\|K_{r,L}\|}}2<\frac12 .
 \tag{12}
\]
Thus every \(\psi(K_{r,L})\) is a bounded two-sided unit,
with inverse norm at most two. Both its series and its inverse
preserve the period kernel. Indeed each term is a product of
full-polydisk holomorphic multiplication and an original primitive;
both preserve that kernel, and the series converge in norm.

Each color factor has the form
\[
                    1-(\alpha+z)^{\pm1}e^{K_{r,L}}.
 \tag{13}
\]
It is a small operator-norm perturbation of the nonzero scalar
\(1-\alpha^{\pm1}\). Its inverse likewise converges by a Neumann
series and preserves the whole period quotient. All monomial
factors are products of scalar meridian units, exponentials of
bounded primitives, and full-polydisk spectral exponentials.
Their inverses are bounded for the same reason.

This proves that all the factors apart from the displayed
\(D_L+r zI\) in (8) are actual quotient units. It proves no inverse
for \(D_L+r zI\) itself. In particular a zero of \(L\cdot\theta\)
inside the spectral polydisk is not deleted.

The action \(\widehat M^{\,v}\) is also defined with its full
history on the actual entire-clock family. If
\(|F|\le M e^{C\|\nu\|_1}\) along the path, its primitive series gives
\[
 |\widehat M^{\,v}F|
       \le M\exp\!\left((C+|z|L_0\|v\|_\infty)\|\nu\|_1\right).
 \tag{14}
\]
We used \(\|I^nF\|\le L_0^n\|F\|/n!\) and the exponential's
additional \(1/n!\). Thus this action has an actual bounded
exterior density after increasing \(R_0\). For finitely many
steps, choose this radius first and then shrink \(z\) in (11).
The radius remains independent of the clock values.

For precision about external shifts, [E] proves the original row
\(\mathsf T\mathscr W=Q^{c/2}\mathcal R(Y,\mathsf E)\mathscr W\).
Its finite iterates are
\[
 \mathsf T^j\mathscr W=C_j(Q,Y,\mathsf E)\mathscr W,\qquad
 C_j=
 \begin{cases}
 Q^{jc/2}\prod_{r=0}^{j-1}\mathcal R(Q^rY,X),&j>0,\\
 1,&j=0,\\
 Q^{jc/2}\prod_{r=j}^{-1}\mathcal R(Q^rY,X)^{-1},&j<0.
 \end{cases}
 \tag{15}
\]
These identities keep \(h,m\) fixed. Since \(\mathsf T\) commutes
with \(M^v\), while
\(M^v a(\mathsf E)=a(Q^v\mathsf E)M^v\), the mixed action is
\[
           \mathsf T^jM^v\mathscr W
                 =C_j(Q,Y,Q^v\mathsf E)M^v\mathscr W .
 \tag{16}
\]
Every coefficient in (15)--(16) is holomorphic near
\(Q=1,Y=\alpha,X=\mathbf1\), with no denominator zero on a
slightly larger full spectral polydisk for small \(z\).
Replacing \(Q\) by \(e^{z^2I}\) and \(X^L\) by \(e^{zD_L}\)
gives a normally convergent bounded operator there. This can be
seen either factor by factor from (13), or by its convergent
analytic Taylor series in the commuting operators.
It gives the actual Borel continuation of (16), as in [E];
no exponential of the external differential generator on arbitrary
functions has been assumed.

Consequently every term of (9) is jointly holomorphic on the
smaller actual source chart. The unnormalized identity continues
there from the original germ. For \(z\ne0\) division by its common
scalar is legitimate, and holomorphy extends (9) through \(z=0\).
This proves the exact analytic normalized system for each fixed
finite collection of lattice and external shifts.

## 4. The explicit leading projective equations

For \(\theta\in\mathbb C^d\), write \(n(\theta),o(\theta)\), and
\(M(\theta)=n(\theta)+o(\theta)\) for the crossing linear forms.
Define homogeneous polynomials of degree \(d_v\):
\[
\begin{split}
 A_v(\theta)&=\prod_c
 M_c(\theta)^{(\delta_{M,c})_+}
 n_c(\theta)^{(-\delta_{n,c})_+}
 o_c(\theta)^{(-\delta_{o,c})_+},\\
 B_v(\theta)&=\prod_c
 M_c(\theta)^{(-\delta_{M,c})_+}
 n_c(\theta)^{(\delta_{n,c})_+}
 o_c(\theta)^{(\delta_{o,c})_+}.
\end{split}
 \tag{17}
\]
These polynomial products do not involve quotients at their zeros.
Put
\[
 \rho_v(Y)=Y^{H(v)/2}
     (1-Y^{-1})^{\sum_+\delta_n}
     (1-Y)^{\sum_-\delta_n},\qquad
             \Phi_v(\theta)=B_v(\theta)-\rho_v(\alpha)A_v(\theta).
 \tag{18}
\]
The scalar \(\rho_v(\alpha)\) is nonzero. Negative integer
exponents in this scalar cause no problem at \(\alpha\ne0,1\).

At \(z=0\), each retained factor \(D_L+r zI\) becomes \(D_L\),
each \(\psi\) becomes one, and all external and \(M^v\) actions
in (16) become the identity. The ratio of the remaining scalar
coefficient units is exactly (18). To check it directly from [R],
the positive color ratio at \(Q=1,X=\mathbf1\) is
\((1-Y^{-1})^{\delta_n}\), and the negative ratio is
\((1-Y)^{\delta_n}\), for every \(j\); its start changes cancel.
The monomial ratio is \(Y^{H(v)/2}\). Thus, after division by a
nonzero scalar, the leading equation of (9) is
\[
                         \Phi_v(\partial_\nu)F(0,\eta,\nu)=0.
 \tag{19}
\]
The external shift does not supply an extra leading transverse
equation in this normalization.

The actual initial family [A] is
\[
 F(0,\eta,\nu)=\frac r{w(\eta)}
                     e^{a(\eta)\mu\cdot\nu},\qquad
 w^2=1-4\sigma\eta,\quad
 a=\frac{1-w}{2\sigma},\qquad r\sigma\ne0,\quad\mu\ne0.
 \tag{20}
\]
Choose any sufficiently small nonzero \(\eta\); then \(a\ne0\)
and \(w\ne0\). Homogeneity in (19) proves
\[
                           \boxed{\Phi_v(\mu)=0.}
 \tag{21}
\]
Thus the direction \([\mu]\) belongs to the actual projective
ideal generated by these leading rows, not to an independently
chosen saddle system.

For \(v\ne0\), \(d_v>0\). Indeed if it were zero, all
\(\delta_n,\delta_o\) would vanish. Following the physical component
from the zero cut, the linear matching equations then force every
occupation variation to vanish: underpasses add \(\delta_n=0\)
and overpasses exit with \(\delta_o=0\). The integral lattice
coordinates are a basis of these matching data, so \(v=0\).
For \(v=0\) the leading polynomial is zero and gives no constraint,
consistently with (19).

If an actual forced face satisfies \(L(k)=0\) on the support,
its exact equation \((\mathsf E^L-1)\mathscr W=0\) remains.
The same scalar normalization gives \(D_LF(0,\eta,\nu)=0\),
and hence \(L(\mu)=0\). These linear rows must be retained
together with (21).

## 5. What is and is not established about the Jacobian

There is an explicit zero-safe differential of every row in (18).
For a monomial product \(G(\theta)=\prod_i L_i(\theta)^{e_i}\),
\[
 dG_\mu(\xi)=
   \sum_{i:e_i>0}e_i L_i(\xi)L_i(\mu)^{e_i-1}
                       \prod_{t\ne i}L_t(\mu)^{e_t}.
 \tag{22}
\]
Use this separately for \(B_v\) and \(A_v\). Formula (22) makes
no division by an occupation, transfer, or total-input coordinate.
It shows exactly why a rank conclusion needs more information:
if each monomial in a row has at least two vanishing factors,
counted with multiplicity, its entire first differential is zero.
A common vanishing factor can also remove the differential when
the residual row vanishes at that point.

The simple determinant zero of the classical cut matrix gives a
corank-one matrix \(K=I-L_\beta T_0\) and a rank-one residue of
its inverse. That fact underlies the actual vector \(\mu\) in
(20). It does not, without an additional descent argument,
identify the scheme of the unreduced equations (18) with the
matrix kernel-pair equations, or prove that their differentials
and forced-face rows span the projective conormal at \([\mu]\).
No such identification is used in this proof.

The result is therefore the exact normalized analytic system,
its bounded quotient units, and its actual leading projective
direction. All derivative factors and boundary data survive.
It is not a criterion asserting an unproved full-rank hypothesis,
nor a claim that zeros of those derivative symbols can be canceled.
Moving marked minors, finite-meridian clock characters, and the
physical scalar remain beyond the statement.

## 6. Complete proof directs

| Label | Complete proof source | SHA256 |
|---|---|---|
| R | notes/research_actual_unreduced_boundary_exact_clock_ratios.md | 32ab75fa662dfb0afab9f3ced8e94a01dcc72e43f3bb17fadc7684eaeedab534 |
| E | notes/research_actual_quantum_meridian_clock_connection.md | 883a4526e8db3e666f8f962b8eb5311700afbc7813b1b74b16be03bcdac3e865 |
| A | notes/research_full_clock_outer_borel_continuation.md | 8bec9e7934ba671d3dee836cb32dde3870113ed3e95348a83c39ac9e33b611f0 |

R supplies the actual unreduced boundary-exact ratios and completion.
E supplies the full-polydisk period quotient and original external
connection. A supplies the actual continued entire-clock source
and exceptional family. The scalar balance, normalized factors,
finite-path bounds, mixed-shift adapter, and leading polynomial
membership are proved above.

Only written mathematics, text reads and hash checks were used.
Frozen notes and public manuscripts are unchanged.
