# An actual bounded source in the Fourier--Mellin polarization

Research construction, 27 October 2026. A fixed rational inhomogeneous
source need not be assumed as a special factorization of the original
meridian operator. It can be constructed in the Fourier--Mellin
polarization directly from any actual all-level operator and finitely
many fixed colors. The original Kashaev invariant is retained as an
exact coefficient period. It is not replaced by point evaluation or
by a new state.

This gives an actual sourced quantum-A object for arbitrary knots.
Its classical geometric support and selected regulator norm still
require proof; the volume conjecture is not proved here.

## 1. Actual input and the Q convention

Choose the nonzero rational operator supplied by the
[Q-only construction](even_meridian_norm_descent.md), clear its
coefficient denominators, and remove a common shift:

    P=sum_(j=0)^d a_j(Q,Y) T^j,
    a_j=sum_m a_(j,m)(Q) Y^m,
    TY=QYT, a_0 a_d!=0.                          (1.1)

Here d>=1, the m support is finite, and the coefficients belong to
the rational function field ℚ(Q). The associated fixed-color periods
are C_n(Q), normalized by C_n(1)=1. They are the actual finite
reduced periods of the existing color-pointing theorem. The exact
identities are

    F_N(Y=Q_N^n)=C_n(Q_N), 1<=n<=N,
    C_N(Q_N)=F_N(1)=<K>_N,
    Q_N=exp(2pi*i/N).                            (1.2)

There is no large-color asymptotic premise in (1.2).

For completeness these fixed-color functions descend to Q=q^2 as
well. On the ordinary n-dimensional color x=q^(n-1), use the same
stripped crossing coefficients, ordinary pivot K and residual twist
x. The total x-power on a closed state is

    E_ord=b-1-w+sum_positive(-a-c)+sum_negative(a+c)
         =-kappa_D+2sum_negative a-2sum_positive c,

because sum(c-a)=0. It is even for a knot. All remaining factors
are expressed in Q and x^2. At x=q^(n-1) this is a rational function
of Q. The known Laurent regularity and normalization of C_n are
those of the original finite color construction, not an additional
asymptotic or Jones-identification assumption.

Applying the actual root equation to (1.2), then using infinitely
many distinct Q_N for every fixed n, gives the generic recurrence

    sum_(j=0)^d a_j(Q,Q^n) C_(n+j)(Q)=0, n>=1.   (1.3)

This is the same elementary cross-level rigidity used in the
[all-level period theorem](all_level_a_period.md).

## 2. Choose a nonsingular fixed starting color

Let A be the Q-exponent span in the collected Laurent support of
a_d(Q,Y). For every integer r>A, the substitution a_d(Q,Q^r) is
nonzero. Indeed distinct monomials Q^u Y^v become Q^(u+rv), and
a collision with v!=v' would imply r<=|u-u'|<=A. Equal-v terms
were already collected.

Choose the fixed integer

    n_0>=d+A+1.                                 (2.1)

Then a_d(Q,Q^(n_0-d))!=0, and also
a_d(Q,Q^(r-d))!=0 for every r>=n_0. Every C_n is nonzero since
C_n(1)=1. These facts will give both a nonzero source and unique
formal propagation in the chosen source lattice.

## 3. The exact Fourier--Mellin operator and its boundary source

Form the actual formal generating period

    Z(Q,X)=sum_(n>=n_0) C_n(Q) X^n
           in X^(n_0) ℚ(Q)[[X]].                (3.1)

Let S act by S f(X)=f(QX), so SX=QXS. The quantum-torus Fourier
map is the exact algebra map

    Y |-> S, T |-> X^(-1).

It respects TY=QYT because X^(-1)S=QSX^(-1). In the recorded
left-coefficient ordering its image is

    P^M=sum_(j,m) a_(j,m)(Q) Q^(-mj) X^(-j) S^m. (3.2)

Negative m are allowed; they are invertible shifts. A fixed left
power of S makes the displayed operator have nonnegative order,
transporting its source by the same power, if that convention is
desired. No factor of the source is discarded by doing so.

Multiplying (1.3) by X^n and summing n>=n_0 gives

    P^M Z=B(Q,X),                               (3.3)

where the source is the explicit fixed Laurent polynomial

    B=sum_(j,m) a_(j,m)(Q) Q^(-mj) X^(-j)
          sum_(r=n_0)^(n_0+j-1) C_r(Q) Q^(mr) X^r. (3.4)

The empty sum for j=0 is zero. The identity follows termwise from

    sum_(n>=n_0) Q^(mn) C_(n+j) X^n
      =Q^(-mj) X^(-j)
           [Z(Q,Q^m X)
                -sum_(r=n_0)^(n_0+j-1) C_r(Q) Q^(mr) X^r].

Every coefficient of every X power involves only finitely many
terms; convergence is not assumed.

The source uses exactly the d fixed colors C_(n_0),...,C_(n_0+d-1).
Its X powers lie between n_0-d and n_0-1. Its lowest coefficient is

    [X^(n_0-d)]B=C_(n_0)(Q) a_d(Q,Q^(n_0-d))!=0. (3.5)

Thus it is a genuine nonzero bounded source, not a possibly vanishing
right-hand side inferred from formal elimination.

## 4. The pointing and the original period are retained

Equation (3.3), together with the lattice condition Z in X^(n_0)[[X]],
specifies Z uniquely. A nonzero homogeneous difference W in this
lattice, of lowest power r>=n_0, would contribute at power r-d only
through j=d. Its coefficient would be

    a_d(Q,Q^(r-d)) [X^r]W,

which is nonzero by (2.1), a contradiction. Thus the source and
specified lattice retain the actual finite-color pointing.

For every N>=n_0 the original invariant is exactly

    <K>_N=[ [X^N]Z(Q,X) ]_(Q=Q_N)
          =Res_(X=0) Z(Q_N,X) X^(-N-1)dX.        (4.1)

The first expression means whole-germ specialization of the
coefficient C_N(Q). Even if coefficients of a recurrence or a
companion solution have poles at Q_N, C_N itself is the original
regular Laurent period. No division by such a pole precedes its
cancellation. The residue notation means coefficient extraction;
it does not assert an analytically convergent contour realization.

The full ADO period is still d_N(M)F_N(M), with its marked pole,
residue, first jet and sign retained in the original meridian
realization. This change of polarization constructs the same
reduced Kashaev scalar in (4.1); it does not silently evaluate or
remove d_N. A comparison of full-state realizations must transport
that specified normalization line as well.

## 5. Classical support and the affine extension

At Q=1 the symbol of (3.2) is exactly

    P_cl(S,X^(-1)).                              (5.1)

Thus the classical Fourier transformation exchanges the meridian
coordinate and the inverse longitude coordinate in the specified
ordering. If a geometric factor occurs in the original actual
symbol, its transformed geometric factor occurs here. No such
factor is inferred merely from the transform.

The marked regulator action is compatible with this polarization.
Let y=Log Y, lambda=Log(L/L_c) and use H=Log Q, centering the
longitude logarithm at the chosen complete lift L_c. Use the
corresponding centered WKB action dW=lambda dy. The original
constant character L_c is retained separately, rather than dropped
from the period. In centered coordinates x=Log(X/X_c)=-lambda,
X_c=L_c^(-1), with new momentum y. Hence

    W^M=W-y lambda,  dW^M=y dx.                 (5.2)

Its symmetric regulator coordinate is unchanged:

    R=W-(1/2)y lambda
      =W^M-(1/2)x y.                            (5.3)

Indeed dR=(lambda dy-y d lambda)/2, exactly the marked regulator
differential after Y=m and L^2=l are substituted. At the chosen
complete lift y=0 the Legendre correction vanishes, including a
retained longitude sign. Thus the previously calibrated complete
imaginary action is preserved. This checks the classical marked
action, not a normalization or asymptotic theorem for the quantum
coefficient period (4.1).

Grouping the m powers of S and using its usual companion realization
turns (3.3), when its S-order is positive, into an affine difference
extension with rational coefficients and the explicit source (3.4).
One can homogenize it by the exact source annihilator

    (S-B(Q,QX)/B(Q,X)) P^M Z=0.                 (5.4)

The source quotient and the chosen formal lattice must remain marked;
(5.4) is not permission to replace the original object by an arbitrary
homogeneous solution. If the transformed order is zero, (3.3) is
instead its rational algebraic source equation; no artificial order
is inserted to manufacture a geometric block.

This removes the need to assume a special inhomogeneous right factor
in order to obtain some canonical generic sourced polarization of the
actual A-period. It does not prove that this extension is generically
nonsplit, identify its geometric source class, or bound the selected
coefficient norm in (4.1).

## 6. The precise comparison residual

For two supplied affine systems sigma v_i=C_i v_i+c_i, a proposed
map v_act=P v_geo+b is horizontal precisely when

    sigma(P) C_geo=C_act P,
    (sigma-C_act)b=c_act-sigma(P)c_geo.           (6.1)

Thus after a homogeneous comparison P, the remaining obstruction is
the explicit class

    [c_act-sigma(P)c_geo]
              in F^d/(sigma-C_act)F^d.           (6.2)

An affine cut ell_i v_i+k_i is preserved additionally when

    ell_act P=ell_geo,
    k_act+ell_act b=k_geo.                       (6.3)

The second equation retains the dual affine constant. Generic matrix
invertibility does not by itself transport the boundary lattice.

The new construction supplies the actual side of (6.1)--(6.3) in this
polarization. It does not supply the geometric side or assert that
their class (6.2) vanishes. Multiplicative rank-one curvature descent
alone does not solve this additive source problem.

The [actual Mellin normal-source theorem](actual_mellin_normal_source_rigidity.md)
now uses this very source quotient to exhibit a dual cocycle
with value one on the selected section. Its normal symbol is
therefore nonzero for every knot, without a semisimplicity
assumption. Whole first-normal compatibility removes central
scalar freedom on that selected line. The
[cyclotomic jet theorem](mellin_cyclotomic_jet_uniqueness.md)
additionally fixes arbitrary root sections in the exact pole
lattice using a bounded number of source-compatible quantum
levels. Neither theorem constructs the geometric side of
(6.1)--(6.3) or estimates the selected residue's norm.

[Exact audit](../experiments/audit_fourier_mellin_actual_source.py).
[Results](../experiments/fourier_mellin_actual_source_results.json).
