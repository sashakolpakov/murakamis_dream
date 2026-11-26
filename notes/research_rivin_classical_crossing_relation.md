# The classical crossing relation in the external Rivin coordinates

Private written deduction, 14 November 2026. The external formulas are
those of `rivin-jones` at commit
`e956fb919ac7d1bbc7cb3d3873fbac993feb94b7`, in
`docs/MATHEMATICS.md` and `python/rivin_jones/r_matrix.py`. Their text was
read; no code, numerical calculation, import, or test was executed.

This gives the holomorphic generating function directly from those
coefficients, an explicit rational crossing map, and its triangular
matrix and Wirtinger interpretation. It keeps the actual highest-weight
cut, quantum pivots, writhe factor and ordinary bends in view. The general
critical-correspondence-to-representation theorem is already present in
[the marked braid calculation](marked_braid_holonomy.md), Sections 4--6.
The contribution here is its direct derivation and coordinate dictionary
for the external matrices, not a new proof that a geometric critical
component contributes to the original scalar.

## 1. A holomorphic primitive fixed by the actual coefficients

Put \(d=N-1\), \(q=e^{\pi i/N}\), \(Q=q^2\), and
\(A_N=e^{-\pi i/(2N)}\).
Let \(I,J\) be the overstrand and understrand inputs and \(k\) the
transfer. The outputs on these two strands are \(I-k,J+k\), with
\(0\le k\le\min(I,d-J)\). External positive input order is \((I,J)\)
and negative input order is \((J,I)\). The literal coefficient is
\[
 R_\sigma(I,J;k)=A_N^{Q_\sigma(I,J,k)}
       \frac{S_I S_{J+k}}{S_{I-k}S_JS_k},\qquad
 S_a=\prod_{r=1}^a2\sin(\pi r/N),\quad S_0=1.             \tag{1}
\]
where
\[
 \begin{split}
 Q_+&=(d-2I+2k)(d-2J-2k)+k(k-1)+Nk,\\
 Q_-&=-(d-2I)(d-2J)-k(k-1)-Nk.
 \end{split}                                             \tag{2}
\]
These identities, including their phases, were derived directly in
[the role-frame calculation](research_rivin_role_frames_and_bridge_angles.md),
Section 1. No positive boundary frame is applied in this section.

On a simply connected neighborhood of a compact subinterval of
\(0<z<1\), fix
\[
 \ell(z)=\Log(1-e^{2\pi iz})-\pi iz+\frac{\pi i}{2},
 \qquad
 \mathcal J(z)=
 \frac{\operatorname{Li}_2(1)-\operatorname{Li}_2(e^{2\pi iz})}{2\pi i}
       +\frac{\pi i}{2}(z-z^2).                           \tag{3}
\]
The marks are the continuation for which \(\ell(z)=\log(2\sin\pi z)\)
on that real interval and \(\mathcal J(0)=0\) by a one-sided limit.
Then \(\mathcal J'=\ell\), and \(\mathcal J\) restricts to the real
sine-factorial integral. Continue this marked primitive on logarithmic
charts avoiding the integer divisors; no entire interpolation of the
finite factorials is asserted.

For \((u,v,t)=(I/N,J/N,k/N)\), define
\[
 \begin{split}
 p_+&=(1-2u+2t)(1-2v-2t)+t^2+t,\\
 p_-&=-(1-2u)(1-2v)-t^2-t,\\
 \mathcal S_\sigma(u,v,t)
   &=\mathcal J(u)+\mathcal J(v+t)-\mathcal J(u-t)
       -\mathcal J(v)-\mathcal J(t)-\frac{\pi i}{2}p_\sigma.
 \end{split}                                             \tag{4}
\]
The principal action is calibrated by the physical lattice: on every
compact subset of
\(0<t<u<1\), \(0<v<v+t<1\), the exact logarithm
\(-\pi iQ_\sigma/(2N)\) of the monomial phase and the positive logarithms
of the \(S\)'s give
\[
                    \log R_\sigma=N\mathcal S_\sigma+O(\log N).
                                                               \tag{5}
\]
This uses the endpoint-uniform factorial estimate in
[the crossing norm proof](weighted_crossing_source_gap.md), Section 2.
In particular the leading phase in (4) is fixed by (2), not chosen
by a stationary point. Equation (5) alone does not justify replacing a
whole finite sum by an integral on an arbitrary complex cycle.

The same action follows directly from exact contiguity. For example,
\[
 \frac{R_\sigma(I+1,J;k)}{R_\sigma(I,J;k)}
  =A_N^{Q_\sigma(I+1,J,k)-Q_\sigma(I,J,k)}
        \frac{\sin(\pi(I+1)/N)}{\sin(\pi(I-k+1)/N)},       \tag{6}
\]
and the \(k\)-ratio has sine factor
\(2\sin(\pi(J+k+1)/N)\sin(\pi(I-k)/N)/\sin(\pi(k+1)/N)\).
Their limits are \(e^{\partial_u\mathcal S_\sigma}\) and
\(e^{\partial_t\mathcal S_\sigma}\). The \(J\)-ratio gives the third
derivative. Thus the following rational equations are symbols of the
actual difference ratios, rather than consequences of an arbitrary
off-grid continuation.

### Exact primitive comparison with the physical and incidence actions

The finite strand adapter fixes this comparison, including the constant.
Write its scalar coefficient as
\[
 T_Ne_i=t_N(i)|d-i\rangle,\qquad
 t_N(i)=q^{-i(i-1)/2}.
\]
Equation (3) of
[the local adapter](research_rivin_jones_local_crossing_adapter.md)
identifies the external sign \(\sigma\) with physical sign \(-\sigma\),
with no extra scalar. For either signed coefficient in the over/under
notation of (1), its exact output/input scalar ratio is
\[
 \frac{t_N(J+k)t_N(I-k)}{t_N(I)t_N(J)}
                  =q^{k(I-J-k)}.                         \tag{6a}
\]
The order of the two outputs does not affect this product. In physical
roles the over-input, under-input and transfer are
\((d-J,d-I,k)\). Thus the limiting physical coordinates used in
[the joint clock action](research_joint_clock_phase_equations.md),
equation (27a), are
\[
             (U,V,J_0)=(t,1-v-t,1-u),                    \tag{6b}
\]
where \(V\) is the physical over-output and \(J_0\) the under-input.
The real domain of (5) maps into
\(U,V,J_0>0\), \(U+V<1\), \(U+J_0<1\).

For clarity that physical action, with its state-independent Cartan
factor kept separately, is
\[
 \begin{split}
 G_\tau(U,V,J_0)
   &=\mathcal J(U+V)+\mathcal J(J_0+U)
        -\mathcal J(V)-\mathcal J(J_0)-\mathcal J(U)
          +\pi i\tau\psi(U,V,J_0),\\
 \psi(U,V,J_0)
   &=-J_0-V+2VJ_0-U/2+U(J_0+V)+U^2/2.
 \end{split}
\]
On these canonical real strips, and on their common marked analytic
continuations, the primitive identity is exactly
\[
 \boxed{\quad
 \mathcal S_\sigma(u,v,t)+\pi i\,t(u-v-t)
   =G_{-\sigma}(t,1-v-t,1-u)-\frac{\sigma\pi i}{2}.
 \quad}                                                   \tag{6c}
\]
Here \(\pi i\,t(u-v-t)\) is precisely the leading logarithm of
(6a), while \(-\sigma\pi i/2\) is the leading logarithm of the
physical factor \(\kappa^{-\sigma}\),
\(\kappa=q^{d^2/2}\). No additive constant has been chosen from a
critical point.

To verify (6c) directly, the marked sine primitive satisfies
\(\mathcal J(1-z)=-\mathcal J(z)\) on the strip. This follows from
\(\ell(1-z)=\ell(z)\) and the endpoint value \(\mathcal J(1)=0\).
Applying reflection to each term of \(G\) gives exactly the five
sine-primitive terms of (4). Put
\[
 \psi_*=-u-v+2uv+t(u-v)+t/2-t^2/2
        =\psi(t,1-v-t,1-u).
\]
The remaining quadratic identities are
\[
 \frac{p_+}{2}-t(u-v-t)=\psi_*+\frac12,
 \qquad
 -\frac{p_-}{2}+t(u-v-t)=\psi_*+\frac12.
 \tag{6d}
\]
Expansion proves both, and hence (6c) for both signs with its displayed
constant.

The joint clock theorem, equations (27e)--(27g), proves that the
corrected incidence primitive on its specified canonical clock graph
is exactly \(G_\tau\). Consequently (6c) completes the local primitive
comparison from the external coefficients to the physical crossing
and to the full incidence action. The finite boundary frame changes,
the Cartan constants and the logarithmic/Fourier lifts remain part of
that comparison. Neither this identity nor its analytic continuation
identifies the original quantum cycle with a descending cycle.

## 2. Exponentiated derivatives and the rational crossing maps

Write \(x=e^{\pi iu},y=e^{\pi iv},z=e^{\pi it}\), and let
\(E_{\sigma,u}=e^{\partial_u\mathcal S_\sigma}\), with analogous
notation for \(v,t\). Differentiation of (3)--(4) gives
\[
\begin{array}{c|cc}
 &\sigma=+&\sigma=-\\ \hline
E_{\sigma,u}
 &-\dfrac{1-x^2}{y^2z(z^2-x^2)}
 &-\dfrac{y^2z(1-x^2)}{z^2-x^2}\\[6pt]
E_{\sigma,v}
 &-\dfrac{z(1-y^2z^2)}{x^2(1-y^2)}
 &-\dfrac{x^2(1-y^2z^2)}{z(1-y^2)}\\[6pt]
E_{\sigma,t}
 &\dfrac{yz^2(1-y^2z^2)(z^2-x^2)}{x^3(1-z^2)}
 &-\dfrac{(1-y^2z^2)(z^2-x^2)}{xy(1-z^2)}.
\end{array}                                                \tag{7}
\]
For instance \(e^{\ell(u)-\ell(u-t)}
=z^{-1}(1-x^2)/(1-x^2/z^2)\); the quadratic phase in (4) supplies
the rest of the first row. This also fixes the half-clock signs.

Use the canonical convention that an action differential is output
momentum times output variation minus input momentum times input
variation. Conservation gives output positions \((u-t,v+t)\).
Introducing the arbitrary exponential \(\tau\) of its conormal
multiplier, the four momentum exponentials satisfy
\[
 p_I=\frac{\tau}{E_uE_t},\quad p_J=\frac{\tau}{E_v},\quad
 p_{I'}=\frac{\tau}{E_t},\quad p_{J'}=\tau.                \tag{8}
\]
Equivalently their three ratios are \(p_{I'}/p_I=E_u\),
\(p_{J'}/p_J=E_v\), \(p_{J'}/p_{I'}=E_t\). These equations follow
by differentiating with \(t=u-u'\) on \(u'+v'=u+v\); they retain the
otherwise undetermined common momentum.

Make the same momentum gauge on every strand:
\[
 X=x^2,\quad Y=y^2,\quad Z=z^2,\qquad a=p_I/x,\quad b=p_J/y.
                                                               \tag{9}
\]
It preserves the cotangent two-form, since subtracting \(\pi iu\)
from \(\log p_I\) adds a function of the position alone. Eliminating
\(\tau,z\) in (7)--(8) gives the following rational formulas.

For the external positive crossing,
\[
 \begin{split}
 Z&=1-\frac ab\frac{(1-X)(1-Y)}Y,\\
 X'&=X/Z,\qquad Y'=YZ,\\
 a'&=-\frac{a(1-X)}{Y(Z-X)},\qquad
 b'=-\frac{b(1-YZ)}{X(1-Y)}.
 \end{split}                                               \tag{10}
\]
Here the output is in checked order \(((Y',b'),(X',a'))\).
For the external negative crossing, written with the same over/under
roles as in (1),
\[
 \begin{split}
 Z^{-1}&=1-\frac ab\frac{(1-X)(1-Y)}X,\\
 X'&=X/Z,\qquad Y'=YZ,\\
 a'&=-\frac{aYZ(1-X)}{Z-X},\qquad
 b'=-\frac{bX(1-YZ)}{Z(1-Y)}.
 \end{split}                                               \tag{11}
\]
Its input is \(((Y,b),(X,a))\) and output is
\(((X',a'),(Y',b'))\). All formulas concern the regular open set
where their displayed factors and the shapes in (7) are nonzero.

For completeness, the cancellation that solves for \(Z\) is
\[
 \frac{p_I}{p_J}=
 \begin{cases}
 xy(1-z^2)/[(1-x^2)(1-y^2)],&+,\\
 (x^3/y)(1-z^{-2})/[(1-x^2)(1-y^2)],&-.
 \end{cases}
\]
Substitution of (9) gives (10)--(11). Their other formulas follow
from \(a'/a=zE_u\) and \(b'/b=E_v/z\).

They are inverse checked maps. Indeed after (10),
\[
 \frac{a'}{b'}=
       \frac{X(1-Z)}{(Z-X)(1-YZ)}.
\]
Putting \((X/Z,YZ,a',b')\) into (11) gives \(Z_-=1/Z\).
Its two momentum multipliers are respectively the reciprocals of
those in (10), so it returns \((X,Y,a,b)\). This proves the inverse
on the stated open chart. In particular fixed positive and negative
powers and arbitrary fixed signed words have rational classical
relations obtained by composition, with their singular loci retained.

## 3. Exact triangular factorization on a parabolic surface

For one strand define
\[
 k=-X,\qquad e=(1-X)a,\qquad f=\frac{1-X}{Xa}.
\]
Then
\[
                 ef+k+k^{-1}=-2.                          \tag{12}
\]
These are also the principal symbols of the external generators:
with \(v=A_N^2=q^{-1}\) and
\([r]_v=(v^r-v^{-r})/(v-v^{-1})\), the source module has
\(K_v e_i=v^{d-2i}e_i\), \(E_v e_i=[N-i]_v e_{i-1}\),
\(F_v e_i=[i+1]_v e_{i+1}\). On a local exponential state the
symbols of \(K_v,(v-v^{-1})E_v,(v-v^{-1})F_v\) are precisely
\((k,e,f)\). A lowering matrix reads the input state one index higher,
which is the momentum factor \(p_I\); the raising matrix gives its
inverse. The displayed external realization and coproducts are
proved in [the regular bend note](research_rivin_jones_regular_bends_and_newton_turn.md),
Section 1.

Introduce
\[
 B_+(k,e)=\begin{pmatrix}1&e\\0&k\end{pmatrix},\qquad
 B_-(k,f)=\begin{pmatrix}1&0\\-f&k^{-1}\end{pmatrix},
 \qquad
 M=k^{-1}B_-^{-1}B_+
   =\begin{pmatrix}k^{-1}&e/k\\f&k+ef\end{pmatrix}.         \tag{13}
\]
Thus \(\det M=1\), \(\operatorname{tr}M=-2\). On \(X\ne1\),
it is noncentral; its image in \(\mathrm{PSL}_2\) is parabolic.

Label input over/under strands by \(1,2\), and retain these role
labels on \(1',2'\). Formula (10) gives
\[
 Z=1-e_1f_2,\quad k_1'=k_1/Z,\quad k_2'=k_2Z,\quad
 e_1'=e_1/(k_2Z),\quad f_2'=k_1f_2/Z.                    \tag{14}
\]
It also satisfies the two full coproduct identities
\[
 e_2'k_1'+e_1'=e_1k_2+e_2,\qquad
 f_2'+(k_2')^{-1}f_1'=f_1+k_1^{-1}f_2.                   \tag{15}
\]
Here is an elementary coefficient check of both, beyond trace matching.
Put \(T=(a/b)(1-X)\), so \(Z=1-T(1-Y)/Y\) and
\(1-YZ=(1-Y)(1+T)\). The first identity after cancellation of its
nonzero factors is
\[
 Y(1-Y)(1+T)^2-T
       =[Y-T(1-Y)]\{(1-Y)-YT\}.
\]
For the second, use \(a(1-X)f_2=1-Z\); after clearing factors it is
\[
 (Z-X)^2-X^2(1-Z)
              =Z\{(1-X)^2-(1-Z)\}.
\]
Both are polynomial identities by expansion. This proves (15).

Equations (14)--(15) yield three actual matrix factorizations:
\[
 \begin{split}
 B_{+,1}B_{+,2}&=B_{+,2'}B_{+,1'},\\
 B_{-,1}B_{-,2}&=B_{-,2'}B_{-,1'},\\
 B_{+,1}B_{-,2}&=Z\,B_{-,2'}B_{+,1'}.
 \end{split}                                               \tag{16}
\]
The first two are (15) and conservation of \(k_1k_2\). The third
can be checked entrywise: its left side is
\(\left(\begin{smallmatrix}Z&e_1/k_2\\-k_1f_2&k_1/k_2\end{smallmatrix}\right)\);
substitution of (14) gives exactly that matrix on the right. The
scalar \(Z\) is essential with these unnormalized triangular matrices.

## 4. Explicit dressing gives the actual Wirtinger rule

On a horizontal slice with \(b\) ordered heads put
\[
 H_i=B_{-,i+1}\cdots B_{-,b},\qquad
                   \widehat M_i=H_i^{-1}M_iH_i.            \tag{17}
\]
An empty suffix is the identity. These are genuine determinant-one,
trace-minus-two matrices, not just Casimir values.

First take two heads. The mixed and lower identities in (16) imply
\[
 M_{1'}=B_{-,2}^{-1}M_1B_{-,2}.                           \tag{18}
\]
Indeed substitute
\(B_{-,1'}=B_{-,2'}^{-1}B_{-,1}B_{-,2}\) and
\(B_{+,1'}=Z^{-1}B_{-,2'}^{-1}B_{+,1}B_{-,2}\)
in (13); \(k_1'=k_1/Z\) cancels the extra scalar.
Also the product of the dressed meridians is
\[
 \widehat M_1\widehat M_2
  =(k_1k_2)^{-1}(B_{-,1}B_{-,2})^{-1}(B_{+,1}B_{+,2}),     \tag{19}
\]
which is preserved by (16). The checked output order is \((2',1')\).
Thus (18) leaves the overstrand meridian unchanged, and (19) gives
the complete positive rule
\[
                         (A,B)\longmapsto(ABA^{-1},A).     \tag{20}
\]
The negative rule is its inverse, \((A,B)\mapsto(B,B^{-1}AB)\).
For adjacent heads in a longer word, conjugate this calculation by the
common suffix to their right. Suffixes of earlier heads contain the
unchanged product \(B_{-,1}B_{-,2}\), so all spectator meridians are
unchanged. This proves (20) for arbitrary signed braid words in their
actual chronological operator order.

The dressing has an explicit rational inverse. Given a tuple
\((A_1,\ldots,A_b)\) with determinant one and trace minus two, work
backwards from \(i=b\). Once the later \(B_-\)'s are known, set
\[
 M_i=H_iA_iH_i^{-1},\quad
 k_i=(M_i)_{11}^{-1},\quad e_i=k_i(M_i)_{12},\quad
 f_i=(M_i)_{21},\quad X_i=-k_i,\quad a_i=e_i/(1+k_i).       \tag{21}
\]
Require \((M_i)_{11}\ne0,-1\) at each step. Determinant one gives
\((M_i)_{22}=k_i+e_if_i\); trace minus two gives (12). The condition
\(k_i\ne-1\) then makes \(e_i,f_i,a_i\) nonzero. Equation (21)
recovers (13) and defines the next \(B_{-,i}\). It is a rational
inverse on this specified open set, rather than an argument by
dimension count. A word uses the intersection with the corresponding
regular sets at every intermediate stage. No claim that a particular
representation belongs to that intersection is needed here.

Consequently the rational crossing map is conjugate on this open set
to the ordinary parabolic Wirtinger action. This statement also proves
its braid relations there. It is consistent with, and substantially
covered by, the earlier marked braid theorem; (21) and the suffix
convention specify the present external coordinates independently.

## 5. Ordinary bends and fixed short compositions

The external repository supplies no cup/cap API. Use exactly the
regular self-dual extension in the cited bend note. At the root its
cup and ordinary cap are supported on \(i+j=d\), and their adjacent
coefficients satisfy
\[
                 c_{i+1}/c_i=q^{2i+3},\qquad
                 b_{i+1}/b_i=q^{-2i-1}.                    \tag{22}
\]
These follow from that note's equation (6), using
\([i+1]_q=[d-i]_q\). Their leading action derivatives have exponentials
\(X\) and \(X^{-1}\), respectively. With the canonical input/output
signs of (8), both bend relations in the chart (9) are
\[
                          Y=X^{-1},\qquad b=-a.            \tag{23}
\]
For example the cup has \(p_I/p_J=X\). Its support has
\(v\to1-u\), so \(y=-x^{-1}\); inserting (9) gives \(b=-a\).
The same result for the cap uses the negative input derivative. The
minus sign retains the original complementary-index lift; replacing
it by \(+1\) would change the bend.

Substitution in (13) shows
\[
                 B_{+,1}B_{+,2}=B_{-,1}B_{-,2}=I.
\]
Hence its two dressed meridians multiply to the identity. The bends
create or remove inverse oriented meridians, exactly as required by
the tangle group. Their finite scalar and phase normalizations remain
those of the regular bend theorem; (22)--(23) do not reset them.

It follows that arbitrary fixed signed powers, stacking, ordinary
turns and finite tangle compositions have a rational classical
relation compatible with the actual oriented meridian words wherever
the corresponding charts are regular. This includes inserting any
fixed short signed tangle into an existing boundary relation. It is
not a uniform asymptotic estimate for that tangle's prescribed
observation, nor a theorem about its geometric coefficient.

## 6. The prescribed closing and the representation it yields

The external source on \(b\) heads fixes the first input and output
index to zero and closes the others with \(K_{\rm ext}\), then applies
the prescribed writhe correction. In the present variables its exact
diagonal weight is
\[
                    (K_{\rm ext})_{ii}=-q\,Q^i=-qX.        \tag{24}
\]
At the literal pinned endpoint \(X=1\), the regular chart of (7)--(13)
is singular. The pin is therefore not simply declared a regular
periodic boundary point.

For the **complete assembled braid intertwiner**, the prescribed cut
equals its normalized first-head average. This is proved directly in
[the cut-functional theorem](research_rivin_jones_prescribed_cut_and_hermite_recovery.md),
Section 2: the tail quantum trace commutes with the first-head
generators, and hence is scalar. Thus the exact external invariant is
also
\[
 \frac{q^{w(N^2-1)/2}}{N}
   \sum_{i_1,\ldots,i_b=0}^d
      \left(\prod_{r=2}^b[-qQ^{i_r}]\right)
                   W_{\boldsymbol i,\boldsymbol i}.       \tag{25}
\]
This equality uses no division by a vanishing quantum dimension.
It is not permitted for an arbitrary inserted exterior that fails
the intertwining hypothesis; that case retains the literal pin and
its actual boundary data.

Every pivot in (24) has a nonzero, bounded magnitude and bounded
logarithm on any fixed compact complex chart in \(X\ne0\). Its
logarithm is order one, not order \(N\). Its exact lattice shift
ratio is \(Q\), tending to one. Hence it remains an amplitude and
finite shift mark in (25), but does not alter the leading exponentiated
internal stationary equations. The exact framing factor is
\[
 q^{w(N^2-1)/2}=
     \exp(N\pi i w/2)\exp(-\pi i w/(2N)).                 \tag{26}
\]
It contributes the leading constant \(\pi iw/2\) to the action;
it has not been discarded merely because its internal derivatives
are zero.

At a regular full stationary point of (25), the sum of the local
actions (4) has matching internal positions and momenta. Exponentiated
stationarity includes the usual integer logarithmic branches; they
are not a choice of a favorable saddle. Equations (8)--(11) therefore
give a fixed point of the checked braid map on all heads. Conversely
a fixed point in the specified regular chart supplies those
exponentiated equations by the local generating relations.

Under (17), this fixed locus is exactly the open part of
\[
 \{(A_1,\ldots,A_b):\det A_i=1,\ \operatorname{tr}A_i=-2,
                              \beta(A_i)=A_i\ \text{for every }i\}.
                                                               \tag{27}
\]
The presentation obtained by placing one meridian on each braid
strand, using (20) at crossings, and identifying the closing endpoints
is the Wirtinger presentation of the braid closure. Therefore (27)
gives actual parabolic representations of its group. Conversely any
such representation whose tuple and intermediate stages lie in the
explicit inverse-dressing chart (21) gives a fixed point and hence a
regular exponentiated critical point. This is a converse on a stated
open chart, not a claim about every representation or every boundary
stratum.

For a knot, a noncentral parabolic meridian has a parabolic centralizer
in \(\mathrm{PSL}_2\); its commuting longitude consequently fixes the
same ideal point. Thus these representations are boundary-parabolic.
The trace-minus-two lift records the present convention. No preferred
longitude eigenvalue, regulator constant, or quantum normal is inferred
from that elementary centralizer statement.

## 7. What has and has not been transported

The exact [external-to-Newton adapter](research_rivin_jones_local_crossing_adapter.md)
reverses crossing signs at
\(A_N\). All signs in this note are external signs. The adapter and
its scalar lines must be applied when comparing the corresponding
physical mirror word; the statement (20) does not silently change
that convention. The full finite adapter and
[split-incidence recovery](research_rivin_jones_split_boundary_source_equivalence.md)
retain all Newton Hermite data. A principal classical symbol by itself
does not estimate those normal coefficients.

The earlier
[positive-chart obstruction](research_rivin_jones_positive_chart_sewing_obstruction.md)
concerns simultaneous strict upper-half-plane choices for particular
raw Fourier shapes. The present maps live on complex rational charts;
they assert neither positivity of those shapes nor an equality of a
raw full-function density with the finite polynomial away from its
sampling grid. There is no conflict with its two-crossing reciprocal
shape relation or its retained seam character.

This explicit character map does not by itself identify
\(2\pi\operatorname{Re}\mathcal S_{\mathrm{total}}\) with hyperbolic
volume in the chosen orientation. Here the action is normalized by
\(\log R/N\), so its real part governs exponential magnitude. The earlier
marked braid and [fundamental-cycle results](crossing_fundamental_cycle.md)
address regulator comparisons in their recorded coordinates. Equation
(6c), together with the joint clock theorem's calibrated primitive,
now supplies the local marked-action comparison among the external,
physical and incidence coordinates, with the exact adapter and all
boundary/framing conventions retained. Transporting a chosen global
branch must retain those same lifts and the already specified
orientation; equality of group relations alone would not suffice.
More decisively, neither a representation nor a regular
critical point proves that the prescribed quantum cycle has a nonzero
coefficient there. Global cycle transport, endpoint contributions,
cancellation and the lower bound needed for arbitrary fixed short
partial filling remain separate requirements.

## 8. Pinned written sources

The direct local formulas and scope comparisons above were checked at
these SHA-256 versions. The two external files are at the commit stated
at the beginning. No saved numerical audit is a premise of this note.

| Source | SHA-256 |
| --- | --- |
| External `docs/MATHEMATICS.md` | `0b7b0c0df2452d9691c807d0c3f556fe38ef3f284ebd0c0c227ae90d2af6ce5d` |
| External `python/rivin_jones/r_matrix.py` | `b6c5b48a9094587faa2ea6a9467ff801d838cfb007974a0fcd22a6e11aabfa76` |
| `research_rivin_role_frames_and_bridge_angles.md` | `125155bcd008e24bf5714457d9c6d1788a152bc563380f859c80bfe8b997ccf8` |
| `weighted_crossing_source_gap.md` | `a6a6411a780c904493db4fca3b5536f902aa5be8b6ef7cfb880a4f57509f436c` |
| `research_rivin_jones_regular_bends_and_newton_turn.md` | `ced2c87e74c255d68f367d553fb5b36da9432a90d59687823fa6401778b72af0` |
| `research_rivin_jones_prescribed_cut_and_hermite_recovery.md` | `1b0e105ffb67b2b8552f5fddc5f0a3ac009e9795b33e27599ac4726ebd74079e` |
| `marked_braid_holonomy.md` | `eff47c757d0e44bda0c396c094315b8e1fce11f1fc2d6445d636c6d2d3a46c4f` |
| `crossing_fundamental_cycle.md` | `0d7d7da0f5cf4fe0d16907e7e999d5ce7980f7ff39d437df167c99ca30205b0f` |
| `research_rivin_jones_local_crossing_adapter.md` | `c4a9a92ec22f31a035036642e0621ef9abe569646b2488dbac2d2add786500f0` |
| `research_rivin_jones_split_boundary_source_equivalence.md` | `f5b481568c2cef411ab67e88de6f818288383c8e0f8d8e3f69272551e7d81a22` |
| `research_rivin_jones_positive_chart_sewing_obstruction.md` | `7809489b46a1eb50accca9910428ca929fd98622734060e39b42e1e2070c7910` |
| `research_joint_clock_phase_equations.md` | `71393aa353909dfa2dd19b078b1d3fccdf8561520aa071b7537e4bbfc50bb867` |
