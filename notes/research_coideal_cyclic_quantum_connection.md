# A cyclic quantum connection for the actual marked overlap

24 November 2026. Written research proof.

The opposed marked overlap satisfies an exact first-order equation
on its finite coideal clock. The equation has determinant four and a
polynomially bounded inverse. Its homogeneous second-order equation
has one normalized cyclotomic source line, without inverting the level.
Thus this particular local scalar can be computed by a conditioned
quadratic residual problem.

The same displayed coefficients select a unique rational solution of
the unreduced cyclic equation. It is invariant under the actual
two-sheeted height map. On each compact set outside the limiting
height cut, this specified representative converges holomorphically
to an explicit nonzero rational function. The result does not identify
it with a moving-color period or authorize crossing its extra poles.

## 1. Actual scalar and finite clock

Keep [G]'s complete conventions:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \delta=\pi/N,\quad \theta=\delta/2,\quad
 \kappa=q^{d^2/2}.
 \tag{1}
\]
The half-powers use the displayed exponential branch.
The coideal roots are
\(\mu_l=Q^l+qQ^{-l}\), \(0\le l<N\).
For the original marked row \(r_l\), actual crossing matrices
\(B^\pm\), and \(s_l=B^+e_*\), [G] retains the scalar
\[
 \gamma_l=r_lB^-e_*=r_l\overline{s_l},\qquad
 G_l=\kappa\gamma_l .
 \tag{2}
\]
The corresponding boundary coefficient is
\(\beta_N\gamma_l\), with
\[
 \beta_N=\frac{T_*}{A_c}\frac{\kappa(1-q)}2,\qquad
 |\beta_N|=\frac1{N^2\sin3\theta}.
 \tag{3}
\]
Any original exterior factor \(\chi_N\) remains a further factor.
The variable introduced below is an auxiliary height clock, not
a knot peripheral eigenvalue.

The exact tail formula of [G] is
\[
 U_t=\prod_{j=1}^t\frac{1-Q^{-j}}{1-q^{2j-1}},\quad
 W_t=|U_t|^2,\quad
 V_l=\frac2{U_l(1-q^{2l-1})},\quad
 E_t=q^{2t^2-t},
\]
\[
 H_l=\sum_{t=l}^{d}(E_t-E_{t+1})W_t,\qquad
 G_l=\frac{|V_l|^2}{2}E_l^{-1}H_l,\qquad E_N=-1 .
 \tag{4}
\]
In particular \(H_N=0\); it is not a periodic tail value.
No positive interpolation of these scalars is assumed.

Use the finite clock ring
\[
 \mathcal O=\mathbb Z[q,1/2]\subset\mathbb C,\qquad
 R_N=\mathcal O[z]/(z^N-1),\qquad
 (Sf)(z)=f(Qz).
 \tag{5}
\]
Here \(z\) is a unit and \(S^N=I\). This ring is free of rank
\(N\) over the characteristic-zero domain \(\mathcal O\).
Counting norms below mean the Euclidean norm of the values at
\(z=Q^l\). The shift is a unitary permutation in that norm.

Put
\[
 a(z)=(q-z)^2,\quad b(z)=z^2(1-Qz)^2,\quad
 h(z)=-2qz(1-qz^2),
\]
\[
 \mathcal A=M_a-M_bS,\qquad
 \mathcal B=M_{1-qz^2}S-QM_{1-qQ^2z^2}.
 \tag{6}
\]
The notation \(M_f\) means multiplication by \(f\); coefficients
in (6) are on the left of the shift.

## 2. The source equation, including its last row

The tails obey
\[
 H_l=(E_l-E_{l+1})W_l+H_{l+1}.
\]
Use
\[
 \frac{E_{l+1}}{E_l}=qQ^{2l},\quad
 \frac{W_{l+1}}{W_l}
       =\frac{\sin^2((l+1)\delta)}
                    {\sin^2((l+\tfrac12)\delta)},\quad
 |V_l|^2W_l=\frac1{\sin^2((l-\tfrac12)\delta)}.
 \tag{7}
\]
Substitution into (4) gives, for \(0\le l<d\),
\[
 2\sin^2((l-\tfrac12)\delta)G_l
 -2qQ^{2l}\sin^2((l+1)\delta)G_{l+1}
                                      =1-qQ^{2l}.
 \tag{8}
\]
At \(l=d\) the second coefficient is zero. The same equation
holds with the cyclic convention \(G_N=G_0\), since it multiplies
that value by zero. Its last row is exactly
\[
                         G_d=\frac2{1-q^3}.
 \tag{9}
\]
Thus no tail endpoint was replaced by a periodic boundary condition.
Writing \(z=Q^l\) in (8) and clearing its nonzero sine denominator
proves the actual clock equation
\[
 \boxed{\qquad \mathcal A G=h\quad\hbox{in }R_N\otimes\mathbb C.\qquad}
 \tag{10}
\]
The coefficients have bounded degree independently of \(N\).
Their values at small levels are interpreted in the quotient ring;
no assumption \(N>4\) is made.

## 3. Integral inverse and the normalized source line

There are exact geometric-series identities in \(R_N\):
\[
 (q-z)^{-1}
   =-\frac12\sum_{j=0}^{N-1}q^{N-1-j}z^j,\qquad
 (1-qz^2)^{-1}=\frac12\sum_{j=0}^{N-1}(qz^2)^j.
 \tag{11}
\]
Indeed their products with the respective factors are
\(-\tfrac12(q^N-z^N)=1\) and
\(\tfrac12(1-q^Nz^{2N})=1\).
Consequently \(a\) and \(h\) are units of this ring.
Only the factor two has been inverted.

Let \(\mathcal T=M_{a^{-1}b}S\). The full orbit product is
\[
 \mathcal T^N=
 M_{\prod_{j=0}^{N-1}b(Q^jz)/a(Q^jz)}=0 .
 \tag{12}
\]
Its numerator contains
\(\prod_j(1-Q^{j+1}z)^2=(1-z^N)^2=0\);
its denominator is a unit by (11). Therefore
\[
 \mathcal A^{-1}
       =\left(\sum_{j=0}^{N-1}\mathcal T^j\right)M_{a^{-1}}
                                      \quad\hbox{over }\mathcal O.
 \tag{13}
\]
It follows that the vector in (10) is the specialization of the
distinguished integral vector
\[
                           G_N=\mathcal A^{-1}h\in R_N .
 \tag{14}
\]
The equality with the actual values (2) follows from (10) and
uniqueness. It is not an integrality assertion for the separate
factors \(\gamma_l,\beta_N,\chi_N\).

The exact counting-matrix determinant is
\[
                              \det\mathcal A=4 .
 \tag{15}
\]
For example over \(\mathbb C\), evaluate at the roots \(Q^l\).
The cyclic matrix has determinant
\(\prod_l a(Q^l)-\prod_l b(Q^l)=(-2)^2-0=4\).
This also proves the integral identity, since \(\mathcal O\)
embeds in \(\mathbb C\). Equivalently (12) gives
\(\det(I-\mathcal T)=1\), while the multiplication norm of \(a\)
is four. Domain and codomain use the same basis, so the Fourier
change to root values contributes no determinant normalization.

The forcing is annihilated by the displayed operator:
\[
 \mathcal B h=0,\qquad
 \mathcal B(hu)=k(z)(Su-u),\quad
                  k(z)=(1-qz^2)h(Qz)\in R_N^\times .
 \tag{16}
\]
For \(u=\sum_{j=0}^{N-1}u_jz^j\), the equation \(Su=u\) says
\((Q^j-1)u_j=0\).
For \(1\le j<N\) this coefficient is nonzero in the domain
\(\mathcal O\), so \(u_j=0\). Hence
\[
 \ker(S-I)=\mathcal O,\quad
 \ker\mathcal B=\mathcal O h,\quad
 \boxed{\qquad\ker(\mathcal B\mathcal A)=\mathcal O G_N.\qquad}
 \tag{17}
\]
Multiplication by \(h^{-1}\) followed by \(\mathcal A\) is an
\(\mathcal O\)-linear automorphism sending \(G_N\) to \(1\).
Thus this is a primitive free source line, normalized by (10).
It does not say that \(G_N\) is a multiplicative unit.
Nor is (17) asserted after arbitrary base change: torsion can
make some \(Q^j-1\) vanish or become a zero divisor.

## 4. Polynomial inverse and a quadratic residual certificate

On the counting grid every \(a(Q^l)\) is nonzero, and
\[
 |a(Q^l)|=4\sin^2((l-\tfrac12)\delta)\ge4/N^2.
 \tag{18}
\]
A nonzero product of successive absolute transfer coefficients
from \(l\) to \(k\), \(l\le k\le d\), is exactly
\[
 \prod_{j=l}^{k-1}\left|\frac{b(Q^j)}{a(Q^j)}\right|
  =\frac{W_k}{W_l}\,
       \frac{\sin^2((k-\tfrac12)\delta)}
            {\sin^2((l-\tfrac12)\delta)}
                                      \le CN^3 .
 \tag{19}
\]
Here [G] gives \(1\le W_t\le CN\), and the smallest sine
has magnitude at least \(1/N\).
A product that reaches the last row is zero before it wraps.
Since each \(\mathcal T^j\) is a diagonal times a permutation,
(18)--(19) prove
\[
 \left\|(I-\mathcal T)^{-1}\right\|_2\le CN^4,\qquad
                         \|\mathcal A^{-1}\|_2\le CN^6 .
 \tag{20}
\]
These bounds include both parities and \(N=2\).
They are estimates for the actual source equation, not for an
unspecified annihilator with the same classical zero set.

For any trial clock vector \(g\) one obtains
\[
 \boxed{\quad
 \|g-G_N\|_2\le CN^6\|\mathcal A g-h\|_2 .
 \quad}
 \tag{21}
\]
The residual energy is quadratic in the \(N\) coordinates of \(g\).
Thus this local scalar has a known fixed-degree replacement with
a quantitative error certificate. It does not replace an entire
short component by an \(N\)-dimensional compiler, or bound the
residual of an unconstructed geometric trial field.

For reference the homogeneous operator in (17), before taking
the root quotient, has the commuting classical symbol
\[
 (1-z)^2(1-z^2)(L-1)(1-z^2L).
 \tag{22}
\]
On \(z\ne\pm1\), removing its displayed coefficient factors gives
the two shift branches \(L=1\) and \(L=z^{-2}\).
Those factors and their source/cut normal data remain in the exact state.
This is an auxiliary height equation. It is not identified with
the knot's peripheral curve or its geometric component.

## 5. A rigid rational lift of the displayed equation

The finite root values do not alone determine an off-grid function.
We now specify a lift by requiring the very same coefficients
to satisfy an unreduced rational equation:
\[
 (q-z)^2\mathscr G_N(z)
      -z^2(1-Qz)^2\mathscr G_N(Qz)
                              =-2qz(1-qz^2)
                              \quad\hbox{in }\mathbb C(z).
 \tag{23}
\]
This requirement, rather than positivity or interpolation from
a real asymptotic, selects the following representative.

Set \(Z=z^N\) and regard \(1,z,\ldots,z^{N-1}\) as a basis over
\(\mathbb C(Z)\). The shift \(S\) fixes \(Z\).
The matrix of (23) has polynomial entries in \(Z\), with determinant
\[
 \mathfrak D(Z)=(1+Z)^2-Z^2(1-Z)^2
                  =(1+Z^2)(1+2Z-Z^2).
 \tag{24}
\]
To see the determinant, extend to a field in which \(z^N=Z\)
splits, and evaluate on the orbit \(Q^jz\). The products of the
diagonal and cyclic coefficients are
\[
 \prod_j(q-Q^jz)^2=(1+Z)^2,\qquad
 \prod_j(Q^jz)^2(1-Q^{j+1}z)^2=Z^2(1-Z)^2.
 \tag{25}
\]
The determinant of a diagonal minus a single cyclic shift is
their difference. This proves (24) over the original field.
It also applies at \(N=2\), where the two off-diagonal entries
are the two directions of that cycle.

Since \(\mathfrak D\) is not the zero polynomial, (23) has one
and only one rational solution. Adjugate inversion shows that it
can be written with denominator \(\mathfrak D(z^N)\); no extra
poles at \(q-Q^jz=0\) are introduced by a partial division.
In particular \(\mathfrak D(1)=4\), and reduction of (23) modulo
\(z^N-1\) is legitimate. By (13),
\[
                         \mathscr G_N(Q^l)=G_l .
 \tag{26}
\]
The apparent transfer singularity at \(Z=-1\) is removable in
this cyclic solution, since \(\mathfrak D(-1)=-4\).

## 6. Exact height descent and its poles

The involution of the physical height map is
\[
                   \iota(z)=q/z,\qquad \rho=z+q/z.
 \tag{27}
\]
It preserves the solution of (23). Here is the coefficient check.
Put \(v=q^{-1}/z\) and \(k_0=-q^2z^4\). Direct multiplication gives
\[
 k_0a(v)=-b(z),\qquad
 k_0b(v)=-a(z),\qquad k_0h(v)=h(z).
 \tag{28}
\]
The equation at \(v\), multiplied by \(k_0\), is therefore
the same equation for \(z\mapsto\mathscr G_N(q/z)\), because
\(Qv=q/z\) and \(q/(Qz)=v\).
Rational uniqueness proves
\[
 \mathscr G_N(z)=\mathscr G_N(q/z)
                         =\widehat G_N(\rho).
 \tag{29}
\]
The fixed field is \(\mathbb C(\rho)\): \(z\) satisfies
\(z^2-\rho z+q=0\), and any rational function reduces to a sum
of a rational function of \(\rho\) and \(z\) times another one.
Invariance kills the latter coefficient.

The only possible finite poles of \(\widehat G_N\) are
\[
                   p_N(\rho)=2,\quad 2i,\quad -2i .
 \tag{30}
\]
Indeed \(p_N(z+q/z)=Z-Z^{-1}\).
The roots \(Z=\pm i\) of the first factor in (24) give
\(p_N=\pm2i\); the roots \(Z=1\pm\sqrt2\) of the second
give \(p_N=2\). Some of these possible poles may be removable;
none is added by this statement. At finite \(\rho\) its two
preimages \(z\) are nonzero, so the list is exhaustive.

At \(z=0\), (24) is nonzero and (23) gives
\[
 \mathscr G_N(z)=-2q^{-1}z+O(z^2),\qquad
                    \widehat G_N(\rho)=-2/\rho+O(\rho^{-2})
                    \quad(\rho\longrightarrow\infty).
 \tag{31}
\]
Thus the normalization at infinity is fixed, not an unknown
scalar multiple of a homogeneous branch.

Equation (26) is an exact source statement. In particular,
on an actual finite tail coideal with these simple eigenvalues,
rational functional calculus in (29) is defined, since \(p_N=0\)
on its spectrum. It gives exactly this original block-diagonal tail
coefficient with values \(\kappa\gamma_l\), on its full multiplicity spaces.
No commutation with an arbitrary crossing is asserted.
This does not replace the original repeated-root Casimir algebra
by its values: its first-normal directions remain in those full
physical multiplicities, as in the inputs.

## 7. A holomorphic off-cut limit with no exponential loss

Let
\[
                 \Omega=\mathbb C\setminus[-2,2].
 \tag{32}
\]
For every compact \(K\subset\Omega\), the function \(\widehat G_N\)
is holomorphic and nonzero on a buffered neighborhood of \(K\)
for all sufficiently large \(N\), depending on \(K\), and
\[
 \boxed{\qquad
 \widehat G_N(\rho)=\frac2{2-\rho}+O_K(N^{-1})
                       \quad\hbox{locally uniformly on }\Omega .
 \qquad}
 \tag{33}
\]
Its fixed-order holomorphic derivatives have the same local
error bound after enlarging the compact set.

We prove the assertion without continuation of the real-grid
asymptotic in [G]. Fix \(0<r<1\) and rewrite (23) as
\[
 \mathscr G_N(z)=\alpha_N(z)
                      +\tau_N(z)\mathscr G_N(Qz),
\]
\[
 \alpha_N(z)=\frac{-2qz(1-qz^2)}{(q-z)^2},\qquad
 \tau_N(z)=\frac{z^2(1-Qz)^2}{(q-z)^2}.
 \tag{34}
\]
Uniformly on \(|z|\le r\),
\[
 \tau_N(z)=z^2+O_r(N^{-1}),\qquad
              \sup_{|z|\le r}|\tau_N(z)|\le r_*^2<1
 \tag{35}
\]
eventually, for some fixed \(r<r_*<1\).
The shift preserves that disk. Iterating around its finite
orbit proves that the inverse of \(I-M_{\tau_N}S\) is bounded
there by \(1/(1-r_*^2)\).
Alternatively this is its convergent geometric series on
bounded holomorphic functions.

There are no poles of \(\mathscr G_N\) on this fixed disk
eventually: every nonzero root of \(\mathfrak D(z^N)\) has
modulus \(|Z_0|^{1/N}\longrightarrow1\).
Put
\[
                         g(z)=\frac{-2z}{(1-z)^2}.
 \tag{36}
\]
At \(q=1\) it solves \(g(z)-z^2g(z)=\alpha_\infty(z)\).
Direct substitution, with \(Qz=z+O_r(1/N)\), gives
\[
 \sup_{|z|\le r}
   |g(z)-\tau_N(z)g(Qz)-\alpha_N(z)|=O_r(N^{-1}).
 \tag{37}
\]
The inverse just proved therefore yields
\[
                    \mathscr G_N(z)=g(z)+O_r(N^{-1})
                         \quad(|z|\le r).
 \tag{38}
\]

For a buffered compact \(K\subset\Omega\), the equation
\(z^2-\rho z+q=0\) has a unique root \(z_N(\rho)\) of modulus
less than one eventually. It is holomorphic near \(K\), with
\[
                    0<a_K\le|z_N(\rho)|\le r_K<1 .
 \tag{39}
\]
To check this, at \(q=1\) these are the usual two reciprocal
roots off the segment. A unit-modulus root at general \(q\)
would place \(\rho\) on \(\sqrt q[-2,2]\). This moving segment
stays a positive distance from \(K\) eventually. Compactness
and the product of the roots, \(q\), then prove (39).
The branch is the one with \(z_N\sim q/\rho\) at infinity.
Use (29),(38) and
\(\rho-(z_N+z_N^{-1})=(q-1)/z_N=O_K(1/N)\).
The identity \(g(z)=2/(2-z-z^{-1})\) proves (33).
Its limit is bounded away from zero on the enlarged compact,
proving the asserted eventual zero-free neighborhood.
Cauchy's formula proves the derivative assertion.

Consequently the specified original-boundary representative obeys
\[
 \frac{c_K}{N}\le
       |\beta_N\bar\kappa\,\widehat G_N(\rho)|
       \le\frac{C_K}{N}\qquad(\rho\in K)
 \tag{40}
\]
eventually. The factor \(\chi_N\), if present, is still separate.
No single threshold making (33) pole-free on all of
the unbounded domain \(\Omega\) is asserted.

## 8. What is and is not selected

The lift (23) is fixed by an explicit source-derived coefficient
equation and cyclic consistency. It agrees with the whole finite
scalar operator and supplies a nonzero complex-height representative
on every fixed off-cut compact. It is not the assertion that the
degree-\(<N\) polynomial interpolant has the same off-grid bound.
Those are different representatives of the same finite clock class.

The possible poles (30) accumulate at the limiting cut. A contour
deformation crossing them must keep its residue terms. Nor does
the grid congruence identify this rational lift with an independently
defined color-deformed source, its meridian derivatives, or a moving
quantum-parameter family. Such an identification requires its actual
intertwiners and source comparison. No arbitrary complex continuation
has been inferred from the real asymptotic.

[W] already proves whole-source clock recovery, cleared equations
and the distinction between abstract normal fibers and value fibers.
[C] already gives explicit cyclic scalar connections, source lattices
and resonant flags with their actual caps. No novelty for quantum
connections, finite geometric inverses or cyclic period methods is
claimed. The additions are this overlap's normalized rank-one
cyclotomic source, exact determinant and inverse bounds, and the
specified rational height representative with its quantitative
off-cut asymptotic.

The missing global quantity remains the original coherent scalar
after an arbitrary fixed short partial filling. This note does not
construct its geometric trial field, select its contour, identify
the auxiliary symbol with a knot peripheral curve, or prove the
finite-exception volume theorem.

## Complete inputs and closest coverage

| Label | Complete text | Lines | SHA256 |
| --- | --- | ---: | --- |
| G | [Actual opposed marked overlap](research_coideal_opposed_marked_mode_overlap.md) | 639 | 4b599b4a8d8fcd7b17de406509276014d03b7fd4003fa728899ce246c08b7c87 |
| W | [Whole-source Newton transport](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/whole_source_newton_transport.md) | 523 | 82ae351b9e9418a8ce733958009a1af80fc9902e1abc2e510ab36f9babbed90f |
| C | [Cyclic source connection and resonant flags](https://github.com/sashakolpakov/murakamis_dream/blob/19d5b911bc409486f0e72b51a876a6a2bc70ee02/notes/cyclic_source_connection_and_resonant_flags.md) | 401 | cdb07713bec8bd0b45b1a36a9676d2f1bb890b842c7d85d947cfa7e978c2d7b3 |

Only written mathematics, source reads and text/hash operations were used.
Earlier final notes, the ledger and public manuscripts are unchanged.
