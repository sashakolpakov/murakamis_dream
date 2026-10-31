# The boundary term and repeated monodromy sector of the Mellin equation

31 October 2026.

The Fourier--Mellin construction packages the ordinary color invariants
of a knot into a generating function. Its equation has a nonzero
inhomogeneous term, determined by finitely many starting colors. That
term is essential: after converting the equation to a homogeneous
companion system, it provides a linear functional that detects the
selected solution.

For a knot with positive exponential growth of its Kashaev invariant,
this homogeneous companion necessarily has at least two independent
rational directions fixed by root monodromy. Thus a simple monodromy
eigenvalue is not the reason its actual solution is selected. The
selection also uses the prescribed source and the allowed expansion
at the origin. The proof below keeps those data and explains why the
Mellin and main-meridian realizations cannot be identified by merely
renaming their variables.

## 1. The meridian equation and its ordinary colors

Work over $\mathbb C(q)$ and set $Q=q^2$. The meridian multiplication
operator $Y$ and shift $T$ satisfy

\[
 TY=QYT.
 \tag{1}
\]

At level $N\ge2$, put $q_N=e^{\pi i/N}$ and $Q_N=q_N^2$. The
marked meridian eigenvalue is $M=-q_Nx$, where $x$ is the exponential
unrolled color parameter, and $Y=M^2$. Write $f_N(Y)$ for the actual
reduced, zero-framed ADO state. Its fixed normalization is

\[
 f_N(1)=K_N,\qquad f_N(Q_N^r)=C_r(q_N)\quad(1\le r\le N),
 \qquad C_1(q)=1.
 \tag{2}
\]

Here $K_N$ is the reduced Kashaev invariant, and $C_r(q)$ is the
reduced ordinary invariant in dimension $r$. The equality at $r=N$
means $C_N(q_N)=K_N$. These are the
[actual color specializations](root_orbit_pointing.md), with the
[squared-meridian convention](even_meridian_norm_descent.md) retained.

Choose a specified all-level annihilator, whose existence follows
from the [finite cut-state construction](finite_sum_annihilator.md).
After clearing its coefficient denominators and shifting its order
once, write it as

\[
 P=\sum_{j=0}^{d}a_j(q,Y)T^j,\qquad
 a_j\in\mathbb C[q^{\pm1},Y^{\pm1}],\qquad
 d\ge1,\quad a_0a_d\ne0.
 \tag{3}
\]

Its root equation holds at all sufficiently large levels. Keeping
$\mathbb C(q)$ as the coefficient field avoids assuming that a chosen
operator descends in its coefficients to $\mathbb C(Q)$.

For every fixed positive integer $n$, apply its root equation at
$Y=Q_N^n$, taking $N>n+d$. Equation (2) gives a relation among fixed
ordinary colors at infinitely many distinct $q_N$. Since those colors
are Laurent polynomials, rational-function rigidity proves

\[
 \sum_{j=0}^{d}a_j(q,Q^n)C_{n+j}(q)=0
 \qquad(n\ge1).
 \tag{4}
\]

This is the color recurrence used below. Its coefficients, ordering,
and initial colors are those of the specified knot equation.

## 2. Starting the generating series creates a nonzero source

Let $A_q$ be the difference between the largest and smallest
$q$ exponents in the collected Laurent monomials of $a_d(q,Y)$.
Choose a fixed starting color

\[
 n_0\ge d+A_q+1,
 \qquad Z(q,X)=\sum_{n\ge n_0}C_n(q)X^n.
 \tag{5}
\]

The series is initially formal at $X=0$. No convergence for generic
$q$ is assumed. The choice of $n_0$ makes every substitution
$a_d(q,Q^r)$ with $r\ge n_0-d$ nonzero. Indeed, distinct monomials
$q^uY^v$ become $q^{u+2rv}$; a collision with different $v$ would
require $2r\le A_q$. Monomials with the same $v$ were already
collected.

Let $S_Xg(X)=g(QX)$. The exact quantum-torus Fourier map is

\[
 \Phi(Y)=S_X,\qquad \Phi(T)=X^{-1},\qquad
 X^{-1}S_X=QS_XX^{-1}.
 \tag{6}
\]

Write $a_j(q,Y)=\sum_m a_{jm}(q)Y^m$. Its ordered action on (5) is

\[
 A:=\Phi(P)=\sum_{j,m}a_{jm}(q)Q^{-mj}X^{-j}S_X^m,
 \qquad AZ=\mathcal B,
 \tag{7}
\]

where

\[
 \mathcal B(q,X)=
 \sum_{j,m}a_{jm}(q)Q^{-mj}X^{-j}
       \sum_{r=n_0}^{n_0+j-1}C_r(q)Q^{mr}X^r.
 \tag{8}
\]

To obtain (8), multiply (4) by $X^n$ and sum over $n\ge n_0$.
For a term with shift $j$, the substitution $r=n+j$ leaves out
exactly the colors $n_0,\ldots,n_0+j-1$. Those omitted terms are
the inner sum in (8); it is empty for $j=0$. The factor $Q^{-mj}$
comes from the operator ordering in (6).

The source is a Laurent polynomial in $X$, supported between
$n_0-d$ and $n_0-1$. Its least coefficient is

\[
 [X^{n_0-d}]\mathcal B
       =C_{n_0}(q)a_d(q,Q^{n_0-d})\ne0.
 \tag{9}
\]

Only $j=d$ contributes to this coefficient. The second factor is
nonzero by the monomial argument above, and $C_{n_0}(1)=1$ makes
the first nonzero as well. Thus this finite-start construction has a
nonzero source. Its least coefficient
is a fixed nonzero rational function of $q$, so its specialization
is nonzero at all but finitely many $q_N$.

The source equation also determines the actual series uniquely in
the prescribed space $X^{n_0}\mathbb C(q)[[X]]$. If a nonzero
homogeneous difference had least exponent $r\ge n_0$, its image
under $A$ would have a nonzero coefficient at $X^{r-d}$, namely
$a_d(q,Q^{r-d})$ times that least coefficient. This is impossible.
This is the [finite-start source construction](fourier_mellin_actual_source.md);
it is stronger than choosing any rational solution of its root
specialization.

## 3. Root rationality and the finite Fourier comparison

The [actual root color-periodicity theorem](cyclotomic_mellin_residue.md)
gives $C_{n+N}(q_N)=C_n(q_N)$ for all $n\ge1$, including the
multiples of $N$. Consequently, for $N\ge n_0$,

\[
 Z_N(X):=Z(q_N,X)
 =\frac{\displaystyle\sum_{r=1}^{N-1}C_r(q_N)X^r+K_NX^N}
        {1-X^N}
   -p_N^{\mathrm{pre}}(X),\qquad
 p_N^{\mathrm{pre}}(X)=\sum_{r=1}^{n_0-1}C_r(q_N)X^r.
 \tag{10}
\]

This is the rational function with the same formal expansion at zero.
Where the fixed operator specializes regularly, it satisfies
$A_NZ_N=\mathcal B_N$ as a rational identity. It has at most simple
poles at the $N$th roots of unity, and its residue retains the
original scalar:

\[
 \operatorname{Res}_{X=\infty}Z_N(X)\frac{dX}{X}=K_N.
 \tag{11}
\]

Indeed the fraction in (10) tends to $-K_N$ at infinity, while
$p_N^{\mathrm{pre}}$ has no constant term. The full modified ADO value remains
$i^{N+3}K_N/N$ at completeness; (11) does not replace its whole
meridian normalization by a different one.

The central coordinates explain the limit of this Fourier
comparison. At a primitive level-$N$ root, write

\[
 U=Y^N,\quad V=T^N,\qquad
 U_X=X^N,\quad V_X=S_X^N.
 \tag{12}
\]

The algebra map (6) sends them to

\[
 \Phi(U)=V_X,\qquad \Phi(V)=U_X^{-1}.
 \tag{13}
\]

In the rational main-meridian realization, $T$ acts by the root
shift of $Y$, so $V=1$ and $U$ varies. Its Fourier image is
therefore supported on $U_X=1$, with $V_X$ variable. In the rational
Mellin realization, $S_X$ acts by the root shift of $X$, so instead
$V_X=1$ and $U_X$ varies. In the original coordinates this is
$U=1$, with $V=X^{-N}$ variable. These are two different central
divisors, meeting at $(1,1)$. An isomorphism over a fixed center
cannot equate their distinct annihilator ideals.

At their intersection there is a genuine finite Fourier map. Its
domain is the orbit ring $\mathbb C[Y^{\pm1}]/(Y^N-1)$, equivalently
the functions on the $N$ meridian root points. A rational function
may be used only when it is regular at those points; the actual
$f_N$ is Laurent polynomial and meets this condition. Put

\[
 \mathscr F_N(h)=\sum_{r=0}^{N-1}h(Q_N^r)X^r
       \quad\text{in }\mathbb C[X]/(X^N-1).
 \tag{14}
\]

Termwise multiplication and cyclic reindexing prove
$\mathscr F_N(Yh)=S_X\mathscr F_N(h)$ and
$\mathscr F_N(Th)=X^{-1}\mathscr F_N(h)$. For $h=f_N$, this
produces $K_N+\sum_{r=1}^{N-1}C_r(q_N)X^r$. It is precisely the
class of the numerator

\[
 (1-X^N)(Z_N+p_N^{\mathrm{pre}})
       =\sum_{r=1}^{N-1}C_r(q_N)X^r+K_NX^N.
 \tag{15}
\]

modulo $X^N-1$. Thus the finite map compares the meridian orbit
with the Mellin pole numerator. It does not evaluate $Z_N$ at a
pole or identify their meridian neighborhoods. In particular it
does not replace the retained normal coordinate of the
[ramified Weyl fibre](ramified_weyl_fibre.md) by an ordinary orbit
value.

## 4. Why the root clock cannot be lifted as a finite matrix gauge

The distinction persists in the first quantum-normal direction.
Vary the parameter through dual numbers by
$Q=Q_N(1+\epsilon)$, $\epsilon^2=0$; the compatible half-root is
$q=q_N(1+\epsilon/2)$. In the whole quantum torus, (1) implies

\[
 VU=Q^{N^2}UV=(1+N^2\epsilon)UV,
 \qquad [V,U]=N^2\epsilon UV.
 \tag{16}
\]

Suppose a nonzero finite free matrix realization of the intersection
fibre lifted through this parameter change, with both central
actions reducing to identity. It would have
$U=I+\epsilon E$ and $V=I+\epsilon F$, whose commutator is zero
modulo $\epsilon^2$. Equation (16) instead gives
$N^2\epsilon I$, a contradiction in characteristic zero.
For the usual $N$-dimensional clock matrices the same obstruction
follows by taking determinants in $TY=QYT$, which would require
$Q^N=1$ rather than $1+N\epsilon$.

This rules out lifting (14) as an ordinary finite matrix gauge
through the quantum-normal direction. It does not rule out a
comparison with differential normal operators or retained relative
sources. The [first quantum-normal construction](first_quantum_normal_connection.md)
includes a derivation because an off-root shift no longer has
finite order. That derivation and its source cannot be inferred
from the root Fourier matrix alone.

## 5. Positive growth forces two rational companion directions

Assume now that the knot has positive exponential complete growth:

\[
 \liminf_{N\to\infty}\frac1N\log|K_N|>0.
 \tag{17}
\]

This is supplied, for example, by the established
[strict-tree](actual_conway_all_strict_tree_long_twist_volume.md) and
[net-twist](actual_conway_net_twist_volume.md) volume theorems for
their stated knot classes. The next argument only uses (17).

For every coefficient in (3), form the fixed Laurent polynomial
$r_i(q)=a_i(q,q^{-2i})$. If it were nonzero, it would have a finite
vanishing order $\nu_i$ at $q=1$, and hence
$|r_i(q_N)|\ge cN^{-\nu_i}$ for all large $N$. Evaluate the actual
root equation at $Y=Q_N^{-i}$. When $N>d$, its $i$th term is
$r_i(q_N)K_N$ and all other terms are ordinary-color values.
Those values are polynomially bounded in $N$ by the
[positive ordinary-color trace](regularized_kashaev_period.md).
The fixed Laurent coefficients are bounded on the root torus, so
this equation would bound $K_N$ polynomially as well, contradicting
(17). Therefore every $r_i$ is identically zero.

Laurent-polynomial division now gives the exact right factor

\[
 P=B(Y-1),\qquad A=\Phi(B)(S_X-1).
 \tag{18}
\]

Indeed the $i$th coefficient of $B(Y-1)$ is
$b_i(q,Y)(Q^iY-1)$. This is the
[boundary-column argument](peripheral_normal_period.md), applied
here to the positive growth already known. In particular $A(1)=0$.
Any fixed left shift used to give $A$ nonnegative $S_X$ order is
applied to its source as well and preserves this identity.
In that normalization $A$ has positive $S_X$ order. Otherwise it
would be multiplication by a nonzero rational function, which
cannot annihilate $1$.

Retain the canonical homogeneous equation of the sourced Mellin
system:

\[
 \widehat A=(S_X-\sigma(\mathcal B)/\mathcal B)A,
 \qquad \sigma g(X)=g(QX).
 \tag{19}
\]

For every sufficiently large $N$, both $1$ and $Z_N$ are rational
solutions of (19). They are independent over $\mathbb C(X^N)$:
if $Z_N$ were central, then $A_NZ_N=Z_NA_N(1)=0$, contradicting
$\mathcal B_N\ne0$.

This gives two independent vectors in the monodromy eigenspace,
not merely two scalar formulas. Let $\mathsf C_N$ be the forward solution
companion of (19), let $Jf=(f,S_Xf,\ldots)^t$ be its finite jet
vector, and set $\mathsf T_0=\mathsf C_N^{-1}S_X$, $H_0=\mathsf T_0^N$.
The positive order of $A$ makes (19) have at least two companion
coordinates.
Both $J1$ and $JZ_N$ are fixed by $\mathsf T_0$. If these vectors
were dependent over $\mathbb C(X)$, their first coordinates would
force $JZ_N=Z_NJ1$. Their second coordinates would then give
$S_XZ_N=Z_N$, again making $Z_N$ central. Thus

\[
 \dim_{\mathbb C(X)}\ker(H_0-I)\ge2,
 \qquad
 \left.\frac{d}{dt}\det(tI-H_0)\right|_{t=1}=0.
 \tag{20}
\]

The source and the companion endpoints exclude only finitely many
specialization levels. Equation (20) concerns this canonical
homogenization of a denominator-cleared reduced-state operator.
It does not assert a Jordan block, specify the full dimension of
the eigenspace, or apply to every alternative minimal operator.

Nor does it contradict selection of the actual series. The extra
constant solution is outside $X^{n_0}\mathbb C[[X]]$. The source
equation and that starting condition still distinguish $Z$ from
the larger rational solution space. At roots, the
[cyclotomic quantum-jet theorem](mellin_cyclotomic_jet_uniqueness.md)
retains further source and pole-lattice data when selecting the
entire rational function.

## 6. The source row still detects the selected solution

Write the normalized Mellin operator as
$A=\sum_{j=0}^{r}c_j(q,X)S_X^j$. Its canonical homogenization
(19) has order $r+1$. On its companion vectors there is the
explicit row

\[
 \ell=\frac1{\mathcal B}(c_0,\ldots,c_r),\qquad
 \ell Jf=Af/\mathcal B.
 \tag{21}
\]

Equation (19) says that this quotient is shift-invariant. In
companion form, $\sigma(\ell)\mathsf C=\ell$, so at a root

\[
 \ell H_0=\ell,\qquad
 \ell J1=0,\qquad \ell JZ_N=1.
 \tag{22}
\]

The row kills the image of $H_0-I$ but does not kill the selected
vector. Therefore the natural map from the kernel to the cokernel
of $H_0-I$ is nonzero on $JZ_N$. This is the
[observable-source criterion](actual_mellin_normal_source_rigidity.md),
which remains valid even though the simple-root test in (20)
fails. It detects a specified direction rather than asserting
semisimplicity of the entire monodromy.

The algebraic boundary module explains the distinction. Before
localization it is
$\Delta_Y=\mathcal R_Q/\mathcal R_Q(Y-1)$, where $\mathcal R_Q$
is the quantum torus (1). Passing to rational meridian coefficients
kills it because $Y-1$ becomes invertible. Its Fourier image is
$\mathcal R_X/\mathcal R_X(S_X-1)$, which survives over
$\mathbb C(q,X)$ as a rank-one trivial difference module. The
two rational localizations thus retain different boundary data.
The row (21) is an observable of the sourced Mellin presentation;
it is not automatically a row for a localized main-meridian
companion. The [source-symbol comparison](source_symbol_duality_and_presentation.md)
also gives explicit examples where an extra homogeneous factor
changes that test.

What remains is a source-and-lattice comparison, not a choice of
a preferred eigenvalue by its size or multiplicity. A proposed
geometric realization must retain the finite-start source, the
cyclotomic pole numerator, the normal derivatives, and the marked
period functional through the change of polarization. The root
Fourier identity proves the finite numerator comparison, while
(16) explains why it does not supply the quantum-normal lift.
Neither (20) nor (22) identifies a geometric factor of the
classical main-meridian operator.
