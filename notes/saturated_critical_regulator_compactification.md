# The saturated critical variety has no excess-volume boundary

28 October 2026. The actual full-Psi period now has a calibrated regulator
at every regular FULL critical point, including its integer cut marks.
This note extends that conclusion to the entire shape compactification
of those critical points. It also distinguishes this compactification
from the much larger set obtained by retaining only cleared equations
or weak angle constraints.

The result concerns the ACTUAL critical variety. It does not assert that
every endpoint of the original integration cycle lies in that variety.
In particular it does not prove an upper bound for the whole period or
its nonzero geometric coefficient.

## 1. The fixed algebraic object

Fix the original signed knot diagram and its complete peripheral mark.
Use the regular rational canonical graphs of its nine-atom crossings,
with all original cap equations. Exponentiating the FULL critical
equations gives a finite-type algebraic variety X over Q (with the
specified finite sign/lift data). Invert all denominators used by these
graphs and all shape factors z and 1-z. Retain only the components
meeting this regular locus. Thus X describes genuine regular
boundary-parabolic knot representations with their auxiliary frames;
it is not a freely enlarged cleared gluing scheme.

Every integer cut mark adds 2*pi*i times the logarithm of an actual
monomial. It leaves these exponentiated equations unchanged. The exact
[critical-action calculation](actual_wall_critical_regulator.md) gives

    Im W_m(x) = R(x) := sum_j epsilon_j D(z_j(x))
                       = Vol(rho_x),                    (1)

whenever the marked lift is a FULL critical point. Here D is the
single-valued Bloch--Wigner function and epsilon_j is the actual
signed atom multiplicity. The scalar and peripheral normalization are
those in that calculation. No change of source is made here.

There are finitely many rational shape functions for this fixed word.
Let Y be the Zariski closure of their JOINT image in (P^1)^s. Equivalently
take the graph of all shape functions on X, close it in a projective
compactification of X times (P^1)^s, and use the proper projection to
the shape factors. Closing only over affine X and projecting would
miss possible escaping limits and is not the operation intended here.
Using the joint image prevents unrelated boundary values of different
atoms from being assembled into a fictitious critical configuration.

## 2. The regulator is constant on each critical component

Here is an elementary face calculation establishing the required
constancy without a rigidity citation. Choose vector lifts v_i for an
idealized tetrahedron and put p_ij=det(v_i,v_j). Work in the rational
multiplicative group, so signs have zero class. In the six edge classes

    a=[p_01], b=[p_02], c=[p_03],
    d=[p_12], e=[p_13], f=[p_23],

the convention of the actual fundamental-cycle note gives

    [z]=e+b-c-d,     [1-z]=a+f-c-d.               (2)

Define the oriented triangular expression

    T(i,j,k)=[p_ij] wedge [p_jk]
             +[p_jk] wedge [p_ki]
             +[p_ki] wedge [p_ij].                (3)

Expansion of the exterior products gives the exact identity

    [z] wedge [1-z]
       =-T(1,2,3)+T(0,2,3)-T(0,1,3)+T(0,1,2).  (4)

For a boundary-parabolic representation, decorate each lifted cusp
vertex by its peripheral fixed vector. Peripheral SL2 eigenvalues are
signs, so face transports preserve the determinant classes used above.
Interior auxiliary vertices are decorated equivariantly. Summing (4)
over the oriented idealized relative fundamental cycle cancels its
paired faces. Hence its Bloch sum beta has delta(beta)=0 in the
rational multiplicative wedge of the component's function field.
An ordinary cusp-only ideal triangulation can be identically
degenerate for a nonfaithful representation. To avoid taking the
wedge of zero in that case, first barycentrically subdivide the
abstract relative fundamental cycle and decorate its new free
interior vertices generically and equivariantly. Each refined
tetrahedron contains at most one original cusp vertex; its other
vertices belong to distinct free vertex types. On the component's
function field, adjoining independent generic decorations makes
all the finitely many required determinants nonzero. Face transports
still match. The extra vertex stars are interior balls: idealizing
their decorations is the limit of the ordinary finite-vertex chain
identity and changes no total regulator. The explicit crossing
five-term certificate identifies the actual coefficient regulator
with this same fundamental regulator. Thus the argument also covers
components where the initial ideal triangulation is degenerate.

For nontrivial meridians, peripheral parabolicity follows directly:
in PSL2 the centralizer of a nonidentity unipotent consists of the
unipotents fixing its unique point. The longitude commutes with the
meridian. If a knot meridian is trivial, normal generation makes the
entire representation trivial, with regulator zero.

The differential identity

    dD(z)=log|z| dArg(1-z)-log|1-z| dArg z          (5)

factors through this multiplicative wedge. Thus dR=0 on the smooth
regular part of each irreducible complex component of X. That part
is connected. Continuity extends its constant value across its other
regular points. There are only finitely many irreducible components,
so the regular critical regulator takes a FINITE set of real values.
This statement allows positive-dimensional components and does not
assume that every representation is isolated.

The same conclusion holds for the nine-atom sum: its regulator equals
the five-symbol crossing regulator identically on each regular rational
crossing graph, by the independently audited wedge/real-anchor proof.

## 3. Every genuine critical degeneration retains the same value

The function D extends continuously to P^1(C), with value zero at
0, 1 and infinity. For example, for |z|<1/2 the convergent dilogarithm
series and the logarithm bound give

    |D(z)| <= 2|z|(1+|log|z||).

The identities D(1-z)=-D(z) and D(1/z)=-D(z) give the other two
limits. Therefore the signed sum R extends continuously to all
of (P^1)^s, including simultaneous zeros and poles of different atoms.

The image of a regular algebraic component is constructible and dense
in its Zariski closure; it is also dense in that closure in the complex
topology. Indeed it contains a dense Zariski-open subset of the closure,
and a proper complex algebraic subset has no analytic interior. Every
point of that closure is consequently a limit of actual regular shape
tuples. The extended R has the SAME constant value at every such limit.

Combining this with the independently proved representation-volume
bound in [the smearing argument](regular_critical_values_and_representation_volume_bound.md)
gives

    |sum_j epsilon_j D(z_j)| <= Vol(M)             (6)

on ALL of Y, including its degenerate boundary. In fact each component
of Y carries one of the finitely many values from Section 2. Components
with different values cannot intersect in this joint shape
compactification, since R is continuous there.

This also covers an escaping sequence of genuine regular critical
representations: compactness of (P^1)^s gives convergent shape
subsequences, and none acquires a larger limiting regulator. It does
not cover a sequence of approximate critical points with an uncontrolled
gradient times an unbounded logarithmic coordinate. For those points
the exact residual Im W-R=rho dot Im(gradient W) need not vanish.

## 4. Why saturation matters: an exact Pachner example

The ordinary rational two-to-three shape map can be written

    w=xy,
    u=x(1-y)/(1-xy),
    v=y(1-x)/(1-xy).                             (7)

Its cleared graph equations are

    f1=w-xy,
    f2=(1-w)u-x+w,
    f3=(1-w)v-y+w.                               (8)

These equations alone contain the spurious surface x=y=w=1 with
u,v arbitrary. Put

    g=uv-w(1-u)(1-v).

Writing X0=w+(1-w)u and Y0=w+(1-w)v gives the exact certificate

    (1-w)g = -f1+f2*Y0+x*f3.                    (9)

Consequently g belongs to (f1,f2,f3):(1-w)^infinity. Conversely, when
w!=1, equation g=0 and x=X0,y=Y0 recover (7). The saturated graph
therefore has the additional necessary equation g=0 even on its
boundary. At w=1 it requires u+v=1. The collapsed three-tetrahedron
regulator there is D(1)+D(u)+D(1-u)=0.

In contrast, the unsaturated equations admit

    x=y=w=1, u=v=i.

Their putative output regulator is 2D(i)>0, whereas the input regulator
is zero. This point is excluded by g=2i-1!=0. Thus even ONE cleared
Pachner graph can manufacture extra boundary volume. The failure has
an exact algebraic certificate; it is not a question of numerical
optimization or choice of a logarithmic lift.

This example is not asserted to be the existing nine-tetrahedron
oversized alias. The general consequence is sufficient: the certified
oversized alias, once interpreted as its joint shape tuple, cannot
belong to the saturated genuine critical closure if its regulator
exceeds Vol(M). Weak angle compatibility never established that
membership in the first place.

## 5. What this removes from the remaining problem

Uncontrolled volume of a genuine critical degeneration is no longer
an obstruction in this algebraic compactification. A proof of the
quantum upper bound must still show that every exponentially relevant
boundary contribution of the ORIGINAL relative cycle is supported
on this critical closure, is canceled exactly, or obeys an independent
estimate. Ordinary constrained endpoint maxima need not satisfy the
full critical equations; they are not covered by (6).

The lower bound also remains independent. A bounded list of possible
critical rates does not show that the original cycle has a nonzero
coefficient on the component with value Vol(M).

The accompanying exact audit checks the universal exterior identity
(4), the saturation certificate (9), elimination of the saturated
Pachner graph, and the explicit false cleared-graph boundary point.
These checks support the proofs above; no finite knot census is used
to infer the general statement.
