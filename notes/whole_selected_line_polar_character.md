# The whole selected period: its polar character controls the volume rate

Research theorem and scope audit, 27 October 2026. The user's proposal is
to construct the function or torsor first and regard quantum jets as its
restrictions. The classical part of that proposal is already proved in
[the doubled-phase optimizer](doubled_phase_rivin_optimizer.md) and
[whole cyclotomic reconstruction](whole_period_cyclotomic_rigidity.md).
This note gives a different sufficient quantum target: a meromorphic
connection on the **whole selected period line**, with the correct polar
character. Algebraicity of every quantum amplitude is unnecessary for
this criterion. Existence of that line for the actual knot period is
not asserted here; the general volume conjecture remains unproved.

**Applicability audit.** The subsequent
[actual atom theorem](unfolded_atom_cyclotomic_divisors_and_two_nome_source.md)
proves that neither the original unfolded Ward factorial nor its
two-nome completion is an ordinary meromorphic H-line at H=0.
Accumulating cyclotomic singularities and exact interior zeros give
the obstructions. Thus this sufficient criterion is not an established
model for the actual local quantum factors. The usable whole object
keeps its difference transports, cyclotomic divisors and independent
power/source normal. A completed selected word could still have
additional cancellations, but those have not been proved here.

## 1. What the classical optimizer supplies

For a positive ideal triangulation at a nondegenerate complete point,
the monomial shape equations and peripheral equations are defined over
Q, with their sign characters retained. The fixed-meridian shape
Jacobian is invertible. Therefore the normalized selected shape germ
is algebraic and etale over its meridian germ. Its shapes are algebraic
over the function field of the marked geometric A-curve, and the
complete shapes are algebraic numbers. Here M and L satisfy A(M,L)=0;
they are not two independent deformation parameters. At completeness
the specified SL2 meridian lift has M=+1 or -1 and the longitude lift
retains its prescribed sign.

Strict concavity of the volume on its affine positive angle slice
selects this geometric solution. It does not assert that an arbitrary
ideal triangulation has a positive interior optimum. The independent
arguments, including the nonzero Jacobian, are in the linked notes.
For literature coverage of the critical-point formulation, see
[Futer--Gueritaud, 1004.0440](https://arxiv.org/abs/1004.0440);
no proof from that paper is used as a premise here.

The algebraic coordinates are the shapes, not their arguments or
the dilogarithm value. The latter is a marked regulator period of
an algebraic connection. The fundamental-class and peripheral marks
fix the additive constant in the action. In the actual q convention
used here,

    h = Log q,    h_N = pi*i/N,
    Im S_geo = Vol(S^3 minus K)/2.                 (1.1)

Consequently the character exp(S_geo/h_N) has precisely the desired
volume rate. This character and an ordinary leading Gaussian
coefficient are different data. The question is whether the ORIGINAL
selected quantum period has this character, with only lower-rate
factors remaining.

## 2. A finite polar-character theorem for a whole rank-one line

Let L be a rank-one meromorphic connection at h=0. After a specified
finite ramification h=s^e, choose a meromorphic frame and write the
horizontal scalar equation as

    dP = omega P,
    omega = sum_(j=-m)^infinity a_j s^j ds.         (2.1)

Meromorphic here means a convergent Laurent germ with FINITE polar
part. Fix one sector and logarithmic sheet containing the physical
ray. Suppose P is a nonzero horizontal section there. Integrating
(2.1), exactly rather than asymptotically, gives

    P(s) = C s^rho exp(B(s) + H(s)),
    rho = a_(-1),
    B(s) = sum_(r=1)^(m-1) b_r s^(-r),
    b_r = -a_(-r-1)/r,                           (2.2)

where C is nonzero and H is holomorphic at zero. If m<2 the sum is
empty. These equations follow simply by differentiating the right
side. No summation of a divergent formal series is involved.

Choose the marked root kappa with kappa^e=pi*i and put

    s_N = kappa N^(-1/e),   s_N^e = h_N.          (2.3)

Then the exact norm expansion is

    (2*pi/N) log|P(s_N)|
      = 2*pi sum_r Re(b_r kappa^(-r)) N^(r/e-1)
        + O(log N/N).                            (2.4)

Indeed B(s_N) is the finite displayed sum; H(s_N) is bounded;
and log|s_N^rho| equals Re(rho) log|s_N| minus the bounded marked
argument times Im(rho). The constant C contributes O(1/N).

Thus the rate depends only on a finite polar character of the whole
connection. In particular:

* Terms r<e have zero limiting contribution, even though their
  exponentials need not be algebraic or polynomially bounded.
* The r=e term contributes 2 Im(b_e), since kappa^e=pi*i.
* Terms r>e contribute a divergent real power unless their real
  coefficients on the marked physical ray vanish. Distinct r give
  distinct powers, so they cannot cancel each other.

It follows that the limit equals a specified V if and only if

    Re(b_r kappa^(-r))=0 for all r>e,
    2 Im(b_e)=V,                                 (2.5)

with b_e=0 when absent. This is a criterion for the norm on this
particular marked ray. It allows higher polar terms which are pure
phase there; no uniform assertion on adjacent sectors is inferred.

## 3. The criterion belongs to the line, not to a chosen Taylor frame

A fixed nonzero meromorphic frame change P -> g(s)P changes omega
by dlog g. Write g=s^nu u(s), where nu is an integer and u is a
holomorphic unit. Then

    dlog g = nu ds/s + dlog u.

It has no polar term of order two or higher. Consequently B(s) in
(2.2) is unchanged, and the scalar norm changes by O(log N).
The criterion is invariant under every such frame change, including
zeros and poles of fixed order. Changing the ramification root
changes B and kappa compatibly and leaves B(s_N) unchanged.

The quotient by the geometric character is particularly useful.
The character has

    P_geo = exp(S_geo/h) = exp(S_geo s^(-e)),
    omega_geo = -e S_geo s^(-e-1) ds.             (3.1)

If L tensor P_geo^(-1) admits a logarithmic connection at s=0 in
a meromorphic frame, then its entire B is zero. For a nonzero
selected horizontal section the theorem therefore gives

    (2*pi/N) log|P(s_N)|
          = Vol(S^3 minus K) + O(log N/N).        (3.2)

A logarithmic quotient is a clean sufficient condition, stronger
than necessary. A quotient whose polar primitive has degree below e
still has zero limiting rate, with the finite fractional-power error
given by (2.4). This weakens the earlier amplitude requirement that
the whole comparison coefficient itself belong to a fixed finite algebraic
extension. For example exp(1/s) with e=2 is not algebraic and grows
as exp(O(sqrt N)) on a suitable ray, but it does not affect the
volume limit.

## 4. Why this is a substantive quantum theorem to prove

The hypothesis concerns the WHOLE selected period, not only the
nonzero rank-one Gaussian germ at a geometric critical point.
The source and co-source must put the actual finite Kashaev values
in the proposed line, with the original finite endpoint and polar
data. A local block, or the existence of an unpointed abstract line,
does not imply that statement.

More precisely, the application requires ONE common horizontal
section v(s) and a FIXED nonzero meromorphic cut lambda(s), with
the original scalar equal to lambda(s_N)v(s_N). The theorem is
applied to that scalar in its induced meromorphic frame. A nonzero
anchor fixes its integration constant. Arbitrarily varying level
rows, or an essential exponential hidden in lambda, are not covered.

Also the differential equation supplied by a quantum A-operator is
in the meridian direction. A factor exp(C/h), independent of the
meridian, preserves that operator equation and changes the h
connection by -C dh/h^2. It changes the normalized rate by 2 Im C.
The already specified Kashaev source does not admit this arbitrary
renormalization; the example shows why the full period connection
and its action anchor contain data beyond the A-operator alone.

All of (1.1)--(3.2) uses the fixed complete peripheral slice. With a
moving meridian one must first pull back the FULL connection along
the actual marked peripheral path. One must also retain
S_geo(M(s))/h, not replace its differential by the fixed-meridian
partial derivative. Even the flat extra term d((M-M_0)/h^2) restricts
to zero on M=M_0 but becomes d(1/h) along M=M_0+h, changing a
leading character. If S_geo(M(h))-S_geo(M_0)=O(h), the action
replacement changes the norm by O(1); a finite-Puiseux motion may
give larger, still sublinear, corrections that (2.4) must retain.

Marked root phases also remain part of the comparison. For example
q^(N^2)=exp(-pi^2/h) on h=pi*i/N. Its polar character is nonzero
but pure phase on that ray, and hence has zero norm contribution.
It satisfies the weaker real-character test (2.5); it need not give
a logarithmic quotient before that recorded phase is absorbed.

It is also not legitimate to define omega=dlog P for any interpolated
function and declare the hypothesis automatic. For example, if A!=B
and C_1 C_2!=0, the entire punctured function

    P(h) = C_1 exp(A/h) + C_2 exp(B/h)

has infinitely many zeros accumulating at h=0:

    h_k = (A-B)/(Log(-C_2/C_1)+2*pi*i*k),

omitting a possible zero denominator. Its logarithmic derivative
therefore has infinitely many poles accumulating at zero and is not
a meromorphic germ at zero. A finite cover does not remove this
obstruction. Two local rank-one characters are not a single whole
meromorphic selected line. One may instead need a higher-rank period
object and its actual source projection.

Nor does finite type of an algebraic torsor imply a logarithmic
quotient. The previously proved whole unit example

    Q_N=exp(2*pi*i/N),
    u(Q)=1+i(Q-1),     C_N=u(Q_N)^(N^2)

has u(1)=1 but (1/N)log|C_N| -> -2*pi. In the present coordinate
its one whole logarithm is

    F(h) = -pi^2 h^(-2) Log(1+i(exp(2h)-1)).

Its polar primitive is -2*i*pi^2/h. Thus its connection really has
an additional leading irregular character, and (2.4) detects the
rate change -4*pi^2 in the normalization 2*pi/N. It is not a
counterexample to the theorem. This example is not claimed to
preserve the actual knot source.

## 5. The revised cyclotomic rigidity target

The proposed route can now be phrased without computing an infinite
list of quantum Taylor coefficients:

1. Use the normalized geometric A-curve, its algebraic optimizer,
   and its marked regulator connection as the whole geometric object.
2. Construct the whole period object selected by the actual quantum
   source and cut; carry its endpoints, peripheral units and pole
   lattice. Determine whether its selected geometric contribution
   descends to a rank-one line of the type above.
3. Prove equality of the leading polar character with (3.1), and
   prove the selected pairing is nonzero. A logarithmic quotient
   would give the stronger error estimate (3.2).
4. Use exact cyclotomic restrictions to certify identities of the
   whole algebraic transport and source maps. The existing
   reconstruction theorem applies once their fixed presentation is
   supplied. It does not by itself assert existence of this period
   connection or preservation of its marked polar character.

This is a different sufficient target from proving all amplitude
coefficients algebraic and then estimating them. It has a weaker
amplitude requirement conditional on the stronger structural input
of a whole selected rank-one line. It does not establish that the
actual knot object satisfies the target.
If only a local geometric summand is obtained, its global coefficient
and the other summands must still be controlled; formula (3.2)
cannot be applied to the entire selected invariant in that situation.

[Symbolic audit](../experiments/audit_whole_selected_line_polar_character.py)
checks the polar integration, ramification and frame laws, lower-rate
characters, the amplified-unit example, and the accumulating zeros.
The [independent proof audit, Section 6](doubled_phase_and_critical_source_independent_audit.md#6-the-whole-selected-line-polar-criterion)
checks the constants, physical-ray criterion and whole-period scope.
