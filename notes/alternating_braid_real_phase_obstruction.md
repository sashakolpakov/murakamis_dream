# Alternating generator signs do not make the charged-flow maximum a real saddle

28 October 2026. This is an exact obstruction in the original enhanced
Kashaev source. It applies at arbitrary braid width. It concerns a real
charged-flow approach, not the existence of a selected complex geometric
cycle or the volume conjecture itself.

## 1. A source-retaining local variation at arbitrary width

Use the original crossings and actual inverse of
[the charged-state note](original_crossing_winding_convexity.md). Put
Q=exp(2 pi i/N). Suppose that the first crossing touching the cut head is
sigma_1^epsilon, epsilon=+1 or -1. Suppose its outgoing second head next
meets sigma_2^(-epsilon), before any other crossing touching that head.
Crossings on disjoint heads can occur in between. This includes arbitrary
width weaving blocks beginning sigma_1^epsilon sigma_2^(-epsilon), and
does not restrict the rest of the word to a twist family.

The [actual source theorem](original_source_cyclic_variation_peeling.md)
forces the first head to remain zero and the incoming second head of this
first cut crossing to equal 1. Call its outgoing second-head color D.
The first local factor is consequently

    T+_(D,1)=Q^D,              T-_(D,1)=Q^(-1),        (1)

for 1<=D<N. All original pivot, framing, Cartan, and other crossing
factors remain in the whole path weight W(D).

At the next crossing, write its input as (D,b), its output as (c,d),
and its original corner indices as

    u=[b-D-1], v=[D-c], t=[c-d], h=[d-b],
    u+v+t+h=N-1.                                    (2)

Fix every other color in the actual source path. Assume D+1<N and that
the variation D -> D+1 remains in this same support chamber, so u>=1,
u -> u-1 and v -> v+1 without a residue wrap. Then the WHOLE original
summand obeys the exact identity

    W(D+1)/W(D)
      = sin(pi u/N)/sin(pi(v+1)/N)
                       * exp[-epsilon*pi*i*(t+h)/N]. (3)

The magnitude ratio in (3) is strictly positive. Only the two displayed
crossings depend on D; none of the exterior source factors has been
replaced by an arbitrary co-source or discarded.

For epsilon=+1, the positive second-crossing coefficient has ratio

    Q^(t+h) (1-Q^u)/(1-Q^(-(v+1))).

Its actual inverse has ratio Q^(-1) times the conjugate of this expression.
Multiplying by the ratio Q from (1) gives

    Q^(-(t+h)) (1-Q^(-u))/(1-Q^(v+1)).               (4)

Using the sine forms of the two linear factors and the EXACT charge in
(2) proves (3). For epsilon=-1 the ratio of the first factor in (1) is
one; the positive second crossing gives the conjugate sine-phase in
(3). This proves both signs at every N, including even and composite
levels, without a semiclassical approximation.

## 2. Consequence for the proposed real-saddle mechanism

Let a source-support region have a limiting interior direction D/N=z,
and let tau=(t+h)/N tend to a number in (0,1]. Equation (3) says that
the limiting phase derivative of the whole summand in this direction is

    partial_z Theta = -epsilon*pi*tau modulo 2*pi.   (5)

It cannot vanish, even after adding an integer lattice phase. Thus the
leading complex action cannot have a REAL critical point on such a
region. In particular, a real maximizer of the strictly concave absolute
action is not thereby a critical point of the original complex state.

If a real critical point is sought in a region where this local color
variation is free, (5) forces tau=0. Since the corners are nonnegative,
t=h=0 in the limiting configuration. The opposite-sign crossing then
has at most two nonzero corners, with sum one, and its limiting absolute
entropy is zero. This is a forced degeneracy, not the nondegenerate
positive chart contemplated in a direct Laplace argument.

This argument does not apply at a face where the D variation is no longer
free. Nor does it rule out complex saddles or a source-preserving
complex contour homotopy. It shows that such further transport cannot be
replaced by the assertion that alternating generator signs automatically
make the original real charged-flow optimizer stationary.

## 3. The actual figure-eight source gives an interior strict maximum

For the word (sigma_1 sigma_2^(-1))^2, consider the actual supported paths

    (0,1,B+1) -> (0,D,B+1) -> (0,E,F)
              -> (0,0,F) -> (0,0,B).                (6)

In the full-dimensional limiting chamber

    0<F<E<D<B<1,                                    (7)

letters now denote colors divided by N. The four corner lists tend to

    (0,0,1-D,D),
    (B-D,D-E,E-F,1+F-B),
    (E,0,0,1-E),
    (F,0,1-B,B-F).                                  (8)

The two cut end crossings have zero limiting absolute action. With
Lambda'(theta)=-log(2 sin theta), the whole absolute action is

    H=(1/pi)[Lambda(pi(B-D))+Lambda(pi(D-E))
            +Lambda(pi(E-F))+Lambda(pi(1+F-B))
            +Lambda(pi F)+Lambda(pi(1-B))
            +Lambda(pi(B-F))].                      (9)

This has a unique strict interior maximum on the closure of (7).
Indeed fix s=B-F. The first three angles sum to s, so strict concavity
of Lambda on that fixed-charge simplex makes them all s/3. For the two
remaining free angles F and 1-B, their sum is 1-s; strict concavity makes
both (1-s)/2. Finally Lambda(pi(1-s))+Lambda(pi s)=0 cancels, leaving

    H_red(s)=[3 Lambda(pi s/3)
                       +2 Lambda(pi(1-s)/2)]/pi,
    H_red'(s)=log[cos(pi s/2)/sin(pi s/3)].            (10)

This derivative changes sign only at s=3/5, from positive to negative.
The unique maximum is therefore

    (B,D,E,F)=(4/5,3/5,2/5,1/5),
    H_max=5 Lambda(pi/5)/pi=0.7936696457597476... .    (11)

Here the entropy statement only concerns this actual source chamber;
no identification of its maximum with a knot volume is made.

The retained leading phase, computed from the original quadratic
crossing phases with signs (+,-,+,-), is, modulo lattice-invisible
linear phases,

    Theta/pi=BD-2BF-DE-D+EF+E+F.                     (12)

At the strict absolute maximum its gradient divided by pi, in the order
(B,D,E,F), is

    (1/5,-3/5,3/5,-1/5) modulo 2 Z^4.               (13)

In particular partial_D Theta=-3 pi/5. More strongly, throughout (7),
partial_D Theta=-pi(1+E-B) lies strictly between -pi and zero. This is the
arbitrary-width obstruction (5) realized at a strict interior entropy
maximum of the original hyperbolic-knot source.

## 4. What changes in the next proof step

For alternating homogeneous braids, one cannot close noncancellation by
combining real source-flow concavity with automatic phase stationarity.
The original state already contains a local opposite-sign phase flux
(3). A viable general proof must transport that genuinely oscillatory
state to its complex geometric cycle, or perform exact source-preserving
summations that change this presentation while retaining its selected
period. Concavity remains useful after that transport; it does not
perform the transport.

The [audit](../experiments/audit_alternating_braid_real_phase_obstruction.py)
checks (3) against the independently implemented original crossing and
actual inverse over finite fields, verifies its complex sine phase, and
checks the full symbolic phase and entropy critical point. These tests
supplement the uniform proof above.
