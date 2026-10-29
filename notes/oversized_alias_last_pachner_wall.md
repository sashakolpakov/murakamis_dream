# The oversized weak alias fails at the last Pachner norm wall

28 October 2026. This traces the certified oversized weak alias of
[the nine-tetrahedron counterexample](positive_geometric_alias_volume_counterexample.md)
backward through its actual last $2\to3$ move. The first inverse step
already has no boundary-preserving nonnegative angular preimage.
The exact five-term map locates the norm divisor and its direction
data. This does not prove that the original quantum source assigns
zero to the wall.

The exact audit is
[audit_oversized_alias_last_pachner_wall.py](../experiments/audit_oversized_alias_last_pachner_wall.py),
with [results](../experiments/oversized_alias_last_pachner_wall_results.json).
It derives the local vertex labels from the actual saved face
permutations, verifies the shape map in the certified cubic field,
and checks the angle and norm identities symbolically.

## 1. A universal angular preimage criterion

Label a triangular bipyramid by equatorial vertices $A,B,C$ and
apices $D,E$. The actual old tetrahedron orderings in this example are

$$
 (D,A,B,C),\qquad (B,E,C,A).
$$

Its new orderings are

$$
 (E,D,C,B),\qquad(E,D,B,A),\qquad(E,D,A,C).             \tag{1}
$$

Write each new angle triple as $(\alpha_j,\beta_j,\gamma_j)$,
$j=0,1,2$. The new internal edge $DE$ and its opposite equatorial
edge both carry $\alpha_j$. Each triple sums to $\pi$.

Boundary angle preservation uniquely forces the old triples to be

$$
\begin{split}
 X={}&(\beta_1+\gamma_2,\ \beta_0+\gamma_1,\
                         \gamma_0+\beta_2),\\
 Y={}&(\gamma_0+\beta_1,\ \gamma_1+\beta_2,\
                         \beta_0+\gamma_2).          \tag{2}
\end{split}
$$

For example, old edge $DA$ is split between the new $\beta_1$ and
$\gamma_2$ corners; the other entries follow in the same way from
the actual vertex labels.

Both forced old sums are

$$
 \sum X=\sum Y=\sum_j(\beta_j+\gamma_j)
                    =3\pi-\sum_j\alpha_j.            \tag{3}
$$

Consequently:

**A boundary-preserving replacement by two nonnegative angle
tetrahedra exists if and only if the new internal angle is exactly
$2\pi$.** When this holds, (2) supplies the replacement and every
old triple sums to $\pi$. If the new non-internal angles are positive,
both old triples are positive. The three equatorial angle equations
are then also preserved; for instance

$$
 X_0+Y_1=\alpha_0,\quad
 X_2+Y_2=\alpha_1,\quad
 X_1+Y_0=\alpha_2.                                  \tag{4}
$$

This is an angular boundary statement, not an assertion that arbitrary
off-critical shape moduli or quantum integration cycles are transported
by this linear map.

In particular the angular image of an ordinary positive Pachner
chart, and its continuous closure with its angle marks retained,
has internal winding **one**. Exponentiating the edge equation and
then admitting every weak nonnegative winding locus forgets this
local support condition.

## 2. The certified face fails at the first reverse step

The last forward move in the six-move sequence is $(1,0)$:
old tetrahedron 1, face opposite its vertex 0, is adjacent to old
tetrahedron 0. The actual face maps identify the new tetrahedra
as final tetrahedra $0,1,2$ with orderings (1).

Their new edge is final global edge 7, locally $01$ in every new
tetrahedron. Its three opposite equatorial edges are final global
edges $8,6,3$, respectively.

At the oversized rational point the three new triples are

$$
 (0,1/20,19/20),\quad
 (0,2/5,3/5),\quad
 (0,1/10,9/10),                                      \tag{5}
$$

in units of $\pi$. Their new edge winding is zero. Formula (2)
would force the old triples

$$
 X=(13/10,13/20,21/20),\qquad
 Y=(27/20,7/10,19/20),                               \tag{6}
$$

each summing to $3$, rather than $1$. Equivalently, preserving the
three equatorial angles would require their sum to be zero, whereas
the sum of those six old angles is necessarily $2\pi$.

Thus the face cannot be pulled back even one step through the
previous nonnegative angular contour with its boundary marks fixed.
No earlier part of the six-move chain is needed to find the obstruction.
Each forced old local sum has an extra $2\pi$; removing it requires
a non-positive angle or a change of branch/boundary charge.

## 3. The exact actual five-term map

Use the cross-ratio convention

$$
 [p,q;r,s]=\frac{(p-r)(q-s)}{(p-s)(q-r)}.
$$

Normalize $D=\infty,A=0,B=1,C=x$. If $y$ is the old native
shape of $(B,E,C,A)$, then

$$
 E=\frac{xy}{x+y-1}.
$$

For the new native shapes $u,v,w$ of (1), direct substitution gives

$$
 \boxed{\quad
 u=\frac{x}{1-y},\qquad
 v=\frac{(1-x)(1-y)}{xy},\qquad
 w=\frac{y}{1-x},\qquad uvw=1.
 \quad}                                              \tag{7}
$$

The audit verifies these identities for the actual old and new
geometric shapes in the field $a^3-2a^2+3a-1=0$.

The inverse is

$$
 \boxed{\quad
 x=\frac{u(1-w)}{1-uw},\qquad
 y=\frac{w(1-u)}{1-uw}.
 \quad}                                              \tag{8}
$$

In the positive geometric branch the new edge has the marked relation

$$
 \operatorname{Log}u+\operatorname{Log}v+
 \operatorname{Log}w=2\pi i.                         \tag{9}
$$

For a positive tetrahedron with angles $(\alpha,\beta,\gamma)$,
the native shape is

$$
 z=e^{i\alpha}\frac{\sin\beta}{\sin\gamma}.
$$

At (5), $\alpha=0$ and $\beta+\gamma=\pi$, so all three radial
minimum shapes are exactly

$$
 u=v=w=1.
$$

Their marked log sum is zero, not $2\pi i$. The inverse (8) is
simultaneously $0/0$, on the norm divisor $1-uw=0$.
The weak point is not a limit of the positive geometric branch:
near three positive real unit shapes their principal arguments
are all small positive numbers and cannot sum to $2\pi$.

Away from the simultaneous corner, the inverse logarithmic connection
forms have genuine divisor residues

$$
 \operatorname{Res}_{1-uw=0}d\log x
 =\operatorname{Res}_{1-uw=0}d\log y=-1.              \tag{10}
$$

At the simultaneous corner the numerator zeros matter. Blow up by

$$
 u=1+\varepsilon A,\qquad w=1+\varepsilon B,
 \quad AB(A+B)\ne0.
$$

Then

$$
 x\longrightarrow\frac{B}{A+B},\qquad
 y\longrightarrow\frac{A}{A+B},\qquad x+y\longrightarrow1.
                                                            \tag{11}
$$

Thus the exceptional divisor retains the direction $A:B$.
Its finite old shapes cannot both lie in the upper half-plane,
since their sum is real. Formula (10) is a generic divisor
residue; it must not be copied unchanged to the simultaneous
corner where the numerator and denominator valuations cancel.

## 4. Exact comparison with the retained cyclic pentagon norms

Use the primitive pentagon of
[cyclic_tetrahedron_pentagon.md](cyclic_tetrahedron_pentagon.md),
with its actual centers and roots:

$$
 a_N^N=1-U,\qquad b_N^N=1-V,\qquad
 h_N^N=H=1-U+UV.
$$

The exact substitution for (7) is

$$
 U=w,\qquad V=x,\qquad H=1-y.                        \tag{12}
$$

Its left centers $(V,(1-V)U)$ are precisely $(x,y)$.
Its right centers are

$$
 \left(U,\frac{-UV}{1-U},\frac{V}{H}\right)
       =\left(w,\frac1{1-v},u\right).               \tag{13}
$$

The middle new shape has undergone the indicated quad rotation;
its center cannot be frozen at $v$.

Under (11), the three right norm-root powers behave as

$$
\begin{split}
 a_N^N&=1-w\sim-\varepsilon B,\\
 (h_N/a_N)^N&=\frac{1-y}{1-w}
                   \sim-\frac1{\varepsilon(A+B)},\\
 (a_Nb_N/h_N)^N&=\frac{(1-w)(1-x)}{1-y}
                   \sim-\varepsilon A.             \tag{14}
\end{split}
$$

Their valuations are therefore $(1/N,-1/N,1/N)$ on a compatible
root cover. The middle center in (13) goes to infinity. The
anchored cyclic pentagon theorem is localized away from these
norm divisors and does not itself supply this simultaneous
boundary extension or its source/co-source residues.

Equivalently, a small loop of $\varepsilon$ around zero, at fixed
generic direction $A:B$, changes the three compatible root frames by
$(Q,Q^{-1},Q)$, where $Q=e^{2\pi i/N}$. The two old norm roots
$b_N,h_N$ have no local winding at a generic finite direction.
This is a concrete root-torsor monodromy charge. It cannot be
removed by choosing the three right roots independently.

Norm-root zeros cannot justify deleting the wall. For example, in the
normalized finite atom of that note put $t=1-\text{center}$ and choose
the spectral root $\mu=(1-t)^{1/N}$. Its eigenvalues obey

$$
 f_0=1,\qquad f_j=\frac{t^{j/N}}{(\mu;Q)_j},
 \qquad D_j=\gamma f_j,\qquad
 \gamma^N=\left(\prod_jf_j\right)^{-1}.
$$

For $1\le j<N$, exactly one denominator factor vanishes:
$1-\mu\sim t/N$. All other factors are nonzero at a primitive
$N$th root, including composite $N$. Hence

$$
 \operatorname{ord}_tD_0=\frac{N-1}{2N},\qquad
 \operatorname{ord}_tD_j=\frac{2j-N-1}{2N}\quad(1\le j<N).
                                                            \tag{15}
$$

There are both zeros and poles for every $N\ge2$, while their
sum is zero. A vanishing norm root does not give a vanishing
operator or source.

This is consistent with the original
[cap-wall residue theorem](cap_wall_fermat_quad_residue_transport.md):
at its actual Fermat cusp a raw source has a compulsory simple
pole with nonzero cap residue. The relevant boundary extension
must retain those residues, the dual shift, and the central
Jacobian, rather than assign zero from the norm alone.

### A removable singularity for the full normalized local product

There is nevertheless a precise local extension, with a narrower
claim than separate atom or source extension. Fix a generic
holomorphic blow-up curve with
$x(0)=x_0\notin\{0,1\}$ and $y(0)=1-x_0$ as in (11). Choose
regular initial cyclic clock/shift frames and the compatible root
component of the strict primitive pentagon. Then its **full normalized
right three-atom product**, expressed between the common initial and
final frames, extends holomorphically and invertibly across the
ramified corner.

Indeed the left centers are $x$ and $y$, whose limiting values are
neither zero nor one. Their norm roots $b_N,h_N$ are therefore
locally nonzero holomorphic functions; their normalization determinants
are nonzero as well. The two left matrices are holomorphic and
invertible. The common final splitting roots are $b_N$ times the
initial first root and the initial second root divided by $h_N$;
they remain regular and nonzero. On the punctured compatible root
cover the exact pentagon identifies the right product with this
left product. The equality supplies its removable extension.

This conclusion retains all determinant roots and common-frame
identifications. A raw product must retain its raw scalar from
the pentagon theorem. No claim is made that its unnormalized
individual factors have removable singularities. The argument gives
no estimate uniform in $N$, no right to drop intermediate residues,
and no comparison with an original knot source unless the required
exterior source/co-source maps have also been transported.

## 5. The precise constructive target

The local classical support test is now explicit:
**an inverse positive angular Pachner replacement must retain new-edge
winding one, not merely the exponentiated equation $uvw=1$.**
For the certified excessive face, the failing move, its marked
integer defect, the norm divisors, and the direction $A:B$ are known.

The remaining quantum task is a matched source/carry extension of
this last move across (14), proving how its marked $2\pi$ charge is
represented and paired. Original integer degree conservation can
retain information lost modulo $N$, but no identification of that
integer carry with this geometric edge winding has been proved here.
The existing Ward augmentation shows that some wall charge survives;
it does not allow all walls to be discarded.

In particular we have not proved a zero quantum coefficient for
(5), nor inferred an oversized original period. What is available
for a general proof is a universal local angular admissibility
criterion and an exact divisor calculation on which the required
quantum source theorem can be tested.
