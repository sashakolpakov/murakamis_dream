# Full source certificates are closed under protected triangular sums

This note proves a constructive closure theorem for full source
certificates. The inputs are actual marked simple-sphere diagrams
whose phase-uniform local envelopes admit an unabridged finite
shared-radius certificate. The output is their literal protected
triangular sum. Its full source has a strict complementary gap at
both level parities, and its independently sufficiently long fixed
signed fillings satisfy the volume limit for the actual new knot.

The result is stronger than invariance of one cap response. It does
not claim that arbitrary triangular blocks preserve a source bound.
In particular the certified R54 block does not satisfy the input
certificate hypothesis. If the inputs are weak-balanced, the output
is itself weak-balanced; this part is a constructive closure
corollary within that existing theorem, not a new analytic condition.

**Closure theorem.** Any fixed finite sequence of the protected
triangular sums defined below preserves an unabridged certificate.
For every half-twist pattern passing the assembled diagram's original
knot test, all independently sufficiently long fixed signed primitive
fillings then satisfy the full reduced-invariant volume limit (22).
The required threshold may depend on the entire fixed assembled
diagram and pattern. Section 7 gives arbitrary finite sizes for which
the resulting marked complete packing fails weak balance, using an
existing seventeen-region finite-cover certificate.

## 1. The diagrams, local envelopes, and exact certificate hypothesis

An input \(D\) is a fixed connected oriented simple triangulated
white sphere, a perfect matching of its dual triangles, the literal
inverse-cut diagram in \(S^3\), its cyclic crossing orders and disk
framings, and a marked nonmatching edge \(uv\). The two protected
face variables are exactly \(L_u=L_v=0\). Every other vertex has the
original target \(d=N-1\). Write \(R_D\) for their number, which is
also the number of matching regions.

The white sphere is the combinatorial record of the two reflected
polyhedral pieces obtained by cutting the augmented diagram. A
matched pair of white triangles records one crossing circle and its
twice-punctured disk. The inverse-cut construction retains the order
of the four adjacent white faces and the disk framing; these are part
of the data, not choices made after the gluing.
Let \(Y_D\) denote the complete augmented exterior in \(S^3\), before
filling its crossing-circle cusps and with the main strand components
retained. Its positive convex cell realization is supplied by the
simple-sphere construction in
[the terminal-fan theorem, §§2–4](actual_balanced_terminal_fan_volume.md).
The literal diagram realization and primitive disk curves are those of
[the general Morse geometric theorem, §§1–2](actual_morse_geometric_contribution.md).

Use the source-normalized complete triangle potential
\[
 Q(w_1,w_2,w_3)=
 \max_{\substack{\alpha_i\ge0\\\sum\alpha_i=1/2\\
                  \alpha_i=0\ \text{if}\ w_i=0}}
 \left\{\sum_i f(\alpha_i)+\sum_{w_i>0}\alpha_i\log w_i\right\},
 \quad
 f(t)=\frac{\Lambda(\pi t)+\Lambda(\pi/2-\pi t)}{\pi}.
                                                               \tag{1}
\]
Here \(\Lambda(s)=-\int_0^s\log|2\sin t|\,dt\) is the
Lobachevsky function; only \(0\le t\le1/2\) occurs in \(f(t)\).
Zero coordinates are deleted from the supported simplex. Thus, for
example, \(Q(0,0,B)=\tfrac12\log B\) exactly.
At an ordered quartet \((x,b,c,y)\), the input and output triangles
are \((x,b,y)\) and \((x,y,c)\). Put
\[
 \begin{split}
 A_C&=Q(x,b,y)+Q(x,c,y),\\
 A_L&=\max\{\log c,Q(x,b,y)+\tfrac12\log c\},\\
 A_R&=\max\{\log b,Q(x,c,y)+\tfrac12\log b\}.
 \end{split}                                                   \tag{2}
\]
left is absent when \(c\) is protected; right is absent when \(b\)
is protected. These are the proved bounds for the actual local
path pieces, uniform in their real spectral parameter and all
face phases. central includes its original odd central row. The
physical reflected order, rather than an arbitrary relabeling of a
matrix, supplies right.

For each locally allowed label string \(\omega\), define
\[
 G_{D,\omega}(q)
       =\sum_e A_{e,\omega_e}(e^q)-\sum_{f\ne u,v}q_f,
 \qquad
 \mathcal C_{D,\omega}=\inf_{q\in\mathbb R^{R_D}}G_{D,\omega}(q).
                                                               \tag{3}
\]
Protected coordinates are kept zero in this notation. Complete
simple-sphere geometry gives a finite positive stationary vector,
modulo a common scale, and
\[
 \mathcal C_{D,C}=\Phi_D
        =\frac{\operatorname{Vol}(Y_D)}{2\pi}.                  \tag{4}
\]

**Certificate hypothesis.** There is \(\gamma_D>0\) such that
for every locally allowed string \(\omega\ne C\), a positive shared
ordinary vector \(L^{D,\omega}\) satisfies
\[
 G_{D,\omega}(\log L^{D,\omega})
                  \le\Phi_D-\gamma_D.                         \tag{5}
\]
Different strings may use different vectors. Each vector is shared
by all incidences of its face; there is no independently chosen
weight for a triangle corner or crossing incidence.

A finite branch cover using maxima of the allowed local rates is
sufficient for (5), by assigning each string to a branch that covers
it. There are finitely many strings for a fixed input. Conversely,
one witness per string is a finite cover. This is a hypothesis about
the original phase-uniform envelopes, not merely a bound for a
signed coefficient at a selected spectrum.

The cover must be unabridged: it covers every locally allowed
noncentral string, including one whose final shared coefficient
might vanish identically for a separate reason. A certificate that
omits strings by a global support or cancellation argument is not
automatically an input to this theorem. No transfer of such an
omission is assumed. Protected-overloaded labels are the only
automatic omissions used here.

Multiplying all ordinary weights by \(t>0\) increases each triangle
potential by \(\tfrac12\log t\), and each local rate by \(\log t\).
Since there are \(R_D\) rates and \(R_D\) ordinary targets, every \(G_{D,\omega}\)
is invariant under \(q\mapsto q+t\mathbf1\). Thus a whole witness
may always be normalized at any specified ordinary face.

## 2. The oriented protected triangular sum

Choose a triangle incident to the marked edge in each of two
inputs. Identify their three boundary vertices so that the
protected pair is \(u,v\), the ordinary third vertex is \(B\),
and their matched boundary sides agree. Record the orientations as
\[
 \begin{array}{c|c|c}
 &\text{removed triangle}&\text{original quartet}\\ \hline
 D_1&(u,v,B)&(u,v,c,B)\\
 D_2&(u,B,v)&(u,a,v,B).
 \end{array}                                                   \tag{6}
\]
The two removed faces have opposite orientations. The ordinary
vertices \(a,c\) are distinct after relabeling the interiors.
If a reflection of an entire input is needed to achieve these
conventions, transport its complete cyclic orders, source labels
and crossing signs with that reflection. The envelope functions
and absolute volume are unchanged.

Delete the two faces, glue their boundary triangles, remove their
two matching pairs, and pair their former partners. The retained
triangles are
\[
                  (u,a,B),\qquad(u,B,c),
\]
so the merged crossing has the exact quartet
\[
                         (u,a,c,B).                            \tag{7}
\]
Keep every other oriented face, matching edge and local order.

The two punctured spheres are triangulated disks with disjoint
interiors and no additional common
vertices. Their union is a simple oriented triangulated sphere.
The merged matching edge \(uB\) has four distinct incident vertices;
all remaining matching pairs were already valid. The edge \(uv\)
is retained and remains nonmatching. Every triangle is paired once.
The count is
\[
 R=R_1+R_2-1,\qquad
 |V|=R+2,\quad |F|=2R,\quad |E|=3R.                            \tag{8}
\]
Only \(u,v,B\) are identified; every other ordinary coordinate in
one input is distinct from every such coordinate in the other.

The original inverse-cut construction therefore realizes the new
data as an augmented link in \(S^3\), with its own primitive disk
curves. This is an operation on recorded diagrams, not only an
abstract tensor contraction. A knot-producing pattern can be obtained
directly. The untwisted physical strands form projection circles,
and a box joins the two circles that pass through its disk. Their
adjacency graph is connected because the original four-valent
diagram is connected. Choose a spanning tree, switch precisely its
boxes to the odd terminal pairing, and leave all others even.
Each tree edge joins two distinct current components; induction
leaves a single main component. Either odd sign is allowed.
This is the marked construction of
[the inverse-cut source theorem, §3](research_matched_sphere_morse_source.md).
The theorem below permits any parity
choice passing the new diagram's original one-component test, with
no internally closed extra main component. It does not assert that
arbitrary old parity choices can be merged without that test.

## 3. The complete action and the original target correction

Put \(q_B=\log B\), \(Q_a=Q(0,a,B)\), and \(Q_c=Q(0,c,B)\).
The two old complete bridge rates and the new one are
\[
 C_1=\tfrac12q_B+Q_c,\qquad
 C_2=Q_a+\tfrac12q_B,\qquad
 X=Q_a+Q_c=C_1+C_2-q_B.                              \tag{9}
\]
Every other complete triangle rate is retained. On the other hand,
the combined ordinary target at \(B\) is counted once, rather than
once in each input. Write \(P_i=G_{D_i,C}\) and
\(P_{\mathrm{new}}=G_{\mathrm{new},C}\). Thus
\[
 P_{\mathrm{new}}(q_1,q_2)
                   =P_1(q_1)+P_2(q_2)                        \tag{10}
\]
whenever the two displayed vectors agree at \(B\). This is an
identity of the full shared functions, not an inequality between
separately optimized local terms.

Normalize both complete minimizers by \(q_B=0\). They then combine
to a minimizer of (10); conversely (10) is bounded below by the sum
of their minima. Hence
\[
                    \Phi=\Phi_1+\Phi_2.                       \tag{11}
\]
This also proves that the original complete curvatures on each
piece are unchanged after their common rescaling. The complete
simple-sphere theorem identifies \(2\pi\Phi\) with the actual
new augmented volume. It does not identify independently filled
input manifolds with the filled output manifold.

## 4. Every genuine sector at the merged crossing

The variational formula (1), using the simplex vertex at \(B\),
gives
\[
                    Q_a,Q_c\ge\tfrac12q_B.                   \tag{12}
\]
They are strictly larger because \(a,c,B\) are ordinary and positive.
No positivity of \(q_B\) itself is needed.

At the old first crossing only left survives among the one-sided
labels, and at the old second only right survives among them:
\[
 L_1=\max\{q_c,\tfrac12q_B+\tfrac12q_c\},\qquad
 R_2=\max\{q_a,\tfrac12q_B+\tfrac12q_a\}.                       \tag{13}
\]
The new local rates are
\[
 L=\max\{q_c,Q_a+\tfrac12q_c\},\qquad
 R=\max\{q_a,Q_c+\tfrac12q_a\}.                                \tag{14}
\]
Together (9) and (12) give all three required cases:
\[
 \begin{array}{c|c|c}
 \text{new label}&\text{input labels}&\text{rate comparison}\\ \hline
 C&(C,C)&X=C_1+C_2-q_B\\
 L&(L,C)&L\le L_1+C_2-q_B\\
 R&(C,R)&R\le C_1+R_2-q_B .
 \end{array}                                                  \tag{15}
\]
For example
\[
 L_1+C_2-q_B
  =\max\{q_c+Q_a-\tfrac12q_B,\ Q_a+\tfrac12q_c\}
  \ge\max\{q_c,Q_a+\tfrac12q_c\}=L.
\]
The right case is identical with \(a,c\) exchanged. The inequality
retains the mixed branch of the genuine one-sided rate; it is not
a replacement by a pure-middle monomial.

For a whole output string \(\omega\), leave every other local label
on its original input and use (15) at the merged crossing. This
defines input strings \(\omega_1,\omega_2\). They are locally
allowed; no protected-overloaded side was introduced. If the output
is noncentral, at least one input string is noncentral. The one
target correction in (10) now gives
\[
 G_{\mathrm{new},\omega}(q_1,q_2)
             \le G_{1,\omega_1}(q_1)+G_{2,\omega_2}(q_2),
                    \qquad (q_1)_B=(q_2)_B.                  \tag{16}
\]

For a noncentral input choose its witness (5); for a central input
choose its complete minimizer. Rescale each whole vector to \(B=1\).
Homogeneity changes none of these actions. The vectors now agree
on every shared coordinate: \(u,v\) are zero and \(B=1\). Hence
they form one legal shared Cauchy vector for the new source.
Equations (11) and (16) prove
\[
 G_{\mathrm{new},\omega}\le
       \Phi-\min(\gamma_1,\gamma_2)
                   \qquad(\omega\ne C).                      \tag{17}
\]
If both input strings are noncentral their losses add. Per-sector
witnesses are essential to this simple statement: the other input
can use its complete minimizer when its induced string is central.
There is no claim that one input witness vector works for every
case simultaneously.

Equivalently, taking infima after the \(B=1\) normalization gives
\[
 \mathcal C_{\mathrm{new},\omega}
       \le\mathcal C_{1,\omega_1}+\mathcal C_{2,\omega_2}.       \tag{18}
\]
No existence of a noncentral capacity minimizer is needed.

## 5. The full finite source and the volume limit

Set \(q_N=e^{\pi i/N}\), \(d=N-1\). The local polynomial
\(H_{V_N}\) is the original homogeneous face numerator of
\[
 V_N(\sigma;\Omega)=\chi_N(\sigma)(\sigma-\Omega)^{-1},
 \qquad \chi_N(\sigma)=2T_N(\sigma/2)+2,                 \tag{19a}
\]
where \(\Omega\) is the original two-strand Casimir and the right
side denotes its degree-\(d\) polynomial numerator, including at
the repeated roots. \(T_N\) is the Chebyshev polynomial.
In its face expansion, a recurrence path from index \(j\) to \(i\)
has middle powers \(b^ic^{d-j}\). If \(h=\lfloor d/2\rfloor\),
central means \(i\le h\) and \(d-j\le h\), left means \(d-j>h\),
and right means \(i>h\). These supports are disjoint and exhaustive.
This fixes the source normalization and the meaning of every label
used above.

The original full numerator is
\[
 S_{N,\mathrm{full}}(\boldsymbol\sigma)
 =[\prod_{f\ne u,v}L_f^{N-1}]\,
       \left.\prod_eH_{V_N}(L_x,L_b,L_c,L_y;\sigma_e)
       \right|_{L_u=L_v=0}.                                  \tag{19}
\]
The actual Morse identity includes the unrestricted physical mark,
all cup and cap factors, the even coset and the face measure. No
additional mark or factor \(N\) is introduced at the triangular sum.
Each local polynomial has degree at most \(N-1\) in its spectral
variable. The C/L/R partition and rates (2) are valid at both
parities and uniformly over all face phases and
\(\sigma_e\in[-2,2]\).
The literal coefficient identity is
[the general Morse source theorem, §§5–6](research_matched_sphere_morse_source.md);
the phase-uniform estimates (2) are the cofactor bounds used in
[the finite-cover theorem](general_actual_sector_cover_filling_volume.md)
and [weak balance, §§4–6](general_weak_balance_volume.md).

Use the vector supplied by (17) for each genuine noncentral string.
Cauchy's coefficient inequality, with the original targets \(N-1\),
gives its rate at most \(\Phi-\gamma\), where
\(\gamma=\min(\gamma_1,\gamma_2)>0\). Replacing the normalized
targets by one costs only a fixed logarithmic term divided by \(N\).
The finite number of factors, polynomial prefactors and local
uniform errors contribute \(o(N)\) for the fixed new diagram.
There are only finitely many strings. Therefore
\[
 \limsup_{N\to\infty}\frac1N
 \log\|S_{N,\mathrm{full}}-S_{N,C}\|_{[-2,2]^R}
                    \le\Phi-\gamma.                         \tag{20}
\]
The limit superior includes even, odd and composite levels. This
proves a bound for the entire complementary polynomial, not merely
a fixed endpoint slice.

Apply the finite Hermite functional of Appendix N,
equivalently [the uniform filling bound](actual_uniform_filling_supremum_bound.md),
to (20). It inserts the original power \(R^{n_e}\), including the
normal data at double spectral roots. More precisely, the original
reduced ribbon contraction is
\[
 Z_N(\boldsymbol n)=
       \left(\bigotimes_e\mathcal L_N^{n_e}\right)S_{N,\mathrm{full}},
 \qquad
 \left\|\bigotimes_e\mathcal L_N^{n_e}\right\|
       \le\prod_e(1+|n_e|/2).                              \tag{20a}
\]
For fixed integer powers this bound has zero exponential rate, so
the complementary filled contribution has rate at most
\(\Phi-\gamma\).

Appendix O, equivalently [the Morse period theorem](actual_morse_cross_filling_period.md)
and [its geometric identification](actual_morse_geometric_contribution.md),
supplies the nonzero full
all-central period for this original matched sphere. Its selected action
\(S_{\boldsymbol p}\) obeys
\[
 \Re S_{\boldsymbol p}\longrightarrow\Phi
 \quad\text{as every }|p_e|\longrightarrow\infty
 \quad\text{independently},\qquad
 2\pi\Re S_{\boldsymbol p}
       =\operatorname{Vol}(S^3\setminus K_{\boldsymbol p}).    \tag{21}
\]
The latter equality uses the new diagram's complete positive cells,
its original meridians and longitudes, the primitive equations
\(U_e+p_eV_e=-2\pi i\), the main cusp left complete, and the
same-chain volume calibration. It is not inferred from (11) or
from a formal critical value.

Choose the independent long-filling threshold so that the selected
real action is larger than \(\Phi-\gamma/2\), and so that the
original primitive completion and nonzero all-charge asymptotic
apply. The complementary contribution is then exponentially
smaller. The full reduced zero-framed invariant satisfies
\[
 \boxed{\displaystyle
 \lim_{N\to\infty}\frac{2\pi}{N}
       \log|\langle K_{\boldsymbol p}\rangle_N|
   =\operatorname{Vol}(S^3\setminus K_{\boldsymbol p}).}       \tag{22}
\]
Here \(\langle K\rangle_N\) is the original reduced, zero-framed
complete-color Kashaev invariant, with unknot value one. Conversion
from \(Z_N\) retains the original framing/component character, which
has modulus one at complete color; for a knot its enhanced component
sign is one. The full one-cut modified convention retains its
additional factor \(i^{N+3}/N\), whose exponential rate is zero.
The knot pattern and every signed integer
\(p_e\), with \(n_e=\epsilon_e-2p_e\), are fixed before \(N\)
tends to infinity. No ratio bound between the large fillings or
uniform threshold over growing diagrams is asserted.

## 6. Arbitrarily many blocks and weak balance as an input

Take any finite number \(k\ge2\) of certified marked inputs. Repeatedly
perform the operation of section 2 at the retained common marked
edge \(uv\), identifying the chosen ordinary third vertex of the
next block with the ordinary third vertex on the selected incident
triangle of the current sphere. The previous ordinary coordinates
are retained; only the two chosen third vertices are identified.
At each step use fresh interior vertices.

After every step the sphere is simple and \(uv\) is still
nonmatching, so it has two incident triangles available for the
next step. Thus the construction has no upper bound on \(k\).
Induction on (8), (11) and (17) gives
\[
 R_{\mathrm{new}}=\sum_{j=1}^kR_j-(k-1),\qquad
 \Phi_{\mathrm{new}}=\sum_{j=1}^k\Phi_j,\qquad
 \gamma_{\mathrm{new}}\ge\min_{1\le j\le k}\gamma_j.            \tag{23}
\]
The exact witnesses are obtained recursively. At the next attachment
one may rescale the entire previous witness to normalize its new
joining face; protected zeros remain zero and all existing
incidence identifications remain intact. One does not normalize
already shared faces independently. The limiting statement always
fixes this finite assembled diagram first.

If each input packing is weak-balanced, the new complete packing
retains all their unmerged local comparisons. At the new crossing,
\[
 X=Q_a+Q_c\ge C_1\ge\log c,\qquad
 X\ge C_2\ge\log a,                                      \tag{24}
\]
where the first comparisons use (12). They are in fact strict at
this merged crossing. Thus protected triangular sums of
weak-balanced inputs are themselves weak-balanced. The existing
power-flattening theorem supplies their unabridged certificates.
This gives a direct constructive family, with unrestricted finite
numbers of certified pieces and arbitrary cycles already present
inside those pieces.

More generally the theorem uses (5), which includes refined
per-sector or finite-branch shared-radius certificates. It does not
assert that the result lies outside all previously known knot
presentations. Its contribution is the closure proof retaining the
literal matching and the single original target at every face.

## 7. Arbitrarily large certified marked diagrams outside weak balance

The closure is not confined to weak-balanced inputs. This statement
concerns the recorded diagram and mark: a knot might have another
presentation or mark satisfying a different criterion.

First recall why weak balance implies an anchored witness at the
same mark. At the complete vector \(q^*\), let
\(P(q)=\sum_eX_e(q)-\sum_fq_f\), where \(X_e=A_C\), and put
\[
 H_e=\max\{X_e,q_b,q_c\},                               \tag{25}
\]
omitting protected logarithms. The entropy proof of
[weak balance, §§3–5](general_weak_balance_volume.md)
gives \(h_*>0\), a finite \(\mathcal E\ge0\), and, for
\(q(t)=(1-t)q^*\), \(0<t<1\),
\[
 P(q(t))\le\Phi+\tfrac12t^2\mathcal E,\qquad
 X_e(q(t))-A_s(q(t))\ge t h_*
                   \quad\text{for every surviving side }s.    \tag{26}
\]
The positivity of \(h_*\) uses the overloaded triangle, which has
at least two ordinary corners: the matched outer edge cannot be
the protected nonmatching edge. Since \(A_L\ge q_c\) and
\(A_R\ge q_b\), (26) implies \(H_e(q(t))=X_e(q(t))\).
Thus every fixed surviving anchor satisfies
\[
 A_{a,s}(q(t))+\sum_{e\ne a}H_e(q(t))-\sum_fq_f(t)
 \le\Phi+\tfrac12t^2\mathcal E-t h_*<\Phi               \tag{27}
\]
for a sufficiently small positive \(t\).
This proves the anchored implication without treating equality
in the original balance test as a strict loss.

Now take the original width-three source with word
\[
 (1,3,0,2,4,1,3,0,2,4,1,3,0,2,4,1,3),\qquad
 \{u,v\}=\{0,16\}.                                     \tag{28}
\]
Its construction and rational certificates are given in
[the separation theorem](actual_shared_radius_certificate_separation.md).
The exact data are
[the forty-branch certificate](../experiments/actual_sector_cover_certificate.json)
and [the anchor certificate](../experiments/actual_shared_radius_anchor_obstruction_certificate.json);
their verifiers are
[the cover verifier](../experiments/audit_actual_sector_cover.py)
and [the anchor verifier](../experiments/audit_actual_shared_radius_anchor_obstruction.py).
They retain the original compiler, mark, local orders, and all
ordinary targets.

There are seventeen matching regions. Put \(J=\{2,4,7,12\}\).
The first fifteen cover branches prescribe right on a nonempty
subset of \(J\), allow central/left on its complement in \(J\), and
allow all surviving labels elsewhere. In the remaining case no
region in \(J\) is right; choose any surviving one-sided anchor,
allow central/left at the other regions of \(J\), and all surviving
labels elsewhere. There are twenty-five such anchor branches.
Every locally allowed noncentral string is covered by this
combinatorial division, whether or not its global coefficient
vanishes. Thus this is exactly the unabridged hypothesis (5).
The rational bounds prove a uniform gap greater than \(0.04\).

The same data locate a weak-balance failure away from a usable
joining triangle. The obstructed anchor is right at crossing 12,
whose quartet is \((0,11,16,14)\). Its dual rational flow mixes
the complete and pure-middle rows only at spectators \(2,4,7\);
all other spectators use their complete triangle rows.
Consequently that very flow bounds the smaller function
\[
 \widetilde G(q)=A_{12,R}(q)+
      \sum_{e\in\{2,4,7\}}H_e(q)+
      \sum_{e\notin J}X_e(q)-\sum_fq_f
                  >\Phi_{17}+0.025
            \quad\text{for every ordinary }q.                 \tag{29}
\]
Indeed the recorded rational row loads cancel every ordinary
target. The mixed rows are bounded by \(H_e\), while each
unmixed row is already bounded by \(X_e\); no replacement by
\(H_e\) at an unmixed spectator is required.
The certificate gives the flow entropy greater than
\(19.95975965735\) and a complete-action upper bound less than
\(19.92324700353\), which imply (29).

If all four crossings in \(J\) were weak-balanced at the complete
vector, then \(H_e=X_e\) at \(2,4,7\), and
\(A_{12,R}\le X_{12}\). The latter follows from
\(X_{12}\ge q_{11}\) and
\(Q(0,e^{q_{11}},e^{q_{14}})\ge q_{11}/2\). Here \(11\) and \(14\)
are face labels; their positive coefficient weights are
\(e^{q_{11}}\) and \(e^{q_{14}}\). The latter inequality tests the
simplex vertex at the weight \(e^{q_{11}}\).
It would give \(\widetilde G(q^*)\le P(q^*)=\Phi_{17}\),
contradicting (29). Thus at least one crossing in \(J\) fails
weak balance. This localization only needs the non-strict
comparison at completeness; the flattening in (26)–(27)
explains the broader anchored implication.

The two marked-edge triangles belong to crossings 12 and 15.
At crossing 15 the quartet and its marked output triangle are
\[
             (16,14,0,17),\qquad (16,17,0).             \tag{30}
\]
Choose this latter triangle for the first sum. In (6) the
seventeen-region input is \(D_2\), with
\((u,v,B,a)=(16,0,17,14)\).
None of the four crossings in \(J\) is removed or merged.
Equation (10) preserves their complete curvatures up to a common
scale on that input. Each difference \(X_e-q_b\) or \(X_e-q_c\)
is invariant under this scale, so the failed comparison survives.

For an explicit repeatable input take the tetrahedral sphere
with oriented faces
\[
 (u,v,B),\ (u,B,C),\ (B,v,C),\ (v,u,C)
                                                               \tag{31}
\]
and matching edges \(uB,vC\), with \(uv\) protected and
nonmatching. Its two quartets are
\((u,v,C,B)\) and \((v,u,B,C)\).
At \(B=C=1\), each ordinary face receives load \(1/2\) from
one singleton triangle and \(1/4\) from each of the other two
triangles. This is the complete stationary vector. Each local
complete rate is \(2f(1/4)>0\), whereas its positive middle
logarithm is zero. This input is strictly balanced and therefore
has an unabridged certificate.

Attach any fixed number \(r\ge1\) of these tetrahedral inputs,
always continuing on the newly attached side of the retained
marked edge. The matching side can be aligned by the recorded
whole-input orientation choice in (6). No later step touches
the four original crossings in \(J\). The resulting sphere has
\[
              R_r=17+r,\qquad
              \Phi_r=\Phi_{17}+4r f(1/4).              \tag{32}
\]
It satisfies (5) by the closure theorem and fails weak balance
at its retained mark by (29)–(30). Choose any knot-producing
terminal parity pattern for this new sphere. For all independently
sufficiently long fixed signed fillings, (22) is the volume
limit for that new knot. This gives arbitrary finite sizes of
certified marked diagrams outside weak balance at that mark;
it does not classify their unmarked knots or their other possible
presentations.

## 8. Scope and related constructions

Classical volume additivity for belted sums is part of the
background to constructions of augmented links. For the geometric,
combinatorial, and diagrammatic classification of such decompositions,
see Morgan, Ransom, Spyropoulos, Trapp, and Ziegler,
[Belted sum decompositions of fully augmented links](https://arxiv.org/abs/2311.13540).
Van der Veen's [Proof of the volume conjecture for Whitehead chains](https://arxiv.org/abs/math/0611181)
establishes the volume conjecture for that specific infinite family.
No identification of the present ordered protected operation with
those marked constructions is used here. In particular classical
volume additivity itself is not claimed as a new phenomenon.
The statement proved here is closure of the original phase-uniform
source certificates, with every shared target retained, and its
independent-long-filling consequence for the recorded diagrams.

An arbitrary block need not satisfy (5): the
[fifty-four-region example](actual_singleton_sector_envelope_obstruction.md)
has a genuine fixed-sector envelope capacity exceeding its complete
action by more than \(1/5\). The present proof does not assert an
exact scalar factorization of finite spectral kernels. It proves
an inequality for every genuine sector with its full real spectrum
and all face phases, and therefore retains the normal data required
by the finite filling functional.

The certificate hypothesis cannot be weakened here to an arbitrary
closed-source cancellation estimate, or to a cap estimate with other
spectra fixed. Such estimates need not provide witnesses for (16).
Likewise globally omitted strings require an independent support
transfer argument. The theorem changes diagrams by an explicit
operation; it is not a claim that the original input knot type is
preserved.
