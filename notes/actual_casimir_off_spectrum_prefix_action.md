# The actual Casimir prefix has a selected off-spectrum action

30 October 2026. This is a theorem for the
original physical Casimir matrix, with an arbitrary spectral variable.
It supplies a forward/backward Green-kernel ingredient for the exact
exceptional-block contour. It does not continue a finite color or a
magnetic index, evaluate the full polynomial operator by its symbol,
or prove that a geometric saddle contributes to the source contour.

## 1. Statement and the strict half-prefix condition

Use the original root matrix J_t of the
[physical generic-jet theorem](actual_q_hahn_physical_generic_jet_bound.md),
with q=exp(pi i/N), Q=q^2, 0<=t<=N-1. Let J_[m] be its first m rows
and columns. Suppose

    t/N -> tau, m/N -> nu, 0<nu<tau/2, 0<tau<1.

All convergence below is uniform when the two real parameters stay in
compact subsets of this strict domain. Put

    beta=pi(1-tau+2nu) in (0,pi),
    H_beta={z: Re[exp(-i beta/2)(2-z)]>0}.

On every compact subset of H_beta, the actual matrices J_[m]-zI are
invertible for all sufficiently large N, with a uniformly bounded
inverse. In particular this includes every fixed compact set of real
spectral parameters z<2. The bound does not hold here at a central
prefix nu=tau/2; that endpoint is deliberately excluded.

There is a canonical analytic logarithm of the determinant, selected
from negative real infinity, for which

    N^-1 Log det(J_[m]-zI) -> S_(tau,nu)(z),          (1)

locally uniformly on H_beta, with every fixed z derivative. Write

    A(x)=-4 exp(i pi(2x-tau))
                         sin(pi(tau-x))sin(pi x),
    w=2-z.

The limiting action is the explicit single integral

    S_(tau,nu)(z)=integral_0^nu
       Log[(w+2A(x)+sqrt(w(w+4A(x))))/2] dx.          (2)

The square root and logarithm in (2) are selected at large positive
w and continued in H_beta. They are not pointwise principal choices
of a determinant or discriminant. Formula (1) is a leading action,
not a relative-amplitude expansion.

## 2. An exact Dirichlet decomposition of the original matrix

The actual root entries, with U=Q^r and T=Q^t, are

    D_r=U/T [2(q^-1+qT)-(q+q^-1)U],
    A_r=(U-T)(1-q^2 U)/T.

Put A_(-1)=0. Direct algebra gives BOTH identities

    D_r=q+q^-1+q^-1 A_r+q A_(r-1),                 (3)

    R_r:=D_r-2-A_r-A_(r-1)
      =-U(q-1)^2(Tq^2-Uq^2-Uq-U+1)/(Tq^2).        (4)

Hence |R_r|<=C/N^2, uniformly over all physical r,t. The unitary
diagonal sign matrix changes the offdiagonals of J_[m] to -A_r.
After this conjugation, (4) says exactly

    J_[m]-2I=L_A+diag(R_r),                        (5)

where L_A has diagonal A_(r-1)+A_r and adjacent entries -A_r.
For v_m=0 its sesquilinear form is

    <v,L_A v>=sum_(r=0)^(m-1) A_r |v_r-v_(r+1)|^2. (6)

The term r=m-1 is the retained Dirichlet boundary term. At the other
endpoint A_(-1)=0 exactly; no omitted boundary term is being estimated.

The original coefficients also have the exact polar form

    A_r=-4 exp(i(2r+1-t)pi/N)
                    sin((t-r)pi/N)sin((r+1)pi/N).

For 0<=r<m, both sine factors are positive and their marked arguments
obey

    0<Arg A_r<=beta_N:=pi+(2m-1-t)pi/N<pi.         (7)

In the strict scaling range beta_N tends to beta<pi. If w=2-z,
rotation of wI+L_A by exp(-i beta_N/2) gives

    Re <v,exp(-i beta_N/2)(wI+L_A)v>
       >=Re[exp(-i beta_N/2)w] ||v||^2.             (8)

The perturbation (4) costs at most C/N^2 in (8). Every compact of
H_beta has a positive margin in its right side; (5)--(8) therefore
give the claimed uniform inverse bound for the original prefix.
The sign conjugation is unitary and does not alter determinants.

## 3. Determining the actual logarithm, without an assumed WKB solution

For a finite N, restrict first to

    Re[exp(-i beta_N/2)(2-z)]>2C/N^2.

There the rotated matrix in (8) is strictly accretive. Its principal
matrix logarithm defines

    Log det(J_[m]-zI)
       :=i m beta_N/2
          +tr Log[exp(-i beta_N/2)(J_[m]-zI)].       (9)

This agrees with m Log(-z)+O(m/|z|) as z tends to negative real
infinity. These halfplanes exhaust every compact subset of H_beta.
The logarithm in (9), rather than the principal logarithm of the
scalar determinant, retains the actual accumulated phase.

The inverse bound gives

    |N^-1 partial_z Log det(J_[m]-zI)|<=C_K m/N.

At one sufficiently negative fixed real z, the uniformly bounded
entries and fixed bandwidth give a bounded normalized logarithm by
its convergent trace series. The derivative bound then gives local
boundedness throughout H_beta. These analytic functions form a
locally bounded normal family there.

It remains to determine its limit on a nonempty open set. For each
fixed integer k, multiplication of the tridiagonal matrices gives
a finite sum over nearest-neighbor closed paths. Paths within k
rows of an endpoint contribute O(k/N) after normalized trace, since
their entries are uniformly bounded. On all other paths, the slowly
varying entries may be replaced by their common local limits with
error O_k(1/N). Thus

    N^-1 tr(J_[m]^k) -> integral_0^nu (1/pi) integral_0^pi
            [2+2A(x)+2A(x)cos(phi)]^k dphi dx.       (10)

The coefficient of the zero Laurent power in the local tridiagonal
symbol is precisely the inner integral in (10); this proves the
path count directly. For |z| sufficiently large, the uniformly
convergent logarithmic trace series and (10) show that (1) has limit

    integral_0^nu (1/pi) integral_0^pi
           Log[w+4A(x)cos^2(phi/2)] dphi dx.         (11)

For every x in [0,nu], A(x) is zero or lies in the cone of (7).
The argument of the logarithm in (11), after rotation, has strictly
positive real part for z in H_beta. Consequently (11) is analytic
on H_beta with the branch selected by negative infinity. The identity
theorem and the normal-family bound make every subsequential limit
equal to (11), proving convergence of the full sequence. Cauchy's
formula proves convergence of all fixed spectral derivatives.

Finally integrate the elementary logarithmic symbol. For large positive
w, expansion in A/w (or differentiation in w followed by its value at
infinity) gives

    (1/pi) integral_0^pi Log[w+4A cos^2(phi/2)] dphi
       =Log[(w+2A+sqrt(w(w+4A)))/2].                (12)

Both sides continue analytically on H_beta. Indeed w and w+4A lie
in the same rotated right halfplane; the selected product square root
is nonzero there. The selected numerator in (12) is nonzero as well:
a zero would force A=0 after squaring, whereas then it equals 2w.
Equation (12) proves (2) with its source-selected branch.

## 4. What this gives to the exceptional-block problem

The forward resolvent numerator is exactly det(zI-J_[m]); it differs
from the determinant in (1) by (-1)^m, whose marked logarithm must be
retained. The actual trailing prefix is the reflected conjugate root
matrix, so it has the conjugate statement with its own corresponding
halfplane and branch. Thus suitable strict forward/backward portions
of the original Green kernel have a selected off-spectrum leading
action, including all real geometric target traces below 2.

This does not yet control prefixes reaching or crossing their midpoint,
complex magnetic continuation, a relative nonzero amplitude, or the
resolvent contour's intersection with a geometric steepest-descent
cycle. No large-degree polynomial has been replaced by scalar symbol
evaluation in this theorem. The moving generic-q normal also remains
the one in the exact contour formula; (1) concerns spectral derivatives
of the root prefix, not generic-q derivatives of the whole source.

Focused audit: [original prefix, exact row residual and selected action](../experiments/audit_actual_casimir_off_spectrum_prefix_action.py).

The theorem requires a strict half-prefix and concerns root spectral derivatives and the leading action. It includes no relative amplitude or source-cycle contribution. Finite logarithm and trace-moment samples check the formulas, not the limiting theorem.