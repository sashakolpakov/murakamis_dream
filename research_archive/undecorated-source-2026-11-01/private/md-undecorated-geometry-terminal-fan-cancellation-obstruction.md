# Opposite terminal powers do not cancel the long fan as a tangle

The operation in the balanced-terminal construction inserts actual
quarter-turned elementary tangles. It does not insert a braid followed
by its inverse on one fixed axis. This distinction can be certified
by the fundamental group of a twofold branched cover, with all joining
strips kept fixed.

## 1. The literal stack from the attachment table

Let \(P_v=T^{-1}h_v\) be the original box exposed in its prescribed
product collar. For a right-side insertion the two old strips change by
\[
\begin{array}{c|c}
 v_1-x_1&v_1-w_1,\quad w_2-x_1,\\
 v_2-x_2&v_2-w_0,\quad w_3-x_2.
\end{array}
\tag{1}
\]
Here the physical endpoint tuple of the new factor is
\((w_0,w_1,w_2,w_3)\), and the ordinary stack joins the upper
endpoints of the lower factor to the lower endpoints of the next.
Thus a list of insertions on this same exposed side gives, in its
inherited order,
\[
 P_v h_{n_1}\cdots h_{n_k},\qquad h_n=T(R^n).
\tag{2}
\]
If each newest factor is inserted immediately beside \(P_v\), its
displayed order is reversed relative to the chronological insertion
order; this changes no assertion below. The left-side table similarly
prepends factors \(h_n\). In neither case does it alternate between
\(h_n\) and \(R^n\). These are exactly the two local strip tables
of `actual_all_circle_octahedral_decomposition.md` and the full fan
source adapter.

For odd \(n\), \(h_n\) has the crossing endpoint pairing
\((0,2),(1,3)\). An even list has the through pairing. Pairing
composition proves that no extra closed component is created, but it
does not supply a tangle isotopy. The actual quarter-turn is a rotation
of a four-ended ball; it is not a homomorphism for the chosen product.
In particular one cannot replace \(T(R^n)T(R^{-n})\) by
\(T(R^nR^{-n})\).

## 2. The marked branched cover of one factor

The twofold cover of a ball branched over a rational two-string tangle
is a solid torus. In this instance no classification theorem is needed:
start with the two straight strands, whose cover is the product of the
twofold branched cover of a two-point disk with an interval. The
two-point disk cover is an annulus, so the product is a solid torus.
The braid and quarter-turn are boundary homeomorphisms extending to
homeomorphisms of the corresponding branched pairs, and hence preserve
this solid-torus description while changing its marked boundary slopes.

On the boundary of the straight-strand cover choose a meridian
\(\mu_0\) and the longitude \(\ell_0\) given by the annulus core
over a joining disk containing the two upper endpoints. They intersect
once. A positive half twist of the two branch points lifts to one
Dehn twist about that annulus core: cut the two-point disk along the
joining branch arc, glue two copies with opposite banks, and the half
twist makes the resulting annulus banks wind once before regluing.
Consequently, after the braid \(R^n\), the solid-torus meridian has
the boundary class
\[
                       \mu_0+n\ell_0,
\tag{3}
\]
up to the simultaneous orientation signs fixed by the original disk
frame. The quarter-turn exchanges the two separating curves on the
four-punctured sphere, so exchanges \(\mu_0,\ell_0\) up to sign
on its torus cover.

It follows that, for \(h_n=T(R^n)\), the core of the annulus over
the actual product-joining disk has image \(\pm n\) times a
generator of the solid torus's fundamental group. Equivalently, before
the quarter-turn this joining curve is \(\mu_0\); modulo the
meridian relation (3), it is \(-n\ell_0\). The signs depend on
the chosen orientation of the annulus and do not affect its nonzero
multiplicity \(|n|\).

This is the precise place where the actual fan differs from ordinary
braid stacking. For the unturned braid the joining annulus core is
\(\ell_0\), of multiplicity one for every \(n\), and inverse
braids do cancel. In the turned factor its multiplicity is \(|n|\).

## 3. The exact obstruction for opposite powers

Stacking two factors identifies their joining disks with the two branch
points and their ordered boundary paths. On the branched covers this
glues the two solid tori along the corresponding annulus. For nonzero
\(n,m\), both annulus inclusions are injective on fundamental groups.
Van Kampen therefore gives
\[
 \pi_1\bigl(\widetilde{h_nh_m}\bigr)
     =\langle a,b\mid a^n=b^{\eta m}\rangle,
 \qquad \eta\in\{1,-1\},
\tag{4}
\]
where \(\eta\) records the fixed gluing orientation. Quotienting
by the common element in (4) gives
\[
                         C_{|n|}*C_{|m|}.
\tag{5}
\]
This group is nonabelian when both \(|n|,|m|\ge2\). Thus the
group (4) cannot be cyclic. The cover of the identity two-string
tangle is a solid torus with fundamental group \(\mathbb Z\),
so \(h_nh_m\) is not isotopic relative to its four marked endpoints
to that identity tangle.

For the potentially misleading inverse-power pair \(m=-n\), even
abelianization already distinguishes it:
\[
 H_1\bigl(\widetilde{h_nh_{-n}};\mathbb Z\bigr)
                  \cong\mathbb Z\oplus\mathbb Z/|n|.
\tag{6}
\]
The torsion is independent of \(\eta\). It is nontrivial for
\(|n|\ge2\), whereas the identity tangle's cover has torsion-free
first homology. Opposite rational fractions or opposite signed powers
therefore do not give cancellation in this product collar.

More generally an ordered stack of \(k\ge2\) such factors has
the iterated annular amalgam. Quotienting by its common annulus class
gives \(C_{|n_1|}*\cdots*C_{|n_k|}\). If all \(|n_i|\ge2\),
this excludes identity-tangle cancellation for the whole stack,
irrespective of signs or an even number of factors. The fan theorem's
added powers are odd and independently sufficiently long, so they
lie in this range. The argument makes no claim for the exceptional
unit powers, where (5) no longer supplies an obstruction.

## 4. What this does and does not establish

The retained even endpoint pairing in the fan theorem is compatible
with the nontrivial branched-cover topology above. It is not a claim
that paired terminal pieces can be removed while retaining the core
knot. The independently signed long-filling quantifier introduces no
local inverse-pair cancellation: every factor remains a turned rational
tangle whose joining-annulus multiplicity is its power's absolute value.

This proves the requested local obstruction from the actual attachment
maps. It does not claim that every decorated closure is nonisotopic to
every possible core closure; special global coincidences would require
their own argument. The published construction correctly says that it
preserves the endpoint pairing and generally changes the knot. No
operation in the present note changes an original knot or supplies an
undeformed full-source volume bound.
