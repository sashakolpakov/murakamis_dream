# Independent audit of the partial geometric-support construction

Audit, 27 October 2026, of
[the partial geometric-support theorem](partial_geometric_support_theorem.md).
The new partial-sum argument is valid given the repository's actual
critical-chart/Hessian theorem and the global zero-extended finite-array
dimension lemma. In particular its transverse moment argument avoids
assuming the missing covariance of a full framing-period functional.
This audit does not assert the selected global period is nonzero on
the geometric branch.

## 1. Why a pair of actual external coordinates suffices

Let V be the tangent space of actual independent flow coordinates,
with symmetric Hessian B and two-dimensional radical R. A coordinate
projection p:V->k^2 whose restriction to R is invertible exists by
selecting a nonzero two-by-two minor of a basis of R. Put K=ker p.
Then V=R direct_sum K and B restricted to K is nondegenerate:
any vector orthogonal to K is also orthogonal to R, and hence to V;
if it belongs to K it is zero.

Fixing those two original coordinates therefore gives precisely a
nondegenerate transverse stationary problem. Its internal critical
equations have a unique local solution over the external coordinates
and meridian. The full two-dimensional framed critical germ maps
etale to those same external coordinates, so its internal solution
is that unique solution. Thus the full critical gradient vanishes
on the partially contracted branch, including its external components.
The critical action consequently has zero frame derivatives and
retains the marked unframed meridian/longitude derivative.

This is stronger than choosing an arbitrary framing section after
performing the finite sum: the external labels remain genuine
independent variables in both the certificate and the formal block.

## 2. Exact contiguity survives the specialization used here

The global certificate annihilates the entire zero-extended array,
including the finite boundary. Dividing by a nonzero common central
power of z+1 is valid for every fixed generic integer N, since
q^N+1 is a nonzero rational function of q. The full-array identity
therefore specializes regularly at z=-1, q=q_N, after fixed scalar
denominators are cleared. A nonzero fixed rational operator can have
only finitely many exceptional q_N levels.

Separately, the interior cone-density argument makes the divided
certificate a rational contiguity identity in independent variables
q,x,z,Ahat,Bhat,t. That identity can also be specialized at z=-1.
This separate independent-variable identity is essential: a relation
only on a finite frame grid at one root would not suffice for the
formal Gaussian block.

The compact-product formal solution has exactly the same interior
shift ratios, since its Bernoulli series obeys the functional equation
P_Q(Qz)=P_Q(z)/(1-z) coefficientwise. Fixed singular arguments such
as P_Q(Q) occur only in the retained common base line; all variables
on the chosen regular geometric chart avoid the polar divisors.
Thus the formal identity uses rational factor cancellation, never
evaluation of an individual infinite compact product at a root.

## 3. The finite and formal moment repairs agree exactly

The physical logarithmic internal coordinate is u_i=Hj_i,
H=Log Q. Hence exp(v dot j) is implemented in the formal period by
the phase S+v dot u, divided by H. Its critical point deforms
uniquely because the transverse Hessian is invertible. The weighted
formal period belongs to the original WKB line times
k((H))[[v]]; its negative H orders may grow with the v degree.
No uniform lower H bound over all v degrees is required.

Formal Gaussian contraction satisfies integration by parts. For
the quadratic kernel exp(x^t B x/(2H)), Wick covariance is
-H B^(-1); contraction of a derivative of a monomial cancels the
contraction of (Bx)_i/H times that monomial. Expanding cubic and
higher vertices gives the same identity coefficientwise, with
finitely many contractions in each allowed order. Thus a formal
total derivative has zero contraction.

Translate one internal coordinate by H. The weighted integrand
then changes by exp(-v_i) after the corresponding formal change of
coordinate. Equivalently the infinitesimal translation equation is
G_v(H partial_i f)=-v_i G_v(f); integrating the translation parameter
gives G_v(S_i f)=exp(-v_i)G_v(f). The H-dependent shift is a valid
formal translation around the unique critical germ. The determinant
half-line is continued with that same germ, rather than rechoosing
its square root after shifting.

External multiplication and the meridian step commute with this
contraction. The latter shifts log M by H/2, while Ahat,Bhat are
held fixed, and carries the critical point to its unique nearby
one. It leaves H and the retained common base line fixed.

There are no internal multiplication variables in the certificate's
operator coefficients. Therefore its expansion in (S-1) has exactly
the same least nonzero multi-degree after either finite weighted
summation or formal transverse contraction. At that degree every
positive moment is multiplied by a lower, identically zero operator
coefficient. The same nonzero D_alpha annihilates the actual partial
finite family and its nonzero transverse formal block.

This would not justify an unproved integration functional in either
of the two remaining framing directions. They remain external.

## 4. The leading-symbol conclusion and its scope

After dividing the common scalar q-1 valuation, the operator has
a nonzero leading classical symbol. The transverse formal block
has unit leading amplitude and the actual marked longitude as its
leading meridian ratio. Its annihilation therefore forces that
symbol to vanish on the marked geometric longitude branch.

The external coordinates range over a dense open frame chart by
the etaleness in Section 1. They are algebraically independent over
the geometric branch field; a purely transcendental extension does
not split its irreducible rational defining polynomial. Thus the
stated A_geo factor divisibility over Q(Ahat,Bhat) is valid.

The conclusion concerns the specifically constructed partial-state
annihilator. It neither identifies its minimal operator nor says
that the full finite scalar contraction retains that component.
In particular a nonzero local formal transverse block is not yet
a nonzero selected global geometric contribution. No global cycle,
Stokes, cancellation, or volume conclusion has been added here.
