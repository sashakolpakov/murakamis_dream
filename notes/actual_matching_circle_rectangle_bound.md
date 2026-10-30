# Every certified crossing-circle rectangle has ratio at most one

30 October 2026. For every crossing
circle in an ACTUAL complete right-angled matching-polyhedron
certificate, the disk-framed rectangle ratio satisfies

    0<c<=1.                                        (1)

Thus its actual recoupled target trace is at most -2. This holds
for both retained half-twist signs, not just the pure or Conway
subclass. The equality case remains a nontrivial parabolic target;
no strict inequality or operator asymptotic is inferred.

## 1. The geometric and marked input

Assume the labeled actual cut, complete cusp metric and primitive
crossing-circle paths of
[the general matching-polyhedron certificate](general_augmented_plat_matching_geometry.md).
Its actual crossing-circle rectangle has vertices
(1,E,-1,-E), with E=exp(2pi i x), 0<x<1/2, and c=cot(pi x)>0.
An arbitrary abstract ideal rectangle is not asserted to satisfy (1).
The conclusion concerns one realized in this complete manifold with
these actual disk and meridian identifications.

The original based pair and its transport may be normalized as

    A=-[[1,1],[0,1]], B=-[[1,0],[-4,1]],
    P=BA, H=P+I, H^2=0,
    C=I+bH, B_out=C B C^-1.

The actual primitive collar and quantum half-twist calibration give

    tau_epsilon=2ic/(1-epsilon ic),
    b-epsilon/2=1/tau_epsilon,
    b=-i/(2c), epsilon in {0,+1,-1}.                (2)

The literal inverse-cup bend fixes the target word

    W=B^-1 B_out,
    Tr W=2+16b^2=2-4/c^2,                          (3)

as proved in [the actual geometric target theorem](actual_matching_edge_geometric_target_polynomial.md).
The only possible concern for a discreteness argument is whether
C itself is a group element when a retained half twist occurs.
The next calculation removes that concern without assuming it.

## 2. The half-transport still gives actual based meridian words

Put S=I+H/2. The original primitive-collar reconstruction in
[the actual critical scheme](actual_augmented_plat_critical_scheme.md),
at the complete endpoint J=-1, says PROJECTIVELY

    mu=C^-1 S^epsilon.                             (4)

Here mu is the actual based auxiliary meridian. Indeed its generic
factor (P^-1-I)^epsilon specializes using

    P^-1-I=-2S,

and the recorded scalar h_J^(-epsilon)=(-2)^(-epsilon) cancels
that constant. The remaining lift scalar is central and has no
effect on the conjugation below. Thus (4) retains the primitive
meridian; it does not replace it by a half-longitude.

Direct multiplication in the original pair gives

    S B S^-1=A, S^-1 B S=B A B^-1.                 (5)

Since C=mu^-1 S^epsilon projectively, the three physical outputs are

    epsilon=0:  B_out=mu^-1 B mu,
    epsilon=+1: B_out=mu^-1 A mu,
    epsilon=-1: B_out=mu^-1 B A B^-1 mu.            (6)

Every expression in (6) is an ACTUAL based holonomy word in the
same complete manifold. The meridians A,B,mu have the common
basepaths fixed by the original threading word. In particular
W=B^-1 B_out is a group element for every retained parity. The
matrix S need not itself be a group element; none of (6) assumes
that it is. Changes of lift sign cannot affect the ensuing absolute
trace classification.

## 3. The complete metric excludes the forbidden trace

The certified metric is complete and its universal developing
cover is hyperbolic three-space, as in the complete gluing theorem.
Its holonomy acts by deck transformations and hence freely. A
nonidentity element of this group cannot fix an interior point.

If c>1, equation (3) gives -2<Tr W<2. Its determinant-one matrix
therefore has distinct eigenvalues exp(+i theta), exp(-i theta),
with 0<theta<pi. After conjugacy its Möbius action is a nontrivial
rotation about the geodesic joining its two ideal fixed points.
It fixes every interior point on that geodesic. This contradicts
the free deck action. Consequently c<=1, proving (1).

This is an elementary group consequence of the ACTUAL primitive
word (6). No unproved packing inequality or exterior cusp-shape
estimate is used. It also explains why the same assertion could
not be made about an abstract rectangle without the marked quotient.

At c=1 the target is genuinely parabolic, not the identity. In the
normalization above its matrix is

    W=[[8b^2-4b+1,4b^2],[16b^2,8b^2+4b+1]],

and at b=-i/2, W+I=[[2i,-1],[-4,-2i]] is nonzero and squares to
zero. Nothing here rules out that parabolic word in the manifold.
A strict bound would require an additional topological or geometric
argument about that word, which is not supplied by this theorem.

## 4. Consequence and scope

Every actual complete target in this certified class is therefore

    c<1: Tr W<-2, a real off-spectrum target;
    c=1: Tr W=-2, the parabolic spectral endpoint.

The formal c>1 branch of the local algebraic four-parabolic relation
still exists, but cannot be the complete crossing-circle geometry
with the marked certificate used here. This removes the in-spectrum
case for these actual geometric targets. It does not show that a
given common frame places the target's physical rows in the strict
cross-central domain, identify a surrounding continuant state,
or prove contour contribution or equality of source and volume.

Focused audit: [actual half-twist words and target trace](../experiments/audit_actual_matching_circle_rectangle_bound.py).

Primary-agent full analytical review: PASS. The reader checked the
actual primitive scalar cancellation, both half-transport conjugations
and all three based words, the elliptic fixed-axis contradiction, and
the explicit nonidentity parabolic equality case.

Independent full analytical review and fresh focused replay: PASS.
A second reader verified the group-word status without assuming S
belongs to the group, the complete free-deck argument and endpoint
matrix, and reproduced all sixteen exact audit identities. Neither
review asserts a strict bound, a common favorable frame, or an original
source asymptotic.
