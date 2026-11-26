# What triangular substitution preserves in the full source

This note pressure-tests the triangular-block identity in
md-cap-triangular-block-response-invariance.md. That identity is correct
at the level of complete triangle entropy and the original coefficient
targets. It does not, by itself, promote a full knot-volume theorem
from a smaller diagram to a larger one.

Three precise conclusions are available. Arbitrary triangular
substitution preserves the complete boundary pressure up to a constant.
At a protected triangular attachment there is an exact finite
factorization on one odd complete-node spectral slice. On the other
hand, arbitrary substitution can destroy weak balance and can import
the certified R54 obstruction to the same shared-radius envelopes.
An independently variable joining spectrum is a substantive remaining
obligation, not a change of notation.

All sources in this note are the literal matched-sphere Morse sources.
All diagram constructions are made before the level tends to infinity.
Only private statements are recorded here.

## 1. The classical identity and its precise hypotheses

Let \(P\) be a triangulated disk with boundary \(abc\), with distinct
boundary vertices, such that capping by \(abc\) gives a simple
triangulated sphere. All \(k\) interior vertices are ordinary, each
with target one in the normalized action. No restriction on separating
triangles or internal cycles is required. With the original triangle
potential \(Q\),
\[
 \mathcal{Q}_P(a,b,c)=
 \inf_{\ell_i>0}
 \left\{\sum_{t\subset P}Q_t(\ell)-\sum_{i\in P^\circ}\log\ell_i\right\}
 =Q(a,b,c)+C_P.                                      \tag{1}
\]

For positive boundary radii, the fixed-boundary packing theorem
constructs the unique strict interior solution. Its center triangles
develop to the prescribed boundary center triangle with degree one.
Thus the aggregate angle at each boundary vertex equals the angle of
that triangle. The three derivatives of the difference in (1) vanish:
\[
 \partial_{\log a}\mathcal{Q}_P
 =\frac{\Theta_a}{2\pi}
 =\frac1\pi\arctan\frac{a}{\sqrt{ab+bc+ca}}
 =\partial_{\log a}Q,                               \tag{2}
\]
and similarly at \(b,c\). The positive octant is connected. This fixes
the additive constant as \(\mathcal{Q}_P(1,1,1)-Q(1,1,1)\).

The corresponding compact concave entropy identity is
\[
 \mathcal{E}_P(\alpha_a,\alpha_b,\alpha_c)
 =\sum_{i=a,b,c}f(\alpha_i)+C_P,\qquad
 \alpha_i\ge0,\quad\sum_i\alpha_i=\frac12.             \tag{3}
\]
It follows by closed concave duality from (1). In particular, a
protected boundary coordinate has aggregate load zero, hence every
corner there has load zero. This retains the original targets
exactly. One or two protected boundary vertices are allowed; three
protected corners are not. The supported Hall and boundary-exclusion
arguments in the earlier note supply finite interior multipliers.

The supporting geometric inputs are the fixed-boundary construction in
actual_smoothed_source_capacity_blocks.md, section 4, the simple-sphere
packing in actual_balanced_terminal_fan_volume.md, section 2, and the
source-normalized entropy in actual_triangle_entropy_algebraic_balance.md.
No statement about a noncentral local spectral polynomial is used in
(1)–(3).

## 2. Literal matching and the actual augmented volume

To substitute \(P\) for a triangle \(t\) of a matched sphere, supply
a matched simple sphere \(B=P\cup f\), where \(f=abc\) is the removed
face. Let \(g\) be the triangle matched to \(f\). If \(t'\) is the
triangle matched to \(t\), identify the boundary so that their matched
sides agree, delete \(t,f\), and pair \(t'\) with \(g\). Keep all
remaining matching edges and oriented face orders.

Every interior vertex of \(P\) is new. Thus the result is again a
simple oriented triangulated sphere; the two triangles at the new
matching edge have four distinct vertices. A protected mark on a
boundary side is retained only when that side is nonmatching in both
inputs. If the mark lies outside the replaced triangle, it is
untouched. These conditions are needed: an abstract triangulation
with a newly selected matching is not the same recorded diagram.

The inverse-cut theorem gives the resulting augmented link in
\(S^3\), with its own primitive disk meridians and longitudes.
The connected matching graph admits a knot-producing parity pattern
by the original spanning-tree pairing argument. This does not assert
that an arbitrary preassigned parity pattern survives the substitution.
The substitution can change knot type.

Applying (1) before optimizing the old variables gives
\[
 \Phi_{\mathrm{new}}=\Phi_{\mathrm{old}}+C_P,\qquad
 \operatorname{Vol}(Y_{\mathrm{new}})
   =2\pi(\Phi_{\mathrm{old}}+C_P).                    \tag{4}
\]
The second equality uses the actual complete simple-sphere metric and
its original fundamental chain. It is not an identification of the
filled complements. Sufficiently long primitive fillings of this
fixed new diagram are geometrically realized by the general-Morse
completion theorem. Their filled volume is its selected continued
action, rather than an asserted sum of independently filled volumes.
Without a full-source estimate, this geometric conclusion is not a
limit theorem for the full invariant.

## 3. Arbitrary substitution does not preserve weak balance

Consider a matching edge with nonnegative curvatures
\((x,b,c,y)\), \(A=x+y>0\), and keep the opposite triangle
\((x,c,y)\) fixed. Repeated stellar insertion only in the triangle
on the \(b\) side is a special case of triangular substitution.
Its actual packing curvatures are
\[
 b_j=b+2j\sqrt{Ab+xy}+j^2A
     =A\left[(u+j)^2-\delta\right],\quad
 u=\sqrt{b/A+\delta},\quad\delta=xy/A^2.              \tag{5}
\]
This is the literal positive Descartes insertion, with the original
matching edge retained. The other old curvatures, including \(c\),
do not move.

For fixed \(x,y\) with \(A>0\), the triangle entropy gives
\[
 Q(x,t,y)-\frac12\log t\longrightarrow0
 \quad(t\longrightarrow\infty).                     \tag{6}
\]
Indeed its variational formula, after subtracting
\(\frac12\log t\), has nonnegative maximum and penalizes every
positive outer load by a logarithm tending to minus infinity.
Compactness forces the maximizing loads to the middle simplex vertex,
where the entropy is zero. This proof also permits one zero outer
curvature.

Consequently the inherited matching edge satisfies
\[
 Q(x,b_j,y)+Q(x,c,y)-\log b_j
 =Q(x,c,y)-\frac12\log b_j+o(1)\longrightarrow-\infty.
                                                               \tag{7}
\]
It eventually violates even nonstrict complete weak balance.
Every new matched edge created by this particular fan has its newly
inscribed curvature as an outer weight, larger than either middle,
so those new matching edges satisfy the elementary strict balance
test. The failure is at the inherited interface.

This is a structural obstruction across arbitrary size, not a
floating-point example. Starting with any covered weak-balanced core
does not prevent it. Even numbers of inserted odd terminal pieces may
be used, preserving the original four-endpoint pairing and hence its
existing knot test; this still can change knot type. It disproves
inheritance of the weak-balance hypothesis under arbitrary triangular
substitution, not a volume theorem for the resulting knots.

## 4. A protected attachment imports a certified envelope obstruction

There is a stronger obstruction to promoting the same shared-radius
method. Let a fixed marked core \(D\) have protected nonmatching edge
\(uv\). Choose one incident triangle \(t=(u,v,B)\); it is a singleton
row after the protected specialization. Its matching edge is one of
\(uB,vB\), since \(uv\) is nonmatching.

In the certified R54 sphere the mark is \(29\!-\!50\). The two incident
faces are
\[
 (29,50,22),\qquad(50,29,0).
\]
Remove \(f=(29,50,22)\), face 34 of the certificate. It belongs to
crossing 28, whose quartet is \((29,50,45,22)\), and is matched
to \(g=(29,22,45)\), face 97. The selected left region 32, with
quartet \((0,50,16,29)\), uses faces 39 and 62, so neither of its
triangles is removed.

Glue this punctured sphere into \(t\), identifying \(22\) with \(B\)
and the protected pair with \(u,v\), with the matching edge aligned.
An orientation reversal of the entire block, if required, transports
all cyclic orders and the chosen left/right label together. It does
not select a different local comparison function. The new sphere has
\(R_D+53\) matching edges. Its selected noncentral region is the
inherited R54 region; all other regions are central.

Let \(G_{54}\) be the exact convex envelope for that fixed R54 string,
and \(P_D\) the complete core action before minimization. Let
\(q_B=\log B\). Each of the two removed triangles contributes
exactly \(q_B/2\). On merging the sources, the ordinary target at
\(B\), previously counted once in each input, is counted once.
Thus the weighted functions satisfy the exact identity
\[
 G_{\mathrm{new}}(q_D,q_{\mathrm{int}})
       =P_D(q_D)+G_{54}(q_{\mathrm{int}},q_B).         \tag{8}
\]
Every coordinate is shared as indicated; none has been independently
optimized per incidence. Homogeneity makes the infimum of \(G_{54}\)
independent of the prescribed finite \(q_B\). Taking infima in (8)
therefore proves
\[
 \mathcal{C}_{\mathrm{new}}=\Phi_D+\mathcal{C}_{54},
 \qquad
 \Phi_{\mathrm{new}}=\Phi_D+\Phi_{54}.                \tag{9}
\]
The second identity is the complete version of the same calculation,
or (1) with this protected boundary. No attainment of the noncentral
infimum is required.

The public certificate gives
\[
 \mathcal{C}_{54}>\Phi_{54}+\frac15,
 \qquad
 \mathcal{C}_{\mathrm{new}}>\Phi_{\mathrm{new}}+\frac15. \tag{10}
\]
In particular no shared-radius weak-balance or strict-restoration
argument using these same local envelope functions can be inherited
under arbitrary block substitution. This imports an obstruction into
any such marked core, including cores for which a full volume theorem
is already known. It still is not a lower bound for the signed
coefficient, the full spectral supremum, or the filled invariant.
This proposition concerns envelope capacity; it makes no additional
claim here about all-level support after gluing.

The exact R54 incidence above was read from
experiments/actual_singleton_sector_obstruction_certificate.json.
The only numerical inequality imported in (10) is the already
certified theorem of actual_singleton_sector_envelope_obstruction.md;
no new optimizer or uncertified value enters this argument.

## 5. A genuine finite factorization on a protected odd endpoint slice

There is an exact finite statement, narrower than full spectral
substitution. Let both closed matched spheres have their mark on
\(uv\), and glue protected singleton triangles as in section 4.
Write \(e_D,e_B\) for their matching regions and \(e_*\) for the
merged region. For odd \(N=2m+1\), \(d=2m\), use the original
homogeneous numerator \(S_N\), with all ordinary targets \(d\).

At the simple complete node, the literal local formula is
\[
 H_{V_N(-2)}(x,b,c,y)
      =N^2D_N(x,b,y)D_N(x,c,y),\qquad
 D_N(0,0,B)=B^m.                                    \tag{11}
\]
The endpoint determinant has degree \(m\). Its normalization follows
from the original \(R_m\) recurrence: \(D_N=R_m/N\), and both pure
outer and pure middle coefficients equal one by the root sine-product
identities. Thus (11) keeps the \(N^2\) scalar, not merely its
exponential rate.

Specialize the merged spectrum to \(-2\); every other original
spectrum is arbitrary. The old marked-region factors are
\[
 N^2B^mD_{t'},\qquad N^2B^mD_g,
\]
whereas the merged factor is \(N^2D_{t'}D_g\).
After extracting all targets in either punctured input except \(B\),
homogeneity leaves exactly degree \(m\) in \(B\). That partial
polynomial is therefore a scalar multiple of \(B^m\), regardless of
the other spectra or phases. The final \(B^d\) extraction gives
\[
 S_{N,\mathrm{new}}(\boldsymbol\sigma,\boldsymbol\tau;
                    \sigma_{e_*}=-2)
 =N^{-2}
 S_{N,D}(\boldsymbol\sigma;\sigma_{e_D}=-2)\,
 S_{N,B}(\boldsymbol\tau;\sigma_{e_B}=-2).             \tag{12}
\]
This is a complete finite coefficient calculation, not an
entropy approximation. It applies to the original full homogeneous
sources on that slice. No independent boundary coefficient target was
introduced.

At this node the local full numerator is central. Hence the central
parts obey the same factorization. If both input diagrams have full
source remainder estimates with gaps \(\gamma_D,\gamma_B\) and full
source upper rates at most their complete actions, then (12) gives
an odd-level full remainder gap at least
\(\min(\gamma_D,\gamma_B)\) on the merged slice. This permits every
other spectral variable to vary on its full real interval.

It does not permit the merged variable to vary. A filling functional
there uses the whole spectral polynomial, including paired-node
derivative data; its value at the odd simple node does not determine
that functional. Fixing this node is also not the same as inserting
the zero crossing power. Thus (12) alone gives no new fully filled
knot-volume theorem.

## 6. Why scalar contraction fails for the full spectral polynomial

The failure is visible at a single original stellar attachment at
level \(N=3\), so it does not depend on endpoint asymptotics.
Put \(A=x+y\), and set
\[
 a_s=(s-1)(s+2),\qquad b_s=(s-1)^2.
\]
The original face Casimir has diagonal \(1,-2,1\), one-step entries
\(-3(x+y)\), and two-step entry \(-3xy\). Since
\(\chi_3(s)=s^3-3s+2\), its polynomial resolvent is
\(s^2I+s\Omega+\Omega^2-3I\). The exact homogeneous numerator is
\[
 H_3(x,b,c,y;s)
 =a_s(b^2+c^2)+b_sbc
   +3(1-s)(x+y)(b+c)
   +9(x+y)^2-3(s+2)xy.                              \tag{13}
\]

The actual stellar ordering is
\[
 \mathcal{B}_3=[w^2]\,
 H_3(x,w,c,y;s)\,H_3(b,y,x,w;t).                     \tag{14}
\]
In particular its new quartet has input middle \(y\), output middle
\(x\); it has not been reflected to a preferred order.
Its coefficients satisfy
\[
 [b^2]\mathcal{B}_3=[c^2]\mathcal{B}_3=9a_s,\qquad
 [bc]\mathcal{B}_3=3(4-t)b_s.                           \tag{15}
\]
At \(s=t=0\), equality with a scalar multiple of the old \(H_3\)
would force that scalar to be \(9\), from \(b^2\), whereas its
\(bc\) coefficient is \(12\), rather than \(9\). Thus even an
arbitrary scalar depending on both spectral parameters cannot make
the full inserted kernel equal to the old kernel. Both parameters
here lie in the physical real spectral interval.

At the complete node \(s=-2\), the same calculation instead gives
\[
 \mathcal{B}_3=3(4-t)H_3(x,b,c,y;-2),                    \tag{16}
\]
which illustrates why a complete-node scalar calculation can look
promising while failing away from that node. No large-level
exponential obstruction follows from this finite example. It only
disproves the proposed exact scalar identity on which a direct
full-source promotion might otherwise rely.

## 7. The available full-volume consequence and the remaining estimate

For a given substituted diagram, a genuine full volume theorem follows
if its new complete packing satisfies the existing weak-balance or
quantified-defect hypothesis. Equation (1) makes this a modular
geometric check:

* every matching edge disjoint from the substituted triangle and its
  matching neighbor has its old four curvatures and old comparison;
* the new internal matching edges use the fixed-boundary block
  packing;
* the single inherited matching edge uses its new block-side middle
  and the unchanged opposite middle.

If these last two sets of comparisons hold, the existing full-source
theorem applies to the actual new source at both parities, the finite
Hermite functional restores every independent long filling, and the
general-Morse primitive completion identifies the rate with the
actual new knot-complement volume. The diagram, parity pattern and
powers are fixed before \(N\) grows. This is a useful local way to
check the existing theorem, not a new criterion implied by arbitrary
block topology.

To transfer a full theorem without those new comparisons, one still
needs a bound for the partially extracted, matrix-valued or
polynomial-valued block on the original shared boundary variables,
uniform in its independent real spectra and with the true Hermite
normal data retained. It must control every newly introduced
noncentral sector and the inherited interface. The complete pressure
identity (1), an odd fixed-node factorization (12), and a cap gap with
all other spectra fixed do not supply this estimate. Equations
(7), (10), and (15) show three distinct reasons why the most immediate
promotions fail.

The most general unconditional geometric statement retained here is
(4), together with actual long primitive completion of the new
simple-sphere diagram. The most general new finite contraction proved
here is (12). No unconditional full invariant-volume equality for
arbitrary triangular substitutions has been established.
